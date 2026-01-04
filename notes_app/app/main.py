from kivy.app import App
from notes_app.app.views.main_view import MainView
from notes_app.app.controllers.main_controller import MainController


class NotesApp(App):
    def build(self):
        # 1. Создаём View без контроллера
        view = MainView(controller=None)

        # 2. Создаём Controller и передаём ему View
        controller = MainController(view)

        # 3. Связываем View с Controller
        view.controller = controller

        # 4. Возвращаем корневой виджет
        return view


if __name__ == '__main__':
    NotesApp().run()