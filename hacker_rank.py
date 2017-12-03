"""
 Find Merge Point of Two Lists

 Find the node at which both lists merge and return the data of that node.
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node
"""

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