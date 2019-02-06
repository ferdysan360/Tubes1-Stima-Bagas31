from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition, FallOutTransition

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
        BoxLayout:
            rows: 2
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
        GridLayout:
            rows: 2
            Button:
                text: 'Draw cards'
                on_press:
                    label1.text = root.GetNumber1()
                    label2.text = root.GetNumber2()
                    label3.text = root.GetNumber3()
                    label4.text = root.GetNumber4()
                    solvebutton.disabled = False

            Button:
                id: solvebutton
                text: 'Solve'
                disabled: True
                on_press:
                    root.manager.transition.direction = 'right'
                    root.manager.current = 'answer'
            Button:
                text: 'Reset'
                on_press:
                    root.CardsReset()
                    solvebutton.disabled = True

            Button:
                text: 'Back to menu'
                on_press:
                    root.CardsReset()
                    root.manager.transition.direction = 'right'
                    root.manager.current = 'menu'

<ButtonInputScreen>:
    GridLayout:
        rows: 2
        BoxLayout:
            Label:
                font_size: 72
                text: 'Hello, World!'

        BoxLayout:
            Button:
                text: 'Back to menu'
                on_press:
                    root.manager.transition.direction = 'right'
                    root.manager.current = 'menu'

<AnswerScreen>:
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'Answer : ' + root.Solve()
        
        Label:
            text: 'Points : ' + root.Points()
    
        Button:
            text: 'Back to menu'
            on_press:
                root.manager.transition.direction = 'right'
                root.manager.current = 'menu'
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
    
    def CardsReset(self):
        self.ids.label1.text = 'No card'
        self.ids.label2.text = 'No card'
        self.ids.label3.text = 'No card'
        self.ids.label4.text = 'No card'

    pass

class ButtonInputScreen(Screen):
    pass

class AnswerScreen(Screen):
    def Solve(self):
        return FileInputScreen().GetNumber1() + '+' + FileInputScreen().GetNumber2() + '+' + FileInputScreen().GetNumber3() + '+' + FileInputScreen().GetNumber4()
    
    def Points(self):
        return str(15)
    pass

# Create the screen manager
sm = ScreenManager(transition=FadeTransition())
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(FileInputScreen(name='fileinput'))
sm.add_widget(ButtonInputScreen(name='buttoninput'))
sm.add_widget(AnswerScreen(name='answer'))

class TestApp(App):

    def build(self):
        return sm


if __name__ == '__main__':
    TestApp().run()

