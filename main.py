
print("Будь ласка, введіть число: ")
number = int(input());

c = int(number%10)
d = int(number/10)
x = 1
k = 0
sum = 0
while ((number / 10)!=0):
      sum = sum + int(number%10)
      x = x*10
      number = (number - (number % x))/x
      k=+1
      print (number)
      print(x)
      print (sum)
      print(k)
      ave = float((sum)/k)
      print(ave)
      



  
      

# # a = int(number / 100)
# # b = int((number/10)%10)
# # c = int(number%10)

# # d = int(number/10)

# ave = float((sum)/k)

# print("Число одиниць: "+ str(c)) 

# print("Число десятків: " + str(d))

# print("Середнє арифметичне: " + str(ave))
