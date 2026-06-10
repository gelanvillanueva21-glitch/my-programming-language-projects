
class Queue:
    def __init__(self):
        self.Queue = []


    def enqueue(self, value):
        self.Queue.append(value)


    def dequeue(self):
        if self.size() == 0:
            return "Queue is Empty"
        return self.Queue.pop(0)


    def peek(self):
        if self.size() == 0:
            return "Queue is Empty"
        return self.Queue[0]


    def isEmpty(self):
        return len(self.Queue) == 0


    def size(self):
        return len(self.Queue)


queue = Queue()

queue.enqueue("Gelan")
queue.enqueue(1)
queue.enqueue(13)
queue.enqueue("Chanzine")
queue.enqueue("Wahhhhhh")

print(queue.size())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.isEmpty())