
# The size of the queue = it is not allowed to grow!
N = 10

# The actual queue - only indexing (i.e. queue[<index>]) is alowed - no append()
queue = [None] * N

# Feel free to add more variables that you might need!
head = 0
tail = 0

vector = (1, 2)

# TASK: Fill the four fucntions below with the correct implementation


def enqueue(element) -> bool:
    """Adding the given element in the `queue`.

    Args:
        element (any): the element to be enqueue

    Returns:
        bool: If there were enough space and the element added
    """
    global head, tail
    if is_full():
        return False

    queue[tail] = element
    tail += 1
    if tail >= N:
        tail = 0
    return True


def dequeue() -> any | None:
    """Removing an element from the `queue`.

    Returns:
        any: The dequeued element.
    """
    global head, tail
    if is_empty():
        return None
    a = queue[head]
    head += 1
    return a


def is_empty() -> bool:
    """Checks if the queue is empty

    Returns:
        bool: `True` if there are no elements in the queue
    """
    global head, tail
    return tail == head


def is_full() -> bool:
    """Checks if the `queue` is full, or it has space for more elements.

    Returns:
        bool: `True` if there is NO more space for elements
    """
    global head, tail
    if head == 0:
        return tail == N - 1
    else:
        return tail == head - 1


assert (is_empty())
assert (not is_full())
assert (dequeue() == None)
assert (enqueue(5))
assert (not is_empty())
assert (enqueue(6))
assert (dequeue() == 5)
