from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class Solver24Grid(GridLayout):
    pass


class Solver24App(App):

    def build(self):
        return Solver24Grid()


if __name__ == '__main__':
    Solver24App().run()

# comments:
    # self.cols = 3
    # self.btn1 = Button(text='1')
    # self.btn2 = Button(text='2')
    # self.btn3 = Button(text='3')
    # self.btn4 = Button(text='4')
    # self.btn5 = Button(text='5')
    # self.btn6 = Button(text='6')
    # self.btn7 = Button(text='7')
    # self.btn8 = Button(text='8')
    # self.btn9 = Button(text='9')
    # self.btn0 = Button(text='0')

    # self.btn1.bind(on_press=print('1'))
    # self.btn2.bind(on_press=print('2'))
    # self.btn3.bind(on_press=print('3'))
    # self.btn4.bind(on_press=print('4'))
    # self.btn5.bind(on_press=print('5'))
    # self.btn6.bind(on_press=print('6'))
    # self.btn7.bind(on_press=print('7'))
    # self.btn8.bind(on_press=print('8'))
    # self.btn9.bind(on_press=print('9'))
    # self.btn0.bind(on_press=print('0'))

    # self.add_widget(self.btn1)
    # self.add_widget(self.btn2)
    # self.add_widget(self.btn3)
    # self.add_widget(self.btn4)
    # self.add_widget(self.btn5)
    # self.add_widget(self.btn6)
    # self.add_widget(self.btn7)
    # self.add_widget(self.btn8)
    # self.add_widget(self.btn9)
    # self.add_widget(Label(text=''))
    # self.add_widget(self.btn0)
    # self.add_widget(Label(text=''))
