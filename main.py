"""
Name: Kyaw Zaww linn
Date Started: 18/1/2024
Brief Project Description: A Python project with GUI and Console programs that (re)use classes to manage a list of songs to learn.
GitHub URL: https://github.com/JCUS-CP1404/cp1404-song-list-assignment-2-kyawzawwlinn/blob/master/a1_classes.py
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.spinner import Spinner
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView
from kivy.properties import ObjectProperty
from song import Song
from songcollection import SongCollection
import json


class MainWidget(BoxLayout):
    sort_spinner = ObjectProperty(None)
    song_list_layout = ObjectProperty(None)
    learned_label = ObjectProperty(None)
    status_label = ObjectProperty(None)
    title_input = ObjectProperty(None)
    artist_input = ObjectProperty(None)
    year_input = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.song_collection = SongCollection()
        self.load_songs()
        self.display_songs()

    def load_songs(self):
        self.song_collection.load_songs('songs.json')

    def save_songs(self):
        try:
            self.song_collection.save_songs('songs.json')
        except Exception as e:
            self.status_label.text = f'Error saving songs: {str(e)}'

    def add_song(self):
        title = self.title_input.text
        artist = self.artist_input.text
        year_text = self.year_input.text
        if not (title and artist and year_text):
            self.status_label.text = 'All fields must be completed'
            return
        try:
            year = int(year_text)
            if year <= 0:
                self.status_label.text = 'Year must be > 0'
                return
            new_song = Song(title, artist, year)
            self.song_collection.add_song(new_song)
            self.title_input.text = ''
            self.artist_input.text = ''
            self.year_input.text = ''
            self.display_songs()
        except ValueError:
            self.status_label.text = 'Please enter a valid number'

    def display_songs(self):
        self.song_list_layout.clear_widgets()
        grid_layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
        grid_layout.bind(minimum_height=grid_layout.setter('height'))

        for song in self.song_collection.get_songs():
            button_color = (0, 1, 0, 1) if song.learned else (1, 0, 0, 1)
            button = Button(text=f'{song.title} by {song.artist} ({song.year})', background_color=button_color,
                            size_hint_y=None, height=40)
            button.bind(on_release=lambda instance, s=song: self.toggle_learned(s, instance))
            grid_layout.add_widget(button)

        scroll_view = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
        scroll_view.add_widget(grid_layout)

        self.song_list_layout.add_widget(scroll_view)
        learned_count = len(self.song_collection.get_learned_songs())
        unlearned_count = len(self.song_collection.get_unlearned_songs())
        self.learned_label.text = f'To learn: {unlearned_count}   Learned: {learned_count}'

    def toggle_learned(self, song, instance):
        song.learned = not song.learned
        self.display_songs()

    def clear_fields(self):
        self.title_input.text = ''
        self.artist_input.text = ''
        self.year_input.text = ''
        self.status_label.text = ''

    def on_stop(self):
        self.save_songs()


Builder.load_file('app.kv')  # Manually load the app.kv file


class SongListApp(App):
    def build(self):
        Window.bind(on_request_close=self.on_request_close)
        return MainWidget()

    def on_request_close(self, *args, **kwargs):
        self.root.save_songs()
        return False


if __name__ == '__main__':
    SongListApp().run()
