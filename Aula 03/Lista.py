from No import No

class Lista: 

    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def __len__(self):
        return self.tamanho 

    def adicionar_inicio(self, dado):
        no = No(dado)
        if self.tamanho == 0:
            self.inicio = no
            self.fim = no
        else:        
            aux = self.inicio
            aux.anterior = no
            no.proximo = aux
            self.inicio = no
        self.tamanho += 1

    def adicionar_fim(self, dado):
        no = No(dado)
        if self.tamanho == 0:
            self.inicio = no
            self.fim = no
        else:
            aux = self.fim
            aux.proximo = no
            no.anterior = aux
            self.fim = no
        self.tamanho += 1

    def excluir_inicio(self, dado):
        if self.tamanho == 0:
            print( "--Lista Vazia--")
        elif self.tamanho == 1 :
            if self.inicio.dado == dado:
                self.inicio = None
                self.fim = None
                self.tamanho -= 1
            else:
                print( "--não consta na lista--")
        else:
            if self.inicio.dado == dado:
                aux = self.inicio.proximo
                self.inicio = aux
                self.tamanho -= 1
            else:
                print( "--não consta como início da lista--")       

    def excluir_fim(self, dado):
        if self.tamanho == 0:
            print( "--Lista Vazia--")
        elif self.tamanho == 1 :
            if self.fim.dado == dado:
                self.inicio = None
                self.fim = None
                self.tamanho -= 1
            else:
                print( "--não consta na lista--")
        else:
            if self.fim.dado == dado:
                aux = self.fim.anterior
                self.fim = aux
                self.tamanho -= 1
            else:
                print( "--não consta como fim da lista--")

    def imprimir(self):
        aux = self.inicio
        if self.tamanho == 0:
            print("--Lista Vazia--")
        else:
            while(aux):
                print( str(aux.dado) + "\n" )
                aux = aux.proximo
        print( "Tamanho da Lista: " + str(self.tamanho))

    def imprimir_inverso(self):
        aux = self.fim
        if self.tamanho == 0:
            print("--Lista Vazia--")
        else:
            while(aux):
                print( str(aux.dado) + "\n" )
                aux = aux.anterior
        print( "Tamanho da Lista: " + str(self.tamanho))
        

    