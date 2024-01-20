# list1=['黑马程序员','传智播客','黑马程序员','传智播客']
# set1=set()
# for element in list1:
#     set1.add(element)
# print(set1)





# dict1={'fufu':155,'xuanxuan':165,'taozi':166}
# dict2={}
# dict3=dict()
# print(dict1)
# print(type(dict1))
# print(dict1['fufu'])






# dict1={'fufu':{'语文':149,'数学':70},'xuanxuan':{'语文':110,'数学':100}}
# print(dict1['fufu']['语文'])





#
# dict1={'fufu':155,'xuanxuan':165,'taozi':166}
# dict1['qizi']=160
# dict1['xuanxuan']=153
# h=dict1.pop('fufu')
# print(dict1)
# dict1.clear()
# print(dict1)
# dict1={'fufu':155,'xuanxuan':165,'taozi':166}
# yy=dict1.keys()
# print(dict1)




# dict1={'fufu':155,'xuanxuan':165,'taozi':166}
# # hhh=dict1.keys()
# # for key in hhh:
# #     print(key)
# #     print(dict1[key])
#
# for key in dict1:
#     print(key)
#     print(dict1[key])
#
# print(len(dict1))





# dict1={'wanglihong':{'bumen':'keji','gongzi':3000},'zhoujielun':{'bumen':'shichang','gongzi':5000}}
# for key in dict1:
#     print(key)
#     for key2 in dict1[key]:
#         if(key2=='gongzi'):
#             dict1[key][key2]+=1000
#         print(key2)
#         print(dict1[key][key2])


# a = [1,2,3,4]
# b = [9,8,7] + a
# print(b)
# b.sort()
# print(b)
# b.sort(reverse=True)
# print(b)
# import random
# random.shuffle(b)
# print(b)
# c = sorted(b,reverse=True)
# print(c)
# print(max(c))
# print(min(c))
# print(sum(c))

#
# a = [
#     ["刘德华",18,30000,'广东'],
#     ["林俊杰",28,20000,"香港"],
#     ["陈奕迅",38,5000,"深圳"],
# ]
#
# for m in range(3):
#     for n in range(4):
#         print(a[m][n],end = "\t")
#     print()

# a = [x*10 for x in range(5)]
# print(a)
# b = (x*10 for x in range(7))
# print(b)
# c = tuple(b)
# d = tuple(b)
# print(c)
# print(d)
# e = (x for x in range(3))
# print(e.__next__())
# print(e.__next__())
# print(e.__next__())




# k = ['name','age','job']
# v = ['lhh','19','hero']
# d = dict(zip(k,v))
# print(d)
# f = dict.fromkeys(['name','age','job'])
# print(f)
# a,b,c=d
# h,hh,hhh=d.values()
# print(a)
# print(hh)
# a,b,c=d.items()
# print(a)
#


# a = range(10)
# print(a)


# for m in range(1,10):
#     for n in range(1,m+1):
#         print("{0}*{1}*{2}".format(m,n,n*m),end='\t')
#     print()


# names = ("刘德华","林俊杰",'陈奕迅','周杰伦')
# ages = (18,28,38,48)
# jobs = ("老师",'公务员','程序员')
# for name,age,job in zip(names,ages,jobs):
#     print('{0}---{1}---{2}'.format(name,age,job))


# a = [x*2 for x in range (1,20) if x%2==0]
# print(a)

# cells = [(row,col) for row,col in zip(range(1,10),range(101,110))]
# for cell in cells:
#     print(cell)



# values = ['北京','上海','深圳','广州']
# cities = {id:city for id,city in zip(range(1,5),values)}
# print(cities)


# my_test = 'i love you, i love sxt, i love gaoqi'
# char_count = {c:my_test.count(c) for c in my_test}
# print(char_count)



# gnt = (x for x in range(1,101) if x%9==0)
# print(tuple(gnt))
# print(tuple(gnt))


