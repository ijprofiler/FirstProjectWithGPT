from kivy.app import App
from notes_app.app.views.main_view import MainView


class NotesApp(App):
    def build(self):
        return MainView()


if __name__ == '__main__':
    NotesApp().run()