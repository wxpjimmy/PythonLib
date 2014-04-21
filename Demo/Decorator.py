
class EntryExist(object):
    def __init__(self, func):
        self.func = func

    def __call__(self):
        print "Entering ", self.func.__name__
        self.func()
        print "Exited ", self.func.__name__


@EntryExist
def func1():
    print "inside func1()"

@EntryExist
def func2():
    print "inside func2()"


func1()
func2()
