# Copyright 2021 Cadwork.
# All rights reserved.
# This file is part of VolumeAttribute,
# and is released under the "MIT License Agreement". Please see the LICENSE
# file that should have been included as part of this package.

import sys
import attribute_controller as ac
import element_controller as ec
import geometry_controller as gc
import utility_controller as uc
import visualization_controller as vc

# get active elements
active_elements = ec.get_active_identifiable_element_ids()
uc.print_to_console(str(active_elements))

if len(active_elements) == 0:
    uc.print_error('No element selected')
    sys.exit()

# create allowed element list
active_allowed = []
for element in active_elements:
    if ac.is_wall(element):
        active_allowed.append(element)
    elif ac.is_floor(element):
        active_allowed.append(element)
    elif ac.is_roof(element):
        active_allowed.append(element)
    elif ac.is_beam(element):
        active_allowed.append(element)
    elif ac.is_panel(element):
        active_allowed.append(element)

vc.set_inactive(active_elements)
vc.set_active(active_allowed)
vc.refresh()

# volume in attribute 16
for element in active_allowed:
    volume_cube_mm = gc.get_volume(element)
    volume = volume_cube_mm / 1000000000
    ac.set_user_attribute([element], 16, "%.2f" % volume)

uc.print_error("Volume (m³) saved in user attribute 16...")
