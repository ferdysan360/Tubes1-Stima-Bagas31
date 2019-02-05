from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition

a = 1
b = 3
c = 7
d = 4

# kivy file implementation
Builder.load_string("""
<MenuScreen>:
    GridLayout:
        rows: 2
        BoxLayout:
            Label:
                text: 'Nothing to see here'

        BoxLayout:
            Button:
                text: 'File input'
                on_press:
                    root.manager.transition.direction = 'left'
                    root.manager.current = 'fileinput'

            Button:
                text: 'Button input'
                on_press:
                    root.manager.transition.direction = 'left'
                    root.manager.current = 'buttoninput'

<FileInputScreen>:
    GridLayout:
        rows: 2
        font_size: 72
        BoxLayout:
            Label:
                id: label1
                text: 'Label 1'
            Label:
                id: label2
                text: 'Label 2'
            Label:
                id: label3
                text: 'Label 3'
            Label:
                id: label4
                text: 'Label 4'

        BoxLayout:
            Button:
                text: 'Draw cards'
                on_press:
                    label1.text = root.GetNumber1()
                    label2.text = root.GetNumber2()
                    label3.text = root.GetNumber3()
                    label4.text = root.GetNumber4()
            Button:
                text: 'Reset'
                on_press:
                    label1.text = 'Label 1'
                    label2.text = 'Label 2'
                    label3.text = 'Label 3'
                    label4.text = 'Label 4'

<ButtonInputScreen>:
    Label:
        font_size: 72
        text: 'Hello, World!'
""")

# Declare screens

class MenuScreen(Screen):
    pass

class FileInputScreen(Screen):
    global a
    global b
    global c
    global d
    def GetNumber1(self):
        return str(a)

    def GetNumber2(self):
        return str(b)

    def GetNumber3(self):
        return str(c)

    def GetNumber4(self):
        return str(d)
    pass

class ButtonInputScreen(Screen):
    pass

# Create the screen manager
sm = ScreenManager(transition=FadeTransition())
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(FileInputScreen(name='fileinput'))
sm.add_widget(ButtonInputScreen(name='buttoninput'))

class TestApp(App):

    def build(self):
        return sm


if __name__ == '__main__':
    TestApp().run()
