init -510 python:
    class ModEpisode:

        def __init__(self, name, author, start_label, icon, version, author_link = None):
            self.name = name
            self.author = author
            self.start_label = start_label
            self.icon = icon
            self.version = version
            self.author_link = author_link

    class ModEpisodes:

        def __init__(self):
            self.episodes = []

        def add(self, episode):
            self.episodes.append(episode)

init -510 python:
    Mod.episodes = ModEpisodes()