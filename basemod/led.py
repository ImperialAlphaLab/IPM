from imputil import rgb
from imputil import imprgbcode

class LED():
    def __init__(self):
        self.Name = ""
        self.Pin = 0
        self.Cstate = False
        self.Stategraph
    def _record(self):
        pass
    def _srecord(self):
        pass
    def _get_state(self):
        return self.Cstate = False
    def _turn_on(self):
        pass
    def _turn_off(self):
        pass
    def _activate(self):
        pass
    def _desactivate(self):
        pass
    
class CLRLED(LED):
    def __init__(self):
        LED.__init__(self)
        self.CLR = rgb.RGB
    def _show_color(self, rgb):
        pass
    def _read_imprgbcode(self, imprgbcode)
