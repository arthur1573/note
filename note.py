# print("hello")





# output = 0
# print(f"1: {output}")

# def help_me_get_the_answer():
    # output = 3 * 2
    # print(f"2: {output}")
    # return output 
# print(f"3: {output}")



# help_me_get_the_answer()
# print(f"4: {output}")


# output = help_me_get_the_answer()
# print(f"5: {output}")


# output = "None"
# print(f"6: {output}")


# output = None
# print(f"7: {output}")






# output = help_me_get_the_answer()
# print(output)








# o = "OXFORD BOOKWORMS LIBRARY".title()
# print(o)



# print("built a ladder notes 21".title())




# vs code could open these hint
# not notepad++

# def help_me_get_a_apple():
    # """This function is going to help a human
    # get a apple.hhhhhhhhhhhhh"""
    # print("apple")

# help_me_get_a_apple()









# http://patorjk.com/software/taag/#p=display&f=Graffiti&t=Ya-Tao%20Zhao

# logo = '''

# _____.___.              ___________               __________.__                   
# \__  |   |____          \__    ___/____    ____   \____    /|  |__ _____    ____  
 # /   |   \__  \    ______ |    |  \__  \  /  _ \    /     / |  |  \\__  \  /  _ \ 
 # \____   |/ __ \_ /_____/ |    |   / __ \(  <_> )  /     /_ |   Y  \/ __ \(  <_> )
 # / ______(____  /         |____|  (____  /\____/  /_______ \|___|  (____  /\____/ 
 # \/           \/                       \/                 \/     \/     \/        
# '''



# logo2 = '''
 # __     __       _______            _______                 
 # \ \   / /      |__   __|          |___  / |                
  # \ \_/ /_ _ ______| | __ _  ___      / /| |__   __ _  ___  
   # \   / _` |______| |/ _` |/ _ \    / / | '_ \ / _` |/ _ \ 
    # | | (_| |      | | (_| | (_) |  / /__| | | | (_| | (_) |
    # |_|\__,_|      |_|\__,_|\___/  /_____|_| |_|\__,_|\___/ 
# '''
 
 
 
# print(logo)
# print(logo2)
 
 
 
 
 



# remover old dict:
# dict1 = {
    # 'value': 11
# }
# dict2 = dict1

# print(dict1)
# print(dict2)
# print("--------------------------")
# dict1['value'] = 22
# print(dict1)
# print(dict2)





# dict = {
    # "value": 11,
    # "next": None
# }

# print(dict)

# dict.pop("value")
# print(dict)
 
 
 

# 4!
# def factorial(n):
    # if n == 1:
        # return 1
    # return n * factorial(n-1)
 # print(factorial(4))




# def factorial_number(4):
    
    
# for i in range(1,5):
    # print(f"{i}*{i+1}")
    
# print(range(4))



# def factorial(n):    
    # if n == 1:
        # return 1
    # return print(f"4! = {n} * {factorial(n-1)}")

# factorial(4)





# n = input("Enter a number: ")
# factorial = 1
# if int(n) >= 1:
    # for i in range (1,int(n)+1):
        # print(i)
        # factorial = factorial * i
        # print(f"{factorial} * {i}")
# print("Factorail of ",n , " is : ",factorial)



# def factorial(x):
   # n = 1
   # while x > 1:
       # n *= x
       # x -= 1
   # return n

# print (factorial(5))





# def factorial(x):
    # n = 1   # this will store the factorial value
    # while x > 0:
        # n = n*x
        # x -= 1
    # return n






# def factorial(x):

    # while x > 0:

        # print(x)
        
    
# factorial(4)



# def factorial(x):
    # n = x
    # while n >= 0:
        # x = n * (n - 1)
        # n -= 1
    # return x
    
# print(factorial(4))






# def factorial(x):
    # n = 1
    # while x > 0:
        # print(x)
        # print(f"{n} * {x}")
        # n = x * n
        # print(f"{n} * {x}")
        # x -= 1
        # print(x)
        # print("----------------")
    # return print(n)

# factorial(4)





