import math
def theNumber(n): 
  if n <= 1: 
    return False
  for i in range(2, (int)(math.sqrt(n))): 
    if n % i == 0: 
      return False
  return True
def Oppour(n):
  if theNumber(n) and theNumber(n - 2): 
    return True
  else: 
    return False
n = 13
if Oppour(n) == True: 
  print("Yes") 
else: 
  print("No")

def countThe3(n):
  count = 0
  while (n > 0):
      if (n % 10 == 3):
          count = count + 1
          n = int(n / 10)
          return count

def CountTheRange(n):
  count = 0
  for i in range(2,n):
    count = count + countThe3(i);
    return count

    number = int(input("Enter the number : "))
    print(CountTheRange(number))

mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
sum = 0
theStart = 0
theEnd = 0;
m = 3
n = 3
theArr = []
z = 0
print("Sum of rows is ", end = "")
for row in range(0, m):
  sum = 0
  for col in range(0, n):
    sum = sum + mat[row][col]
    print(sum, end =  "")
    z = z + 1
    theArr.append(sum)

    temp_row = theArr[0]
    for i in range(1, m):
        if(temp_row < theArr[i]):
            temp_row = theArr[i]
            theStart = i
            print("Row", theStart+1,"has maximum sum")
            print("Sum of columns is ", end = "")

            sum = 0
            y = 0
            col_arr = []
            for i in range(0, n):
                sum = 0
                for j in range(0, m):
                    sum = sum + mat[j][i]
                    print(sum, end = "")
                    y = y + 1
                    col_arr.append(sum)

                    temp_col = col_arr[0]
                    for i in range(1, n):
                        if(temp_col < col_arr[i]):
                            temp_col = col_arr[i]
                            col_ind = i
print("Column", col_ind+1,"has maximum sum")