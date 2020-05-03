#factorial calculation with for loop

factorial = 1
while (True):
    num = int(input("Please enter a natural number: "))
    if (num <= 0):
        print("Please enter a natural number!")
    else:
        for i in range(1,num+1): #in i, start from 1 and increase number 1 --> 1*2= 2 *3 =6 * 4= 24 *5 =120 (factorial 5)
            factorial *= i #or factorial = factorial * i

        print("Factorial: ",factorial)
        break
