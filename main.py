# https://www.edutorial.nl/python/modules/

from modules import mycsv

r = open("test.txt", "rt")
# print(len(r.readlines()))

persons = []
for i in open("test.txt", "rt"):
     clean_list = mycsv.sanitize(i)
     person = mycsv.create_person(clean_list)
     mycsv.add_fullname(person)
     persons.append(person)
    
print(len(persons))