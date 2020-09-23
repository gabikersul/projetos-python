from No import No

class Stack: 

    def __init__(self):
        self.top = None
        self.size = 0

    def is_empty(self):
        if self.size == 0:
            return True
        return False

    def stack_push(self, value):
        no = No(value)
        if self.is_empty():
            self.top = no
        else:
            aux = self.top
            self.top = no
            no.next = aux
        self.size += 1

    def stack_pop(self):
        if self.is_empty():
            print('-- Pilha vazia! --')
        else:
            aux = self.top.next
            self.top = aux
            self.size -= 1

    def stack_print(self):
        if self.is_empty():
            print('-- Pilha vazia! --')
        else:
            aux = self.top
            while(aux):
                print(str(aux.item))
                aux = aux.next

    def stack_size(self):
        if self.is_empty():
            print('-- Pilha não contém itens --')
        elif self.size == 1:
            print('-- Pilha contém 1 item --')
        else:
            print('-- Pilha contém {} itens --'.format(str(self.size)))
