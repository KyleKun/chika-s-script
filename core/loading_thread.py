from time import sleep
from threading import Thread
from utils.utils import LoaderCondition


class Loading(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.loaded = False
        self.bar = [
            ' [Loading   ]',
            ' [Loading.  ]',
            ' [Loading.. ]',
            ' [Loading...]',
        ]
        self.i = 0

    def run(self):
        while not self.loaded:
            self.loaded = LoaderCondition.loaded
            print(self.bar[self.i % len(self.bar)], end='\r')
            sleep(.2)
            self.i += 1
        print('', end='\r')
        return
