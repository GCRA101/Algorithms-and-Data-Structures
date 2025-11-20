# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 11:10:49 2023

@author: giorg
"""


from DoubleRecord import RecordDoppio


class ListaPuntataDoppia:
    
    # ATTRIBUTES
    _primoRecord=None
    _ultimoRecord=None
    
    # CONSTRUCTOR
    def __init__(self,_primoRecord=None,_ultimoRecord=None):
        self._primoRecord=_primoRecord
        self._ultimoRecord=_ultimoRecord
    
    # METHODS
    
    'Setters'
    def setPrimoRecord(self,_primoRecord):
        self._primoRecord=_primoRecord
    def setUltimoRecord(self,_ultimoRecord):
        self._ultimoRecord=_ultimoRecord
    
    'Getters'
    def getPrimoRecord(self):
        return self._primoRecord
    def getUltimoRecord(self):
        return self._ultimoRecord
    
    'ToString'
    def __str__(self):
        p_corr=self._primoRecord
        output=""
        while p_corr!=None:
            if p_corr.getNext()!=None:
                output+="["+str(p_corr.getData())+"]"+" - "
            else:
                output+="["+str(p_corr.getData())+"]"
            p_corr=p_corr.getNext()
        return output


    'LETTURA - READING'
    
    '''For definizione, the lettura (reading) consente of ottenere the value
    of a element to partire dal suo index all'interno of a list'''
    def read(self,index):                                # T(n)
        'Controllo input'
        if index<0:                                      # Θ(1)
            return None                                  # Θ(1)
        'Inizializzazione record corrente'
        p_corr=self._primoRecord                         # Θ(1)
        'Ricerca record corrispondente to indice'
        for the in range(0,index,1):                       # n*Θ(1)
            p_corr=p_corr.getNext()                      # Θ(1)
            if p_corr==None:                             # Θ(1)
                return None                              # Θ(1)
        'Restituzione value contained in the Record'
        return p_corr.getData()                          # Θ(1)
        
    # Computational Cost: 
    # Worst case - T(n)=Θ(1)+n*Θ(1)+Θ(1)=O(n) -l'index e' maggiore del max'
    # Best case - T(n)=Θ(1)+1*Θ(1)+Θ(1)=Ω(1) -l'index e' zero'


    'RICERCA - SEARCH'
    
    '''For definizione, the ricerca consente of ottenere l'index of a element
     all'interno of a list to partire dal suo value'''
    def search(self,key):                                # T(n)
        p_corr=self._primoRecord                         # Θ(1)
        the=0                                              # Θ(1)
        while p_corr!=None and p_corr.getData()!=key:    # n*Θ(1)+Θ(1)
            p_corr=p_corr.getNext()                      # Θ(1)
            the+=1                                         # Θ(1)
        if p_corr!=None:                                 # Θ(1)
            return the                                     # Θ(1)
        return None                                      # Θ(1)
    
    # Computational Cost: 
    # Worst case - T(n)=Θ(1)+n*Θ(1)+Θ(1)=O(n) -the key not c'e' 
    # Best case - T(n)=Θ(1)+1*Θ(1)+Θ(1)=Ω(1) -the key e' in first posizione
    
    
    
    'INSERIMENTO - INSERTION'
    
    '''For definizione, l'inserimento consente of aggiungere a element ad 
    one specificato indice all'interno della lista'''
    
    def insert(self,index,given):                        # T(n)
    
        'PREPARATIVI'
        'Controllo input'
        if index<0:                                     # Θ(1)
            return                                      # Θ(1)
        'Creazione nuovo record'
        record=RecordDoppio(given)                       # Θ(1)
        
        'INSERIMENTO IN TESTA'
        if index==0:                                    # Θ(1)
            record.setNext(self.getPrimoRecord())       # Θ(1)
            self.setPrimoRecord(record)                 # Θ(1)
            return                                      # Θ(1)
        
        'INSERIMENTO IN MEZZO'    
        p_corr=self._primoRecord                        # Θ(1)
        for the in range(0,index-1,1):                    # k*Θ(1)+Θ(1)
            p_corr=p_corr.getNext()                     # Θ(1)
            if p_corr==None:                            # Θ(1)
                return                                  # Θ(1)
        record.setPrev(p_corr)                          # Θ(1) 
        record.setNext(p_corr.getNext())                # Θ(1)
        p_corr.setNext(record)                          # Θ(1)
        
        return                                          # Θ(1)
            
        
    # Computational Cost: 
    # T(n)=Θ(1)+n*Θ(1)=O(n) (for worst case - index>indexMax)
    # T(n)=Θ(1)+1*Θ(1)=Ω(1) (for best case - index<=0)
    
    
    
    'DELETION - DELETION'
    
    '''For definizione, the cancellazione consente of eliminare a element 
    contenuto in a lista sulla base del suo indice'''
    
    def delete (self,index):                              # T(n)
      'Controllo input'
      if index<0:                                         # Θ(1)
          return                                          # Θ(1)
      'Inizializzazione Record corrente'
      p_corr=self._primoRecord                            # Θ(1)
      
      'Cancellazione first element'
      if index==0:                                        # Θ(1)
          self.setPrimoRecord(p_corr.getNext())           # Θ(1)
      
      'Cancellazione element Intermedio'
      for the in range(0,index-1,1):                        # k*Θ(1)+Θ(1)
          p_corr=p_corr.getNext()                         # Θ(1)
          if p_corr==None:                                # Θ(1)
              return                                      # Θ(1)
      p_corr.getNext().getNext().setPrev(p_corr)          # Θ(1)
      p_corr.setNext(p_corr.getNext().getNext())          # Θ(1)
      
      return                                              # Θ(1)
        
  
  # Computational Cost: 
  # T(n)=O(n) - Worst case (element from eliminare not esiste)
  # T(n)=Ω(1) - Best case (element from eliminare e' the first della list) 