# import sys
from typing import Callable, Iterable, Iterator
def ft_filter(function:  Callable[[object], bool], iterable: Iterable) -> Iterator:
    # result = []
    # for elt in iterable:
    #     if function(elt):
    #         result.append(elt)
    # return result
    return [elt for elt in iterable if function(elt)]
