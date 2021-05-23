from libqtile.layout.tile import Tile

class TileSingle(Tile):
    def configure(self, client, screen_rect):
        screen_width = screen_rect.width
        screen_height = screen_rect.height
        border_width = self.border_width if len(self.clients) > 1 else 0
        if self.clients and client in self.clients:
            pos = self.clients.index(client)
            if client in self.master_windows:
                w = int(screen_width * self.ratio) \
                    if len(self.slave_windows) or not self.expand \
                    else screen_width
                h = screen_height // self.master_length
                x = screen_rect.x
                y = screen_rect.y + pos * h
            else:
                w = screen_width - int(screen_width * self.ratio)
                h = screen_height // (len(self.slave_windows))
                x = screen_rect.x + int(screen_width * self.ratio)
                y = screen_rect.y + self.clients[self.master_length:].index(client) * h
            if client.has_focus:
                bc = self.border_focus
            else:
                bc = self.border_normal
            client.place(
                x,
                y,
                w - border_width * 2,
                h - border_width * 2,
                border_width,
                bc,
                margin=self.margin,
            )
            client.unhide()
        else:
            client.hide()

