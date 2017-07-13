from .node import Node


class Sequenceable(object):
    def __init__(self):
        self.start = None


    def get_elements(self):
        """returns a list of all the values"""
        items = []
        current = self.start
        while current is not None:
            items.append(current.value)
            current = current.next
        return(items)
            


class Appendable(object):
    def append(self, element):
        """adds an Node with the element value to the end of the list"""
        nodeElement = Node(element)
        current = self.start
        if (current == None):
            self.start = nodeElement
        else:
            while current.next is not None:
                current = current.next
            current.next = nodeElement


class Popable(object):
    """removes the first node of the list and returns its value"""
    def pop(self):
        if (self.start == None):
            raise IndexError
        else:
            temp = self.start
            self.start = self.start.next
            return(temp.value)


class Pushable:
    """adds a node with the element value to the start of the list"""
    def push(self, element):
        nodeElem = Node(element)
        nodeElem.next = self.start
        self.start = nodeElem
        
