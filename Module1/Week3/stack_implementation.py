class Stack:
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
    def pop(self):
        if not self.is_empty():
            top = self.storage[-1]
            self.storage.pop()
            return top
    def push(self, value): 
        if not self.is_full():
            self.storage.append(value)
    def top(self):
        if not self.is_empty():
            return self.storage[-1]

if __name__ == "__main__":
    stack1 = Stack(capacity = 5)
    stack1.push(1)
    stack1.push(2)
    print(stack1.is_full())
    print(stack1.top())
    print(stack1.pop())
    print(stack1.top())
    print(stack1.pop())
    print(stack1.is_empty())