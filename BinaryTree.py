from Node import node as n

class binaryTree:

  def __init__(self):
    self.root = None

  
  def iterar(self):
    mae, controle= None, self.root
    lista = []
    while controle is not None: 
      
      if controle.esquerda is not None: 
        lista.append(controle.value) 
        mae, controle = controle, controle.esquerda
        
      if controle.direita is not None:       
        lista.append(controle.value)
        mae, controle = controle, controle.direita

  
  def printar(self):
    mae, controle= None, self.root
    lista = []
    while controle is not None: 
      
      if controle.esquerda is not None: 
        lista.append(controle.value) 
        mae, controle = controle, controle.esquerda
        
      if controle.direita is not None:       
        lista.append(controle.value)
        mae, controle = controle, controle.direita

    print(lista)
    

  def adicionar(self,value):
    aux = self.root
    node = n(value)

    while(True):

      if(self.root == None):      
        self.root = node
        break
      
      if(node.esquerda == None): 
        if(value < aux.value):
          node.setEsquerda(value)
          break

      if(node.direita == None):   
        if(value > aux.value):
          node.setDireita(value)
          break

      if(value<aux.value):
        aux = aux.esquerda

      if(value>aux.value):
        aux = aux.direita 


  def remover(self,controle,value):
    if(self.root == None):
      return self.root

    if(value<self.root.value):
      self.root.esquerda = self.remover(self.root.esquerda,value)

    if(value>self.root.value):
      self.root.direita = self.remover(self.root.direita,value)
    