# def factorial(x):
    # while x != 1:
        # print(x)
        # for i in range(1, x+1):
            # n = x * (x - i)
            # print(f"{n} = {x} * {(x-i)}")
        # x -= 1
        # print("-------------------------")
    # return print(n)

# factorial(4)










# def factorial(x):
    # while x != 1:
        # print(x)
        # for i in range(1, x+1):
            # n = (x - i)
            
            # print(f"{n} = {x} * {(x-i)}")
        # x -= 1
        # print("-------------------------")
    # return print(n)

# factorial(4)





# for i in range(1,5):
    # print(i, end = "")
    
    
    
    
# for i in range(4, 0, -1):
    # if i == 1:
        # print(i, end = "")
        # break
    # print(i, end = "*")
    



# print(type(4/2))






# py -m venv env



# from math import log
# import numpy as number_python
# import matplotlib.pyplot









# Fibonacci series:
# the sum of two elements defines the next
# a, b = 0, 1
# while a < 100:
    # print(a)
    # a, b = b, a+b






# a = 1
# b = 2
# c = 0
# while a < 100:
    # print(a)
    # c = a + b
    # a = b
    # b = c
    




# users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}
# print(users)
# for user, status in users.copy().items():
    # if status == 'inactive':
        # del users[user]
        # print(users)






# a = [1, 2, 3, 4, 5]
# b = [i*2 for i in a ]
# print(b)
# c = map(lambda x: x*2, a)
# print(list(c))








# print("This will always be run.")

# def main():
    # print(
    # """
    # This will NOT always be run. 
    # This module's name = {}
    # """
    # .format(__name__))
    
    
 # if __name__ == "__main__":
    # main()
# else:
    # print("this note.py module is run from import.")







# def fullname():
    # return print('arthur')
    ## return 'arthur'
# fullname()







# python object-oriented programming

# class employee:
    # pass
    
# emp_1 = employee()
# emp_2 = employee()

# print(emp_1)
# print(emp_2)












# # print('↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓')
# # print("This will always be run.")


# def main():
    # # print(
    # # """
    
    # # This will NOT always be run. 
    # # This module's name = {}
    # # """
    # # .format(__name__))
    
    
        
    
    # # # class employee:
        # # # pass
        
    # # # emp_1 = employee()
    # # # emp_2 = employee()

    # # # print(emp_1)
    # # # print(emp_2)
    
    # # # emp_1.first = 'Corey'
    # # # emp_1.last = 'Schafer'
    # # # emp_1.email = 'Corey.Schafer@company.com'
    # # # emp_1.pay = '50000'
        
    # # # emp_2.first = 'Test'
    # # # emp_2.last = 'User'
    # # # emp_2.email = 'Test.User@company.com'
    # # # emp_2.pay = '40000'
    
    # # # print()
    # # # print(emp_1.email)
    # # # print(emp_2.email)
    
    # raise_amount = 1.05
    # print(raise_amount)


    # class employee:
        
        # # class variable
        # raise_amount = 1.04
        # print(raise_amount)
        # # print(raise_amount)
        
    
    
    
        # def __init__(self, first, last, pay):
            # # first, last, pay are positional arguments
            # self.first = first
            # # self.first: object's atriburion
            # # first: programmer's input
            # # emp_1.first = "corey"
            # # emp_2.first = 'test'
            # # self = employee's object
            
            # self.last = last
            # self.pay = pay
            # self.email = first + '.' + last + "@company.com"
            
        
        # def fullname(self):
            # return '{} {}'.format(self.first, self.last)
            
            
            
        # def apply_raise(self):
            # print(raise_amount)
            # print(employee.raise_amount)
            # print(self.raise_amount)
            
            # self.pay = int(self.pay * self.raise_amount )
            # return self.pay
            
        
    # emp_1 = employee('yatao', 'zhao', 50000)
    # emp_2 = employee('arthur', 'run', 60000)
    
    # # print()
    # # print(emp_1)
    # # print(emp_1.first, emp_1.last, emp_1.pay)
    # # print(emp_2.first)
    
    # # print()
    # # print('{} {}'.format(emp_1.first, emp_1.last))    
    
    # # # fullname()
    
    # # # print(emp_1.fullname)
    # # # fullname(emp_1)
    # # # emp_1.fullname()
    # # print(emp_1.fullname())  # clear code way
    # # print(emp_2.fullname())
    # # print()
    
    
    # # print(employee.fullname(emp_1)) # better understand way
    # # # class.method.arguments
    
    # # print(emp_1.pay)
    # # emp_1.apply_raise()
    # # print(emp_1.pay)
    
    # print(emp_1.pay)
    # print(employee.apply_raise(emp_1))
    
    # print(employee.__name__)
    
    
        


