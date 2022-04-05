class Queue():
    def __init__(self, input_list: list):
        self.queue = input_list

    def append(self, __object) -> None:
        return self.queue.append(__object)

    def deque(self):
        assert len(self.queue)!=0, "cannot dequeue an empty queue."
        output, self.queue = self.queue[0], self.queue[1:]
        return output
    
    def __str__(self):
        return f"{self.queue}"


if __name__ == "__main__":
    # Stack operation can be done by List.
    stack = [1,2,3,4,5]
    # stack: push -> list.append()
    stack.append(6)
    
    #stack: pop -> list.pop()
    print(f"Stack.pop: {stack.pop()}")  # -> return the element being poped.
  
    print(f"Print stack: {stack}") #-> return [2]

    # Queue with homemade Queue class.
    queue = Queue([])
    # queue.queue() -> list.append()
    queue.append(1)
    queue.append(2)
    
    # dequeue
    print(f"Queue.deque: {queue.deque()}")
    
    # queue.__str__()
    print(f"Print queue: {queue}") #-> return [2]

    