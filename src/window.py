# window.py
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

from pathlib import Path

from gi.repository import Gtk


@Gtk.Template(resource_path='/org/croissantproject/Croissant/window.ui')
class CroissantWindow(Gtk.ApplicationWindow):
    __gtype_name__ = 'CroissantWindow'

    dock = Gtk.Template.Child()
    grid = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        pages = [
            'cr-home',
            'cr-library',
            'cr-media',
            'cr-news',
            'cr-notes',
            'cr-profile',
            'cr-settings',
        ]
        for page in pages:
            img = Gtk.Image.new()
            img.set_from_icon_name(page)
            img.set_pixel_size(64)

            btn = Gtk.Button.new()
            btn.add_css_class('pastry-overlay-button')
            btn.set_child(img)

            self.dock.append(btn)

        posters = []
        poster_dir = Path('/var/home/eva/gameposters/')
        for fpath in poster_dir.rglob('*.png'):
            if fpath.is_file():
                posters.append(str(fpath.absolute()))

        def add_poster(path, x, y, w, h):
            pic = Gtk.Picture.new_for_filename(path)
            pic.add_css_class('game-poster')
            pic.set_focusable(True)
            pic.set_content_fit(Gtk.ContentFit.CONTAIN)

            self.grid.attach(pic, x, y, w, h)

        for i, poster in enumerate(posters):
            add_poster(poster, i % 6, i // 6 , 1, 1)
