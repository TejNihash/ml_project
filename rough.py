#this is a file I just use to practice the code. 

import logging

logging.basicConfig(
    filename='logs.log',
    level= logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def log_error(message):
    logging.error(message)


def say_my_name(name):

    print("you are ",name)
    log_error("a name has been said")


say_my_name("Heisenberg")


class Car:

    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
        self.print_car(model) #here we have a self function. cool. just like self variable. and since it is __init__, it gets 
        #called automatically


    def print_car(self,model_name):
        print("the car is of the make",model_name)


my_car = Car('audi','bondada')