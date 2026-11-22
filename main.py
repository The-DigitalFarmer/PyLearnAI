import sys

from methods import get_method

#Call function
call_func = get_method(sys.argv[1], sys.argv[2])
print(call_func)
