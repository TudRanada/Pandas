import pandas as pd
cars = pd.read_csv("cars.csv")
print "The data of the first five rows with odd-numbered columns are:"
a = cars.iloc[cars.index[[0,1,2,3,4,]],[1,3,5,7,9]]
print a
print "\n"
print "The model of the Mazda RX4 are as follows:"
b = cars.iloc[0,:]
print b
print "\n"
print "How many cylinders does the Camaro Z28 have?"
c = cars.iloc[[23], cars.columns.get_indexer(['Model','cyl'])]
print c
print "\n"
print "The needed data are the following"
d = cars.iloc[[1,28,18], cars.columns.get_indexer(['Model','cyl', 'gear'])]
print d