# Write a program in python to map 2 lists into a dictionary.

keys=[1,2,3]
values=["values1","values2","values3"]

dict1=dict(zip(keys,values))
print(dict1)

        
#Python zip() method takes iterable containers and returns
#a single iterator object, having mapped values from all the containers.



#It is used to map the similar index of multiple containers
#so that they can be used just using a single entity.

Syntax :  zip(*iterators)

Parameters : Python iterables or containers ( list, string etc ) R...

name = [ "Manjeet", "Nikhil", "Shambhavi", "Astha" ]
roll_no = [ 4, 1, 3, 2 ]
# using zip() to map values
mapped = zip(name, roll_no)
print(set(mapped))
