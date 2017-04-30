

from basemod import axis
from imputil import point
from basemod import laser

class CNCXY():
    def __init__(self):
        self.Name = ""
        self.AxisX = axis.LINAXIS()
        self.AxisY = axis.LINAXIS()
        self.Position = point.POINT(0,0,0)
        self.Limitposition = point.POINT(0,0,0)
        self.Posgraph = []
    def _record(self):
        pass
    def _srecord(self):
        pass
    def _goto(self, pos):
        pass
    def _execute(self, code):
        pass
    
class PENCNC(CNCXY):
    def __init__(self):
        CNCXY.__init__(self)
        self.Fontsize = 0
        self.Style = ''
    def _write(self, text, style=self.Style):
        pass
    
class LASCNC(CNCXY):
    def __init__(self):
        CNCXY.__init__(self)
        self.Large = 0
        self.LASER = laser.CUTLASER()
        self.State = False
    def _cut_line(self, line):
        pass
    def _cut_code(self, code):
        pass
