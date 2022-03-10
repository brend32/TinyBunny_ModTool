init -510 python:
    class BoolVaraible:

        def __init__(self, default):
            self.value = default

        def true(self):
            self.value = True
            renpy.restart_interaction()

        def false(self):
            self.value = False
            renpy.restart_interaction()

        def get_selected(self):
            return self.value == True

        def __nonzero__(self):
            return self.value