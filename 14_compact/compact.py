def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """

#    `0`, `0.0`, `""`, ***None***, ***False***
#  `[]` (empty list), `{}` (empty dictionary), `set()` (empty set)

    return [value for value in lst if value]
print(compact([0, 1, 2, '', [], False, (), None, 'All done']))
