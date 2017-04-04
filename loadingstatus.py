import time
import sys

class Loadingstatus:
    def __init__(self, barlength = 20):
        self.loading = 0
        self.lastCall = self.getMilliSeconds()
        self.barlength = barlength

    def getMilliSeconds(self):
        return int(time.time() * 1000)

    def updateInfiniteLoading(self):
        newCall = self.getMilliSeconds()
        if newCall-self.lastCall > 500:
            #switch loading
            loadingSymbol = {0: "/", 1: "-", 2: "\\", 3: "|"}[self.loading]
            self.loading = (self.loading + 1)%4
            sys.stdout.write(loadingSymbol+"\r")
            sys.stdout.flush()
            self.lastCall = newCall

    def updateLoading(self,percent):
        sys.stdout.write(self.getBar(percent)+"\r")
        sys.stdout.flush()

    def endLoading(self,percent = 1):
        print(self.getBar(percent))

    def getBar(self,percent):
        progressLength = int((self.barlength-2)*percent)
        progress = "=" * progressLength
        bar = "-" * (self.barlength-progressLength-2)
        percentString = "%.2f" % (percent*100)
        return "["+progress+bar+"] "+percentString+"%"
