from animal_class import *

class Sheep(Animal):
    """A Generic Representation of a sheep"""

    def __init__(self,name):
        super().__init__(1,5,7)
        self._type = "Sheep"
        self._name = name

    def grow(self,food,water):
        if food >= self._food_need and water >= self._water_need:
            if self._status == "Young" and food > self._food_need and water > self._water_need:
                self._weight += self._growth_rate * 1.65
            elif self._status == "Young Adult" and food > self._food_need and water > self._water_need:
                self._weight += self._growth_rate * 1.25
            else:
                self._weight += self._growth_rate
        self._days_growing += 1
        self.update_status()
