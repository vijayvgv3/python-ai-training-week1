a =10
b =10.5
c ="python"
d =[1, 2, 3]
e ={"name":"vijay","age":20}
f ={1, 2, 3}
g =(10, 20, 30)

  
print (a, type(a))
print (b, type(b))
print (c, type(c))
print (d, type(d))
print (e, type(e))
print (f, type(f))
print (g, type(g))


sales = [12000, 0, 8500, 15000, -200, 9800]
total = 0
target = 30000

for value in sales:
 

 if value <= 0:
     print("Skipped invsalid value", value)
     continue


 total += value
print("Added ", value,"total",total)

 
if total > target:
     

         print("target reached. stopped at",total)
else:
     print("Target not reached")