print('hello world')

# 每一个逗号是一个空格
print('This is', 'my', 'life')

a = 1024 * 768
print(a)

# 变量赋值 条件语句判断
a = 100
if a >= 99:
        print(a)
else:
        print(-a)

# \ 符号表示转义字符
print('I\'m a girl')

# '''符号表示多个换行显示。
print(''' oneline 
twoline 
threeline ''')

# 指向
a = 'abc'
b = a
print(b)

# 常用运算符  / 被除  //整除  %求余
a = 9/5
b = 10//3
c = 10 % 3
print('被除结果是:', a, '整除结果是:', b, '求余结果是:', c)

# list集合，可以随意组合和更改里面的元素  tuple元组，不能随便更改元素。如果元祖里面包含有list。只能更改list
adc = ['def', 1, 30.5]
cde = ('a', 'b', 'c')
code = (1, 2, ['a', 'b', 'c'])
print('获取集合里面的第一个元素:', adc[1], '获取不可变元祖', cde)
code[2][0] = 'V'
code[2][2] = 'Y'
print('获取更改后的元祖:', code)

# 请用索引取出下面list的指定元素：
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

print(L[0][0], L[1][1], L[2][2])

# 小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
# 低于18.5：过轻
# 18.5-25：正常
# 25-28：过重
# 28-32：肥胖
# 高于32：严重肥胖
# 用if-elif判断并打印结果：
height = 1.75
weight = 80.5
BMI = weight/(height**2)
if BMI < 18.5:
    print('过轻')
elif (BMI >= 18.5) and (BMI < 25):
    print('正常')
elif (BMI >= 25) and (BMI < 28):
    print('过重')
elif (BMI >= 28) and (BMI < 32):
    print('肥胖')
else:
    print('肥胖')

# 输入的为字符串，不能同整数进行直接的比较。所以需要进行先转
# s = input('birth:')
# birth = int(s)
# if birth > 100:
#   print('体重正常')
# else:
#   print('应该减肥了')
# for in循环
# names = ['diudiu', 'allen', 'hour']
# for na in names:
#     print(na)
# # 整数计算 range()函数，可以生成一个整数序列
# me = 0
# for x in range(101):
#     me = me + x
#     print(me)

# # while循环 计算100以内所有奇数之和
# one = 0
# n = 99
# while n > 0:
#     one = one + n
#     n = n - 2
#     print('计算基数之和:', n)
#
#     L = ['Bart', 'Lisa', 'Adam']
#     for name in L:
#         print(name)
# # 判断基数
#     s = 0
#     while s < 10:
#         ｓ = ｓ + 1
#         if s % 2 == 0:
#             continue # 如果是偶数则直接跳过打印
#             print('打印基数：', s)


# 和list比较，dict有以下几个特点：
# 1、查找和插入的速度极快，不会随着key的增加而变慢；
# 2、需要占用大量的内存，内存浪费多。
# 而list相反：
# 1、 查找和插入的时间随着元素的增加而增加；
# 2、占用空间小，浪费内存很少。dict是用空间来换取时间的一种方法。
# dic 字典 用｛ ｝表示
d = {'name': 'allen', 'age': 18, 'sex': 'boy'}
print(d['name'])
# 删除一个key .pop()
d.pop('name')
print(d)
print(d['age'])

# set 和 dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
s = set([1, 2, 3, 5, 6])
# 传入的参数[1, 2, 3]是一个list，而显示的{1, 2, 3}只是告诉你这个set内部有1，2，3这3个元素，显示的顺序也不表示set是有序的。
print(s)
# add(key)方法可以添加元素到set中，可以重复添加，但不会有效果：
s.add(10)
print(s)
# 通过remove(key)方法可以删除元素
s.remove(6)
print(s)
# set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作：
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print('并集：', s1 & s2, '交集：', s1 | s2)

d = {
    'Michael': 95,
    'Bob': 75,
    'Tracy': 85
}
print('d.get(\'Thomas\', -1) =', d.get('Thomas', -1))




