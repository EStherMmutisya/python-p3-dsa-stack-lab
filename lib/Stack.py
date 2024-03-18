class Stack:
    def __init__(self, items=None, capacity=None):
        if items is None:
            self.items = []
        else:
            self.items = items
        self.capacity = capacity

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            return None

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return len(self.items) == 0

    def full(self):
        is_full = self.capacity is not None and len(self.items) >= self.capacity
        print(f"Is full? {is_full}")
        return is_full

    def search(self, target):
        try:
            index = len(self.items) - self.items[::-1].index(target) - 1
            distance = self.size() - index - 1
            print(f"Target {target} found at index {index}, distance from top: {distance}")
            return distance
        except ValueError:
            print(f"Target {target} not found in the stack")
            return -1

# Example usage
stk = Stack([1, 2, 3, 4, 5], 5)
stk.push(6)
stk.full()
stk.search(3)
