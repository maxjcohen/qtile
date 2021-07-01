import re

from libqtile.widget import base


class Wifi(base.ThreadPoolText):

    """Displays wifi connection details."""

    defaults = [
        ("update_interval", 0.2, "Seconds between status updates"),
    ]

    def __init__(self, **config):
        super().__init__("", **config)
        self.add_defaults(self.defaults)

    def poll(self) -> str:
        iw_output = self.call_process("iw dev".split())
        ssid_regex = "ssid (?P<ssid>\w+)"
        try:
            return re.search(ssid_regex, iw_output).groupdict()["ssid"]
        except AttributeError:
            return ""
