# -*- coding: UTF-8 -*-
# test_1
print('test_1:')
x = int(input("Please enter an interger:"))

if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')
print('\n')

# test_2
print('test_2:')
# Measure some strings:
words = ['cat', 'window', 'defenestrate']
for w in words: # words是一个列表，w可以看做是代表列表元素的一个变量
    print(w, len(w))
# 没理解为什么这样写？
# for循环可以遍历任何序列的项目，如一个列表或者一个字符串。
print '\n'

# test_3
# -*- coding: UTF-8 -*-
print('test_3:')
string = '当前字母：'
for letter in 'python':
    print string.decode('UTF-8'), letter
print '\n'

# test_4
print 'test_4:'
fruits = ['banana', 'apple', 'mango']
string = '当前水果：'
for index in range(len(fruits)):
    print string.decode('UTF-8'), fruits[index]
print "Good bye!"
print '\n'
