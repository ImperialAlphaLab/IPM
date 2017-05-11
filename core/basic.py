
from .core import BasicMeta, with_metaclass

class Basic(with_metaclass(BasicMeta)):
    is_ElectronicComposent = False
    is_Solid = False
    
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
    
    
    
    
