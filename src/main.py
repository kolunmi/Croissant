# main.py
#
# Copyright 2025 Eva
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
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later

import sys
import gi

gi.require_version('Gtk', '4.0')
gi.require_version('Pastry', '0.1')

from gi.repository import Gtk, Gdk, Gio, Pastry
from .window import CroissantWindow
from .globals import CrGlobals, CrGame


class CroissantApplication(Gtk.Application):
    """The main application singleton class."""

    def __init__(self):
        super().__init__(application_id='org.croissantproject.Croissant',
                         flags=Gio.ApplicationFlags.DEFAULT_FLAGS,
                         resource_base_path='/org/croissantproject/Croissant')

        self.create_action('quit', lambda *_: self.quit(), ['<control>q'])
        self.create_action('about', self.on_about_action)
        self.create_action('preferences', self.on_preferences_action)

        css_provider = Gtk.CssProvider.new()
        css_provider.load_from_resource('/org/croissantproject/Croissant/style.css')

        Gtk.StyleContext.add_provider_for_display(
            Gdk.Display.get_default(),
            css_provider,
            600,
        )

        self.globals = CrGlobals()

        self.globals.games = Gio.ListStore()
        self.globals.games.append(CrGame(name="antonblast", coverart="/home/kol/Pictures/croissant/game icons/antonblast.png"))
        self.globals.games.append(CrGame(name="hollowknight", coverart="/home/kol/Pictures/croissant/game icons/hollowknight.png"))
        self.globals.games.append(CrGame(name="nmf", coverart="/home/kol/Pictures/croissant/game icons/nmf.jpg"))
        self.globals.games.append(CrGame(name="pizzatower", coverart="/home/kol/Pictures/croissant/game icons/pizzatower.jpg"))
        self.globals.games.append(CrGame(name="ufo 50", coverart="/home/kol/Pictures/croissant/game icons/ufo 50.jpg"))
        self.globals.games.append(CrGame(name="VotV", coverart="/home/kol/Pictures/croissant/game icons/VotV.png"))
        self.globals.games.append(CrGame(name="balatro", coverart="/home/kol/Pictures/croissant/game icons/balatro.png"))
        self.globals.games.append(CrGame(name="hypnospace", coverart="/home/kol/Pictures/croissant/game icons/hypnospace.jpg"))
        self.globals.games.append(CrGame(name="oneshot", coverart="/home/kol/Pictures/croissant/game icons/oneshot.jpg"))
        self.globals.games.append(CrGame(name="SLARPG", coverart="/home/kol/Pictures/croissant/game icons/SLARPG.png"))
        self.globals.games.append(CrGame(name="uncannycatgolf", coverart="/home/kol/Pictures/croissant/game icons/uncannycatgolf.png"))

    def do_activate(self):
        """Called when the application is activated.

        We raise the application's main window, creating it if
        necessary.
        """
        win = self.props.active_window
        if not win:
            win = CroissantWindow(application=self, globals=self.globals)
        win.present()

    def on_about_action(self, *args):
        """Callback for the app.about action."""
        about = Gtk.AboutDialog(transient_for=self.props.active_window,
                                modal=True,
                                program_name='croissant',
                                logo_icon_name='org.croissantproject.Croissant',
                                version='0.1.0',
                                authors=['Eva'],
                                copyright='© 2025 Eva')
        # Translators: Replace "translator-credits" with your name/username, and optionally an email or URL.
        about.set_translator_credits(_('translator-credits'))
        about.present()

    def on_preferences_action(self, widget, _):
        """Callback for the app.preferences action."""
        print('app.preferences action activated')

    def create_action(self, name, callback, shortcuts=None):
        """Add an application action.

        Args:
            name: the name of the action
            callback: the function to be called when the action is
              activated
            shortcuts: an optional list of accelerators
        """
        action = Gio.SimpleAction.new(name, None)
        action.connect("activate", callback)
        self.add_action(action)
        if shortcuts:
            self.set_accels_for_action(f"app.{name}", shortcuts)


def main(version):
    """The application's entry point."""
    Pastry.init()
    app = CroissantApplication()
    return app.run(sys.argv)
