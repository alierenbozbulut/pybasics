while True:
    answer = input("Enter number (press 'q' to exit) : ")
    if answer == "q":
        break
    else:
        num = int(answer)
        sum = 0
        for i in range(1,num): # if the num is 6, "i" becomes 1,2,3,4,5 one by one
            if num % i == 0: # 6/1,6/2,...,6/5
                sum += i  # sum = sum+i , "i" becomes 1,2,3 one by one and summed with "sum"
        if sum == num:
            print("{} is perfect number.".format(num))
        else:
            print("{} is not perfect number.".format(num))


