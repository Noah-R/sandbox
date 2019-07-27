class Node():
    def __init__(self, data):
        self.data=data
    def getData(self):
        return self.data
    def setData(self, data):
        self.data=data
        return None
print(hash(Node("aeroidarnseochiaerocdiaoerciaoei")))
print(hash("woodly"))