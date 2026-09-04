import re
a = ['data.dat',
    'data1.dat',
    'data2.dat',
    'data12.dat',
    'datax.dat',
     'dataXYZ.dat',
     'dataN.dat']

for i in a:
    r = re.match('data\w?\.dat' ,i)
    try:
        print(r.group())
    except AttributeError:
        pass
