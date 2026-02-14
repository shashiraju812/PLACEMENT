class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None
class cll:
    def __init__(self):
        self.head=None
    #add_begin
    def add_begin(self,data):
        new_node=Node(data)
        if(self.head is None):
            self.head=new_node
            self.head.ref=self.head
        else:
            n=self.head
            while(n is not self.head):
                n=n.ref
            n.ref=new_node
            new_node=self.head
    #add_end
    def add_end(self,data):
        new_node=Node(data)
        if(self.head is None):
            self.head=new_node
            self.head.ref=self.head
        else:
            n=self.head
            while(n.ref is not self.head):
                n=n.ref
            n.ref=new_node
            new_node.ref=self.head
    #del_begin
    def del_begin(self):
        if(self.head is None):
            print("linkedlist is empty")
        elif(self.head.ref==self.head):
            self.head=None
        else:
            self.head=self.head.ref
            n=self.head
            while(n.ref is not self.head):
                n=n.ref
    #del_end

    def del_end(self):
        if(self.head is None):
            print("linked list is empty")
        elif(self.head.ref==self.head):
            self.head=None
        else:
            n=self.head
            while(n.ref.ref is not self.head):
                n=n.ref
            n.ref=self.head
    #printing
    def printing(self):
        if(self.head is None):
            print("the linked list is empty")
        else:
            n=self.head
            while(n.ref is not self.head):
                print(n.data,end=" ")
                n=n.ref
            print(n.data)
            print()
    # add_middle
    def add_middle(self, data, pos):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.head.ref = self.head   
        else:
            n = self.head
            while True:
                if n.data == pos:   
                    new_node.ref = n.ref
                    n.ref = new_node
                    return
                n = n.ref
                if n == self.head:  
                    break
                print("Position not found")
    #search
    def search(self,key):
        if(self.head is None):
            print("linked list is empty")
        else:
            n=self.head
            flag=0
            while(n.ref!=self.head):
                if(n.data==key):
                    flag=1
                    print("i founded the element")
                    break
                n=n.ref
            else:
                if(n.data==key):
                    flag=1
                    print("i found my elemenet")
            
            if(flag==0):
                print("the element is not found")
    #delete_middle
    def del_middle(self,pos):
        if(self.head is None):
            print(" the linked list is empty")
        elif(self.head.data== pos):
            self.del_begin()
        
        else:
            n=self.head
            while(n.ref is not self.head):
                if(n.ref.data==pos):
                    n.ref=n.ref.ref
                n=n.ref
a=cll()
a.add_begin(10)
a.add_begin(20)
a.add_begin(30)
a.add_begin(40)
a.printing()
        
    
                
            
