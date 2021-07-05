#random list generator that finds the smallest integer no in another list
import random
list1 = random.sample(range(0, 30), 26)
list2 = []
for j in range(0,100001):
    list2.append(j)
list1.sort()
for k in list1:
    if k in list2:
        list2.remove(k)
print(list2[0])
