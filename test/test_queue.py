from klivi.queue import Queue


def test_enqueue():
    queue = Queue()
    queue.enqueue(1)
    assert queue.queue == [1]
    assert queue.enqueue(1) == True  # it return True


def test_dequeue():
    queue = Queue()
    queue.enqueue(1)
    assert queue.dequeue() == 1
