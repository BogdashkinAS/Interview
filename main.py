class Stack:
    
    def __init__(self):
        self.stack = []
            
    def isEmpty(self):
        if len(self.stack) == 0:        
            return True
        else:
            return False

    def push(self, el):
        self.stack.append(el)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[len(self.stack) - 1]

    def size(self):
        return len(self.stack)

def parentheses():
    list_ = Stack()
    symbols = input('Введите строку со скобками: ')
    count = 0
    for i in symbols:
        list_.push(i)
    while list_.isEmpty() is False:
        count += 1
        if count == list_.size() and list_.isEmpty() is False:
            print('Несбалансированная последовательность - непарное количество скобок')
            break        
        if list_.size() % 2 == 0:
            for i in range(list_.size()):
                if i < list_.size():
                    if list_.stack[i] == '[' and list_.stack[i + 1] == ']':
                        del(list_.stack[i])
                        del(list_.stack[i])
                    elif list_.stack[i] == '(' and list_.stack[i + 1] == ')':
                        del(list_.stack[i])
                        del(list_.stack[i])
                    elif list_.stack[i] == '{' and list_.stack[i + 1] == '}':
                        del(list_.stack[i])
                        del(list_.stack[i])
        else:            
            print('Несбалансированная последовательность - нечетное число скобок')
            break
    if list_.isEmpty() is True:
        print('Сбалансированная последовательность')
    
 
if __name__ == '__main__':
    parentheses()