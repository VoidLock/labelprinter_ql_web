#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
DYMO LabelWriter printer backend
"""

import logging
import subprocess
import tempfile
import os
from PIL import Image

from label_specs.dymo_specs import DYMO_LABEL_SPECS, DYMO_LABEL_SIZES

logger = logging.getLogger(__name__)


class DymoBackend:
    """Backend for DYMO LabelWriter printers"""
    
    def __init__(self):
        self.label_specs = DYMO_LABEL_SPECS
        self.label_sizes_list = DYMO_LABEL_SIZES
        # Check for available DYMO libraries
        self.dymo_available = self._check_dymo_libs()
    
    def _check_dymo_libs(self):
        """Check if DYMO printing libraries are available"""
        try:
            import dymopy
            self.dymo_lib = 'dymopy'
            logger.info("Using dymopy library for DYMO printing")
            return True
        except ImportError:
            try:
                import dymoapi
                self.dymo_lib = 'dymoapi'
                logger.info("Using dymoapi library for DYMO printing")
                return True
            except ImportError:
                logger.warning("No DYMO library found, will use CUPS fallback")
                self.dymo_lib = 'cups'
                return True  # CUPS should be available on Linux
    
    def get_label_sizes(self):
        """Return list of (size_id, name) tuples"""
        return self.label_sizes_list
    
    def get_label_dimensions(self, label_size):
        """Get printable dimensions for a label size in pixels"""
        if label_size not in self.label_specs:
            raise LookupError(f"Unknown label_size: {label_size}")
        
        spec = self.label_specs[label_size]
        return (spec['printable_width_px'], spec['printable_height_px'])
    
    def get_label_kind(self, label_size):
        """Get the kind of label (for DYMO, all are die-cut)"""
        if label_size not in self.label_specs:
            raise LookupError(f"Unknown label_size: {label_size}")
        return self.label_specs[label_size].get('kind', 'die-cut')
    
    def validate_label_size(self, label_size):
        """Check if label size is valid"""
        return label_size in self.label_specs
    
    def _print_via_cups(self, image, label_size, printer_name, debug=False):
        """Print using CUPS (Linux standard printing)"""
        tmp_filename = None
        try:
            # Save image to temporary file
            with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as tmp_file:
                tmp_filename = tmp_file.name
                image.save(tmp_filename, 'PNG')
            
            if debug:
                logger.debug(f"Would print {tmp_filename} via CUPS to {printer_name}")
                return {'success': True, 'message': 'Debug mode: would print via CUPS'}
            
            # Use lpr command to print via CUPS
            # Extract printer name from various formats
            if printer_name.startswith('file://'):
                # For file:// URIs, we can't use CUPS directly
                # Note: This may not work properly for DYMO printers which require specific data format
                device_path = printer_name.replace('file://', '')
                with open(tmp_filename, 'rb') as img_file:
                    with open(device_path, 'wb') as dev_file:
                        dev_file.write(img_file.read())
            else:
                # Use lpr for CUPS printing
                # Get label dimensions for paper size
                spec = self.label_specs[label_size]
                width_mm = spec['width_mm']
                height_mm = spec['height_mm']
                
                cmd = [
                    'lpr',
                    '-P', printer_name,
                    '-o', f'media=Custom.{width_mm}x{height_mm}mm',
                    '-o', 'fit-to-page',
                    tmp_filename
                ]
                
                result = subprocess.run(cmd, capture_output=True, text=True)
                
                if result.returncode != 0:
                    logger.error(f"CUPS print failed: {result.stderr}")
                    return {'success': False, 'message': f"Print failed: {result.stderr}"}
            
            return {'success': True}
            
        except Exception as e:
            logger.error(f"CUPS printing error: {e}")
            return {'success': False, 'message': str(e)}
        finally:
            # Clean up temp file
            if tmp_filename and os.path.exists(tmp_filename):
                try:
                    os.unlink(tmp_filename)
                except Exception as e:
                    logger.warning(f"Failed to clean up temp file {tmp_filename}: {e}")
    
    def _print_via_dymopy(self, image, label_size, printer_name, debug=False):
        """Print using dymopy library"""
        tmp_filename = None
        try:
            import dymopy
            
            if debug:
                return {'success': True, 'message': 'Debug mode: would print via dymopy'}
            
            # Get printer
            printer = dymopy.DymoPrinter(printer_name)
            
            # Convert PIL image to format expected by dymopy
            # dymopy expects a file path or bytes
            with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as tmp_file:
                tmp_filename = tmp_file.name
                image.save(tmp_filename, 'PNG')
            
            # Print the label
            printer.print_image(tmp_filename)
            
            return {'success': True}
            
        except Exception as e:
            logger.error(f"Dymopy printing error: {e}")
            return {'success': False, 'message': str(e)}
        finally:
            # Clean up temp file
            if tmp_filename and os.path.exists(tmp_filename):
                try:
                    os.unlink(tmp_filename)
                except Exception as e:
                    logger.warning(f"Failed to clean up temp file {tmp_filename}: {e}")
    
    def print_label(self, image, label_size, printer_identifier, model=None,
                    threshold=70, rotate='auto', red=False, debug=False):
        """
        Print a label using DYMO printer
        
        Args:
            image: PIL Image object
            label_size: DYMO label part number (e.g., '30252')
            printer_identifier: Printer connection string or CUPS name
            model: DYMO model (e.g., 'LabelWriter-450') - currently not used
            threshold: Threshold for B&W conversion (DYMO printers are B&W only)
            rotate: Rotation setting (ignored for DYMO)
            red: Red color flag (ignored - DYMO LabelWriter 450 is B&W only)
            debug: Debug mode (don't actually print)
            
        Returns:
            dict with success status and optional error message
        """
        result = {'success': False}
        
        # Validate label size
        if not self.validate_label_size(label_size):
            result['message'] = f"Invalid label size: {label_size}"
            return result
        
        try:
            # Convert image to black and white
            # DYMO LabelWriter 450 is monochrome
            if image.mode != 'L':
                image = image.convert('L')
            
            # Apply threshold for pure B&W
            # Values below threshold become black, above become white
            image = image.point(lambda x: 0 if x < threshold else 255, '1')
            
            # Get the appropriate label dimensions
            spec = self.label_specs[label_size]
            target_width = spec['width_px']
            target_height = spec['height_px']
            
            # Resize image to match label dimensions if needed
            if image.size != (target_width, target_height):
                # Create a white background of the correct size
                label_image = Image.new('1', (target_width, target_height), 1)  # 1 = white
                
                # Calculate position to paste the image (centered)
                paste_x = (target_width - image.width) // 2
                paste_y = (target_height - image.height) // 2
                
                # Ensure we don't go out of bounds
                if paste_x < 0:
                    paste_x = 0
                if paste_y < 0:
                    paste_y = 0
                
                # If image is larger than label, resize it
                if image.width > target_width or image.height > target_height:
                    image.thumbnail((target_width, target_height), Image.Resampling.LANCZOS)
                    paste_x = (target_width - image.width) // 2
                    paste_y = (target_height - image.height) // 2
                
                label_image.paste(image, (paste_x, paste_y))
                image = label_image
            
            # Save debug image if in debug mode
            if debug:
                try:
                    debug_path = os.path.join(tempfile.gettempdir(), 'dymo_label_debug.png')
                    image.save(debug_path)
                    logger.debug(f"Saved debug label image to {debug_path}")
                except Exception as e:
                    logger.warning(f"Failed to save debug image: {e}")
            
            # Choose printing method based on available library
            if self.dymo_lib == 'dymopy':
                result = self._print_via_dymopy(image, label_size, printer_identifier, debug)
            elif self.dymo_lib == 'dymoapi':
                # Dymoapi not yet implemented, fall back to CUPS
                logger.warning("dymoapi not yet implemented, falling back to CUPS")
                result = self._print_via_cups(image, label_size, printer_identifier, debug)
            else:
                # Fall back to CUPS
                result = self._print_via_cups(image, label_size, printer_identifier, debug)
            
            if debug and result.get('success'):
                result['data'] = f"DYMO label {label_size} prepared for printing"
            
        except Exception as e:
            result['message'] = str(e)
            logger.error('DYMO print error: %s', e)
        
        return result
