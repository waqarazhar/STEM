import signal

class inputKey():
    
    """docstring for sensorSR04"""
    def __init__(self, timeLimit):
        super(inputKey, self).__init__()
        self.s = signal.signal(signal.SIGALRM, self.handler)
        self.timeLimit = timeLimit

    def handler(self):
        pass

    def get(self):

        signal.alarm(self.timeLimit)

        try:
            key = input().lower()
            signal.alarm(0)
            return key
        
        except Exception:
            return