# print(main.__name__)    
# if __name__ == "__main__":
    # main()
# else:
    # print("this note.py module is run from import.")
















# print("This will always be run.")

# def main():
    # print("This will be run when you do not import this.")
    # print('What\'s up?')
    
    
# if __name__ == "__main__":
    # main()
# else:
    # print("this note.py module is run from import.")
    
    
    






# f(x) = x + 10  ## x belong Z
# f(1) = 11


# def f(x):
    # y = x + 10
    # print(y) 

# f(1)










# turtle.pencolor('blue')
# for line in range(4):
    # turtle.forward(100)
    # turtle.left(90)


# turtle.penup()
# turtle.forward(-20)
# turtle.left(90)
# turtle.forward(-20)
# turtle.pendown()
# turtle.right(90)


# turtle.pencolor('green')
# for line in range(4):
    # turtle.forward(140)
    # turtle.left(90)    


# turtle.penup()
# turtle.forward(-20)
# turtle.left(90)
# turtle.forward(-20)
# turtle.pendown()
# turtle.right(90)



# turtle.pencolor('black')
# for line in range(4):
    # turtle.forward(180)
    # turtle.left(90)  








######## draw a lot square by turtle
# import turtle

# for square in range(10):
    # for line in range(4):
        # turtle.forward(100+square*40)
        # turtle.left(90)
        
    # turtle.penup()
    # turtle.forward(-20)
    # turtle.left(90)
    # turtle.forward(-20)
    # turtle.pendown()
    # turtle.right(90)

# turtle.done()










################# print factorial number in human way
# n = 10
# print(str(n) + "! = ", end = '')
# def factorial(n):
    # '''
    # print factorial number in human way
    # '''
    # if n < 0:
        # return 'factorial() not defined for negative values'
    # if n == 0:
        # return 1
    # if n == 1:
        # print('', n, '= ', end = '')
        # return 1
    # else:
        # print('', n, '*', end = '')
        # return n * factorial(n - 1)

# print(factorial(n))












##############
# import math
# print(math.pi)
# print(math.e)
# print(math.tau)












################ download a web table
# import pandas

# simpsons = pandas.read_html('https://en.wikipedia.org/wiki/List_of_The_Simpsons_episodes_(seasons_1%E2%80%9320)')
# print(len(simpsons))
# print(simpsons[1])








##############
# import pandas

# england = pandas.read_csv('https://www.football-data.co.uk/mmz4281/2122/E0.csv')
# print(england)










############ Copy a table in pdf file to csv file
# pip install "camelot-py[cv]"

# import camelot

# table = camelot.read_pdf('foo.pdf', page='1')
# print(table)

# # table.export('foo.csv', f = 'csv')
# table.export('foo.csv')
# # table[0].to_csv('foo.csv')










############## Generate QR code in Python
# pip install pypng, pyqrcode

# import pyqrcode
# import png
# import os

# link = "https://zhaoyatao.com"
# qr_code = pyqrcode.create(link)
# qr_code.png('me.png', scale = 10)
# # qr_code.png('me.png', scale=10, module_color=[0, 255, 0])
# os.system('me.png')











###### replace a new line
# import re

# text = '''
# i
# am 
# a 
# text 
# file
# .
# end.
# '''
# print(text)
# text = re.sub('\n', "\n// ", text)
# print(text)











########### replace a new line 2
# import re
# import os

