from ipm.core.basic import Basic


class Motor(Basic):
    
    def __init__(self, name):
        self._name = ""
        self._pins = []
        self._state = False
        self._position = []
        self._cspeed = 0
        self._caccel = 0
        self._speedgraph = []
        self._accelgraph = []
        
    def activate(self):
        pass
    
    def desactivate(self):
        pass
    
    def record(self):
        pass
    
    def srecord(self):
        pass
    
    @property
    def position(self):
        return self._position
    
    @property
    def position(self, newpos):
        self._position = newpos
    
        
class StepperMotor(Motor):
    
    def __init__(self):
        MOTOR.__init__(self)
        self.Adjstep = 1
        self.Cangle = 0
    def _move_step(self, step=1):
        pass
    def _move_adjstep(self, ntimes=1):
        pass
    def _move_angle(self, angle=15):
        pass
    def _set_speed(self, speed):
        pass
    def _linear_speed(self, linearity, speed):
        pass
    def trigonomitric_speed(self, eq):
        pass
    
    
class ServoMotor(Motor):
    def __init__(self):
        MOTOR.__init__(self)
        self.Cangle = 0
        self.Canglegraph = 0
    def _record_ang(self):
        pass
    def _move_to_angle(self, angle=15):
        pass
    def _home(self):
        self._move_to_angle(0)
        
        
class BRSMOTOR(MOTOR):
    def __init__(self):
        MOTOR.__init__(self)
        pass
    
