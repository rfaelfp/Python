from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class MyCalc(GridLayout):
    def __init__(self, **kwargs):
        super(MyCalc, self).__init__(**kwargs)

        self.cols = 1


        self.num1 = TextInput(multiline=True)
        self.add_widget(self.num1)

        self.l2 = Label(text="Digite outro numero: ")
        self.add_widget(self.l2)

        self.num2 = TextInput(multiline=True)
        self.add_widget(self.num2)

        self.somar = Button(text="Efetuar soma", font_size=40)
        self.somar.bind(on_press=self.pressionar)
        self.add_widget(self.somar)

        self.l2 = Label(text="O resultado é: ");
        self.add_widget(self.l2)

        self.resultado = TextInput(multiline=True)
        self.add_widget(self.resultado)

    def pressionar(self, instance):
        self.resultado.text = str(int(self.num1.text) + int(self.num2.text))


class MyApp(App):
    def build(self):
        return MyCalc()


MyApp().run()
