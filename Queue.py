class Node:
    def __init__(self,number,name,position):
        self.number=number
        self.name=name
        self.position=position
        self.Next=None
class Queue:
    def __init__(self):
        self.head=None
        self.tail=None
    def Enqueue(self,number,name,position):
        node=Node(number,name,position)
        if self.head==None:
            self.head=node
            self.tail=node
        else:
            self.tail.Next=node
            self.tail=node

    def dequeue(self):
        node=None
        if(self.head is not None):
            node=self.head
            self.head=self.head.Next
            if(self.head is None):
                self.tail=None
        return node

q1 = Queue()
q1.Enqueue(2,"mariam","student")
node = q1.dequeue()
print("\n",node.number)
print("\n",node.name)
print("\n",node.position)