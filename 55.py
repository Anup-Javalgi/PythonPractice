# Variable scope : Were a variable is visible and accessible
# Scope resolution : (LEGB) Local -> Enclosed -> Global -> Built-in


def func1(a):
    a = 1
    print(a)

def func2():
    b = 2
    print(5)

func1(2)
func2()