"""
Stack to queue converter.
"""
from copy import deepcopy

from arrayqueue import ArrayQueue  # or from linkedqueue import LinkedQueue
from arraystack import ArrayStack  # or from linkedstack import LinkedStack


def stack_to_queue(stack_in: ArrayStack) -> ArrayQueue:
    """
    Convert a stack to a queue.
    """
    stack_copy = deepcopy(stack_in)
    queue_direct = ArrayQueue()
    while not stack_copy.isEmpty():
        queue_direct.add(stack_copy.pop())

    queue_reversed = ArrayQueue()
    while not queue_direct.isEmpty():
        queue_reversed.add(queue_direct.pop())
    return queue_reversed


if __name__ == '__main__':
    stack = ArrayStack()
    for i in range(10):
        stack.add(i)
    queue = stack_to_queue(stack)
    print(queue)
    # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    print(stack)
    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(stack.pop())
    # 9
    print(queue.pop())
    # 9
    stack.add(11)
    queue.add(11)
    print(queue)
    # [8, 7, 6, 5, 4, 3, 2, 1, 0, 11]
    print(stack)
    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 11]
