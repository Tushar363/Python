elements_to_enqueue = [10, 20, 30, 40, 50, 60, 70]
class Queue:
    def __init__(self):
        self.queue = []
        
    def enqueue(self, item):
        self.queue.append(item)
        print(f"Enqueued: {item}")
        
    def dequeue(self):
        if not self.is_empty():
            item = self.queue.pop(0)
            print(f"Dequeued: {item}")
            return item
        else:
            print("Queue is empty, cannot dequeue.")
            return None
            
    def is_empty(self):
        return len(self.queue) == 0

    def display(self):
        print("Queue:", self.queue)

q = Queue()

for elem in elements_to_enqueue:
    q.enqueue(elem)

q.display()

q.dequeue()
q.display()
