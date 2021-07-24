class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)
        return True

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    def get_queue(self):
        return self.queue

    def size(self):
        return len(self.queue)


queue = Queue()
queue.enqueue(1)
print(queue.queue)
