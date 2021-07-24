from klivi.stack import Stack


def test_is_empty():
    stack = Stack()
    assert stack.is_empty() == True


def test_add():
    stack = Stack()
    stack.push(1)
    assert stack.stack == [1]
    assert stack.push(1) == True


def test_pop():
    stack = Stack()
    stack.push(1)
    assert stack.pop() == 1
