set1={23,"boys","look"}
set2={78,"look","books"}
set3={88,97,90.9,"ok",True,"look"}
set4={"yes","ok",89.88,False}
print(set1 |set2 |set3) #it will print the union of three sets(set1,set2 and set3) and | used for union
print(set1.union(set2,set3)) #it also do union
set1 |= set2  #it will update the set1 because |= used for update
set1.update(set2) #it also update
print(set1)  
print(set1 & set2 &set3)  #operator & is used for intersection
print(set1.intersection(set2,set3))
#note: with union and instersection method it is not necessary to pass a set we can pass any data type in their bracs
#but if we donot pass a set to the operators of union and intersection it will give error
set1.intersection_update(set2) #it will update and give common member to set1 can also pass any data type not always set
print(set1)
x=set1-set2
print(set1)