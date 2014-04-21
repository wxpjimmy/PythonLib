def entry_exit(func):
    def wrapper():
        print "Entering", func.__name__
        func()
        print "Exited", func.__name__
#    wrapper.__name__ = func.__name__
    return wrapper


@entry_exit
def func1():
    print "inside func1()"

@entry_exit
def func2():
    print "inside func2()"


func1()
func2()
print func1.__name__
