from collections import deque


class Stack:
    """Create a Stack (LIFO) of products data"""

    def __init__(self):
        self.stack = deque()

    def add_top(self, item):
        """Add new item to the end of stack"""
        self.stack.append(item)

    def peek(self):
        """See last added item of stack without removing it"""
        print(self.stack[-1])

    def pop_top(self):
        """Delete last added item of stack"""
        return self.stack.pop()

    def size(self):
        """Get length of the stack"""
        return len(self.stack)


class Queue:
    """Create a Queue (FIFO) of product data"""

    def __init__(self):
        self.queue = deque()

    def add_new(self, i):
        """Add new item to the left of queue"""
        self.queue.appendleft(i)

    def peek(self):
        """See first added item without removing it"""
        print(self.queue[-1])

    def pop_first(self):
        """Remove first added item of queue"""
        return self.queue.pop()

    def size(self):
        """Get length of the queue"""
        return len(self.queue)


if __name__ == "__main__":
    from operations import Operations

    func = Operations()

    data = func.read_file()
    st = Stack()
    for i in data:
        st.add_top(i)
    print(st.stack)
    for x in range(st.size()):
        top = st.pop_top()
        print(top)
