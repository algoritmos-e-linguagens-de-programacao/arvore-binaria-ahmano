from BinaryTree import binaryTree

arvore = binaryTree()
arvore.adicionar(4)
arvore.adicionar(2)
arvore.adicionar(5)
arvore.adicionar(10)
arvore.adicionar(1)
arvore.adicionar(12)
arvore.adicionar(3)
arvore.printar()
print("------------------------------------")
print("ARVORE APOS REMOVER NUMERO 5")
arvore.remover(5)
arvore.printar()
print("------------------------------------")
print("ARVORE APOS REMOVER NUMERO 2")
arvore.remover(2)
arvore.printar()


