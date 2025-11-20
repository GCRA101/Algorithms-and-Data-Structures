# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 16:52:07 2023

@author: giorg
"""

'''
NODO for ALBERO BINARIO of RICERCA ROSSO-NERO
The Nodo dell'Binary Search Tree RossoNero viene implementato as a 
record triplo, that is a classe containing the value del nodo (key), 
the pointer al figlio sinistro, the pointer al figlio destro and the pointer 
al padre. In aggiunta to these campi ne abbiamo one aggiuntivo, detto "of 
bilanciamento" that contiene the colore assegnato al nodo and that puo' essere 
solamente o ROSSO o NERO.
'''

# IMPORT LIBRARIES dal PACKAGE
from Color import Colore


class Nodo:
 
 # ATTRIBUTES
 key=None
 color=None
 left=None
 right=None
 parent=None
 
 # CONSTRUCTOR
 'Default and Overloaded'
 def __init__(self,key=None, color=None, 
 parent=None, left=None, right=None):
 self.key=key
 self.color=color
 self.parent=parent
 self.left=left
 self.right=right
 
 
 # METHODS
 
 'Setters'
 def setKey(self,key):
 self.key=key
 def setColor(self,color):
 self.color=color
 def setParent(self, parent):
 self.parent=parent
 def setLeft(self, left):
 self.left=left
 def setRight(self, right):
 self.right=right
 
 'Getters'
 def getKey(self):
 return self.key
 def getColor(self):
 return self.color
 def getParent(self):
 return self.parent
 def getLeft(self):
 return self.left
 def getRight(self):
 return self.right
 
 'Overridden ToString()'
 
 def __str__(self):
 return (str(self.key)+"_"+str(self.color).split('.')[1][0])
 
 'Overridden CompareTo'
 def __le__(self,o):
 if isinstance(o, Nodo):
 return self.key<=o.key and \
 self.color<=o.color
 return False
 
 def __lt__(self,o):
 if isinstance(o,Nodo):
 return self.key<o.key and \
 self.color<o.color
 return False
 
 def __ge__(self,o):
 if isinstance(o,Nodo):
 return self.key>=o.key and \
 self.color>=o.color
 return False
 
 def __gt__(self,o):
 if isinstance(o,Nodo):
 return self.key>o.key and \
 self.color>o.color
 return False
 
 def __eq__(self, o):
 if isinstance(o, Nodo):
 return self.key == o.key and \
 self.color==o.color
 return False
 
 def __neg__(self,o):
 if isinstance(o,Nodo):
 return not self.__eq__(o)
 return False
 