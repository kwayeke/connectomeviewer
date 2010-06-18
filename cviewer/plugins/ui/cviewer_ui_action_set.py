"""ConnectomeViewer action set for menus and actions

"""
# Copyright (C) 2009-2010, Ecole Polytechnique Federale de Lausanne (EPFL) and
# University Hospital Center and University of Lausanne (UNIL-CHUV)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# Partly added actions from mayavi_ui_action_set.py
# Author: Prabhu Ramachandran <prabhu [at] aero . iitb . ac . in>
# Copyright (c) 2008, Enthought, Inc. 
# License: BSD Style.

# Enthought library imports.
from enthought.envisage.ui.action.api import Action, Group, Menu, ToolBar
from enthought.envisage.ui.workbench.api import WorkbenchActionSet
from enthought.mayavi.core.registry import registry

########################################
# Groups

file_group = Group(
    id='ConnectomeFileGroup',
    path='MenuBar/File', 
    before='ExitGroup'
)

visualize_group = Group(
    id='VisualizeGroup',
    path='MenuBar/VisualizeMenu', 
)

modules_group = Group(
    id='ModulesGroup',
    path='MenuBar/VisualizeMenu/ModulesMenu', 
)

filters_group = Group(
    id='FiltersGroup',
    path='MenuBar/VisualizeMenu/FiltersMenu', 
)

########################################
# Menus

open_menu = Menu(
    id      = "LoadDataMenu",
    name    = "&Load data",
    path    = 'MenuBar/File',
    group   = 'ConnectomeFileGroup'
)

visualize_menu = Menu(
    id      = "VisualizeMenu",
    name    = "Visuali&ze",
    path    = "MenuBar",
    before  = "View"
)

modules_menu = Menu(
    id      = "ModulesMenu",
    name    = "&Modules",
    path    = "MenuBar/VisualizeMenu",
)

filters_menu = Menu(
    id      = "FiltersMenu",
    name    = "&Filters",
    path    = "MenuBar/VisualizeMenu",
    after   = "ModulesMenu",
)

plugins_menu = Menu(
    id      = "PluginsMenu",
    name    = "&Plugins",
    path    = "MenuBar",
    before  = "Help"
)

####################
# Source actions.

# MODIFY
open_file = Action(
    id            = "OpenFile",
    class_name    = "enthought.mayavi.action.sources.OpenFile",
    name          = "&Open file ...",
    path          =  "MenuBar/File/LoadDataMenu"
)

open_cff = Action(
    id            = "ConnectomeFile",
    name          = "&Connectome File ...",
    class_name    = "cviewer.action.load_cff:"
                    "OpenCFile",
    path          = "MenuBar/File/LoadDataMenu"
)
SOURCE_ACTIONS = [open_cff, open_file]

#
#for src in registry.sources:
#    if len(src.extensions) == 0:
#        action = Action(id=src.id,
#                        class_name="enthought.mayavi.action.sources." + src.id,
#                        name= src.menu_name,
#                        path="MenuBar/File/LoadDataMenu"
#                        )
#        SOURCE_ACTIONS.append(action)


####################
# Save/load actions.

save_viz = Action(
    id            = "SaveVisualization",
    class_name    = "enthought.mayavi.action.save_load.SaveVisualization",
    name          = "&Save Visualization",
    group         = "ConnectomeFileGroup",
    path          = "MenuBar/File",
)

load_viz = Action(
    id            = "LoadVisualization",
    class_name    = "enthought.mayavi.action.save_load.LoadVisualization",
    name          = "&Load Visualization",
    group         = "ConnectomeFileGroup",
    path          = "MenuBar/File",
)

####
# Building a schedule manager, might become a plugin

run_script = Action(
    id            = "RunScript",
    class_name    = "cviewer.action.run_script.RunScript",
    name          = "&Run Python Script",
    path          = "MenuBar/PluginsMenu/Scheduler",
)

########################################
# Visualize menu items.

add_mm = Action(
    id            = "AddModuleManager",
    class_name    = "enthought.mayavi.action.modules.AddModuleManager",
    name          = "&Add ModuleManager",
    path="MenuBar/VisualizeMenu",
    after="FiltersMenu"
)

########################################
# Modules.

MODULE_ACTIONS = []
for module in registry.modules:
    action = Action(id=module.id,
                    class_name="enthought.mayavi.action.modules." + module.id,
                    name= module.menu_name,
                    group = "ModulesGroup",
                    path="MenuBar/VisualizeMenu/ModulesMenu"
                    )
    MODULE_ACTIONS.append(action)

########################################
# Filter items.
########################################
FILTER_ACTIONS = []
for filter in registry.filters:
    action = Action(id=filter.id,
                    class_name="enthought.mayavi.action.filters." + filter.id,
                    name= filter.menu_name,
                    group = "FiltersGroup",
                    path="MenuBar/VisualizeMenu/FiltersMenu"
                    )
    FILTER_ACTIONS.append(action)

########################################
# Help menu items.


help_cviewer = Action(
    id            = "HelpCViewer",
    class_name    = "cviewer.action.help.HelpIndex",
    name          = "User Guide &ConnectomeViewer",
    path          = "MenuBar/Help"
)

help_index = Action(
    id            = "HelpIndex",
    class_name    = "enthought.mayavi.action.help.HelpIndex",
    name          = "User Guide &MayaVi2",
    path          = "MenuBar/Help"
)

bugfix = Action(
    id            = "Bugfix",
    class_name    = "cviewer.action.help.Bugfix",
    name          = "&Report Bugs ...",
    path          = "MenuBar/Help"
)

keybindings = Action(
    id            = "Keybindings",
    class_name    = "cviewer.action.help.Keybindings",
    name          = "&Key Bindings",
    path          = "MenuBar/Help"
)

tvtk_class_browser = Action(
    id            = "TVTKClassBrowser",
    class_name    = "enthought.mayavi.action.help.TVTKClassBrowser",
    name          = "&VTK Class Browser",
    path          = "MenuBar/Help",
)


################################################################################
# `CViewerUIActionSet` class.
################################################################################

class CViewerUIActionSet(WorkbenchActionSet):
    """ All the default actions available in the ConnectomeViewer UI """
    
    id = "cviewer.plugins.ui.action_set"
    
    groups  = [file_group,
               visualize_group,
               modules_group,
               filters_group,               
               #plugins_group,
               ]
    
    menus = [open_menu,
             visualize_menu,
             modules_menu,
             filters_menu,
             plugins_menu,
             ]
    
    actions = SOURCE_ACTIONS + \
              [save_viz, # Save load actions.
               load_viz,
               run_script,
               # Add module manager.
               add_mm,
              ] + \
              MODULE_ACTIONS + \
              FILTER_ACTIONS + \
              [help_cviewer,
               help_index,
               bugfix,
               keybindings,
               tvtk_class_browser,
              ]

