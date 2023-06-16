def calculate():
  print ('укажите соответствующую операцию ')
  print ('* - умножение')
  print ('/ - деление')
  print ('+ - сложение')
  print ('- - вычитание')

  operation = input()

  if operation == '*':
      num1 = input('введите 1 число')
      num2 = input ('введите 2 число')
      try:
          res = int(num1)*int(num2)
      except ValueError:
          print('неизвестные значения')
      else:
          print(res)

  elif operation == '/':
      num1 = input('введите 1 число')
      num2 = input ('введите 2 число')
      try:
        res = int(num1)/int(num2)
      except ValueError:
        print('неизвестные значения')
      else:  
        print(res)

  elif operation == '+':
      num1 = input('введите 1 число')
      num2 = input ('введите 2 число')
      try:
        res = int(num1)+int(num2)
      except ValueError:
        print('неизвестные значения')
      else:
        print(res)

  elif operation == '-':
      num1 = input('введите 1 число')
      num2 = input ('введите 2 число')
      try:
        res = int(num1)-int(num2)
      except ValueError:
        print('неизвестные значения')
      else:
        print(res)

  else:
      print ('операция неизвестна')
      
  print (' ')
  calculate()

calculate()
  

