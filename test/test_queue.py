from klivi.queue import Queue

import unittest


class MyTestCase(unittest.TestCase):
    def test_enqueue(self):
        queue = Queue()
        queue.enqueue(1)

        self.assertEqual(queue.queue, [1])
        self.assertTrue(queue.enqueue(1))

    def test_dequeue(self):
        queue = Queue()
        queue.enqueue(1)
        self.assertEqual(queue.dequeue(), 1)


if __name__ == '__main__':
    unittest.main()
