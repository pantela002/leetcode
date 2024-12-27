class Link:
   def __init__(self,val,prev_link=None,next_link=None):
      self.val=val
      self.next =next_link
      self.prev=prev_link

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = Link(homepage)
        self.tail = self.head
        self.curr = self.head

    def visit(self, url: str):
        self.curr.next = Link(url)
        self.curr.next.prev = self.curr
        self.curr = self.curr.next
        self.tail = self.curr
        
    def back(self, steps: int):
        while steps>0 and self.curr!=self.head:
            self.curr=self.curr.prev
            steps-=1
        return self.curr.val
        
    def forward(self, steps: int):
        while steps>0 and self.curr!=self.tail:
            self.curr = self.curr.next
            steps-=1
        return self.curr.val
    


# Your BrowserHistory object will be instantiated and called as such:
obj = BrowserHistory("homepage")
obj.visit("leet")
obj.visit("google")
obj.visit("facebook")
param_1 = obj.back(1)
param_2 = obj.back(1)
param_3 = obj.forward(1)
obj.visit("youtube")
param_4 = obj.back(2)
param_5 = obj.back(2)
param_6 = obj.forward(2)
print(param_1)
print(param_2)
print(param_3)
print(param_4)
print(param_5)
print(param_6)