# text = open('text.txt', 'r')
# text2read = text.read()
# text.close()

# text2 = open('text.txt', 'w')
# text2write = re.sub('\n','\n// ', text2read)
# text2.write(text2write)
# text2.close()

# print('all text have replaced, close text windows will quit.')

# os.system('text.txt')









############# download a youtube video
# import pytube

# url = input("enter video url: ")
# path = "D:\pytube"

# pytube.YouTube(url).streams.get_highest_resolution().download(path)








############# Extract text from PDF
# import PyPDF2
# pdf = open('foo.pdf', "rb")
# reader = PyPDF2.PdfFileReader(pdf)
# page = reader.getPage(0)
# print(page.extractText())










###################       http://www.pythonchallenge.com/pc/def/map.html
# mystr = input('Paste your code: \n')
# print('')
# mappingtbl = mystr.maketrans('ghijklmnopqrstuvwxyzabcdef','ijklmnopqrstuvwxyzabcdefgh')
# print('Mapping table: \n', mappingtbl)
# print('')
# newstr = mystr.translate(mappingtbl)
# print('Translation: \n', newstr)










#########################    30 days of python

# print(
# '''
# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125
# ''')




# print('I hope everyone is enjoying the Python Challenge.\nAre you ?') # line break
# print('Days\tTopics\tExercises') # adding tab space or 4 spaces 
# print('Day 1\t3\t5')
# print('Day 2\t3\t5')
# print('Day 3\t3\t5')
# print('Day 4\t3\t5')
# print('This is a backslash  symbol (\\)') # To write a backslash
# print('In every programming language it starts with \"Hello, World!\"') # to write a double quote inside a single quote






# # Strings only
# first_name = 'Asabeneh'
# last_name = 'Yetayeh'
# language = 'Python'
# formated_string = 'I am %s %s. I teach %s' %(first_name, last_name, language)
# print(formated_string)

# # Strings  and numbers
# radius = 10
# pi = 3.14
# area = pi * radius ** 2
# formated_string = 'The area of circle with a radius %d is %.2f.' %(radius, area) # 2 refers the 2 significant digits after the point

# python_libraries = ['Django', 'Flask', 'NumPy', 'Matplotlib','Pandas']
# formated_string = 'The following are python libraries:%s' % (python_libraries)
# print(formated_string) # "The following are python libraries:['Django', 'Flask', 'NumPy', 'Matplotlib','Pandas']"







# language = 'Python'
# a,b,c,d,e,f = language # unpacking sequence characters into variables
# print(a) # P
# print(b) # y
# print(c) # t
# print(d) # h
# print(e) # o
# print(f) # n






############ Count Character Occurrences using Python
# def count_characters(s):
    # count = {}
    # for i in s:
        # if i in count:
            # count[i] += 1
        # else:
            # count[i] = 1
    # print(count)

# word = input('Enter your strings: ')
# count_characters(word)






###################   leetcode 9
# x = 12345
# print(type(x))

# nx = str(x)
# print(type(nx))

# print(nx)
# print(-len(nx))

# print(nx[::-1])








##################  30 days of python
# challenge = 'thirty\t days\t of\t python'
# print(challenge)
# print(challenge.expandtabs())   # 'thirty  days    of      python'
# print(challenge.expandtabs(10)) # 'thirty    days      of        python'






# challenge = 'thirty days of python'
# print(challenge.find('y'))  # 5
# print(challenge.find('th')) # 1



# challenge = 'thirty days of python'
# print(challenge.rfind('y'))  # 16
# print(challenge.rfind('th')) # 17









# challenge = 'thirty days of python'
# print(challenge.swapcase())   # THIRTY DAYS OF PYTHON
# challenge = 'Thirty Days Of Python'
# print(challenge.swapcase())  # tHIRTY dAYS oF pYTHON




# strings = ['Thirty', 'Days', 'Of', 'Python']
# new_str = ' '.join(strings)
# print(new_str)



# company = "Coding For All"
# print(company)

# print(len(company))

# new_company = company.upper()
# print(new_company)

