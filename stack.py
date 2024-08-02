class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        print(f"Pushed {item} to the stack.")

    def pop(self):
        if not self.is_empty():
            item = self.stack.pop()
            print(f"Popped {item} from the stack.")
            return item
        else:
            print("Stack is empty. Cannot pop.")
            return None

    def is_empty(self):
        return len(self.stack) == 0

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            print("Stack is empty. Cannot peek.")
            return None

    def display(self):
        if not self.is_empty():
            print("Stack elements are:")
            for item in reversed(self.stack):
                print(item)
        else:
            print("Stack is empty.")

if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.display()

    stack.pop()
    stack.display()

    stack.peek()
    stack.display()

    stack.pop()
    stack.pop()