# import turtle
# p = turtle.Pen()
# radius = [x*20 for x in range(1,11)]
# my_colors = ('red','orange','yellow','pink')
# p.width(8)
# for r,i in zip(radius,range(len(radius))):
#     p.penup()
#     p.goto(0,-r)
#     p.pendown()
#     p.color(my_colors[i%len(my_colors)])
#     p.circle(r)
#
# turtle.done()


# a = 100
# def f1(a,b,c):
#     print(a,b,c)
#     print(locals())
#     print('#'*20)
#     print(globals())
# f1(2,3,4)



# def xuan(x):
#     x += 2
#
# a = 100
# print(id(a))
# xuan(a)
# print(id(a))



# f = lambda a,b,c:a+b+c
# print(f(10,20,30))
# g = [lambda a:a*2,lambda b:b*3,lambda c:c*4]
# print(g[0](6))





# s = 'print("我好帅")'
# eval(s)
#
# a = 10
# b = 20
# c = eval('a+b')
# print(c)





# def xuan(n):
#     print('start:'+str(n))
#     if n==1:
#         print('recursion over!')
#     else:
#         xuan(n-1)
#     print('end:'+str(n))
#
# xuan(3)


# def xuan(n):
#     if n==1:
#         return 1
#     else:
#         return n*xuan(n-1)
# print(xuan(4))


# a = 100
# b = 99
# def outer():
#     b = 10
#     def inner():
#         nonlocal b
#         print('inner b:',b)
#         b = 20
#         global a
#         a = 1000
#     inner()
#     print('outer b:',b)
# outer()
# print('a:',a)




# a = 10
# s = 'global'
# def outer():
#     s = 'outer'
#     def inner():
#         s = 'inner'
#         print(s)
#         print(a)
#     inner()
#
# outer()



# numbers = [1,2,3,4,5,6]
# def doubler(n):
#     return n*2
# result = map(doubler,numbers)
# print(result)
# print(set(result))




# def func(x):
#     print('&&&&&&&&&')
#     print(x)
#     return x > 5
# xuan = [1,2,3,4,5,6,7,8]
# f = filter(func,xuan)
# print(list(f))

#
# class Student:
#     def __init__(self,name,score):
#         self.name = name
#         self.score = score
#     def say_score(self):
#         self.age = 18
#         print('{0}的分数是{1}'.format(self.name,self.score))
#
# s1 = Student('张三',99)
# print(s1.name,s1.score)
# s2 = Student('李四',59)
# s2.say_score()
# s1.say_score()
# print(s1.age)
# s2.address = '道滘'
# print(s2.__dict__)




#
# class Student:
#     company = '广工'
#     count = 0
#     def __init__(self,name,score):
#         self.name = name
#         self.score = score
#         Student.count = Student.count+1
#     def say_score(self):
#         print('我的学校是：',Student.company)
#         print(self.name,'我的分数是：',self.score)
# s1 = Student('刘德华',80)
# s2 = Student('林俊杰',70)
# s1.say_score()
# print('一共创建{0}个Student对象'.format(Student.count))





# class Student:
#     company = 'SXT'
#     def __init__(self,name):
#         self.name = name
#     @classmethod
#     def printCompany(cls):
#         print(cls.company)
#     @classmethod  #@staticmethod
#     def add(self,a,b):
#         print('{0}+{1}={2}'.format(a,b,(a+b)))
#         return a+b
# Student.printCompany()
# Student.add(19,33)



# class Person:
#     def __del__(self):
#         print('销毁对象:{0}'.format(self))
# p1 = Person()
# p1.age=18
# p2 = Person()
# del p2
# print('程序结束')


# class Car:
#     def __call__(self, age,money):
#             print('call方法')
#             print('车龄{0}，金额{1}'.format(age,money))
# c = Car()
# c(18,20000)



# class Employee:
#     __company = '程序员'
#     def __init__(self,name,age):
#         self.name = name
#         self.__age = age
#     def say_company(self):
#         print('我的公司是：',Employee.__company)
#         print('我的年龄是：')
# print(Employee._Employee__company)
# a = Employee('刘德华',18)
# a.say_company()
# # print(a.age)











































