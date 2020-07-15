import time

class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))

class LoggableList(list, Loggable):
   # def __init__(self):
     #   self = []
     #   pass

    def append(self, elem):
        self.extend([elem])
        Loggable.log(self,elem)

a = LoggableList([1, 2, 3])
b = LoggableList([])
a.append('msg 1')
a.append('msg 2')
b.append('msg 3')
b.append('msg 4')
print(a)
print(b)
#x.append([1])
#x.log('3')