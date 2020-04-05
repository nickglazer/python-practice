from collections import OrderedDict
import copy

"""DefaultOrderedDict

Adds defaults to the collections.OrderedDict
"""
class DefaultOrderedDict(OrderedDict):
    '''
    >>> defaultOrderedDict = DefaultOrderedDict('Default')
    >>> defaultOrderedDict[0] = 0
    >>> defaultOrderedDict[1]
    'Default'
    '''
    def __init__(self, default):
        OrderedDict.__init__(self)
        self.default = default
                
    def __getitem__(self, key):
        if key in self:
            return self[key]
        else:
            newDefault = self.default() if callable(self.default) else self.default
            self.__setitem__(key, newDefault)
            return newDefault

    def __copy__(self):
        return DefaultOrderedDict(self.default)

    def __deepcopy__(self, memo):
        return DefaultOrderedDict(copy.deepcopy(self.default, memo))
    
    def __repr__(self):       
        return OrderedDict.__repr__(self) + ', Default: ' + repr(self.default)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
