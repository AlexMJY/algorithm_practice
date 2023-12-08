class LinkedList:
    def __init__(self):
        self.head = None
        
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next
            
    def __repr__(self):
        nodes = []
        for node in self:
            nodes.append(node.val)
        return " -> ".join(nodes)
    
    def add_to_tail(self, node):
        if self.head == None:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.set_next(node)
        
    def remove_form_head(self):
        if self.head == None:
            return None
        temp = self.head
        self.head = self.head.next
        return temp
    
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
    def set_next(self, node):
        self.next = node
    def __repr__(self):
        return self.val 
    
    
linked_list = LinkedList()
linked_list.add_to_tail(Node('john'))
linked_list.add_to_tail(Node('sally'))
linked_list.add_to_tail(Node('jimmy'))
print("ll : ", linked_list)
first = linked_list.remove_form_head()
print("removed : ", first)
print("ll : ", linked_list)