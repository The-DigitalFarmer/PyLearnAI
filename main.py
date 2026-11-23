import sys

from methods import get_method

#Call function

if len(sys.argv) == 3:
    call_func = get_method(sys.argv[1], sys.argv[2])
    print(call_func)
else:
    print("Cantidad de comandos no válidos")
