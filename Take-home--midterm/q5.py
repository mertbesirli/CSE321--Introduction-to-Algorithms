# -*- coding: utf-8 -*-

#Find the lowest person cost
def findProperPeople(people):
    result =  min(people.values())
    return result
#Find the highes job cost
def findProperJob(jobs):
    result = max(jobs.values())
    return result
#Do right job assignment for the person
#The goal is to reduce cost
#I assign the highest cost of work with the lowest human cost.
def assignPersonJob(small,high,people,jobs,personJob):
    tempJob = ""
    tempPerson = ""
    #Finding people by cost
    for i in people.keys():
        if people.get(i) == small:
            tempPerson = i
            break
    #I take the found person out of the dictionary
    people.pop(tempPerson)
    #Finding job by cost
    for i in jobs.keys():
        if jobs.get(i) == high:
            tempJob = i
            break
    #I take the found job out of the dictionary
    jobs.pop(tempJob)
    #Assign person to job
    d = {tempPerson: tempJob}
    personJob.update(d)
    

people = {"Ali": 5,"Veli": 8,"Ahmet": 6,"Mehmet": 12}
jobs = {"Teacher": 14, "Doctor" : 16, "Engineer": 11,"Driver": 7}

personJob = {}



for i in range(len(people)):
    small = findProperPeople(people)
    high = findProperJob(jobs)
    assignPersonJob(small,high,people,jobs,personJob)
    
print(personJob)
    
    








