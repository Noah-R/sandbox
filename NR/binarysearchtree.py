from random import randint


class BinarySearchTree():
    def __init__(self):
        self.top = None
        self.size = 0

    def addElements(self, elements):
        for i in elements:
            self.addElement(i)
        return None

    def addElement(self, element):
        if(self.top == None):
            self.top = Node(element)
            self.size = 1
            return True
        current = self.top
        while(True):
            if(element < current.getData()):
                next = current.getLeft()
                if(next == None):
                    current.setLeft(Node(element))
                    self.size += 1
                    return True
                else:
                    current = next
            elif(element > current.getData()):
                next = current.getRight()
                if(next == None):
                    current.setRight(Node(element))
                    self.size += 1
                    return True
                else:
                    current = next
            else:
                return False

    def removeElement(self, element, remove=True):
        current = self.top
        parent = None
        while(True):
            if(current == None):
                return False
            elif(current.getData() == element):
                if(current.getLeft() != None):
                    parent = current
                    current = current.getLeft()
                    while(current.getRight() != None):
                        current = current.getRight()
                    current = current.getData()
                    self.removeElement(current, False)
                    parent.setData(current)
                    if(remove):
                        self.size -= 1
                    return True
                elif(current.getRight() != None):
                    parent = current
                    current = current.getRight()
                    while(current.getLeft() != None):
                        current = current.getLeft()
                    current = current.getData()
                    self.removeElement(current, False)
                    parent.setData(current)
                    if(remove):
                        self.size -= 1
                    return True
                elif(parent.getData() > element):
                    parent.setLeft(None)
                    if(remove):
                        self.size -= 1
                    return True
                elif(parent.getData() < element):
                    parent.setRight(None)
                    if(remove):
                        self.size -= 1
                    return True
                else:
                    print("Something is seriously wrong - removeElement")
            elif(current.getData() < element):
                parent = current
                current = current.getRight()
            elif(current.getData() > element):
                parent = current
                current = current.getLeft()

    def contains(self, element):
        while(True):
            current = self.top
            if(current.getData() == element):
                return True
            elif(current == None):
                return False
            elif(current.getData() < element):
                current = current.getLeft()
            elif(current.getData() > element):
                current = current.getRight()

    def getSize(self):
        return self.size

    def __str__(self):
        if(self.size == 0):
            return "Empty"
        text = ""
        layer = [self.top]
        nextlayer = []
        while(len(layer) > 0):
            for item in layer:
                text += str(item)+" with "+str(item.getLeft()) + \
                    " to left and "+str(item.getRight())+" to right\n"
                if(item.getLeft() != None):
                    nextlayer.append(item.getLeft())
                if(item.getRight() != None):
                    nextlayer.append(item.getRight())
            layer = nextlayer
            nextlayer = []
        return str(text)


class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def getData(self):
        return self.data

    def setData(self, data):
        self.data = data
        return None

    def getLeft(self):
        return self.left

    def setLeft(self, data):
        self.left = data
        return None

    def getRight(self):
        return self.right

    def setRight(self, data):
        self.right = data
        return None

    def __str__(self):
        return str(self.data)


tree = BinarySearchTree()
tree.addElements([41, 53, 37, 38, 24, 68, 19, 44, 42, 64, 50, 47, 52, 51])
print("Tree of size " + str(tree.getSize()))
print(tree)
tree.removeElement(53)
print("Tree of size " + str(tree.getSize()))
print(tree)
tree.removeElement(19)
print("Tree of size " + str(tree.getSize()))
print(tree)


# can do: balancing function
