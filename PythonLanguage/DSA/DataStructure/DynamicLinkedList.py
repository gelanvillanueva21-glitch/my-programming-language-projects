
class LinkedList:
    def __init__(self):
        self.linked_List = []


    def add(self, value):
        self.linked_List.append(value)


    def remove(self, target):
        if len(self.linked_List) == 0:
            return None
        for i in self.linked_List:
            if i == target:
                self.linked_List.remove(target)


    def getCapacity(self):
        return len(self.linked_List)


    def isEmpty(self):
        return len(self.linked_List) == 0


    def printList(self):
        print(self.linked_List)


    def search(self, value):
        for index in range(len(self.linked_List) - 1):
            if value == self.linked_List[index]:
                return index
        return None

arr_list = LinkedList()

arr_list.add("gelan")
arr_list.add("chanzine")
arr_list.add("molly")
arr_list.add("cookie")

print(arr_list.getCapacity())
arr_list.remove("molly")
arr_list.printList()
print(arr_list.getCapacity())