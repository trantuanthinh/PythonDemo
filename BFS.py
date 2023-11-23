from collections import defaultdict


class Node:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent

    def display(self):
        print(self.name)


def checkEqual(O, G):
    return O.name == G.name


def checkExistInList(temp, list):
    for each in list:
        if checkEqual(each, temp):
            return True
    return False


def findPath(O):
    print(O.name)
    if O.parent != None:
        findPath(O.parent)
    return


data = defaultdict(list)
data["A"] = ["B", "C", "D "]
data["B"] = ["E", "F"]
data["C"] = ["G", "H"]
data["D"] = ["I", "J"]
data["F"] = ["K", "L", "M"]
data["H"] = ["N", "O"]


def BFS(S=Node("A"), G=None):
    open = []
    close = []
    open.append(S)
    while True:
        if len(open) == 0:
            print("cant find")
            return
        O = open.pop()
        close.append(O)
        print("check:", O.name)  # print nodes which was checked
        if checkEqual(O, G):
            print("can find")
            findPath(O)
            return
        for each in data[O.name]:
            temp = Node(each)
            temp.parent = O
            check1 = checkExistInList(temp, open)
            check2 = checkExistInList(temp, close)
            if not check1 and not check2:
                open.append(temp)


BFS(G=Node(input()))
