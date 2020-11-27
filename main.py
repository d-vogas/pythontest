a=0.6
b=0.2+0.2+0.2
print (a)
print (b)
print (a==b)
tol=1e-12
print (abs(a-b)<tol)
mylist=[]
mylist=[1, 53, 349.34, "keimeno"]
print(mylist[0])
print(mylist[-1])
print(mylist[0:2])
print(mylist[0:3])
print(mylist[1:4])
print(mylist[1:])
print(mylist[:-2])
print(mylist[::3])
print(mylist[0::3])
mylist.append("new_element")
print(mylist)
mylist.remove(349.34)
print(mylist)
mylist.insert(0, 2)
print(mylist)
mylist + [15, 22]
print(mylist)
print(mylist*3)
del mylist[0]
print(10 in mylist)
print(53 in mylist)
for metavliti in mylist:
  print(metavliti)
for index in range(20):
  print(index)
for index in range(5, 20):
  print(index)
cubic=[i**3 for i in range(1,10)]
print (cubic)

