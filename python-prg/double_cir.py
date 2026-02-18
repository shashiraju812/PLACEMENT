class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None


class DCLL:
    def __init__(self):
        self.head=None

    def add_begin(self,data):
        new_node=Node(data)
        if(self.head is None):
            self.head=new_node
            new_node.next=new_node
            new_node.prev=new_node
        else:
            last=self.head.prev

            new_node.next=self.head
            new_node.prev=last

                                                last.next=new_node
            self.head.prev=new_node

            self.head=new_node

    def add_end(self,data):
        new_node=Node(data)
        if(self.head is None):
            self.head=new_node
            new_node.next=new_node
            new_node.prev=new_node
        else:
            last=self.head.prev

            last.next=new_node
            new_node.prev=last

            new_node.next=self.head
            self.head.prev=new_node

    def del_begin(self):
        if(self.head is None):
            print("list is empty")
        elif(self.head.next==self.head):
            self.head=None
        else:
            last=self.head.prev
            self.head=self.head.next
            self.head.prev=last
            last.next=self.head

    def del_end(self):
        if(self.head is None):
            print("list is empty")
        elif(self.head.next==self.head):
            self.head=None
        else:
            last=self.head.prev
            second_last=last.prev

            second_last.next=self.head
            self.head.prev=second_last

    def printing(self):
        if(self.head is None):
            print("list is empty")
        else:
            n=self.head
            while True:
                print(n.data,end=" ")
                n=n.next
                if(n==self.head):
                    break
            print()

    def search(self,key):
        if(self.head is None):
            print("Linklist is empty")
        else:
            n=self.head
            flag=0
            while True:
                if(n.data==key):
                    flag=1
                    print("i found my element")
                    break
                n=n.next
                if(n==self.head):
                    break
            if(flag==0):
                print("element not found")

    def add_middle(self,data,pos):
        if(self.head is None):
            print("list is empty")
            return

        new_node=Node(data)
        n=self.head
        flag=0

        while True:
            if(n.data==pos):
                flag=1
                new_node.next=n.next
                new_node.prev=n

                n.next.prev=new_node
                n.next=new_node
                break

            n=n.next
            if(n==self.head):
                break

        if(flag==0):
            print("position not found")

    def del_middle(self,pos):
        if(self.head is None):
            print("list is empty")
        elif(self.head.data==pos):
            self.del_begin()
        else:
            n=self.head
            flag=0

            while True:
                if(n.data==pos):
                    flag=1
                    n.prev.next=n.next
                    n.next.prev=n.prev
                    break
                n=n.next
                if(n==self.head):
                    break

            if(flag==0):
                print("position is not found,i can't delete")

