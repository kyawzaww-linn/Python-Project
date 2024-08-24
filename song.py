"""..."""


class Song:
    def __init__(self, title="", artist="", year=0, learned=False):
        self.title = title
        self.artist = artist
        self.year = year
        self.learned = learned

    def __str__(self):
        learned_status = "Learned" if self.learned else "Not Learned"
        return f"{self.title} by {self.artist} ({self.year}) - {learned_status}"

    def mark_learned(self):
        self.learned = True

    def mark_unlearned(self):
        self.learned = False
