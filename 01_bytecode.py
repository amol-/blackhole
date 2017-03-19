# According to https://docs.python.org/3/reference/expressions.html#operator-precedence
# the two should evaluate the same as evalutaion order is from left to right

def func():
    return True == False in [False, 5]
print(func())

def func2():
    return (True == False) in [False, 5]
print(func2())

# Why they lead to two different results?
import dis
dis.dis(func)
dis.dis(func2)

# Becuase in case 1 what's really happening is
def func3():
    return True == False and False in [False, 5]
print(func())

dis.dis(func3)
