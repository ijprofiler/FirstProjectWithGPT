from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label



class MainView(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'


        self.label = Label(text='Главное окно')
        self.button = Button(text='Нажми меня')
        self.button.bind(on_press=self.on_button_press)


        self.add_widget(self.label)
        self.add_widget(self.button)


def on_button_press(self, instance):
    self.label.text = 'Кнопка нажата'