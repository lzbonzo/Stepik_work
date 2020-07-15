class ExtendedStack(list):
    def sum(self):
        # операция сложения
        self.append(self.pop() + self.pop())

    def sub(self):
        # операция вычитания
        self.append(self.pop() - self.pop())

    def mul(self):
        # операция умножения
        self.append(self.pop() * self.pop())

    def div(self):
        # операция целочисленного деления
        self.append(self.pop() // self.pop())

self = [1, 2, 3, 4, 5, 6, 7, 8, 11, 9, 30]
self.append(self.pop() + self.pop())
print(self)
self.append(self.pop() - self.pop())
print(self)
self.append(self.pop() - self.pop())
print(self)

self.append(self.pop() - self.pop())
print(self)