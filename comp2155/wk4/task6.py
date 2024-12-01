from task5 import Apartment

apartment1 = Apartment("1234 summer hill", 1, 10000, 2, 3)

print(f"bathrooms: {apartment1.bathrooms}")
print(f"bedrooms:  {apartment1.bedrooms}")

apartment1.bathrooms = 3
apartment1.bedrooms = 6

print(apartment1)