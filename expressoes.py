class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class My_Stack:
    def __init__(self):
        self.top = None
        self._size = 0

    def push(self, elem):
        #insere um elemento na pilha
        node = Node(elem)
        node.next = self.top
        self.top = node
        self._size = self._size + 1

    def pop(self):
        # remove o elemento do topo da pilha
        if self._size > 0:
            node = self.top
            self.top = self.top.next
            self._size = self._size - 1
            return node.data
        raise IndexError("The stack is empty")

    def peek(self):
        # retorna o topo sem remover
        if self._size > 0:
            return self.top.data
        raise IndexError("The stack is empty")


    def __len__(self):
        """Retorna o tamanho da lista"""
        return self._size

    def __repr__(self):
        r = ""
        pointer = self.top
        while(pointer):
            r = r + str(pointer.data) + "\n"
            pointer = pointer.next
        return r

    def __str__(self):
        return self.__repr__()
    
    def isEmpty(self):
        return self.top is None


def isBalanced(string):
    leftchars = My_Stack()
    for i in range(len(string)):
        if string[i] == '(' or string[i] == '[' or string[i] == '{':
            leftchars.push(string[i])
        else:
            if leftchars.isEmpty():
                return False
            if string[i] == ')' and leftchars.peek() is not '(' or 
            string[i] == ']' and leftchars.peek() is not '[' or string[i] == '}' and leftchars.peek() is not '{':
                return False
            leftchars.pop()
    return leftchars.isEmpty()

def main():
    t = int(input())
    for i in range(t):
        s = input()
        if isBalanced(s):
            print("S")
        else : print("N")

main()