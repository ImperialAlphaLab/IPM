from IPM.core.Basic import Basic
from imputil import rgb
from imputil import imprgbcode

class LED(Basic):
    is_ElectronicComposent = True
    
    def __init__(self):
        self.name = ""
        self.pin = 0
        self.currebtstate = False
        self.stategraph = []
        
    def record(self):
        pass
    
    def srecord(self):
        pass
    
    def get_state(self):
        return self.Cstate = False
    
    def activate(self):
        pass
    
    def desactivate(self):
        pass
    
class CLRLED(LED):
    
    def __init__(self):
        LED.__init__(self)
        self.CLR = rgb.RGB
        
    def _show_color(self, rgb):
        pass
    
    def _read_imprgbcode(self, imprgbcode):
        pass
