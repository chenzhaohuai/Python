
import functools

print('hello world \n')

print('''line1
line2
line3''')

print(r'''hello,\n
world''')

print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)

print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))

r = 2.5
s = 3.14 * r ** 2
print(f'The area of a circle with radius {r} is {s:.2f}')


# def person(name, age, *, city, job):
#     print(name, age, city, job)

# person('Jack', 24, city='Beijing', job='Engineer')

def person(name, age, *args, city, job):
    print(name, age, args, city, job)

args = {'1','2','3'}

for arg in args: 
   print(arg)

person('Jack', 24, *args , city='Beijing', job='Engineer')

def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs


 
L = count()

for l in L:
    print(l.__name__)
    print(l())


# def log(func):
#     def wrapper():
#         print('call %s():' % func.__name__)
#         return func()
#     return wrapper

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


@log('execute')
def now():
    print('2020-11-24')


print(now.__name__)

now()





class Student(object):
  def __init__(self, name, score):
       self.name = name
       self.score = name


class Class(Student):
   pass



bart = Student('Bart Simpson', 59)
print(bart.name)

bart2 = Class('Bart Simpson', 59)
print(bart2.name)

dirs = dir('ABC')
print(*dirs,sep='\n')
[print(i) for i in dirs]
# name = input()

# print(name)