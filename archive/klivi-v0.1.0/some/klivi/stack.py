class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)
        return True

    def pop(self):
        if self.is_empty():
            return False

        return self.stack.pop()


def split_word(word):
    return [char for char in word]