# new_new_company = company.lower()
# print(new_new_company)


# print(company.capitalize())
# print(company.title())
# print(company.swapcase())

# #9
# print(company[0:7])



# #10
# print(company.index('Coding'))



# #11
# #print(company.replace('Coding','Python'))
# company = company.replace('Coding','Python')
# print(company)





# #12
# company = company.replace('All','Everyone')
# print(company)


# company = 'Coding For All'
# print(company.split())


# company = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
# print(company.split(','))




# #15
# company = 'Coding For All'
# print(company[0])
# print(company[-1])





# for number in range(6):
    # if number == 3:
        # pass
    # print(number)





# import string
# print(string.ascii_letters) # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
# print(string.digits)        # 0123456789
# print(string.punctuation)   # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~









################
# numbers = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
# positive_even_numbers = [ i for i in numbers if i % 2 == 0 and i > 0]
# print(positive_even_numbers)











############ Execution Time
# from time import time
# start = time()

# # code start
# email = input('Enter your Email: ')
# email = email.strip()
# slicer_index = email.index('@')
# username = email[:slicer_index]
# domain_name = email[slicer_index+1:]
# print('Your user name is: ', username, ' and your domain is: ', domain_name)
# # code end

# # clcoding.com
# end = time()
# execution_time = end - start
# print('Execution Time(s): ', execution_time)






########################## Roman to Integer in Python


# class Solution(object):
   # def romanToInt(self, s):
      # """
      # :type s: str
      # :rtype: int
      # """
      # roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
      # i = 0
      # num = 0
      # while i < len(s):
         # if i+1<len(s) and s[i:i+2] in roman:
            # num+=roman[s[i:i+2]]
            # i+=2
         # else:
            # num+=roman[s[i]]
            # i+=1
      # return num
      
      
# ob1 = Solution()
# print(ob1.romanToInt("III"))
# print(ob1.romanToInt("CDXLIII"))






        # 105 ms
        # roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000, 'IV':4, 'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM':900}
        # slicer_s = 0
        # number = 0

        # while slicer_s < len(s):
            # if slicer_s + 1 < len(s) and s[slicer_s:slicer_s+2] in roman:
                # number += roman[s[slicer_s:slicer_s+2]]
                # slicer_s += 2
            # else:
                # number += roman[s[slicer_s]]
                # slicer_s += 1      
        # return number






        # # 65 ms
        # roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000, 'IV':4, 'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM':900}
        # number = 0
        # for i in range(len(s)):
            # # checking the string is the out of the dictionary 
            # if i == len(s):
                # break
            # # checking the string is the last one of the dictionary 
            # if i == len(s) -1:
                # number += roman[s[i]]
                # break
            # if roman[s[i]] >= roman[s[i + 1]]:
                # number += roman[s[i]]
            # else:
                # number -= roman[s[i]]
        # return number










# import numpy

# print(numpy.zeros((3,3)))
# print()
# print(numpy.identity(5))






# import matplotlib.pyplot as plt

# x = range(10)

# y = range(10)
# plt.plot(x, y)
# plt.show()








############### sum of array

# from time import time
# start = time()

# # code start
# email = input('Enter your Email: ')
# email = email.strip()
# slicer_index = email.index('@')
# username = email[:slicer_index]
# domain_name = email[slicer_index+1:]
# print('Your user name is: ', username, ' and your domain is: ', domain_name)
# # code end

# # clcoding.com
# end = time()
# execution_time = end - start
# print('Execution Time(s): ', execution_time)










##########################
# from time import time

# def run_time_decorator(function):
    # def wrapper():
        # start = time()
        
        # result = function()
        
        # end = time()
        # execution_time = end - start
        # print('Execution Time(s): ', execution_time)
        # return result
    # return wrapper
    

# s = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# s1 = range(1,101)
# s2 = range(11, 21)
# s3 = range(21, 31)


# @run_time_decorator
# def find_sum():
    # s1 = range(1,10001)
    # total = 0
    
    # for i in s1:
        # total = total + i 
    # print(total)
    # return total


# # for i in s2:
    # # print(i)

