"""foldr implemented on iterables
fn : ('a * 'b -> 'b) -> 'b -> 'a list -> 'b

Keyword arguments:
func -- function that takes 2 arguments
initial -- initial value for the base case
xs - Iterable collection
"""
def foldr(func, initial, xs):
    '''
    >>> foldr(lambda acc, x: [x] + acc, [], [1, 2, 3, 4])
    [1, 2, 3, 4]
    '''
    def foldrr(func, initial, xs):
        try:
            x = next(xs)
            return func(foldrr(func, initial, xs), x)
        except StopIteration:
            return initial

    return foldrr(func, initial, iter(xs))

"""foldl implemented on iterables
('a * 'b -> 'b) -> 'b -> 'a list -> 'b

Keyword arguments:
func -- function that takes 2 arguments
initial -- initial value for the base case
xs - Iterable collection
"""
def foldl(func, initial, xs):
    '''
    >>> foldl(lambda acc, x: [x] + acc, [], [1, 2, 3, 4])
    [4, 3, 2, 1]
    '''
    def foldlr(func, initial, xs):
        try:
            x = next(xs)
            return foldlr(func, func(initial, x), xs)
        except StopIteration:
            return initial

    return foldlr(func, initial, iter(xs))

if __name__ == "__main__":
    import doctest
    doctest.testmod()
