#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Label specifications modules
"""

__all__ = []

# Try to import Brother QL specs (optional, depends on brother_ql library)
try:
    from .brother_ql_specs import BROTHER_QL_LABEL_SPECS
    __all__.append('BROTHER_QL_LABEL_SPECS')
except ImportError:
    BROTHER_QL_LABEL_SPECS = None

# DYMO specs don't require external dependencies
from .dymo_specs import DYMO_LABEL_SPECS
__all__.append('DYMO_LABEL_SPECS')

