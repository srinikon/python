
 # Find Merge Point of Two Lists

 # Find the node at which both lists merge and return the data of that node.
 # head could be None as well for empty list
 # Node is defined as
 
 # class Node(object):
 
 #   def __init__(self, data=None, next_node=None):
 #       self.data = data
 #       self.next = next_node

def FindMergeNode(headA, headB):
    while(headA):
        if(headA.data == headB.data):
            return(headB.data)
        
        headB_copy = headB
        while(headB_copy):
            if(headA.data == headB_copy.data):
                return(headB_copy.data);
            headB_copy = headB_copy.next        
        headA = headA.next


 # Delete duplicate-value nodes from a sorted linked list
 # head could be None as well for empty list
 # Node is defined as
 
 # class Node(object):
 
 #   def __init__(self, data=None, next_node=None):
 #       self.data = data
 #       self.next = next_node

 # return back the head of the linked list in the below method.


def RemoveDuplicates(head):
    h = Node(head.data)
    n = h
    while(head and head.next):
        if (head.data == head.next.data):
            head = head.next
            continue
        else:
            head = head.next
            n.next = Node(head.data)
            n = n.next
    return(h)


# Dashboard > Python > Basic Data Types > Lists
if __name__ == '__main__':
    N = int(input())
    cmd = []
    list = []
    for i in range (0, N):
        cmd.append(str(input()))
        
    for i in range(0, N):
        temp = cmd[i].split(" ")
        if(temp[0] == 'insert'):
            list.insert(int(temp[1]), int(temp[2]))
        elif(temp[0] == 'print'):
            print(list)
        elif(temp[0] == 'remove'):
            list.remove(int(temp[1]))
        elif(temp[0] == 'append'):
            list.append(int(temp[1]))
        elif(temp[0] == 'sort'):
            list.sort()
        elif(temp[0] == 'pop'):
            list.pop()
        elif(temp[0] == 'reverse'):
            list.reverse()

            
## Dashboard > Python > Basic Data Types > List Comprehensions
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    lx = []
    ly = []
    lz = []
    
    for i in range(0, x+1):
        lx.append(i)
    for i in range(0, y+1):
        ly.append(i)
    for i in range(0, z+1):
        lz.append(i)

    
    ltemp = []
    for x1 in lx:
        for y1 in ly:
            for z1 in lz:
                if (x1 + y1 + z1 != n):
                    ltemp.append([x1, y1, z1])
    
    print(ltemp)


# Dashboard > Python > Basic Data Types > Find the Second Largest Number
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    h2 = h1 = None
    for i in range(0, n):
        if(h1 == None):
            h1 = arr[i]
        elif(arr[i] > h1):
            h2 = h1
            h1 = arr[i]
        elif(arr[i] == h1):
            continue
        elif(h2 == None):
            h2 = arr[i]
        elif(arr[i] > h2):
            h2 = arr[i]
    print(h2)