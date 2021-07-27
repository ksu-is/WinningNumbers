#My copied code from Visual Studio Code 
import random

#Empty list used to store the 6 lucky numbers!
lotteryNumbers = []
 #1-69 
for i in range (0,6):
  number = random.randint(1,69)
  #Check if this number has already been picked...
  while number in lotteryNumbers:
    # ..if number has been picked.. pick a new number instead 
    number = random.randint(1,69)
  
  #Append unique number to our list 
  lotteryNumbers.append(number)

#Sort the list in ascending order
lotteryNumbers.sort()

#Display list on screen:
print(">>> Today's lucky lottery numbers are: ") 
print(lotteryNumbers)

print("Have a great day, hope you win big!")

