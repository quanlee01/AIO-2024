class Queue: 
    def __init__(self, capacity):
        self.storage = []
        self.capacity = capacity

    def is_empty(self):
        if not self.storage:
            return True
        return False
    
    def is_full(self):
        if len(self.storage) == self.capacity:
            return True
        return False
    
    def dequeue(self): 
        if not self.is_empty():
            front = self.storage[0]
            self.storage.pop(0)
            return front
        
    def enqueue(self, value):
        if not self.is_full():
            self.storage.append(value)

    def front(self):
        if not self.is_empty():
            return self.storage[0]
        

if __name__ == "__main__":
    queue1 = Queue(capacity=5)
    queue1.enqueue(1)
    queue1.enqueue(2)
    print(queue1.is_full())
    print(queue1.front())
    print(queue1.dequeue())
    print(queue1.front())
    print(queue1.dequeue())
    print(queue1.is_empty())
