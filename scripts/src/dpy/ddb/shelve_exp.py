import shelve

## http://pymotw.com/2/shelve/
## http://bioportal.weizmann.ac.il/course/python/PyMOTW/PyMOTW/docs/anydbm/index.html#module-anydbm
## http://docstore.mik.ua/orelly/other/python2/1.16.htm
## https://github.com/saffsd/langid.py
## http://www.bogotobogo.com/python/python_fncs_map_filter_reduce.php
## http://www.python-course.eu/lambda.php
## http://www.kernel-panic.it/programming/offtheshelf/#ots-1



flights = {"1":"A", "2":"B", "3":"C"}
times = ["230pm", "320pm", "420pm"]

db = shelve.open("shelved.dat", "n")

db['flights'] = flights
db['times'] = times

print db.keys()

db.close()

f = open("shelved.dat", "r")
data = f.read()
#print data
f.close()

# Retrieving Objects from a Shelve File

db = shelve.open("shelved.dat", "r")

for k in db.keys():
    obj = db[k]
    print "%s: %s" % (k, obj)

flightDB = db['flights']
flights = flightDB.keys()
cities = flightDB.values()
times = db['times']

x = 0
for flight in flights:
    print ("Flight %s leaves for %s at %s" % (flight, cities[x],  times[x]))
    x+=1

db.close()
