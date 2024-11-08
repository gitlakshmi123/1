def area_of_circle(r):
    return(2*3.142*r)
print("area of a circle is",area_of_circle(5)) 
def multiples(s,e):
    print("The Multiples of 3 are:")
    for i in range(s,e):
        if i%3 == 0:
            print(i)
            multiples(2,30) 
def fact(n):
    return n*fact(n-1) if n>1 else 1
print("The factorail of a given number is:",fact(5))  
x=lambda n:n*n*n 
print("The cube of a number is:",x(5))
