from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition,  SlideTransition
from array import array
import random
import copy


datainit = array('i')
data = array('i')
for i in range(1,14):
    datainit.append(i)
    datainit.append(i)
    datainit.append(i)
    datainit.append(i)

data = copy.copy(datainit)

# kivy file implementation
Builder.load_string("""
<MenuScreen>:
    GridLayout:
        rows: 2
        BoxLayout:
            Label:
                font_size: 72
                text: '24 Solver'

        BoxLayout:
            Button:
                font_size: 50
                text: 'Start'
                on_release:
                    root.manager.transition.direction = 'left'
                    root.manager.current = 'fileinput'

            Button:
                font_size: 50
                text: 'Exit'
                on_release:
                    root.CloseApp()

<FileInputScreen>:
    GridLayout:
        rows: 2
        GridLayout:
            rows: 2
            BoxLayout:
                Label:
                    font_size: 50
                    id: cardsleftlabel
                    text: root.GetCardsLeft()

            BoxLayout:
                rows: 2
                Label:
                    font_size: 50
                    id: label1
                    text: 'No card'
                Label:
                    font_size: 50
                    id: label2
                    text: 'No card'
                Label:
                    font_size: 50
                    id: label3
                    text: 'No card'
                Label:
                    font_size: 50
                    id: label4
                    text: 'No card'

        GridLayout:
            rows: 2
            Button:
                font_size: 50
                id: drawbutton
                text: 'Draw cards'
                disabled: False
                on_release:
                    label1.text = root.GetNumber()
                    label2.text = root.GetNumber()
                    label3.text = root.GetNumber()
                    label4.text = root.GetNumber()
                    cardsleftlabel.text = root.GetCardsLeft()
                    solvebutton.disabled = False
                    if (root.GetNeff() == '0'): drawbutton.disabled = True

            Button:
                font_size: 50
                id: solvebutton
                text: 'Solve'
                disabled: True
                on_release:
                    root.manager.transition.direction = 'left'
                    root.manager.current = 'answer'

            Button:
                font_size: 50
                text: 'Reset'
                on_release:
                    root.CardsReset()
                    solvebutton.disabled = True
                    drawbutton.disabled = False

            Button:
                font_size: 50
                text: 'Back to menu'
                on_release:
                    root.manager.transition.direction = 'right'
                    root.manager.current = 'menu'

<AnswerScreen>:
    BoxLayout:
        orientation: 'vertical'
        Label:
            font_size: 72
            text: 'Answer : ' + root.Solve()
        
        Label:
            font_size: 72
            text: 'Points : ' + root.Points()
    
        Button:
            font_size: 50
            text: 'Back'
            on_release:
                root.manager.transition.direction = 'right'
                root.manager.current = 'fileinput'
""")

# Declare screens
class MenuScreen(Screen):
    def CloseApp(self):
        App.get_running_app().stop()
        Window.close()
    pass

class FileInputScreen(Screen):

    def GetNumber(self):
        i = random.randint(0, len(data)-1)
        return str(data.pop(i))
    
    def GetNeff(self):
        return str(len(data))

    def GetCardsLeft(self):
        return 'Cards Left : ' + self.GetNeff()

    def CardsReset(self):
        global data
        global datainit

        self.ids.label1.text = 'No card'
        self.ids.label2.text = 'No card'
        self.ids.label3.text = 'No card'
        self.ids.label4.text = 'No card'
        data = copy.copy(datainit)
        self.ids.cardsleftlabel.text = self.GetCardsLeft()

    pass

class AnswerScreen(Screen):

    def Solve(self):
        return "Hello, World!"
    
    def Points(self):
        return str(15)
    pass

# Create the screen manager
sm = ScreenManager(transition=SlideTransition())
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(FileInputScreen(name='fileinput'))
sm.add_widget(AnswerScreen(name='answer'))

class UIApp(App):

    def build(self):
        self.title = '24 Game Solver'
        return sm


if __name__ == '__main__':
    UIApp().run()

