#!/usr/bin/env python

matrix = [ "hello", 2.0, 5 , [10, 20]] #Euuurgh
color = (255, 10, 30, 255) #this is a tuple, also the 255 at the end is "a", which stands for alpha and denotes transparency



s = "Monty Python"
print s[6:12]


eng2sp = {}
eng2sp["one"] = 'uno'
eng2sp["two"] = 'dos'
for k,v in eng2sp.items():
    print k,v

people = { 'Jonah' : "stupid",
           "Alec" : "smelly",
           "Jack" : "ugly",
           "Paul" : "awesome"}
name = raw_input("Gimme that good name: ")

if name in people:
    print name, "is", people[name]
else:
    print "I don't know about that one."

print matrix
print matrix[0]
print matrix[3]
print matrix[3][0]
print matrix[3][1]
