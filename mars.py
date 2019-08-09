import ephem 

mars = ephem.Mars()
mars.compute('2000/01/01')
print(mars.ra, mars.dec)

