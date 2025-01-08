
class Node:
    def __init__(self,number,name,position):
        self.number=number
        self.name=name
        self.position=position
        self.Next=None
        self.prev=None

class linked_list:
    def __init__(self):
        self.head=None
        self.tail=None

    def insert(self,number,name,position,location):
        node=Node(number,name,position)
        if self.head==None: #if list is empty list
            self.head=node #poth head and tail should arrow to the first node
            self.tail=node
        else:
            if location==0: # if insert in the begining of the list
                node.Next=self.head 
                self.head.prev=node
                self.head=node  
            else:
                curr=self.head
                i=0
                while(i<location-1 and curr !=None): #to reach to the location
                    curr=curr.Next
                    i+=1
                if curr == self.tail or curr ==None: #insert to the and or index that is bigger than the list so it will cose to insert at the end
                    node.prev=self.tail
                    self.tail.Next=node
                    self.tail=node
                else:
                    curr.Next.prev=node
                    node.Next=curr.Next
                    curr.Next=node
                    node.prev=curr

    '''***********************************************************************************'''
    '''isert using id'''
    def update(self,number,name,position):
        flag=False
        if self.head !=None:
            curr=self.head
            while(curr is not None):
                if curr.number==number:
                    curr.name=name
                    curr.position=position
                    flag = True
                    return curr
                curr=curr.Next

    '''*************************************************************************************'''
    '''insert data'''
    def add(self, number, name, position):
        node = Node(number, name, position)
        if self.head is None:  # no data in the list yet
            self.head = node
            self.tail = node 
        else:  # add at the end of the list
            node.prev = self.tail
            self.tail.Next = node
            self.tail = node

    '''**************************************************************************************'''
    '''delete using id'''
    def delete_id(self,location):
        deleted=False
        if self.head is not None:
            if(location==0):
                if(self.head==self.tail):
                    self.head=None
                    self.tail=None
                    deleted=True
                else:
                    self.head=self.head.Next
                    self.head.prev=None
                    deleted=True
            else:
                curr=self.head
                i=0
                while(curr is not None and i < location):
                    curr=curr.Next
                    i+=1
                if curr==self.tail:
                    self.tail=self.tail.prev
                    self.tail.Next = None
                    deleted=True
                else:
                    curr.Next.prev=curr.prev
                    curr.prev.Next=curr.Next
                    deleted=True


    '''*******************************************************************************************'''
    def delete_number(self,number):
        deleted=False
        curr=self.head
        i=0
        if(self.head==None and self.tail==None): # empty 
            deleted = False
            print("empyt list")
        elif(self.head==self.tail): #have only one elemnet
            self.head=None
            self.tail=None
            deleted=True
        else :
            while(curr is not None and curr.number != number):
                curr=curr.Next
                i+=1
            if curr is None:  # the number is not found
                print(f"Node with number {number} not found.")
                return False
            elif curr==self.head: #delete first element
                self.head=self.head.Next
                self.head.prev=None
                deleted=True
            else:
                if curr==self.tail: #delete the last element
                    self.tail=self.tail.prev
                    self.tail.Next = None
                    deleted=True
                else:
                    curr.Next.prev=curr.prev #delete from medel
                    curr.prev.Next=curr.Next
                    deleted=True
    '''********************************************************************************************'''
    def delete_all(self):
        self.head=None
        self.tail=None

    def display_all(self):
        if(self.head==None):
            print("empty")
        curr = self.head
        while(curr is not None):
            print("\nThe name is " ,curr.name)
            print("\nThe number is ",curr.number)
            print("\nThe position is ",curr.position)
            print("\n**************************************")
            curr=curr.Next

list1 = linked_list()
list1.add( 1,"mariam","devoloper")
list1.add( 3,"mariam2","devoloper2")
list1.add( 5,"mariam3","devoloper3")
list1.add( 6,"mariam","devoloper")
list1.insert(1,"radwa","doctor",3)
list1.update(3,"radwa osama","doctor")
list1.display_all()
list1.delete_all()
list1.display_all()



