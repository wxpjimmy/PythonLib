#http://python.net/~goodger/projects/pycon/2007/idiomatic/handout.html
l = ['David', 'Pythonista', '+1-514-555-1234']
name, title, phone = l
print name
print title
print phone
people = [l, ['Guido', 'BDFL', 'unlisted']]
for (name, title, phone) in people:
    print name, phone

david, (gname, gtitle, gphone) = people
print gname
print gtitle
print gphone
print david
#Tuples
a = 1,
print a
b = ()
print b
#interactive_, _ stores the last printed expression
#_ can only be used in interactive mode
colors = ['red', 'blue', 'green', 'yellow']
result = ', '.join(colors)
print result
print 'Choose', ', '.join(colors[:-1]), 'or', colors[-1]
#dictionary get method with default value d.get(key, 0)
#use if key in d:... instead of if d.has_key(key):...
#Dictionary setdefault method == get, or set&get
#defaultdict
from collections import defaultdict
p = defaultdict(list)
data = [['jimmy', 32], ['sunshine', 21], ['jimmy', 34]]
for (port, equity) in data:
    p[port].append(equity)

print p
#building/spliting dictionaries
import pprint
given = ['John', 'Eric', 'Terry', 'Michael']
family = ['Cleese', 'Idle', 'Gilliam', 'Palin']
pythons = dict(zip(given, family))
pprint.pprint(pythons)
#test truth value
#use if x: instead of if x == True:
#for lists: use if items: instead of if len(items) == 0: or if items != []:
#advanced % String Formatting
values = {'name': 'jimmy', 'messages': 50}
print ('Hello %(name)s, you have %(messages)i messages' % values)
pprint.pprint(locals())
#pprint.pprint(pprint.__dict__)
#list comprehension (greedy)
lc = [n ** 2 for n in range(10) if n % 2]
print lc
#generator expression (lazy)
total = sum(num * num for num in xrange(1, 101))
print total
#generator expression2
month_codes = dict((fn(i+1), code) for i, code in enumerate('FGHJKMNQUVXZ')
        for fn in (int, str))
print month_codes
#sorting
def custom_cmp(item1, item2):
    return cmp((item1[1], item1[3]), (item2[1], item2[3]))

#a_list.sort(custom_cmp)
#sorting with keys
def my_key(item):
    return (item[1], item[3])

#a_list.sort(key=my_key)
#Generators, define your own generators
def my_range_generator(stop):
    value = 0
    while value < stop:
        yield value
        value += 1

for i in my_range_generator(10):
    print i
else:
    print 'iterate is done!'

#generator example, csv reader filter blank rows
def filter_rows(row_iterator):
    for row in row_iterator:
        if row:
            yield row

#data_file = open(path, 'rb')
#irows = filter_rows(csv.reader(data_file))
#datafile = open('datafile')
#for line in datafile:
#    do_something(line)
#try/except clause
#try:
#    return str(x)
#except TypeError:
#    ...
#import long_module_name as mod
# to make a simultaneously importable module and executable script:
#if __name__ == '__main__'
#     script code here

#module structure
#"""module docstring"""

# imports
# constants
# exception classes
# interface functions
# classes
# internal functions & classes

#def main(...):
#    ...

#if __name__ == '__main__':
#    status = main()
#    sys.exit(status)

