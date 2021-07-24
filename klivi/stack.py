from typing import List, Any, Iterable


class Stack:
    """Python stack implementation."""
    
    def __init__(self):
        """Initialize a empty stack."""
        self.__stack: List[Any] = []
        
    def __iter__(self) -> Iterable[Any]:
        """Return a iterable over the stack."""
        return iter(self.__stack)

    def __len__(self) -> int:
        """Return the number of items in the stack."""
        return len(self.__stack)

    @property
    def is_empty(self) -> bool:
        """Return whether the stack is empty."""
        return not self.__stack

    def push(self, item: Any) -> bool:
        """Add an item to the stack."""
        self.__stack.append(item)
        return True

    def pop(self) -> Any:
        """Remove an item from the stack."""
        return False if self.is_empty else self.__stack.pop()


def split_word(word: str) -> List[str]:
    """Return a list of every character from a word."""
    return list(word)
