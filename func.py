#def func():
 #   print("This is function")
#func()


#def hello():
 #   print("hello everyone")
#hello()
#print("end of the program")




#def add(num1,num2):
 #   sum = num1 + num2
  #  print("sum of 2 number:",sum)
#add(5,8)
#print("end of the program")






#def func(a,b,c):
 #   print("This is function",a,b,c)
#func(1,2,3)



#def outer():
 #   print("outer function")
  #  def inner():
   #     print("inner function")
    #inner()
#outer()



#def subNumbers(x, y):
 #   return (x-y)
#a = 90
#b = 50
#res = subNumbers(a, b)
#print("subtraction of ", a, " and ", b, " is ", res)




#def fun(func, arg):
 #   return func(arg)
#def square(x):
 #   return x ** 2
#res = fun(square, 5)
#print(res)





#def fun(*args):
 #   for arg in args:
  #      print(arg)
#fun(1, 2, 3, 4, 5)





#def evenOdd(x):
    #if (x % 2 == 0):
   #     print("even")
  #  else:
 #       print("odd")
#evenOdd(2)
#evenOdd(3)




#def fun():
#    print("Welcome to GFG")
#fun()


#var = -94
#print('Absolute value of integer is:', abs(var))




#float_number = -54.26
#print('Absolute value of float is:', 
               #   abs(float_number))


#l = [False, False, True, False, False]
#print(any(l))





#s = "Hi There!"
#print(any(s))
#s = "000"
#print(any(s))
#s = ""
#print(any(s))





def cal_dis(speed, time):
    print(" Time(hr) :", time)
    print(" Speed(km / hr) :", speed)
    return speed * time

def cal_time(dist, speed):
    print(" Distance(km) :", dist)
    print(" Speed(km / hr) :", speed)
    return dist / speed
print(" The calculated Speed(km / hr) is :", cal_speed(abs(45.9), abs(-2)))
print("")
print(" The calculated Distance(km) :",
      cal_dis(abs(-62.9), abs(2.5)))
print("")

print(" The calculated Time(hr) :",
      cal_time(abs(48.0), abs(4.5)))