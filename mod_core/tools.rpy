init -510 python:
    class ModTool:

        def __init__(self, activate, deactivate, id, name, author, version, icon, author_link = None, label_callback = None):
            self.activate = activate
            self.deactivate = deactivate
            self.id = id
            self.name = name
            self.author = author
            self.version = version
            self.icon = icon
            self.author_link = author_link
            self.label_callback = label_callback

            if id in persistent.mod_tools_activated:
                self.activated = persistent.mod_tools_activated[id]
            else:
                self.activated = True

        def init(self):
            if self.activated:
                self.activate()
        
        def get_activated(self):
            return self.activated

        def call_label_callback(self, label, context):
            if not (self.label_callback is None):
                if self.activated:
                    self.label_callback(label, context);

        def on(self):
            self.activated = True
            self.activate()

            self._update()

        def off(self):
            self.activated = False
            self.deactivate()

            self._update()

        def _update(self):
            persistent.mod_tools_activated.update({ self.id: self.activated })
            renpy.save_persistent()

    class ModTools:

        def __init__(self):
            self.tools = {}
            self.inited = False
            config.label_callback = self._label_callback

        def _label_callback(self, label, context):
            if self.inited:
                for tool in self.tools:
                    self.tools[tool].call_label_callback(label, context);

        def register(self, tool):
            self.tools.update({ tool.id: tool })

        def init(self):
            if self.inited == False:
                for tool in self.tools:
                    self.tools[tool].init()

            self.inited = True

init -510:
    default persistent.mod_tools_activated = {}

init -510 python:
    Mod.tools = ModTools()
    if persistent.mod_tools_activated is None:
        persistent.mod_tools_activated = {}