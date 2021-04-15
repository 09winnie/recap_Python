x=10
print x
y=x*10
print(y)
c="ha"
print(c)
v=c*10
print(v)
f=["tomatoes","onions","cucumbers","kales","broccoli","apples"]
print(f[1])
print(f.index("onions"))
items=["avocadoes","mangoes","peas","strawberries"]
f.extend(items)
print(f)
print(f.pop())
print(f)
f.sort()
print(f)
f.reverse()
print(f)
name="Tiffany Kanyumbani"
age=30
weight=57
nationality="Kenyan"
print(
    "Hello,my name is {}.I am {} years old.I weigh {} kgs and i am {}. ".format (name,age,weight,nationality))

a="Welcome to the AkiraChix Community "
print(len(a))
print(a[20])
print(a[-35:18])
print(a[0::2])
print(a[:-3])
print(a[-1:-35:-1])
x=[1,3,5,7,9,11,15]
x.extend("studies")
x.append(18)
print(x)
del x[6]
print(x)

student_name="Melannie Tamara"
stream="AnitaB"
number=7104
nationality="S.Africa"

print("Hello,my name is {}.I am in {} class and my admission number is {}.I am from {}.".format(student_name,stream,number,nationality) )
y=[2,4,6,8,10,12,14,16,18,20]
z=[]
for a in y:
    b=a*a
    z.append(b)
    print(z)
