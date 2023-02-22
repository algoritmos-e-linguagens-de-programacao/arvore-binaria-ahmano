from binary_tree import binaryTree

arvore = binaryTree()
arvore.adicionar(4)
arvore.adicionar(2)
arvore.adicionar(5)
arvore.adicionar(10)
arvore.adicionar(1)
arvore.adicionar(12)
arvore.adicionar(3)


print("ARVORE INICIAL")
arvore.printar()
print("------------------------------------")
print("PRE ORDEM")
arvore.ex_preOrdem()
print("------------------------------------")
print("EM ORDEM")
arvore.ex_emOrdem()
print("------------------------------------")
print("POS ORDEM")
arvore.ex_posOrdem()
print("------------------------------------")
print("ARVORE INICIAL")
arvore.printar()
print("------------------------------------")
print("ARVORE APOS REMOVER NUMERO 5")
arvore.remover(5)
arvore.printar()
print("------------------------------------")
print("ARVORE APOS REMOVER NUMERO 2")
arvore.remover(2)
arvore.printar()




