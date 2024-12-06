class Link:
   def __init__(self,val,prev_link,next_link):
      self.val=val
      self.next =next_link
      self.prev=prev_link

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = Link(homepage)
        self.tail = self.head

    def visit(self, url: str):
        

    def back(self, steps: int):

        
    def forward(self, steps: int):
# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
