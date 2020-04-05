"""KeyIgnorer

The KeyIgnorer class will ignore any attempts to set a key that is already set.
"""
class KeyIgnorer(dict):
    '''
    >>> keyIgnorer = KeyIgnorer()
    >>> keyIgnorer[0] = 0
    >>> keyIgnorer[0] = 1
    >>> keyIgnorer[0]
    0
    '''
    def __init__(self):
        dict.__init__(self)
    
    def __setitem__(self, key, value):
        if key not in self:
            dict.__setitem__(self, key, value)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