# find_sum()











##########  leetcode:14. Longest Common Prefix

# strs = ["flower","flow","flight"]

# # list to dictionary
# # dict_strs = {strs[i]: 0 for i in range(len(strs))} 

# common = {}
# for x in range_strs:
    # if length_strs == x + 1:
        # break
            
    # if strs[x][x] == strs[x+1][x]:
        
        
        # common[strs[x]] = common[strs[x]] + 1
    

# print(common)





###################################
# import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib.collections as collections


# t = np.arange(0.0, 2, 0.01)
# s1 = np.sin(2*np.pi*t)
# s2 = 1.2*np.sin(4*np.pi*t)

# #subplots?
# fig, ax = plt.subplots()
# ax.set_title('using span_where')
# ax.plot(t, s2, color='black')
# ax.axhline(0, color='blue', lw=2)

# collection = collections.BrokenBarHCollection.span_where(
    # t, ymin=0, ymax=1.2, where=s2 > 0, facecolor='green', alpha=0.5)
# ax.add_collection(collection)

# collection = collections.BrokenBarHCollection.span_where(
    # t, ymin=-1.2, ymax=0, where=s2 < 0, facecolor='red', alpha=0.5)
# ax.add_collection(collection)

# plt.legend()
# plt.show()






########################### Monitoring the keyboard
# from pynput import keyboard

# def on_press(key):
    # try:
        # print('alphanumeric key {0} pressed'.format(
            # key.char))
    # except AttributeError:
        # print('special key {0} pressed'.format(
            # key))

# def on_release(key):
    # print('{0} released'.format(
        # key))
    # if key == keyboard.Key.esc:
        # # Stop listener
        # return False

# # Collect events until released
# with keyboard.Listener(
        # on_press=on_press,
        # on_release=on_release) as listener:
    # listener.join()

# # ...or, in a non-blocking fashion:
# listener = keyboard.Listener(
    # on_press=on_press,
    # on_release=on_release)
# listener.start()





################ 
# f = float(input('please input the temperature(F): '))
# c = (f - 32) / 1.8
# print('%.2f F = %.1f C ' % (f,c))






# def append(self, value):
    # new_node = Node(value)
    # if self.head is None:
        # self.head = new_node
        # self.tail = new_node
    # else:
        # self.tail.next = new_node
        # self.tail = new_node
    # self.length += 1







# def print_items(n):
    # for i in range(n):
        # print(i)
    # for j in range(n):
        # print(j)

# print_items(10)



# def print_items(n):
    # for i in range(n):
        # for j in range(n):
            # print(i,j)
    
# print_items(10)




# def print_items(n):
    # for i in range(n):
        # for j in range(n):
            # for k in range(n):   
                # print(i,j,k)

# print_items(10)




# def print_items(n):
    # for i in range(n):
        # for j in range(n):
            # print(i,j)

    # for k in range(n):
        # print(k)

# print_items(10)





# class Cookie:
    # def __init__(self, color):
        # self.color = color
    # def get_color(self):
        # return self.color
    # def set_color(self, color):
        # self.color = color

# cookie_one = Cookie('green')
# cookie_two = Cookie('blue')

# print('Cookie one is', cookie_one.get_color())
# print('Cookie two is', cookie_two.get_color())

# cookie_one.set_color('yellow')

# print('\nRight now,cookie one is', cookie_one.get_color())
# print('Still, cookie two is', cookie_two.get_color())





# num1 = 11
# num2 = num1

# print("Before value is updated:")
# print("num1 =", num1)
# print("num2 =", num2)

# num1 = 22
# num2 = num1

# print("\nAfter value is updated:")
# print("num1 =", num1)
# print("num2 =", num2)



# dict1 = {
    # 'value':11
# }

# dict2 = dict1

# print('Before value is updated:')
# print("dict1 =", dict1)
# print("dict2 =", dict2)




# dict1 = {
    # 'value':11
# }

# dict2 = dict1

# print('Before value is updated:')
# print("dict1 =", dict1)
# print("dict2 =", dict2)

