import pandas as pd
cars = pd.read_csv("cars.csv")
carRows = cars.loc[cars.index[[0,1,2,3,4,27,28,29,30,31]],:]
print "The first five and last five rows of cars are:"
print carRows