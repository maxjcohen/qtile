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

from libqtile import qtile
from libqtile.widget import base


class VolumePulse(base.ThreadPoolText):
    """Widget that display and change volume based on pactl"""

    orientations = base.ORIENTATION_HORIZONTAL
    defaults = [
        ("update_interval", 1, "Update time in seconds."),
        ("padding", 3, "Padding left and right. Calculated if None."),
    ]

    def __init__(self, **config):
        super().__init__("", **config)
        self.add_defaults(self.defaults)

        self.add_callbacks({
            'Button1': lambda: qtile.cmd_spawn('st -e pulsemixer'),
        })

    def get_volume(self):
        get_volume_cmd = "pactl get-sink-volume @DEFAULT_SINK@"
        pactl_output = self.call_process(get_volume_cmd.split())

        volume_regex = "(?P<volume>\w+)%"
        try:
            return int(re.search(volume_regex, pactl_output).groupdict()["volume"])
        except AttributeError:
            return 0

    def get_mute(self):
        get_mute_cmd = ["pulsemixer", "--get-mute"]
        get_mute_cmd = "pactl get-sink-mute @DEFAULT_SINK@"
        return self.call_process(get_mute_cmd.split()) == "Mute: no\n"

    def poll(self):
        mute = self.get_mute()
        volume = self.get_volume()
        if mute:
            icon = ""
        elif volume >= 66:
            icon = ""
        elif volume > 0:
            icon = ""
        else:
            icon = ""

        return f"{icon} {volume}%"
