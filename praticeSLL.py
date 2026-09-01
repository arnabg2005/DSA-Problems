# create the node class
class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next

#  create the sll class 
class SLL:
    def __init__(self,start=None):
        self.start=start

# check whether the list is empty or not
    def is_empty(self):
        return self.start==None

# insert the elemets at first
    def insert_at_first(self,data):
        n=Node(data,self.start)
        self.start=n

#insert the elemets at last
    def insert_at_last(self,data):
        n=Node(data)
        if not self.is_empty():
            temp=self.start
            while temp.next is not None:
                temp=temp.next
            temp.next=n
        else:
            self.start=n
# search the element
    def search(self,data):
        temp=self.start
        while temp is not None:
            if temp.item==data:
                return temp
            temp=temp.next
        return None

#insert at specfic postion
    def insert_at(self,temp,data):
        if temp is not None:
            n=Node(data,temp.next)
            temp.next=n

# print the list
    def print_List(self):
        temp=self.start
        while temp is not None:
            print(temp.item,end=" ")
            temp=temp.next
        print()

# delete from the first
    def delete_at_first(self):
        if self.start is not None:
            self.start=self.start.next

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

# delete a specfic elemet
    def delete_at(self,data):
        if self.start is None:
            pass
        elif self.start.next is None:
            if self.start.item==data:
                self.start=None
        else:
            temp=self.start
            if temp.item==data:
                self.start=temp.next
            else:
                while temp.next is not None:
                    if temp.next.item==data:
                        temp.next=temp.next.next
                        break
                    temp=temp.next
    def __iter__(self):
        return SLLIterable(self.start)

class SLLIterable:
    def __init__(self,start):
        self.current=start
    def __iter__(self):
        return self
    def __next__(self):
        if not self.current:
            raise StopIteration
        data=self.current.item
        self.current=self.current.next
        return data
    

## driver class
mylist=SLL()
mylist.insert_at_first(20)
mylist.insert_at_first(10)
mylist.insert_at_last(30)
mylist.insert_at(mylist.search(20),25)
mylist.print_List()
mylist.delete_at_first()
mylist.print_List()
mylist.delete_at_last()
mylist.insert_at_last(45)
mylist.insert_at_last(50)
mylist.print_List()
mylist.delete_at(45)
for x in mylist:
    print(x,end=' ')

    