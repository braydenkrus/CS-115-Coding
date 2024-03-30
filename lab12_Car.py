'''
CS 115, Lab 12, Inheritance

Author: Brayden Krus
Pledge: "I pledge my honor that I have abided by the Stevens Honor System."
'''

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Part 1 
' Implement missing sections of the Car class.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Car(object):
    '''Write the constructor. It should take in four arguments:
       - make (a string, the company name, a.k.a. brand)
       - model (a string)
       - mpg (miles per gallon, a float)
       - tank_capacity (capacity of the gas tank in gallons, a float)
       These should all be assigned to corresponding private fields, i.e., with
       names that start with '__'.  Use the names in the 'str' method provided below.
       '''
    def __init__(self, make, model, mpg, tank_capacity):
        '''This constructor adds the make, model, mpg, and tank_capacity'''
        self.__make = make
        self.__model = model
        self.__mpg = mpg
        self.__tank_capacity = tank_capacity

    '''Write getters for make, model, mpg, and tank_capacity.'''
    def get_make(self):
        '''This is a getter for make.'''
        return self.__make
    
    def get_model(self):
        '''This is a getter for model.'''
        return self.__model

    def get_mpg(self):
        '''This is a getter for mpg.'''
        return self.__mpg
    
    def get_tank_capacity(self):
        '''This is a getter for tank_capacity.'''
        return self.__tank_capacity
    
    '''Write setters for mpg and tank_capacity.'''
    def set_mpg(self, newmpg):
        '''This is a setter for mpg.'''
        self.__mpg = newmpg

    def set_tank_capacity(self, newtank):
        '''This is a setter for tank_capacity.'''
        self.__tank_capacity = newtank

    '''Write a method called get_total_range.
       It returns the total distance the car can travel on a full tank of
       gas.'''
    def get_total_range(self):
        '''This will return the total range by multiplying miles per gallon by the amount of gallons in the tank.'''
        return self.__mpg * self.__tank_capacity

    def __str__(self):
        '''A string for printing information about a car.'''
        return self.__make + ' ' + self.__model + ', MPG: ' + str(self.__mpg) \
            + ', tank capacity: ' + str(self.__tank_capacity)

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Part 2 
' Implement missing sections of the HybridCar class. 
' Make HybridCar be a subclass of Car.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class HybridCar(Car):  
    '''Write the constructor. It should take in 6 arguments:
    - the first four are the same as in the Car constructor
    - battery_kWh (battery power in kilowatt-hours, a float)
    - miles_per_kWh (miles per kilowatt-hours, a float)
    The additional fields must be private.
    '''
    def __init__(self, make, model, mpg, tank_capacity, battery_kWh, miles_per_kWh):
        '''This constructor adds the make, model, mpg, and tank_capacity to Car. It also adds battery_kWh and miles_per_kWh'''
        Car.__init__(self, make, model, mpg, tank_capacity)
        self.__battery_kWh = battery_kWh
        self.__miles_per_kWh = miles_per_kWh

    '''Implement the following method.'''
    def get_battery_range(self):
        '''Returns the total distance the car can travel on a fully charged
        battery.
        '''
        '''returns the distance the car can get on a fully charged battery'''
        return self.__battery_kWh * self.__miles_per_kWh

    '''Override the method get_total_range.
    Returns the total distance the car can travel on a full tank of
    gas and a fully charged battery.
    Do not do any math here except a single +. To get credit, you must call
    the methods you have already written.
    '''
    def get_total_range(self):
        '''Returns how far the car can go on a full tank and a fully charged battery.'''
        return Car.get_total_range(self) + self.get_battery_range()

    def __str__(self):
        '''A string for printing information about a car.'''
        return super().__str__() + ', battery kWh: ' + \
            str(self.__battery_kWh) + ', miles/kWh: ' + \
            str(self.__miles_per_kWh)