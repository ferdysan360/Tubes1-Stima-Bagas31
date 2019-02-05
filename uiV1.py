from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class Solver24Grid(GridLayout):
    pass


class Solver24V1App(App):

    def build(self):
        return Solver24Grid()


if __name__ == '__main__':
    Solver24V1App().run()
