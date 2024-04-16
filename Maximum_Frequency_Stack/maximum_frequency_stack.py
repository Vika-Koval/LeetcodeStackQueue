from collections import deque
class FreqStack:
    def __init__(self):
        self.rtupe1 = deque()
        self.rtupe2 = deque()
    def push(self, val: int) -> None:
        self.rtupe1.appendleft(val)
        self.rtupe2.appendleft(self.rtupe1.count(val))
    def pop(self) -> int:
        melem = None
        mfrequency = 0
        for elem, frequency in zip(self.rtupe1, self.rtupe2):
            if frequency > mfrequency:
                melem= elem
                mfrequency = frequency

        self.rtupe1.remove(melem )
        self.rtupe2.remove(mfrequency)
        return melem 
