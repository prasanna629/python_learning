 # age = 19
 # if age <= 18:
 #     print("you can vote")
 # elif age == 19:
 #     print("you  can vote but  you are not eligible")
 # else:
 #     print("wait")



 # if True:
 #     print("hi")
 # else:
#     print("hello")


# if False:
#      print("hello world")
#  elif True:
#      print("prasanna")
#  else:
#      print("else")



#  if True:
#        print("outer if")
#        if False:
#              print("inner if")
#  else:
#       print("innner else")


#  age = 20
#  if age >= 18:
#      print("Eligible to vote.")


#  age = 19
#  if age > 18: print("Eligible to Vote.")


#  age = 10
#  if age <= 12:
#     print("Travel for free.")
#  else:
#      print("Pay for ticket.")



#  age = 70
#  is_member = True
#  if age >= 60:
#      if is_member:
#          print("30% senior discount!")
#      else:
#          print("20% senior discount.")
#  else:
#    print("Not eligible for a senior discount.")



#  number = 2
# match number:
#      case 1:
#          print("One")
#      case 2 | 3:
#          print("Two or Three")
#      case _:
#          print("Other number")


#  a = 200
#  b = 33
#  c = 500
#  if a > b and c > a:
#    print("Both conditions are True")




#  a = 200
#  b = 33
#  c = 500
#  if a > b or a > c:
#    print("At least one of the conditions is True")



# a = 33
# b = 200
# if not a > b:
#   print("a is NOT greater than b")





# x = 41

# if x > 10:
#   print("Above ten,")
#   if x > 20:
#     print("and also above 20!")
#   else:
#     print("but not above 20.")






# day = 4
# match day:
#   case 1:
#     print("Monday")
#   case 2:
#     print("Tuesday")
#   case 3:
#     print("Wednesday")
#   case 4:
#     print("Thursday")
#   case 5:
#     print("Friday")
#   case 6:
#     print("Saturday")
#   case 7:
#     print("Sunday")





month = 5
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5 if month == 4:
    print("A weekday in April")
  case 1 | 2 | 3 | 4 | 5 if month == 5:
    print("A weekday in May")
  case _:
    print("No match")