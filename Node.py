class node:

  def __init__(self,value,direita = None,esquerda = None):
    self.value = value
    self.direita = direita
    self.esquerda = esquerda

  def printar(self):
    print(self.value)

  def setDireita(self,direita):
    self.direita = direita

  def setEsquerda(self,esquerda):
    self.esquerda = esquerda

    