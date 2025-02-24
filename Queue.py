from collections import deque

class QueuesPractise:

    def queueOps(self):
        queue = deque(["Paul","Jason","Reddy"])
        queue.append("Bandi")
        queue.popleft()
        print(queue)
        pass

QueuesPractise().queueOps()

class CustomDS:

    member1 : str
    member2 : int

    def __init__(self, m1, m2):
        self.member1 = m1
        self.member2 = m2

custDSObj = CustomDS(1,2)
print(custDSObj.member1)
