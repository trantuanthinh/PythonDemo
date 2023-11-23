from collections import defaultdict
from queue import PriorityQueue


class Node:
    def __init__(self, name, parent=None, length=0):
        self.name = name
        self.parent = parent
        self.length = length

    def display(self):
        print(self.name + self.length)

    def __lt__(self, other):
        if other == None:
            return False
        return self.length < other.length

    def __equal__(self, other):
        if other == None:
            return False
        return self.length == other.length


def checkEqual(O, G):
    if O.name == G.name:
        return True
    return False


def checkInPriority(temp, queue):
    if temp == None:
        return False
    return temp in queue.queue


def getPath(O):
    print(O.name)
    if O.parent != None:
        getPath(O.parent)
    else:
        return


data = defaultdict(list)
data["A"] = ["B", 2, "C", 1, "D", 3]
data["B"] = ["E", 5, "F", 4]
data["C"] = ["G", 6, "H", 3]
data["D"] = ["I", 2, "J", 4]
data["F"] = ["K", 2, "L", 1, "M", 4]
data["H"] = ["N", 2, "O", 4]


def Uniform_Cost_Search(S=Node("A"), G=None):
    open = PriorityQueue()
    close = PriorityQueue()
    open.put(S)
    while True:
        if open.empty():
            print("cant find")
            return
        O = open.get()
        close.put(O)
        print("check:", O.name, O.length)
        if checkEqual(O, G):
            print("can find")
            getPath(O)
            print("distance", O.length)
            return
        i = 0
        while i < len(data[O.name]):
            name = data[O.name][i]
            length = O.length + data[O.name][i + 1]
            temp = Node(name=name, length=length)
            temp.parent = O
            check1 = checkInPriority(temp, open)
            check2 = checkInPriority(temp, close)
            if not check1 and not check2:
                open.put(temp)
            i += 2


Uniform_Cost_Search(G=Node(input()))
