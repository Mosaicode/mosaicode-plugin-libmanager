#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the LibManagerMenu class.
"""
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from mosaicode.model.plugin import Plugin
from mosaicode_plugin_libmanager.GUI.blockeditor import BlockEditor
from mosaicode.system import System as System
import gettext

_ = gettext.gettext

class BlockMenuItem(Gtk.MenuItem):
    """
    This class contains methods related the LibManagerMenu
    """
    # ----------------------------------------------------------------------

    def __init__(self, main_window):
        """Constructor."""
        Gtk.MenuItem.__init__(self, "Edit Block")
        self.main_window = main_window
        self.connect("activate", self.__edit_clicked)

    # ----------------------------------------------------------------------
    def __edit_clicked(self, args):
        """
        This method monitors if the button delete was clicked.

            Parameters:
            * **args**

        """
        BlockEditor(self.main_window,
            System.blocks[self.main_window.block_menu.block.type])

