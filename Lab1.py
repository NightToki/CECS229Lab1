#try a simple program on their own. Get user input (a number)
#if it is positive, print positive.
#if it is negative, print negative.
#if it is zero, print zero
user = True
while(user == True):
    print("Enter a number")
    x = int(input())
    if(x>0):
        print("Positive")
        user =False
    if (x < 0):
        print("Negative")
        user = False
    if (x == 0):
        print("Zero")
        user = False