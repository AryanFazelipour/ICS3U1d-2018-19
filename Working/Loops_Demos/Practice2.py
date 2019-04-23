litres_max = 70
fuel_efficiency = 13.9 #L/100km

#table header
print("{0:>16} {01:>22}".format("Litres Used","Distance Travelled"))

for litres in range(0,litres_max,10):
    distance = (100*litres)/fuel_efficiency
    print("{0:14}L {2:5>} {1:>20.2f}L".format(litres,distance, "$"))




