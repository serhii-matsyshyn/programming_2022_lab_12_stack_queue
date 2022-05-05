"""
Queue to stack converter.
"""
from copy import deepcopy

from arrayqueue import ArrayQueue  # or from linkedqueue import LinkedQueue
from arraystack import ArrayStack  # or from linkedstack import LinkedStack


def queue_to_stack(queue_in: ArrayQueue) -> ArrayStack:
    """
    Convert a queue to a stack.
    """
    queue_copy = deepcopy(queue_in)
    stack_direct = ArrayStack()
    while not queue_copy.isEmpty():
        stack_direct.push(queue_copy.pop())

    stack_reversed = ArrayStack()
    while not stack_direct.isEmpty():
        stack_reversed.push(stack_direct.pop())
    return stack_reversed


if __name__ == '__main__':
    queue = ArrayQueue()
    queue2 = ArrayQueue()
    for i in range(10):
        queue.add(i)
        queue2.add(i)
    print(queue == queue2)
    # True
    stack = queue_to_stack(queue)
    print(queue)
    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(stack)
    # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    print(queue == queue2)
    # True
    print(stack.pop())
    # 0
    print(queue.pop())
    # 0
    stack.add(11)
    queue.add(11)
    print(queue)
    # [1, 2, 3, 4, 5, 6, 7, 8, 9, 11]
    print(stack)
    # [9, 8, 7, 6, 5, 4, 3, 2, 1, 11]
