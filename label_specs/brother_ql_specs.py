#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Brother QL label specifications
Re-export from brother_ql library for consistency
"""

from brother_ql.devicedependent import label_type_specs, label_sizes

BROTHER_QL_LABEL_SPECS = {
    'label_type_specs': label_type_specs,
    'label_sizes': label_sizes
}
