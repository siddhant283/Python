
while True:
  try:
    age = int(input('what is your age?'))
    print(age)
    10/age

  except ValueError:
    print("Please enter a number.") 

  except ZeroDivisionError:
    print("Please enter a number greater than zero.")   

  else:
      print('Thank You!')
      break     