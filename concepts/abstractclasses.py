from abc import abstractmethod


class IInterface:
    @classmethod
    def name(self):
        return "Pop"

    @abstractmethod
    def show(self):
        raise NotImplementedError

    @abstractmethod
    def show_not_implemented(self):
        raise NotImplementedError


class GoodParent(IInterface):
    def show(self):
        print("good")


class BadParent(object):
    def show(self):
        print("bad")


class Child(object):
    def __init__(self, parent):
        if not IInterface.name() == "Pop":
            raise Exception("wrong name")
        if not isinstance(parent, IInterface):
            raise Exception("wrong interface")
        self._parent = parent

    def child_show(self):
        self._parent.show()

    def child_show_not_implemented(self):
        self._parent.show_not_implemented()


# This will print wrong interface
try:
    x = Child(BadParent)
except Exception as exc:
    print(exc)

# This will print good
Child(GoodParent()).child_show()

# This is NotImplementedError
Child(GoodParent()).child_show_not_implemented()
