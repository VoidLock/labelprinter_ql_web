#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Brother QL printer backend
"""

import logging
from brother_ql.devicedependent import models, label_type_specs, label_sizes
from brother_ql.devicedependent import ENDLESS_LABEL, DIE_CUT_LABEL, ROUND_DIE_CUT_LABEL
from brother_ql import BrotherQLRaster, create_label
from brother_ql.backends import backend_factory, guess_backend

logger = logging.getLogger(__name__)


class BrotherQLBackend:
    """Backend for Brother QL label printers"""
    
    def __init__(self):
        self.label_type_specs = label_type_specs
        self.label_sizes = label_sizes
        self.models = models
        self.ENDLESS_LABEL = ENDLESS_LABEL
        self.DIE_CUT_LABEL = DIE_CUT_LABEL
        self.ROUND_DIE_CUT_LABEL = ROUND_DIE_CUT_LABEL
    
    def get_label_sizes(self):
        """Return list of (size_id, name) tuples"""
        return [(name, label_type_specs[name]['name']) for name in label_sizes]
    
    def get_label_dimensions(self, label_size):
        """Get printable dimensions for a label size"""
        try:
            ls = label_type_specs[label_size]
        except KeyError:
            raise LookupError(f"Unknown label_size: {label_size}")
        return ls['dots_printable']
    
    def get_label_kind(self, label_size):
        """Get the kind of label (endless, die-cut, etc.)"""
        try:
            return label_type_specs[label_size]['kind']
        except KeyError:
            raise LookupError(f"Unknown label_size: {label_size}")
    
    def validate_label_size(self, label_size):
        """Check if label size is valid"""
        return label_size in label_sizes
    
    def print_label(self, image, label_size, printer_identifier, model, 
                    threshold=70, rotate='auto', red=False, debug=False):
        """
        Print a label using Brother QL printer
        
        Args:
            image: PIL Image object
            label_size: Label size identifier
            printer_identifier: Printer connection string
            model: Brother QL model
            threshold: Threshold for B&W conversion
            rotate: Rotation setting (0, 90, 'auto')
            red: Whether to use red color
            debug: Debug mode (don't actually print)
            
        Returns:
            dict with success status and optional error message
        """
        result = {'success': False}
        
        try:
            qlr = BrotherQLRaster(model)
            create_label(qlr, image, label_size, red=red, 
                        threshold=threshold, cut=True, rotate=rotate)
            
            if not debug:
                try:
                    selected_backend = guess_backend(printer_identifier)
                    backend_class = backend_factory(selected_backend)['backend_class']
                    be = backend_class(printer_identifier)
                    be.write(qlr.data)
                    be.dispose()
                    del be
                except Exception as e:
                    result['message'] = str(e)
                    logger.warning('Exception happened: %s', e)
                    return result
            
            result['success'] = True
            if debug:
                result['data'] = str(qlr.data)
            
        except Exception as e:
            result['message'] = str(e)
            logger.error('Print error: %s', e)
        
        return result
