# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 18:45:00 2023

@author: nonononon..
"""

class StateMachine:
    def __init__(self, first_state):
        next_state = first_state(self)
        while next_state:
            next_state = next_state()
            
    def Parameters(self) : 
        print("Current State :      {0}".format(self.name))
        print("Can edit feature :   {0}".format(self.canEdit))
        print("Can act on feature : {0}".format(self.canAct))
        print("Next states :        {0}".format(self.nextState))
        
        
class States(StateMachine) :
    def Draft(self) :
        self.name = "Draft" 
        self.canEdit = True
        self.canView = False
        self.canAct = False
        self.nextState = ["Registered"]
        
    def Registered(self) : 
        self.name = "Registered"
        self.canEdit = False
        self.canView = True
        self.canAct = True
        self.nextState = ["Validated", "Draft"]
        
    def Validated(self) : 
        self.name = "Validated"
        self.canEdit = False
        self.canView = True
        self.canAct = True
        self.nextState = ["Approved", "Rejected", "Draft" ]
        
    def Approved(self) : 
        self.name  = "Approved"
        self.canEdit = False
        self.canView = True
        self.canAct = False
        self.nextState = [None]
        
    def Rejected(self) : 
        self.name  = "Rejected"
        self.canEdit = False
        self.canView = False
        self.canAct = False
        self.nextState = [None]
        
    def Next(self) : 
        
        if self.nextState == None : 
            return print("Request has reach its final state")
    
        elif len(self.nextState) == 1: 
            return self.Registered()
        
        while True:
            value = input("Possible next state to push : {0} ".format(self.nextState))
            if value in self.nextState:
                if self.name == "Registered" : 
                    if value == "Validated" : 
                        return self.Validated()
                    return self.Draft()
                if self.name == "Validated" :
                    if value == "Approved" : 
                        return self.Approved()
                    if value == "Rejected" : 
                        return self.Rejected()
                    return self.Draft()


            else:
                print("Error - wrong input!")

        


test = States(States.Draft)

