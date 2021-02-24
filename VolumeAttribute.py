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
import menu_controller as mc

# get active elements
active_elements = ec.get_active_identifiable_element_ids()
uc.print_to_console(str(active_elements))

if len(active_elements) == 0:
    uc.print_error('No element selected')
    sys.exit()

uc.print_message('Select desired output units?', 1, 1)
menu_selection_units = mc.display_simple_menu(['mm³', 'cm³', 'm³', 'in³', 'ft³'])

conversion_factor = 1

if menu_selection_units == 'mm³':
    conversion_factor = 1
elif menu_selection_units == 'cm³':
    conversion_factor = 1000
elif menu_selection_units == 'm³':
    conversion_factor = 1000000000
elif menu_selection_units == 'in³':
    conversion_factor = 16387
elif menu_selection_units == 'ft³':
    conversion_factor = 28320000

user_attribute_selection = uc.get_user_int('Enter user attribute number?')

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

# volume in required attribute
for element in active_allowed:
    volume_cube_mm = gc.get_volume(element)
    volume = volume_cube_mm / conversion_factor
    ac.set_user_attribute([element], user_attribute_selection, "%.2f" % volume)

uc.print_error("Volume (%s) saved in user attribute %d..." % (menu_selection_units, user_attribute_selection))
