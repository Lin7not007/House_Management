# import libriaries
import appliances

class User():
    #Initialize User_Info Class
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
        self.appliances = []
    
    #Method to add an appliance to user's account
    def add_appliance(self, appliance):
        self.appliances.append(appliance)
    
    #Method to remove an appliance from user's account
    def remove_appliance(self, appliance):
        self.appliances.remove(appliance)
    
    #Method to check if the user has an appliance
    def has_appliance(self, appliance):
        return appliance in self.appliances
    
    #Method to list all the appliances of the user
    def list_appliances(self):
        return self.appliances


