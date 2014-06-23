from animal_class import *

class Cow(Animal):
    """A Generic Representation of a cow"""

    def __init__(self,name):
        super().__init__(1,5,7)
        self._type = "Cow"
        self._name = name

    def grow(self,food,water):
        if food >= self._food_need and water >= self._water_need:
            if self._status == "Young" and food > self._food_need and water > self._water_need:
                self._weight += self._growth_rate * 1.50
            elif self._status == "Young Adult" and food > self._food_need and water > self._water_need:
                self._weight += self._growth_rate * 1.15
            else:
                self._weight += self._growth_rate
        self._days_growing += 1
        self.update_status()
