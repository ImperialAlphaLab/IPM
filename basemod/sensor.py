class SENSOR():
    def __init__(self):
        self.Name = ""
        self.Pin = 0
        self.Pos = []
    
    def _get_pin(self):
        return self.Pin
    def _set_pin(self,x):
        self.Pin = x
    def _get_name(self):
        return self.Name
    def _set_name(self, nom):
        self.Name = nom 
    def _get_pos(self):
        return self.Pos
    def _set_pos(self, t):
        self.Pos = t
    def _activate(self):
        pass
    def _desactivate(self):
        pass
    def _record(self):
        pass
    def _srecord(self):
        pass
    
class TSENSOR(SENSOR):
    def __init__(self):
        SENSOR.__init__(self)
        self.Temperature = 0
            self.Temperaturegraph = []
    def _temperatureC(self):
        pass
    def _temperatureF(self):
        pass
class VSENSOR(SENSOR):
    def __init__(self):
        SENSOR.__init__(self)
        self.Velocity = 0
        self.Velocitygraph = []
    
    def _velocityms(self):
        pass
    def _velocitymms(self):
        pass
class LSENSOR(SENSOR):
    def __init__(self):
        SENSOR.__init__(self)
        self.Level = 0
        self.Levelgraph = []
    def _levelm(self):
        pass
class SENSOR():
    def __init__(self):
        self.Name = ""
        self.Pin = 0
        self.Pos = []
    
    def _get_pin(self):
        return self.Pin
    def _set_pin(self,x):
        self.Pin = x
    def _get_name(self):
        return self.Name
    def _set_name(self, nom):
        self.Name = nom 
    def _get_pos(self):
        return self.Pos
    def _set_pos(self, t):
        self.Pos = t
    def _activate(self):
        pass
    def _desactivate(self):
        pass
    def _record(self):
        pass
    def _srecord(self):
        pass
    
class TSENSOR(SENSOR):
    def __init__(self):
        SENSOR.__init__(self)
        self.Temperature = 0
            self.Temperaturegraph = []
    def _temperatureC(self):
        pass
    def _temperatureF(self):
        pass
class VSENSOR(SENSOR):
    def __init__(self):
        SENSOR.__init__(self)
        self.Velocity = 0
        self.Velocitygraph = []
    
    def _velocityms(self):
        pass
    def _velocitymms(self):
        pass
class LSENSOR(SENSOR):
    def __init__(self):
        SENSOR.__init__(self)
        self.Level = 0
        self.Levelgraph = []
    def _levelm(self):
        pass
class STATESNESOR(SENSOR):
    def __init__(self):
        SENSOR.__init__(self)
        self.State = False
        self.Stategraph = []
    def _get_state(self):
        return self.State
    
