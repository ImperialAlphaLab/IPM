
from .core import BasicMeta, with_metaclass

class Basic(with_metaclass(BasicMeta)):
    is_ElectronicComposent = False
    is_Signal = False
    is_Mecanico = False
    
    
    __slots__ = ['_name', '_pins', '_args']
    
    def __new__(cls, *args):
        obj = object.__new__(cls)
        obj._mhash = None  # will be set by __hash__ method.
        obj._args = args  # all items in args must be Basic objects
        return obj
    
    def __eq__(self, other):
        pass
    
    def __ne__(self, other):
        pass
    
    def __str__(self):
        pass
    
    __repr__ = __str__
    
    
    @property
    def pins(self):
        return self._pins
    
    @pins.setter
    def pins(self, pins):
        self._pins = pins
        
    def turn_on(self):
        pass
    
    def turn_off(self):
        pass
    
    @property
    def gcenter(self):
        return self._args['gcenter']
    
    @gcenter.setter
    def gcenter(self, gc):
        self._args['gcenter'] = gc
        
    @property
    def vect(self):
        return self._args['vect']
    
    @vect.setter
    def vect(self, vec):
        return self._aegs['vect'] = vec
    
    
    
    
    
