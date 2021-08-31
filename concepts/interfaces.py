from abc import ABC, abstractmethod


class IInterface(ABC):
    
    @classmethod
    def name(self): return "Pop"
    @abstractmethod
    def show(self): 
        pass
    @abstractmethod
    def show_42(self): 
        pass

class GoodParent(IInterface):
    def show(self):
        print('good')
    def show_42(self):
        print("42")

class BadParent(IInterface):
    def show(self):
        print('bad')
    

# This has error because not all abstractmethods were implemented
x = BadParent()

# This works
z = GoodParent()
z.show()


