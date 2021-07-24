from klivi.stack import Stack

import unittest


class MyTestCase(unittest.TestCase):

    def test_is_empty(self):
        stack = Stack()
        self.assertTrue(stack.is_empty())

    def test_add(self):
        stack = Stack()
        stack.push(1)
        
        self.assertEqual(stack.stack, [1])
        self.assertTrue(stack.push(1))

    def test_pop(self):
        stack = Stack()
        stack.push(1)
        self.assertEqual(stack.pop(), 1)


if __name__ == '__main__':
    unittest.main()
