xValue= 20
while xValue>=10:
  print(xValue)
  xValue= xValue - .5

for i in range(25):
    import math
    print(math.sqrt(i))

vaild= False
while not vaild:
  value= int(input("number please"))
  if value > 0 and value < 100:
    valid= True
  else:
    print("CORRECT!")