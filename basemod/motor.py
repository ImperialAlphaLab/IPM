
class MOTOR():
    
    def __init__(self):
        self.Name = ""
        self.Pins = []
        self.State = False
        self.Position = []
        self.Cspeed = 0
        self.Caccel = 0
        self.Speedgraph = []
        self.Accelgraph = []
        
    def _activate(self):
        pass
    def _desactivate(self):
        pass
    def _record(self):
        pass
    def _srecord(self):
        pass
    def _get_name(self):
        return self.Name
    def _set_name(self, name):
        self.Name = name
    def _get_pos(self):
        return self.Position
    def _set_pos(self,pos):
        self.Position = pos
        
class STPMOTOR(MOTOR):
    
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
    
    
class SRVMOTOR(MOTOR):
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
    
