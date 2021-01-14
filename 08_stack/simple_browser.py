"""
a simple browser realize
     Author: zhenchao.zhu
     Answer: We use two stacks, X and Y. We push the first-viewed pages into stack X in turn, and when we click the back button, we will pop them out of stack X in turn.
     And put the popped data into stack Y in turn. When we click the forward button, we take the data from stack Y in turn and put it into stack X.
     When there is no data in stack X, it means that there is no page to go back and browse. When there is no data in stack Y,
     That means there is no page to browse by clicking the forward button.
"""


from linked_stack import LinkedStack
import sys
# single_linked_list
sys.path.append('linked_stack.py')
#from .linked_stack import LinkedStack


class NewLinkedStack(LinkedStack):

    def is_empty(self):
        return not self._top


class Browser():

    def __init__(self):
        self.forward_stack = NewLinkedStack()
        self.back_stack = NewLinkedStack()

    def can_forward(self):
        if self.back_stack.is_empty():
            return False

        return True

    def can_back(self):
        if self.forward_stack.is_empty():
            return False

        return True

    def open(self, url):
        print("Open new url %s" % url, end="\n")
        self.forward_stack.push(url)

    def back(self):
        if self.forward_stack.is_empty():
            return

        top = self.forward_stack.pop()
        self.back_stack.push(top)
        print("back to %s" % top, end="\n")

    def forward(self):
        if self.back_stack.is_empty():
            return

        top = self.back_stack.pop()
        self.forward_stack.push(top)
        print("forward to %s" % top, end="\n")


if __name__ == '__main__':

    browser = Browser()
    browser.open('a')
    browser.open('b')
    browser.open('c')
    if browser.can_back():
        browser.back()

    if browser.can_forward():
        browser.forward()

    browser.back()
    browser.back()
    browser.back()
