class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()
    
    def peek(self):
        return self.stack[-1]
    
    def isEmpty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)
    
def reverse_string(string):
    stk = Stack()
    for i in range(0, len(string)):
        stk.push(string[i])

    
    result = ""

    while(not stk.isEmpty()):
        result += stk.pop()

    return result

if __name__ == '__main__':
    result = reverse_string("We will conquere COVID-19")
    print(result)
