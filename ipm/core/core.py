ordering_of_classes = []

all_classes = set()

class BasicMeta(type):

    def __init__(cls, *args, **kws):
        all_classes.add(cls)

    def __cmp__(cls, other):
        # If the other object is not a Basic subclass, then we are not equal to
        # it.
        if not isinstance(other, BasicMeta):
            return -1
        n1 = cls.__name__
        n2 = other.__name__
        if n1 == n2:
            return 0

        UNKNOWN = len(ordering_of_classes) + 1
        try:
            i1 = ordering_of_classes.index(n1)
        except ValueError:
            i1 = UNKNOWN
        try:
            i2 = ordering_of_classes.index(n2)
        except ValueError:
            i2 = UNKNOWN
        if i1 == UNKNOWN and i2 == UNKNOWN:
            return (n1 > n2) - (n1 < n2)
        return (i1 > i2) - (i1 < i2)

    def __lt__(cls, other):
        if cls.__cmp__(other) == -1:
            return True
        return False

    def __gt__(cls, other):
        if cls.__cmp__(other) == 1:
            return True
        return False
    
    def __eq__(cls, other):
        if cls.__com__(other) == 0:
            return True
        return False



def with_metaclass(meta, *bases):

    class metaclass(meta):
        def __new__(cls, name, bases, d):
            return meta(name, bases, d)
    return type.__new__(metaclass, "NewBase", (), {})
