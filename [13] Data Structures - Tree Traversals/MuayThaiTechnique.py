# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 10:49:01 2023

@author: giorg
"""


class MuayThaiTechnique :
    
    #ATTRIBUTES
    thaiName=None
    englishName=None
    description=None
    
    #CONSTRUCTORS
    'Both Default and Overloaded'
    def __init__(self,thaiName=None,englishName=None,description=None):
        self.thaiName=thaiName
        self.englishName=englishName
        self.description=description
    
    #METHODS
    'Setters'
    def setThaiName(self,thaiName):
        self.thaiName=thaiName
    def setEnglishName(self,englishName):
        self.englishName=englishName
    def setDescription(self, description):
        self.description=description
    'Getters'
    def getThaiName(self):
        return self.thaiName
    def getEnglishName(self):
        return self.englishName
    def getDescription(self):
        return self.description
    
    
    'ToString'
    def __str__(self):
        info="Thai Name: " + self.thaiName +"\n" + \
             "English Name: " + self.englishName + "\n" + \
             "Description: " + self.description
        return info
    
    'CompareTo'
    def __lt__(self,o):
        return self.getThaiName()<o.getThaiName()
    def __le__(self,o):
        return self.getThaiName()<=o.getThaiName()
    def __eq__(self, o):
        return self.getThaiName()==o.getThaiName()
    def __ne__(self,o):
        return not self.__lt__(o)
    