
class Stack:
    def __init__(self):
        self.stack = []


    def push(self, value):
        self.stack.append(value)


    def pop(self):
        if len(self.stack) >= 1:
            return self.stack.pop()
        return "Stack is Empty"


    def peek(self):
        if len(self.stack) >= 1:
            return self.stack[-1]
        return "Stack is Empty"


    def isEmpty(self):
        return len(self.stack) == 0


    def size(self):
        return len(self.stack)


stack = Stack()

stack.push("Gelan")
stack.push("Cookie")
stack.push("Molly")
stack.push("Dog")
stack.push("Cat")
stack.push("Chanzine")
stack.push("Ilove")

print(stack.size())
print(stack.isEmpty())
print(stack.pop())
print(stack.peek())