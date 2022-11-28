from Node import node as n

class binaryTree:

  def __init__(self):
    self.root = None

  #funcao que itera a arvore para achar o node pai de um node filho
  def acharPai(self,aux,valor,pai = None):
    if(aux is None):
      return
    if(aux.value == valor):
      return pai
    else:
      return self.acharPai(aux.esquerda,valor,aux)
      return self.acharPai(aux.direita,valor,aux)

  
  #funcao privada que printa a arvore
  def __printarArvore(self,controle,distancia):
    if (controle == None):
      return
    else:
      distancia += 1

      self.__printarArvore(controle.direita, distancia)

      print()
      for i in range(0,distancia):
        print(end="    ")
      print(controle.value)

      self.__printarArvore(controle.esquerda,distancia)

  #funcao para printar a arvore
  def printar(self):
    self.__printarArvore(self.root,0)
      
  #funcao para adicionar valores na arvore
  def adicionar(self,value):
    aux = self.root
   

    while(True):

      if(self.root == None): 
        node = n(value)
        self.root = node
        break
      
      if(aux.esquerda == None): 
        if(value < aux.value):
          node = n(value)
          aux.setEsquerda(node)
          break

      if(aux.direita == None):   
        if(value > aux.value):
          node = n(value)
          aux.setDireita(node)
          break

      if(value<aux.value):
        aux = aux.esquerda
      elif(value>aux.value):
        aux = aux.direita 

  #funcao para remover valor da arvore e ajeita-la
  def remover(self,value):
    self.__removerAjeitar(value,self.root)


  #funcao para ajeitar a arvore apos remocao de valor
  def __ajeitar(self,controle):
    aux = controle

    while True:
    
      if(aux.value == None):

        if(aux.esquerda == None and aux.direita == None):
          break
         
        if(aux.esquerda is not None):
          aux.value = aux.esquerda.value
          aux.esquerda.value = None
          aux = aux.esquerda
        if(aux.direita is not None):
          aux.value = aux.direita.value
          aux.direita.value = None
          aux = aux.direita

         

  #funcao que itera a arvore ate achar certo valor para entao remove-lo
  #e chama tambem a funcao de ajeitar
  def __removerAjeitar(self,value,controle = None):

    if(self.root == None):
      return self.root

    if(value == controle.value):
      controle.value = None
      self.__ajeitar(controle)
        
    if(controle.esquerda is not None):
      self.__removerAjeitar(value,controle.esquerda)
      
    if(controle.direita is not None):
      self.__removerAjeitar(value,controle.direita)
    
