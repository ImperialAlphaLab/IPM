from basemod import motor
from basemod import sensor
from imputil import point
from imputil import speed

class AXIS():
    def __init__(self):
        self.Name = ""
        self.Motor = motor.STPMOTOR()
        self.Sensor = sensor.STATESENSOR()
        self.Speed = speed.SPEED(self.Motor)
    def _set_name(self, name):
        self.Name = name
    def _set_speed(self, speed):
        pass
    def _set_step(self, step):
        pass
    def _move_step(self, ntimes):
        pass
    def _activate(self):
        pass
    def _desactivate(self):
        pass
    

    
class LINAXIS(AXIS):
    def __init__(self):
        AXIS.__init__(self)
        self.Axisposition = []
        self.Uniposition = 0
        self.Maxposition = 1
        self.Axispositionrecord = []
    def _move_to_pos(self, pos):
        pass
    def _record(self):
        pass
    def _srecord(self):
        pass
    
class ROTAXIS(AXIS):
    def __init__(self):
        AXIS.__init__(self)
        self.Axisangle = []
        self.Uniposition = 0
        self.Period = 1
    def _move_to_angle(self):
        pass
    def _rotate(self, ntimes):
        pass
        
