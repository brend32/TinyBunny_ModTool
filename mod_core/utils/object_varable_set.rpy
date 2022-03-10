init -510 python:
    class ObjectVaraibleSet(Action, FieldEquality):

        def __init__(self, call, get, value):
            self.call = call
            self.get = get
            self.value = value

        def __call__(self):
            self.call()
            renpy.restart_interaction()

        def get_selected(self):
            return self.get() == self.value