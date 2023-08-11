import neopixel
import settings

lvl1 = (0, 255, 0)
lvl2 = (156, 247, 9)
lvl3 = (244, 200, 12)
lvl4 = (255, 128, 1)
lvl5 = (255, 0, 0)

def apply_strength(color:tuple[int, int, int], strength:float) -> tuple[int, int, int]:
    r = max(min(int(round(color[0] * strength, 0)), 255), 0)
    g = max(min(int(round(color[1] * strength, 0)), 255), 0)
    b = max(min(int(round(color[2] * strength, 0)), 255), 0)
    return (r, g, b)

class NeopixelEngine:
    
    def __init__(self) -> None:
        self.pix = neopixel.Neopixel(5, 0, settings.neopixel_pin, "GRB")
        self.strength:float = 0.50 # LED brightness strenght as a percentage (for dimming). So 1.0 = full brightness

    def show_level(self, level:int) -> None:

        if level == 1:
            self.pix.set_pixel(0, apply_strength(lvl1, self.strength))
            self.pix.set_pixel(1, (0, 0, 0))
            self.pix.set_pixel(2, (0, 0, 0))
            self.pix.set_pixel(3, (0, 0, 0))
            self.pix.set_pixel(4, (0, 0, 0))
            self.pix.show()
        elif level == 2:
            self.pix.set_pixel(0, apply_strength(lvl1, self.strength))
            self.pix.set_pixel(1, apply_strength(lvl2, self.strength))
            self.pix.set_pixel(2, (0, 0, 0))
            self.pix.set_pixel(3, (0, 0, 0))
            self.pix.set_pixel(4, (0, 0, 0))
            self.pix.show()
        elif level == 3:
            self.pix.set_pixel(0, apply_strength(lvl1, self.strength))
            self.pix.set_pixel(1, apply_strength(lvl2, self.strength))
            self.pix.set_pixel(2, apply_strength(lvl3, self.strength))
            self.pix.set_pixel(3, (0, 0, 0))
            self.pix.set_pixel(4, (0, 0, 0))
            self.pix.show()
        elif level == 4:
            self.pix.set_pixel(0, apply_strength(lvl1, self.strength))
            self.pix.set_pixel(1, apply_strength(lvl2, self.strength))
            self.pix.set_pixel(2, apply_strength(lvl3, self.strength))
            self.pix.set_pixel(3, apply_strength(lvl4, self.strength))
            self.pix.set_pixel(4, (0, 0, 0))
            self.pix.show()
        elif level == 5:
            self.pix.set_pixel(0, apply_strength(lvl1, self.strength))
            self.pix.set_pixel(1, apply_strength(lvl2, self.strength))
            self.pix.set_pixel(2, apply_strength(lvl3, self.strength))
            self.pix.set_pixel(3, apply_strength(lvl4, self.strength))
            self.pix.set_pixel(4, apply_strength(lvl5, self.strength))
            self.pix.show()
        else:
            raise Exception("Neopixel level must be 1, 2, 3, 4, or 5")
    