# dict1['value'] = 22
# dict2 = dict1

# print('\nAfter value is updated:')
# print("dict1 =", dict1)
# print("dict2 =", dict2)



# head = {
    # "value": 11,
    # "next": {
        # "value": 3,
        # "next": {
            # "value": 23,
            # "next": {
                # "value": 7,
                # "next": None
            # }
        # }
    
    # }
# }


# head = {
    # "value": None,
    # "next": None
# }

# print(head['next']['next']['value'])

# print(head['value'])
# print(head['next'])


# class Node:
    # def __init__(self, value):
        # self.value = value
        # self.next = None


# class LinkedList:
    # def __init__(self, value):
        # new_node = Node(value)
        # self.head = new_node
        # self.tail = new_node
        # self.length = 1

# my_linked_list = LinkedList(4)

# print(my_linked_list.head.value)







# class Node:
    # def __init__(self, value):
        # self.value = value
        # self.next = None


# class LinkedList:
    # def __init__(self, value):
        # new_node = Node(value)
        # self.head = new_node
        # self.tail = new_node
        # self.length = 1


    # def print_list(self):
        # temp = self.head
        # while temp is not None:
            # print(temp.value)
            # temp = temp.next
    
    
    # def append(self, value):
        # new_node = Node(value)
        # if self.head is None:
        # if self.length == 0:
            # self.head = new_node
            # self.tail = new_node
        # else:
            # self.tail.next = new_node
            # self.tail = new_node
        # self.length += 1

# my_linked_list = LinkedList(1)    

# my_linked_list.append(2)

# my_linked_list.print_list()







###########################  desktop notification
# import time
# from plyer import notification

# if __name__ == '__main__':
    # while True:
        # notification.notify(
            # title = 'ALERT!!!',
            # message = "Take a break! It has been 15minutes!",
            # timeout = 10
        # )
        # time.sleep(900)








##################### leetcode14
# strings = ["dog","racecar","car","cat","a","ab","racecaraaaaa","racecara","racecaraa"]

# # strings = ["flower","flow","flight"]
# # strings = ["dog","racecar","car"]
# print()
# print(max(strings))
# print(min(strings))
# print()
# print(ord("a"))
# print(ord("b"))
# print(ord("c"))
# print()
# print(ord("0"))
# print(ord("1"))
# print()
# print("a" > "ab")
# print("ab" > "aba")

# print([0] > [1])
# print(['0'] > ['1'])













# class Node:
    # def __init__(self, value):
        # self.value = value
        # self.next = None


# class LinkedList:
    # def __init__(self, value):
        # new_node = Node(value)
        # self.head = new_node
        # self.tail = new_node
        # self.length = 1


    # def print_list(self):
        # temp = self.head
        # while temp is not None:
            # print(temp.value)
            # temp = temp.next

    
    # def append(self, value):
        # new_node = Node(value)
        # if self.head is None:
        # # if self.length == 0:
            # self.head = new_node
            # self.tail = new_node
        # else: 
            # self.tail.next = new_node
            # self.tail = new_node
        # self.length += 1




    # def pop(self):

        # if self.length == 0:
        # # if self.head is None:
            # return None  
        # temp = self.head
        # pre = self.head
        
        # # or, while(temp.next is not None)
        # while(temp.next):
            # pre = temp
            # temp = temp.next
        # self.tail = pre
        # self.tail.next = None

        # self.length -= 1
        # # self.length = length - 1

        # # remove the last Node
        # if self.length == 0:
            # self.head = None
            # self.tail = None

        # # get the Node we removed 
        # return temp

# my_linked_list = LinkedList(1)
# my_linked_list.append(2)
# my_linked_list.append(3)
# my_linked_list.append(4)



# print('''\n# to remove the last Node, do not care else''')
# my_linked_list.pop()

# print('''\n# to print the linkedlist right now''')
# my_linked_list.print_list()

# print('''\n# to remove the last Node, print it's object''')
# print(my_linked_list.pop())

# print('''\n# to remove the last Node, and get it's value''')
# print(my_linked_list.pop().value)








