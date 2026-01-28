#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Backend factory for printer backends
"""

from .brother_ql_backend import BrotherQLBackend
from .dymo_backend import DymoBackend

def get_backend(printer_type):
    """
    Get the appropriate backend based on printer type
    
    Args:
        printer_type: String like 'brother_ql' or 'dymo'
        
    Returns:
        Backend class instance
    """
    backends = {
        'brother_ql': BrotherQLBackend,
        'dymo': DymoBackend,
    }
    
    if printer_type not in backends:
        raise ValueError(f"Unknown printer type: {printer_type}")
    
    return backends[printer_type]()
