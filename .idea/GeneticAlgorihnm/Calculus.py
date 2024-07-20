import math

class Calculus:
    def CalculateDistanceFromCities(self,city1,city2):
        cityA_X , cityA_Y = int(city1[1]), int(city1[2])
        cityB_X, cityB_Y = int(city2[1]), int(city2[2])
        return math.sqrt((cityB_X - cityA_X)**2 + (cityB_Y - cityA_Y)**2)


