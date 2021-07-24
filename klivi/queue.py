from typing import List, Any, Optional, Tuple, Iterable


class Queue:
    """Python Queue Implementation."""
    
    def __init__(self):
        """Initialize an empty queue."""
        self.__queue: List[Any] = []
        
    def __len__(self) -> int:
        """Return the number of items in the queue."""
        return len(self.__queue)
    
    def __iter__(self) -> Iterable[Any]:
        """Return a iterable over the queue."""
        return iter(self.__queue)

    def __repr__(self) -> str:
        """Print the queue contents."""
        return f"<Queue() => {self.__queue}>"

    @property
    def items(self) -> Tuple[Any]:
        """Return a read-only list of queue items."""
        return tuple(self.__queue)

    def enqueue(self, item) -> bool:
        """Add an item to the queue."""
        self.__queue.append(item)
        return True

    def dequeue(self) -> Optional[Any]:
        """Remove an items from the queue if possible."""
        if self.__queue:
            return self.__queue.pop(0)


def main() -> None:
    queue = Queue()
    queue.enqueue(1)
    print(queue)


if __name__ == '__main__':
    main()
