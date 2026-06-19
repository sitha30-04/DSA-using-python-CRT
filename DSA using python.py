n = 20
a, b = 0, 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
# write a code whether a number is even or odd
number=int(input("enter a number:"))
if number%2==0:
    print("even")
else:
    print("odd")
stack=[]
stack.append(5)
stack.append(6)
print(stack)#[5,6]
stack.pop() 
print(stack)
stack.append(7)
stack .append(4)
print('stack',stack)
print(stack[-1])
print(len(stack)==0)

stack=[5,3,8,2,9]
l=len(stack)
T=8
for i in range(l):
    if stack.pop()==T:
        print("found")
        break
def isValid(s):
    stack = []

    pairs = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for char in s:
        if char in pairs.values():
            stack.append(char)
        else:
            if not stack or stack.pop() != pairs[char]:
                return False

    return len(stack) == 0
print(isValid("()"))       # True
print(isValid("()[]{}"))   # True
print(isValid("(]"))       # False
print(isValid("([)]"))     # False
print(isValid("{[]}"))     # True

class solution:
    def isvalid(self, s: str) ->bool:
        stack=[]
        brackets={")":"(","]":"[","}":"{"}
        for i in s:
            if i in "([{":
                stack.append(i)
            else:
                if not stack:return False
                if stack.pop()!=brackets[i]:
                    return False
        return len(stack)==0

class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self,name,age):
        print("Name:",self.name)
        print("Age:",age)
student1=student("Alice",20)
student1.display("sai",22)

#push,pop,top,getmin
class Minstack:
    def __init__(self):
        self.stack=[]
        self.min_stack=[]
    def push(self,value: int) ->None:
        stack.append(value)
        if not self.min_stack or self.stack[-1]<=self.min_stack[-1]:
            self.min_stack.append(value)
    def pop(self) -> None:
        self.stack.pop()
        if self.stack[-1]==self.min_stack[-1]:
            self.min_stack.pop()
    def top(self) -> int:
        return self.stack[-1]
    def getMin(self) -> int:
        return self.min_stack[-1]

front=0
rear=-1
queue=[None]*5
size=0
def Enqueue(value):
    if size==len(queue):return False
    rear+=1
    size+=1
    queue[rear]=value
    return True
def dequeue():
    if size==0:return False
    front+=1
    return True
def peek():
    return queue[front]
def isFull():
    return size==len(queue)w
def isEmpty():
    return size==0
class MyCircularQueue:

    def __init__(self, k: int):
        self.queue= [0] * k
        self.k=k
        self.front=0
        self.rear=-1
        self.size=0
    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.rear=(self.rear+1)%self.k
        self.queue[self.rear]=value
        self.size+=1
        return True
        
    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.front=(self.front+1)%self.k
        self.size-=1
        return True
        

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.front]

        

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.rear]
        

    def isEmpty(self) -> bool:
        return self.size==0
        

    def isFull(self) -> bool:
        return self.size==self.k

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
Node1=Node(10)
Node2=Node(20)
Node3=Node(40)
print(Node1.data)
print(Node2.data)
print(Node3.data)
Node1.data=30
Node1.next=Node2
Node2.next=Node3
Node1.next=None
print(Node1.next)
print(Node2.next)

l1=[4,5,3,7,6]
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def createList(l1):
    head=None
    for i in l1:
        newnode=Node(i)
        if head is None:
            head=newnode
            return

l1=[4,5,6,7,3]
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def  createList(l1):
    head=None
    temp=head
    for i in l1:
        newNode=Node(i)
        if head is None:
            head=newNode
            temp=head
        else:
            temp.next=newNode
            temp=newNode

    return head
createList(l1)

class Solution:
    def mergeTwoLists(
        self,
        list1: Optional[ListNode],
        list2: Optional[ListNode]
    ) -> Optional[ListNode]:

        dummy = ListNode(0)
        tail = dummy

        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

            tail = tail.next

        if list1 is not None:
            tail.next = list1
        else:
            tail.next = list2

        return dummy.next

class car:
    def __init__ (self.-----)
      self.tyres=4
      self.engine=1
      self.doors=4
      self.color=black
   def move():
      print('moving')
carobject=car()
carobj.mov()

def longest_substring(s):
         char_set=set()
         left=0
        
         max_lenght=0
         for right in range(len(s)):
                while s[right] in char_set:
                        char_set.remove(s[left])
                        left+=1
                char_set.add(s[right])
                max_length=max(max_length, right-left+1)
         return max_length
print(longest_substring("abcabcbb"))


def max_subarray_sum(arr,k)
        window_sum=sum(arr[:k])
        max_sum=window_sum
        for i in range(k,len(arr)):
                window_sum+=arr[i]-arr[i-k]
                max_sum=max(max_sum,window_sum)
        return max_sum
print(max_subarray_sum([2,1,5,1,3,2],3))

def permute(nums, path=[]):
        if len(path)==len(nums):
               print(path)
               return
        for num in nums:
               if num not in path:
                       permute(nums,path+[num])
nums=[1,2,3]
permute(nums)

A=[1,2,3,4,5]
B=[2,4]
program:
def is_subset(A<B):
         for element in B:
               if element not in A:
                       return False
         return true
A=[1,2,3,4,5]
B=[2,4]
print(is_subset(A,B))

#function to reverse part of array:
Rotating 7 times==Rotating 2 times
def reverse(arr,start,end):
       while start<end:
            arr[start],arr[end],arr[start]
            start+=1
            end-=1
      k=k%n
      reverse(arr,o,k-1)
      reverse(arr,k,n-1)
      reverse(arr,0,n-1)
      return arr
#Right rotate using left rotate
def right_rotate(arr,n-k):
    n=len(arr)
    k=k%n
    return left_rotate(arr,n-k)
print("original array:",arr)
print("right rotate array:',right_rotate(arr,k")

# Calculating area of 3 circles — no functions
r1 = 5
area1 = 3.14159 * r1 * r1
print(area1)
r2 = 7
area2 = 3.14159 * r2 * r2
print(area2)
r3 = 10
area3 = 3.14159 * r3 * r3
print(area3)

def sum_list(numbers):
    if len(numbers)==0:
        return 0
        else:
            return numbers
    
funcs = []
for i in range(3):
 funcs.append(lambda: i)
print([f() for f in funcs])

string = "example"

count = 0
vowels = "aeiouAEIOU"

for char in string:
    if char in vowels:
        count += 1

print("Number of vowels:", count)

def left_rotate(arr,k):
        n=len(arr)
        k=k%n  # important for larger k
        temp=arr[:k]
        arr=arr[k:]+temp
        return arr
arr=[1,2,3,4,5]
printn(left_rotate(arr,7))
step1:[2,3,4,5,1]
step2:[3,4,5,1,2]
step3:[4,5,1,2,3]
step4:[5,1,2,3,4]
step5:[1,2,3,4,5]
step6:[2,3,4,5,1]
step7:[3,4,5,1,2]

        
