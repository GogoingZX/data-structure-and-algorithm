# use list
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)
    
    def peek(self):
        assert not self.is_empty()
        return self.items[-1]
    
    def pop(self):
        assert not self.is_empty()
        return self.items.pop()
    
    def push(self, item):
        self.items.append(item)

#---------------------------------------------------------------------------------------------------
# use linked list
# 如果设计大量push操作, list空间不够时复杂度会退化到O(n), linked list可以保证最坏情况下仍是O(1)
class StackNode:
    def __init__(self,
        item,
        link
    ):
        self.item = item
        self.next = link

class StackV2:
    def __init__(self):
        self.top = None
        self.length = 0
    
    def is_empty(self):
        return self.top is None
    
    def size(self):
        return self.length
    
    def peek(self):
        assert not self.is_empty()
        return self.top.item
    
    def pop(self):
        assert not self.is_empty()
        node = self.top
        self.top = self.top.next
        self.length -= 1
        return node.item
    
    def push(self, item):
        self.top = StackNode(item, self.top)
        self.length += 1


#---------------------------------------------------------------------------------------------------
# I:
s1 = Stack()
s1.push("a")
s1.push("b")
s1.push("c")

print(f"""
{'-'*80}
TEST I
* Size: {s1.size()}
* Top Item: {s1.peek()}
* Popped Item: {s1.pop()}
=> ...
* Is Empty Now? {s1.is_empty()}
* Size: {s1.size()}
* Top Item: {s1.peek()}
{'-'*80}
""")

# II:
s2 = StackV2()
s2.push("A")
s2.push("B")
s2.push("C")
s2.push("D")
s2.push("E")

print(f"""
{'-'*80}
TEST II
* Size: {s2.size()}
* Top Item: {s2.peek()}
* Popped Item: {s2.pop()}
=> ...
* Is Empty Now? {s2.is_empty()}
* Size: {s2.size()}
* Top Item: {s2.peek()}
{'-'*80}
""")