import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import *
from kivy.graphics import Line

class Snake:
    pass

class Food:
    pass


class MainWindow(Widget):
    line_x = None
    line_y = None
    lineNo = 5
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.horizontal_line()
        self.vertical_line()


    def on_size(self, *args):
        # print(self.height)
        # print(self.width)
        # self.update_horizontal_line()
        self.update_vertical_line()


    def horizontal_line(self):
        with self.canvas:
            Color(rgba=(1, 1, 0, 1))
            self.line_x = Line(points=[0, 0, 100, 100], width=2)
    
    def update_horizontal_line(self):
        self.line_x.points = [0, self.height/2, self.width, self.height/2]


    def vertical_line(self):
        with self.canvas:
            Color(rgba=(1, 0, 1, 1))
            for i in range(self.lineNo):
                self.line_y = Line(points=[0, 0, 100, 100], width=2)

    def update_vertical_line(self):
        for i in range(self.lineNo):
            l_x1 = 0 
            l_y1 = 0
            l_x2 = 0
            l_y2 =  self.height
            self.line_y.points = [l_x1, l_y1, l_x2, l_y2]    


    def coOrdinate(self):
        pass

    

class SuperWindow(App):
    def build(self):
        return MainWindow()

SuperWindow().run()


