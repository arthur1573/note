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



a = [1, 2, 3, 4, 5]
b = [i*2 for i in a ]
print(b)
c = map(lambda x: x*2, a)
print(list(c))















