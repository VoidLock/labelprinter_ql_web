#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
DYMO label specifications based on gLabels XML templates
Dimensions converted to pixels at 300 DPI (1mm = 11.811 pixels)
"""

# Conversion factor: 1mm = 11.811 pixels at 300 DPI
MM_TO_PIXELS = 11.811

def mm_to_px(mm):
    """Convert millimeters to pixels at 300 DPI"""
    return int(mm * MM_TO_PIXELS)

# DYMO Label Specifications
# Format: 'part_number': {
#     'name': 'Description',
#     'width_mm': width in mm,
#     'height_mm': height in mm,
#     'width_px': width in pixels,
#     'height_px': height in pixels,
#     'printable_width_px': printable width (accounting for margins),
#     'printable_height_px': printable height (accounting for margins),
#     'priority': 'high' | 'medium' | 'low'
# }

DYMO_LABEL_SPECS = {
    # High Priority Labels (Common Grocy Use Cases)
    '30252': {
        'name': '28mm x 89mm Address labels',
        'width_mm': 28,
        'height_mm': 89,
        'width_px': mm_to_px(28),
        'height_px': mm_to_px(89),
        'printable_width_px': mm_to_px(26),  # Markup-rect: w="26mm"
        'printable_height_px': mm_to_px(77),  # Markup-rect: h="77mm"
        'margin_left_px': mm_to_px(1),
        'margin_top_px': mm_to_px(6),
        'priority': 'high',
        'kind': 'die-cut'
    },
    '99010': {  # Equivalent to 30252
        'name': '28mm x 89mm Address labels',
        'width_mm': 28,
        'height_mm': 89,
        'width_px': mm_to_px(28),
        'height_px': mm_to_px(89),
        'printable_width_px': mm_to_px(26),
        'printable_height_px': mm_to_px(77),
        'margin_left_px': mm_to_px(1),
        'margin_top_px': mm_to_px(6),
        'priority': 'high',
        'kind': 'die-cut'
    },
    '30334': {
        'name': '57mm x 32mm Return address labels',
        'width_mm': 57,
        'height_mm': 32,
        'width_px': mm_to_px(57),
        'height_px': mm_to_px(32),
        'printable_width_px': mm_to_px(51),  # w - 2*3mm margin
        'printable_height_px': mm_to_px(26),  # h - 2*3mm margin
        'margin_left_px': mm_to_px(3),
        'margin_top_px': mm_to_px(3),
        'priority': 'high',
        'kind': 'die-cut'
    },
    '11354': {  # Equivalent to 30334
        'name': '57mm x 32mm Return address labels',
        'width_mm': 57,
        'height_mm': 32,
        'width_px': mm_to_px(57),
        'height_px': mm_to_px(32),
        'printable_width_px': mm_to_px(51),
        'printable_height_px': mm_to_px(26),
        'margin_left_px': mm_to_px(3),
        'margin_top_px': mm_to_px(3),
        'priority': 'high',
        'kind': 'die-cut'
    },
    '11352': {
        'name': '25mm x 54mm Return address labels',
        'width_mm': 25,
        'height_mm': 54,
        'width_px': mm_to_px(25),
        'height_px': mm_to_px(54),
        'printable_width_px': mm_to_px(23),  # Markup-rect: w="23mm"
        'printable_height_px': mm_to_px(42),  # Markup-rect: h="42mm"
        'margin_left_px': mm_to_px(1),
        'margin_top_px': mm_to_px(6),
        'priority': 'high',
        'kind': 'die-cut'
    },
    '99012': {
        'name': '36mm x 89mm Large address labels',
        'width_mm': 36,
        'height_mm': 89,
        'width_px': mm_to_px(36),
        'height_px': mm_to_px(89),
        'printable_width_px': mm_to_px(36),  # No margin
        'printable_height_px': mm_to_px(89),
        'margin_left_px': 0,
        'margin_top_px': 0,
        'priority': 'high',
        'kind': 'die-cut'
    },
    '99014': {
        'name': '54mm x 101mm Shipping address labels',
        'width_mm': 54,
        'height_mm': 101,
        'width_px': mm_to_px(54),
        'height_px': mm_to_px(101),
        'printable_width_px': mm_to_px(54),
        'printable_height_px': mm_to_px(101),
        'margin_left_px': 0,
        'margin_top_px': 0,
        'priority': 'high',
        'kind': 'die-cut'
    },
    
    # Medium Priority Labels
    '11353': {
        'name': '13mm x 25mm Multipurpose labels',
        'width_mm': 13,
        'height_mm': 25,
        'width_px': mm_to_px(13),
        'height_px': mm_to_px(25),
        'printable_width_px': mm_to_px(13),
        'printable_height_px': mm_to_px(25),
        'margin_left_px': 0,
        'margin_top_px': 0,
        'priority': 'medium',
        'kind': 'die-cut'
    },
    '11355': {
        'name': '19mm x 51mm Return address labels',
        'width_mm': 19,
        'height_mm': 51,
        'width_px': mm_to_px(19),
        'height_px': mm_to_px(51),
        'printable_width_px': mm_to_px(19),
        'printable_height_px': mm_to_px(51),
        'margin_left_px': 0,
        'margin_top_px': 0,
        'priority': 'medium',
        'kind': 'die-cut'
    },
    '30258': {
        'name': '54mm x 70mm Multipurpose labels',
        'width_mm': 54,
        'height_mm': 70,
        'width_px': mm_to_px(54),
        'height_px': mm_to_px(70),
        'printable_width_px': mm_to_px(54),
        'printable_height_px': mm_to_px(70),
        'margin_left_px': 0,
        'margin_top_px': 0,
        'priority': 'medium',
        'kind': 'die-cut'
    },
    '30332': {
        'name': '25mm x 25mm Square labels',
        'width_mm': 25,
        'height_mm': 25,
        'width_px': mm_to_px(25),
        'height_px': mm_to_px(25),
        'printable_width_px': mm_to_px(25),
        'printable_height_px': mm_to_px(25),
        'margin_left_px': 0,
        'margin_top_px': 0,
        'priority': 'medium',
        'kind': 'die-cut'
    },
    '99015': {
        'name': '54mm x 70mm Name badge labels',
        'width_mm': 54,
        'height_mm': 70,
        'width_px': mm_to_px(54),
        'height_px': mm_to_px(70),
        'printable_width_px': mm_to_px(54),
        'printable_height_px': mm_to_px(70),
        'margin_left_px': 0,
        'margin_top_px': 0,
        'priority': 'medium',
        'kind': 'die-cut'
    },
    
    # Lower Priority Labels
    '11356': {
        'name': '41mm x 89mm Name badge labels',
        'width_mm': 41,
        'height_mm': 89,
        'width_px': mm_to_px(41),
        'height_px': mm_to_px(89),
        'printable_width_px': mm_to_px(41),
        'printable_height_px': mm_to_px(89),
        'margin_left_px': 0,
        'margin_top_px': 0,
        'priority': 'low',
        'kind': 'die-cut'
    },
    '30256': {
        'name': '59mm x 102mm Address labels',
        'width_mm': 59,
        'height_mm': 102,
        'width_px': mm_to_px(59),
        'height_px': mm_to_px(102),
        'printable_width_px': mm_to_px(59),
        'printable_height_px': mm_to_px(102),
        'margin_left_px': 0,
        'margin_top_px': 0,
        'priority': 'low',
        'kind': 'die-cut'
    },
    '30327': {
        'name': '14mm x 87mm File folder labels',
        'width_mm': 14,
        'height_mm': 87,
        'width_px': mm_to_px(14),
        'height_px': mm_to_px(87),
        'printable_width_px': mm_to_px(14),
        'printable_height_px': mm_to_px(87),
        'margin_left_px': 0,
        'margin_top_px': 0,
        'priority': 'low',
        'kind': 'die-cut'
    },
    '30374': {
        'name': '51mm x 89mm Name badge labels',
        'width_mm': 51,
        'height_mm': 89,
        'width_px': mm_to_px(51),
        'height_px': mm_to_px(89),
        'printable_width_px': mm_to_px(51),
        'printable_height_px': mm_to_px(89),
        'margin_left_px': 0,
        'margin_top_px': 0,
        'priority': 'low',
        'kind': 'die-cut'
    },
    '30376': {
        'name': '14mm x 51mm Hanging folder labels',
        'width_mm': 14,
        'height_mm': 51,
        'width_px': mm_to_px(14),
        'height_px': mm_to_px(51),
        'printable_width_px': mm_to_px(14),
        'printable_height_px': mm_to_px(51),
        'margin_left_px': 0,
        'margin_top_px': 0,
        'priority': 'low',
        'kind': 'die-cut'
    },
    '30856': {
        'name': '62mm x 106mm Name badge labels',
        'width_mm': 62,
        'height_mm': 106,
        'width_px': mm_to_px(62),
        'height_px': mm_to_px(106),
        'printable_width_px': mm_to_px(62),
        'printable_height_px': mm_to_px(106),
        'margin_left_px': 0,
        'margin_top_px': 0,
        'priority': 'low',
        'kind': 'die-cut'
    },
    '30915': {
        'name': '41mm x 31mm Postage stamp labels',
        'width_mm': 41,
        'height_mm': 31,
        'width_px': mm_to_px(41),
        'height_px': mm_to_px(31),
        'printable_width_px': mm_to_px(33),  # Markup-rect: w="33mm"
        'printable_height_px': mm_to_px(24),  # Markup-rect: h="24mm"
        'margin_left_px': mm_to_px(1),
        'margin_top_px': mm_to_px(6),
        'priority': 'low',
        'kind': 'die-cut'
    },
    '99013': {
        'name': '36mm x 89mm Large address labels (transparent)',
        'width_mm': 36,
        'height_mm': 89,
        'width_px': mm_to_px(36),
        'height_px': mm_to_px(89),
        'printable_width_px': mm_to_px(36),
        'printable_height_px': mm_to_px(89),
        'margin_left_px': 0,
        'margin_top_px': 0,
        'priority': 'low',
        'kind': 'die-cut'
    },
    '99017': {
        'name': '12mm x 50mm Hanging folder labels',
        'width_mm': 12,
        'height_mm': 50,
        'width_px': mm_to_px(12),
        'height_px': mm_to_px(50),
        'printable_width_px': mm_to_px(12),
        'printable_height_px': mm_to_px(50),
        'margin_left_px': 0,
        'margin_top_px': 0,
        'priority': 'low',
        'kind': 'die-cut'
    },
    '99019': {
        'name': '59mm x 190mm Lever arch labels',
        'width_mm': 59,
        'height_mm': 190,
        'width_px': mm_to_px(59),
        'height_px': mm_to_px(190),
        'printable_width_px': mm_to_px(59),
        'printable_height_px': mm_to_px(190),
        'margin_left_px': 0,
        'margin_top_px': 0,
        'priority': 'low',
        'kind': 'die-cut'
    },
}

# List of label sizes for UI display (sorted by priority then size)
DYMO_LABEL_SIZES = []
for priority in ['high', 'medium', 'low']:
    for part_num, spec in sorted(DYMO_LABEL_SPECS.items()):
        if spec['priority'] == priority:
            DYMO_LABEL_SIZES.append((part_num, f"{part_num}: {spec['name']}"))
