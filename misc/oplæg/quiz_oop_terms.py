"""
Add oop related comments to this code. Examples:
    class definition
    constructor
    inheritance
    object definition
    attribute
    method
    polymorphism
    encapsulation: protected attribute
    encapsulation: protected method
"""


class Building:
    def __init__(self, area, floors, value):
        self.area = area
        self.floors = floors
        self._value = value

    def renovate(self):
        print("Installing an extra bathroom.")
        self._adjust_value(10)

    def _adjust_value(self, percentage):
        self._value *= 1 + (percentage / 100)
        print(f'Value has been adjusted with {percentage}% to {self._value:.2f}')


class Skyscraper(Building):

    def renovate(self):
        print("Installing a faster elevator.")
        self._adjust_value(6)


small_house = Building(160, 2, 200000)
skyscraper = Skyscraper(5000, 25, 10000000)

for building in [small_house, skyscraper]:
    building.renovate()
