class BinarySearchTree():
    def __init__(self):
        self.top=None
        self.size=0
    def addElement(self, element):
        if(self.top==None):
            self.top=element
            self.size=1
            return True
        current=self.top
        while(True):
            if(element<current.getData()):
                next=current.getLeft()
                if(next==None):
                    current.setLeft(element)
                    self.size+=1
                    return True
                else:
                    current=next
            elif(element<current.getData()):
                next=current.getRight()
                if(next==None):
                    current.setRight(element)
                    self.size+=1
                    return True
                else:
                    current=next
            else:
                return False
    def removeElement(self, element):
        current=self.top
        parent=None
        while(True):
            if(current==None):
                return False
            elif(current.getData()==element):
                #remove and restructure
                return True
            elif(current.getData()<element):
                parent=current
                current=current.getLeft()
            elif(current.getData()>element):
                parent=current
                current=current.getRight()
    """
              4
           2     6
         1   3|5   7

         todo:
         finish remove
         str
         test
    """
    def contains(self, element):
        while(True):
            current=self.top
            if(current.getData()==element):
                return True
            elif(current==None):
                return False
            elif(current.getData()<element):
                current=current.getLeft()
            elif(current.getData()>element):
                current=current.getRight()
    def size(self):
        return self.size
    def __str__(self):
        return "Starts at"+str(self.top)
class Node():
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None
    def getData(self):
        return self.data
    def setData(self, data):
        self.data=data
        return None
    def getLeft(self):
        return self.left
    def setLeft(self, data):
        self.left=data
        return None
    def getRight(self):
        return self.right
    def setRight(self, data):
        self.right=data
        return None