class MainController:
    def __init__(self, view):
        self.view = view


    def on_button_pressed(self):
        self.view.set_label_text('Кнопка нажата (через контроллер)')