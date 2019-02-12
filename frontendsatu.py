from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition,  SlideTransition
from array import array
import random
import copy
import backend

# Iniliasisasi listofanswer
listofanswer = ['0','0']

# Inisialisasi array kartu
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
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: 'lantern.jpg'

    GridLayout:
        rows: 2
        BoxLayout:
            Label:
                font_size: 72
                text: '24 Solver'

        BoxLayout:
            spacing: 200
            padding: 100
            Button:
                background_color: (0,0,0.3,0.5)
                font_size: 50
                text: 'Start'
                on_release:
                    root.manager.transition.direction = 'left'
                    root.manager.current = 'fileinput'

            Button:
                background_color: (0,0,0.3,0.5)
                font_size: 50
                text: 'Exit'
                on_release:
                    root.CloseApp()

<FileInputScreen>:
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: 'lantern.jpg'

    GridLayout:
        padding: 50
        rows: 2
        GridLayout:
            spacing: 50
            padding: 50
            rows: 2
            BoxLayout:
                Label:
                    font_size: 50
                    id: cardsleftlabel
                    text: root.GetCardsLeft()
                BoxLayout:
                    spacing: 30
                    orientation: 'vertical'
                    Label:
                        font_size: 42
                        id: answer
                        text: 'Answer'
                    Label:
                        font_size: 42
                        id: answerpoints
                        text: 'Points'

            BoxLayout:
                rows: 2
                Label:
                    font_size: 60
                    id: label1
                    text: 'No card'
                Label:
                    font_size: 60
                    id: label2
                    text: 'No card'
                Label:
                    font_size: 60
                    id: label3
                    text: 'No card'
                Label:
                    font_size: 60
                    id: label4
                    text: 'No card'

        GridLayout:
            rows: 2
            BoxLayout:
                padding: 30
                Button:
                    background_color: (0,0,0.4,0.8)
                    font_size: 40
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
                        movebackbutton.disabled = False
                        answer.text = 'Answer'
                        answerpoints.text = 'Points'
                        if (root.GetNeff() == '0'): drawbutton.disabled = True
                        else: drawbutton.disabled = False

                Button:
                    background_color: (0,0,0.4,0.8)
                    font_size: 40
                    id: solvebutton
                    text: 'Solve'
                    disabled: True
                    on_release:
                        answer.text = root.Solve()
                        answerpoints.text = 'Points = ' + root.GetPoints()

                Button:
                    background_color: (0,0,0.4,0.8)
                    font_size: 35
                    multiline: True
                    id: movebackbutton
                    text: 'Move cards to deck'
                    disabled: True
                    on_release:
                        root.MoveCardsBack()
                        drawbutton.disabled = False
                        if (label1.text == 'No card'): solvebutton.disabled = True
                        if (label1.text == 'No card'): movebackbutton.disabled = True

            BoxLayout:
                spacing: 200
                padding: 50
                Button:
                    background_color: (0,0,0.4,0.8)
                    font_size: 40
                    text: 'Reset'
                    on_release:
                        root.CardsReset()
                        solvebutton.disabled = True
                        movebackbutton.disabled = True
                        drawbutton.disabled = False

                Button:
                    background_color: (0,0,0.4,0.8)
                    font_size: 40
                    text: 'Back to menu'
                    on_release:
                        root.manager.transition.direction = 'right'
                        root.manager.current = 'menu'
                        root.CardsReset()
                        solvebutton.disabled = True
                        movebackbutton.disabled = True
                        drawbutton.disabled = False
""")

# Deklarasi screens
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

    def MoveCardsBack(self):
        global data

        data.append(int(self.ids.label1.text))
        data.append(int(self.ids.label2.text))
        data.append(int(self.ids.label3.text))
        data.append(int(self.ids.label4.text))

        self.ids.label1.text = 'No card'
        self.ids.label2.text = 'No card'
        self.ids.label3.text = 'No card'
        self.ids.label4.text = 'No card'
        self.ids.cardsleftlabel.text = self.GetCardsLeft()
        self.ids.answer.text = 'Answer'
        self.ids.answerpoints.text = 'Points'

    def CardsReset(self):
        global data
        global datainit

        self.ids.label1.text = 'No card'
        self.ids.label2.text = 'No card'
        self.ids.label3.text = 'No card'
        self.ids.label4.text = 'No card'
        data = copy.copy(datainit)
        self.ids.cardsleftlabel.text = self.GetCardsLeft()
        self.ids.answer.text = 'Answer'
        self.ids.answerpoints.text = 'Points'
    
    def Solve(self):
        global listofanswer
        a = self.ids.label1.text
        b = self.ids.label2.text
        c = self.ids.label3.text
        d = self.ids.label4.text
        
        number = []
        number.append(int(a))
        number.append(int(b))
        number.append(int(c))
        number.append(int(d))

        listofanswer = backend.solve24(number)
        return listofanswer[0]

    def GetPoints(self):
        return listofanswer[1]

    pass

# Membuat screen manager
sm = ScreenManager(transition=FadeTransition())
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(FileInputScreen(name='fileinput'))


class UIApp(App):

    def build(self):
        self.title = '24 Game Solver'
        return sm


if __name__ == '__main__':
    Window.fullscreen = 'auto'
    UIApp().run()
