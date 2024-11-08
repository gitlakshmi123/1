mymodule.py 
person1 = { 
 "name":"John", 
 "age":36, 
 "country":"Norway" 
} 
test.py 
import mymodule 
a = mymodule.person1["age"] 
print(a) 
b = mymodule.person1["name"] 
print(b) 
#built-in modules 
import platform 
x = platform.system() 
print(x) 
y = dir(platform) 
print(y)
