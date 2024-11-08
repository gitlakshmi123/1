def sum(a,b):
    return(a+b) 
def sub(a,b):
    return(a-b) 
def mul(a,b): 
    return(a*b) 
def div(a,b): 
    return(a/b) 
def rem(a,b): 
    return(a%b) 
while(True): 
    print("1.ADDITION 2.SUBTRACTION 3.MULTIPLICATION 4.DIVISION 5. REMAINDER 6. EXIT") 
    choice = int(input("enter your choice:")) 
    if choice == 1: 
        a=int(input("enter first number:")) 
        b=int(input("enter second number:")) 
        print(sum(a,b)) 
    elif choice == 2: 
        a=int(input("enter first number:")) 
        b=int(input("enter second number:")) 
        print(sub(a,b)) 
    elif choice == 3: 
        a=int(input("enter first number:")) 
        b=int(input("enter second number:")) 
        print(mul(a,b)) 
    elif choice == 4: 
        a=int(input("enter first number:")) 
        b=int(input("enter second number:")) 
        print(div(a,b)) 
    elif choice == 5: 
        a=int(input("enter first number:")) 
        b=int(input("enter second number:")) 
        print(rem(a,b)) 
    else: 
        break;
