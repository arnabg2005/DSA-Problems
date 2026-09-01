class Node:
    def __init__(self,prev=None,item=None,next=None):
        self.prev=prev
        self.item=item
        self.next=next
class DLL:
    def __init__(self,start=None):
        self.start=start
    def is_empty(self):
        return self.start==None
    #insert at first position
    def insert_at_start(self,data):
        n=Node(None,data,self.start)
        if self.start is not None:
            self.start.prev=n
        self.start=n
    #insert at last position
    def insert_at_last(self,data):
        if self.start is None:
            n=Node(None,data,None)
            self.start=n
        else:
            temp=self.start
            while temp.next is not None:
                temp=temp.next
            n=Node(temp,data,None)
            temp.next=n
    # search the elemets
    def search(self,data):
        temp=self.start
        while temp is not None:
            if temp.item==data:
                return temp
            temp=temp.next
        return None
    # insert at specfic position
    def insert_at(self,temp,data):
        if temp is not None:
            n=Node(temp,data,temp.next)
            temp.next=n
            n.next.prev=n

    # delete from the first
    def delete_at_first(self):
        if self.start is not None:
            self.start=self.start.next
            if self.start is not None:
                self.start.prev=None

    # delete from the last
    def delete_at_last(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start=None
        else:
            temp=self.start
            while temp.next.next is not None:
                temp=temp.next
            temp.next=None

    #delete at specfic position
    def delete_at(self,temp):
        if temp is not None:
            if temp.prev is not None:
                temp.prev.next=temp.next
            else:
                self.start=temp.next
            if temp.next is not None:
                temp.next.prev=temp.prev

    # print the list
    def print_list(self):
        temp=self.start
        while temp is not None:
            print(temp.item,end=" ")
            temp=temp.next
        print()
    def __iter__(self):
        return DLLIteratot(self.start)

class DLLIteratot:
    def __init__(self,start):
        self.current=start
    def __iter__(self):
        return self
    def __next__(self):
        if self.current is None:
            raise StopIteration
        data=self.current.item
        self.current=self.current.next
        return data
    
#drive code
mylist=DLL()
mylist.insert_at_start(10)
mylist.insert_at_start(20)
mylist.insert_at_last(30)
mylist.insert_at(mylist.search(20),25)
for i in mylist:
    print(i,end=" ")
print()
mylist.delete_at(mylist.search(25))
for i in mylist:
    print(i,end=" ")
print()