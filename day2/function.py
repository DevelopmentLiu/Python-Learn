# 函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”：
n1 = 255
n2 = 1000
print(hex(n1), hex(n2))


# 定义一个函数要使用def语句
def ma_sum(x):
    if x >= 0:
        return x
    else:
        return -x


print(ma_sum(-99))


# 定义一个什么事也不做的空函数，可以用pass语句
# def nop():
#     pass
# 数据类型检查可以用内置函数isinstance()实现
def my_abc(a):
    if not isinstance(a, (int, float)):
        raise TypeError('this bad')
    if a >= 0:
        return a
    else:
        return -a


# 对于power(x)函数，参数x就是一个位置参数。
pow(5, 2)


def allStudent(name, sex, age=6):
    print(name, age, sex)
    # 调用函数


allStudent('hello', '女')


# 定义默认参数要牢记一点：默认参数必须指向不变对象！
# Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去
def add_end(L=None):
    if L is None:
        L = []
        L.append('end')
        return L


print(add_end())


# 可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
# 而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
def userPerson(name, age, **kw):
    print(name, age, kw)


userPerson('allen', 2, city='chengdu')

extra = {'city': 'beijing', 'job': 'dog'}
userPerson('allen', 3, **extra)


# 和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。
def person(name, age, *, job, city):
    print(name, age, job, city)


person('allen', 3, city='chengdu', job='dog')
# 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了：

# 在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。
# 但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
def f1(a, b, c=0, *args, **kwa):
    person(a, b, c, args, kwa)


def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
