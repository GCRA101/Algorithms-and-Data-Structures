# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 11:10:49 2023

@author: giorg
"""

from SingleRecord import RecordSingolo


class ListaPuntataSingola:
    
    # ATTRIBUTI
    _primoRecord=None
    
    # COSTRUTTORE
    def __init__(self,_primoRecord):
        self._primoRecord=_primoRecord
    
    # METODI
    
    'Setters'
    def setPrimoRecord(self,_primoRecord):
        self._primoRecord=_primoRecord
    
    'Getters'
    def getPrimoRecord(self):
        return self._primoRecord
    
    'ToString'
    def __str__(self):
        p_corr=self._primoRecord
        output=""
        while p_corr!=None:
            if p_corr.getNext()!=None:
                output+="["+str(p_corr) +"]" +" - "
            else:
                output+="["+str(p_corr) +"]"
            p_corr=p_corr.getNext()
        return output
    

    'LETTURA - READING'
    
    '''Per definizione, la lettura (reading) consente di ottenere il valore
    di un elemento a partire dal suo indice all'interno di una lista'''
    def read(self,index):                                # T(n)
        'Controllo input'
        if index<0:                                      # Θ(1)
            return None                                  # Θ(1)
        'Inizializzazione record corrente'
        p_corr=self._primoRecord                         # Θ(1)
        'Ricerca record corrispondente a indice'
        for i in range(0,index,1):                       # n*Θ(1)
            p_corr=p_corr.getNext()                      # Θ(1)
            if p_corr==None:                             # Θ(1)
                return None                              # Θ(1)
        'Restituzione valore contenuto nel Record'
        return p_corr.getData()                          # Θ(1)
        
    # Costo Computazionale: 
    # Caso peggiore - T(n)=Θ(1)+n*Θ(1)+Θ(1)=O(n) -l'index e' maggiore del max'
    # Caso migliore - T(n)=Θ(1)+1*Θ(1)+Θ(1)=Ω(1) -l'index e' zero'


    'RICERCA - SEARCH'
    
    '''Per definizione, la ricerca consente di ottenere l'indice di un elemento
     all'interno di una lista a partire dal suo valore'''
    def search(self,key):                                # T(n)
        p_corr=self._primoRecord                         # Θ(1)
        i=0                                              # Θ(1)
        while p_corr!=None and p_corr.getData()!=key:    # n*Θ(1)+Θ(1)
            p_corr=p_corr.getNext()                      # Θ(1)
            i+=1                                         # Θ(1)
        if p_corr!=None:                                 # Θ(1)
            return i                                     # Θ(1)
        return None                                      # Θ(1)
    
    # Costo Computazionale: 
    # Caso peggiore - T(n)=Θ(1)+n*Θ(1)+Θ(1)=O(n) -la key non c'e' 
    # Caso migliore - T(n)=Θ(1)+1*Θ(1)+Θ(1)=Ω(1) -la key e' in prima posizione
    
    
    
    'INSERIMENTO - INSERTION'
    
    '''Per definizione, l'inserimento consente di aggiungere un elemento ad 
    uno specificato indice all'interno della lista'''
    
    def insert(self,index,data):                        # T(n)
    
        'PREPARATIVI'
        'Controllo input'
        if index<0:                                     # Θ(1)
            return                                      # Θ(1)
        'Creazione nuovo record'
        record=RecordSingolo(data)                      # Θ(1)
        
        'INSERIMENTO IN TESTA'
        if index==0:                                    # Θ(1)
            record.setNext(self.getPrimoRecord())       # Θ(1)
            self.setPrimoRecord(record)                 # Θ(1)
            return                                      # Θ(1)
        
        'INSERIMENTO IN MEZZO'    
        p_corr=self._primoRecord                        # Θ(1)
        for i in range(0,index-1,1):                    # k*Θ(1)+Θ(1)
            p_corr=p_corr.getNext()                     # Θ(1)
            if p_corr==None:                            # Θ(1)
                return                                  # Θ(1)
        record.setNext(p_corr.getNext())                # Θ(1)
        p_corr.setNext(record)                          # Θ(1)
        
        return                                          # Θ(1)
            
        
    # Costo Computazionale: 
    # T(n)=Θ(1)+n*Θ(1)=O(n) (per caso peggiore - index>indexMax)
    # T(n)=Θ(1)+1*Θ(1)=Ω(1) (per caso migliore - index<=0)
    
    
    
    'CANCELLAZIONE - DELETION'
    
    '''Per definizione, la cancellazione consente di eliminare un elemento 
    contenuto in una lista sulla base del suo indice'''
    
    def delete (self,index):                              # T(n)
      'Controllo input'
      if index<0:                                         # Θ(1)
          return                                          # Θ(1)
      'Inizializzazione Record corrente'
      p_corr=self._primoRecord                            # Θ(1)
      
      'Cancellazione Primo Elemento'
      if index==0:                                        # Θ(1)
          self.setPrimoRecord(p_corr.getNext())           # Θ(1)
      
      'Cancellazione elemento Intermedio'
      for i in range(0,index-1,1):                        # k*Θ(1)+Θ(1)
          p_corr=p_corr.getNext()                         # Θ(1)
          if p_corr==None:                                # Θ(1)
              return                                      # Θ(1)
      p_corr.setNext(p_corr.getNext().getNext())          # Θ(1)
      
      return                                              # Θ(1)
        
  
  # Costo Computazionale: 
  # T(n)=O(n) - Caso peggiore (elemento da eliminare non esiste)
  # T(n)=Ω(1) - Caso migliore (elemento da eliminare e' il primo della lista)  
    