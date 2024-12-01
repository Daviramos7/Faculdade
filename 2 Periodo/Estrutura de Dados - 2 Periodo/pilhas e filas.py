#pilhas

pilha = []
def inserir(x):
    pilha.insert(0, x)

def remover():
    pilha.pop(0)

inserir('prato A')
inserir('prato B')
inserir('prato C')
inserir('prato D')

remover()
remover()
remover()
remover()

def visitar(x):
    pilha.insert(0, x)

def voltar():
    pilha.pop(0)

visitar('Google')
visitar('Gmail')
visitar('Youtube')

voltar()
voltar()
voltar()

#filas

fila = []

def insert(x):
    fila.append(x)

def remove():
    fila.pop(0)

insert(1)
insert(2)
insert(3)
insert(4)

remove()
remove()
remove()
remove()