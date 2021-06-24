# Copyright (c) 2021 Max Cohen
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import re
import subprocess

from libqtile import bar
from libqtile.widget import base

__all__ = [
    "Volume",
]

re_vol = re.compile(r"\[(\d?\d?\d?)%\]")


class VolumePulse(base._TextBox):
    """Widget that display and change volume based on pulsemixer"""

    orientations = base.ORIENTATION_HORIZONTAL
    defaults = [
        ("update_interval", 0.2, "Update time in seconds."),
        ("padding", 3, "Padding left and right. Calculated if None."),
    ]

    def __init__(self, **config):
        super().__init__("0", width=bar.CALCULATED, **config)
        self.add_defaults(self.defaults)
        self.volume = None

    def timer_setup(self):
        self.timeout_add(self.update_interval, self.update)

    def update(self):
        vol = self.get_volume()
        if vol != self.volume:
            self.volume = vol
            # Update the underlying canvas size before actually attempting
            # to figure out how big it is and draw it.
            self._update_drawer()
            self.bar.draw()
        self.timeout_add(self.update_interval, self.update)

    def get_volume(self):
        get_volume_cmd = ["pulsemixer", "--get-volume"]
        return int(self.call_process(get_volume_cmd).split()[0])

    def _update_drawer(self):
        if self.volume >= 66:
            icon = ""
        elif self.volume > 0:
            icon = ""
        else:
            icon = ""

        self.text = f"{icon} {self.volume}%"
