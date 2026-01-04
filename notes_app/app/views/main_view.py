from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


class MainView(BoxLayout):
    def __init__(self, controller, **kwargs):
        super().__init__(**kwargs)
        self.controller = controller
        self.orientation = 'vertical'


        self.label = Label(text='Главное окно')
        self.button = Button(text='Нажми меня')
        self.button.bind(on_press=self._on_button_press)


        self.add_widget(self.label)
        self.add_widget(self.button)


    def _on_button_press(self, instance):
        self.controller.on_button_pressed()


    def set_label_text(self, text):
        self.label.text = text