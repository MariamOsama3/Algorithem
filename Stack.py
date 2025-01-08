class Node:
    def __init__(self,data):
        self.data=data
        self.Next=None

class Stack:
    def __init__(self,size):
        self.arr=[]
        self.tos=0
        self.size=size

    def push(self,data):
        pushed=False
        if(self.tos < self.size):
            self.arr.append(data)
            self.tos+=1
            pushed=True
        return pushed
    
    def pop(self):
        poped =False
        if(self.tos>0):
            self.tos-=1
            poped=self.arr[self.tos]
        else:
            print("empty stack can't pop from it")
        return poped

Stack1 = Stack(4)
Stack1.push(2)
Stack1.push(6)
Stack1.push(8)
Stack1.push(10)

poped = Stack1.pop()
print(poped ,"\n")

poped = Stack1.pop()
print(poped ,"\n")