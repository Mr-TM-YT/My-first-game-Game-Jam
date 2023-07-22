import pygame as pg


class Camera:
    def __init__(self, width, height):
        self.camera_rect = pg.Rect(0, 0, width, height)

    def apply(self, enity):
        return enity.rect.move(self.camera_rect_topleft)

    def update(self, target):
        x = -target.rect.x + int(target.rect.width / 2)
        y = -target.rect.y + int(target.rect.height / 2)

        # Limit the camera movement to keep the player within the window
        x = min(0, x)  # Left boundary
        y = min(0, y)  # Top boundary
        # Right boundary
        x = max(-(self.camera_rect.width - target.rect.width), x)
        # Bottom boundary
        y = max(-(self.camera_rect.height - target.rect.height), y)

        self.camera_rect = pg.Rect(
            x, y, self.camera_rect.width, self.camera_rect.height)
