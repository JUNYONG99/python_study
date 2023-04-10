def plus(x=0, y=0):
  print(f"plus result {x + y}")


def minus(x=0, y=0):
  print(f"minus result {x - y}")


def mul(x=0, y=0):
  print(f"mul result {x * y}")


def div(x=0, y=0):
  print(f"div result {x / y}")


def power(x=0, y=0):
  print(f"power result {x ** y}")


print("*** calculator_program ***")
print()
while True:
  method = int(
    input("1. plus  2. minus  3. mul  4. div  5. power  0. exit : "))
  if method == 0:
    break
  elif method == 1:
    x = int(input("x: "))
    y = int(input("y: "))
    plus(x, y)
  elif method == 2:
    x = int(input("x: "))
    y = int(input("y: "))
    minus(x, y)
  elif method == 3:
    x = int(input("x: "))
    y = int(input("y: "))
    mul(x, y)
  elif method == 4:
    x = int(input("x: "))
    y = int(input("y: "))
    div(x, y)
  elif method == 5:
    x = int(input("x: "))
    y = int(input("y: "))
    power(x, y)
  else:
    print("your input is not process for method")
