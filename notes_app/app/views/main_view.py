from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label



class MainView(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'


        self.label = Label(text='Главное окно')
        # Создаем кнопку
        self.button = Button(text='Нажми меня')
        # Привязываем метод к кнопке
        self.button.bind(on_press=self.on_button_press)


        self.add_widget(self.label)
        self.add_widget(self.button)


    def on_button_press(self, instance):
        print("Кнопка нажата!")
        # Или измените текст кнопки
        instance.text = "Кнопка нажата"