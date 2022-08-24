from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Rectangle

import random

class KivyTetrisApp(App):
    pass


class GameOver(RelativeLayout):
    pass   


class GridButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.background_color = (0.2, 0.2, 0.2, 1)
        self.disabled = True
        self.background_disabled_normal = ""


class Panel(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(*kwargs) 
        
        self.orientation = "vertical"
        
        self.label1 = Label(text = "KivyTetris",
                            font_size = self.height / 3,
                            font_name = "label_font.ttf",
                            color = (0, 0.25, 0.3, 1),
                            bold = True,
                            size_hint = (1, 2))
        
        self.label2 = Label(text = "Next:",
                            font_size = self.height / 3,
                            font_name = "label_font.ttf",
                            color = (0, 0.25, 0.3, 1),
                            bold = True,
                            size_hint = (1, 1))
        
        self.block = Label(size_hint = (1, 2))
        
        self.label3 = Label(text = "Points:",
                            font_size = self.height / 3,
                            font_name = "label_font.ttf",
                            color = (0, 0.25, 0.3, 1),
                            bold = True,
                            size_hint = (1, 1))
        
        self.points = Label(text = "pts",
                            font_size = self.height / 3,
                            font_name = "label_font.ttf",
                            color = (0, 0.25, 0.3, 1),
                            bold = True,
                            size_hint = (1, 2))
        
        self.add_widget(self.label1)
        self.add_widget(self.label2)
        self.add_widget(self.block)
        self.add_widget(self.label3)
        self.add_widget(self.points) 
        
        with self.canvas:
            Color(0, 0.25, 0.3)
            self.seg1 = Rectangle()
            self.seg2 = Rectangle()
            self.seg3 = Rectangle()
            self.seg4 = Rectangle()
            

    def update(self, r):
        unit = self.width / 14
        
        self.seg1.size = (unit, unit)
        self.seg2.size = (unit, unit)
        self.seg3.size = (unit, unit)
        self.seg4.size = (unit, unit)
        
        if r == 1:
            self.seg1.pos = self.height / 2 + self.width / 2 - unit / 2, self.height / 2 + unit
            self.seg2.pos = self.height / 2 + self.width / 2 - unit / 2, self.height / 2
            self.seg3.pos = self.height / 2 + self.width / 2 - unit / 2, self.height / 2 - unit
            self.seg4.pos = self.height / 2 + self.width / 2 - unit / 2, self.height / 2 - unit * 2
        elif r == 2:
            self.seg1.pos = self.height / 2 + self.width / 2 - unit, self.height / 2
            self.seg2.pos = self.height / 2 + self.width / 2, self.height / 2
            self.seg3.pos = self.height / 2 + self.width / 2 - unit, self.height / 2 - unit
            self.seg4.pos = self.height / 2 + self.width / 2, self.height / 2 - unit
        elif r == 3:
            self.seg1.pos = self.height / 2 + self.width / 2 - unit, self.height / 2 + unit / 2
            self.seg2.pos = self.height / 2 + self.width / 2 - unit, self.height / 2 - unit / 2
            self.seg3.pos = self.height / 2 + self.width / 2 - unit, self.height / 2 - unit * 3 / 2
            self.seg4.pos = self.height / 2 + self.width / 2, self.height / 2 - unit * 3 / 2
        elif r == 4:
            self.seg1.pos = self.height / 2 + self.width / 2, self.height / 2 + unit / 2
            self.seg2.pos = self.height / 2 + self.width / 2, self.height / 2 - unit / 2
            self.seg3.pos = self.height / 2 + self.width / 2, self.height / 2 - unit * 3 / 2
            self.seg4.pos = self.height / 2 + self.width / 2 - unit, self.height / 2 - unit * 3 / 2
        elif r == 5:
            self.seg1.pos = self.height / 2 + self.width / 2 - unit, self.height / 2 - unit
            self.seg2.pos = self.height / 2 + self.width / 2, self.height / 2 - unit
            self.seg3.pos = self.height / 2 + self.width / 2, self.height / 2
            self.seg4.pos = self.height / 2 + self.width / 2 + unit, self.height / 2
        elif r == 6:
            self.seg1.pos = self.height / 2 + self.width / 2 - unit, self.height / 2 - unit * 3 / 2
            self.seg2.pos = self.height / 2 + self.width / 2 - unit, self.height / 2 - unit / 2
            self.seg3.pos = self.height / 2 + self.width / 2, self.height / 2 - unit / 2
            self.seg4.pos = self.height / 2 + self.width / 2, self.height / 2 + unit / 2
        elif r == 7:
            self.seg1.pos = self.height / 2 + self.width / 2 - unit / 2, self.height / 2 + unit / 2
            self.seg2.pos = self.height / 2 + self.width / 2 - unit / 2, self.height / 2 - unit / 2
            self.seg3.pos = self.height / 2 + self.width / 2 - unit / 2, self.height / 2 - unit * 3 / 2
            self.seg4.pos = self.height / 2 + self.width / 2 + unit / 2, self.height / 2 - unit / 2

    
class TetrisWidget(GridLayout):  
    shapes = []
    game_speed = 0.5
    time = 0
          
    def __init__(self, **kwargs):
        super().__init__(**kwargs) 
        
        for i in range(200):
            obj = GridButton()
            self.add_widget(obj)
            
        self.r = random.randint(1, 7)
        self.new_shape()
        
    
    def update_game(self, window_width, dt):
        self.collisions_bottom()
        self.fall(dt)
        self.size_change(window_width)
    
    
    def rotate(self):
        if self.shapes[-1][0].brick == "I" and self.shapes[-1][0].version == 1:
            x = self.shapes[-1][0].position_x
            y = self.shapes[-1][0].position_y
            
            if x < 1:
                x = 1
            elif x > 7:
                x = 7
            
            self.shapes[-1][0].position_x = x - 1
            self.shapes[-1][0].position_y = y
            self.shapes[-1][1].position_x = x
            self.shapes[-1][1].position_y = y
            self.shapes[-1][2].position_x = x + 1
            self.shapes[-1][2].position_y = y
            self.shapes[-1][3].position_x = x + 2
            self.shapes[-1][3].position_y = y
            
            self.shapes[-1][0].version = 2
            
        elif self.shapes[-1][0].brick == "I" and self.shapes[-1][0].version == 2:
            x = self.shapes[-1][0].position_x
            y = self.shapes[-1][0].position_y
            
            self.shapes[-1][0].position_x = x + 1
            self.shapes[-1][0].position_y = y
            self.shapes[-1][1].position_x = x + 1
            self.shapes[-1][1].position_y = y + 1
            self.shapes[-1][2].position_x = x + 1
            self.shapes[-1][2].position_y = y + 2
            self.shapes[-1][3].position_x = x + 1
            self.shapes[-1][3].position_y = y + 3
            
            self.shapes[-1][0].version = 1
            
        elif self.shapes[-1][0].brick == "L" and self.shapes[-1][0].version == 1:
            x = self.shapes[-1][0].position_x
            y = self.shapes[-1][0].position_y
            
            if x > 6:
                x = 6
            
            self.shapes[-1][0].position_x = x 
            self.shapes[-1][0].position_y = y + 1
            self.shapes[-1][1].position_x = x + 1
            self.shapes[-1][1].position_y = y + 1
            self.shapes[-1][2].position_x = x + 2
            self.shapes[-1][2].position_y = y + 1
            self.shapes[-1][3].position_x = x 
            self.shapes[-1][3].position_y = y
            
            self.shapes[-1][0].version = 2
            
        elif self.shapes[-1][0].brick == "L" and self.shapes[-1][0].version == 2:
            x = self.shapes[-1][0].position_x
            y = self.shapes[-1][0].position_y
            
            self.shapes[-1][0].position_x = x + 1
            self.shapes[-1][0].position_y = y - 2
            self.shapes[-1][1].position_x = x + 1
            self.shapes[-1][1].position_y = y - 1
            self.shapes[-1][2].position_x = x
            self.shapes[-1][2].position_y = y 
            self.shapes[-1][3].position_x = x + 1
            self.shapes[-1][3].position_y = y
            
            self.shapes[-1][0].version = 3
            
        elif self.shapes[-1][0].brick == "L" and self.shapes[-1][0].version == 3:
            x = self.shapes[-1][0].position_x
            y = self.shapes[-1][0].position_y
            
            if x > 8:
                x = 8
            
            self.shapes[-1][0].position_x = x + 1
            self.shapes[-1][0].position_y = y - 1
            self.shapes[-1][1].position_x = x + 1
            self.shapes[-1][1].position_y = y
            self.shapes[-1][2].position_x = x
            self.shapes[-1][2].position_y = y - 1
            self.shapes[-1][3].position_x = x - 1
            self.shapes[-1][3].position_y = y - 1
            
            self.shapes[-1][0].version = 4
            
        elif self.shapes[-1][0].brick == "L" and self.shapes[-1][0].version == 4:
            x = self.shapes[-1][0].position_x
            y = self.shapes[-1][0].position_y
            
            self.shapes[-1][0].position_x = x - 1
            self.shapes[-1][0].position_y = y
            self.shapes[-1][1].position_x = x - 1
            self.shapes[-1][1].position_y = y + 1
            self.shapes[-1][2].position_x = x - 1
            self.shapes[-1][2].position_y = y + 2
            self.shapes[-1][3].position_x = x 
            self.shapes[-1][3].position_y = y 
            
            self.shapes[-1][0].version = 1
        
        elif self.shapes[-1][0].brick == "J" and self.shapes[-1][0].version == 1:
            x = self.shapes[-1][0].position_x
            y = self.shapes[-1][0].position_y
            
            if x > 7:
                x = 7
            
            self.shapes[-1][0].position_x = x
            self.shapes[-1][0].position_y = y + 1
            self.shapes[-1][1].position_x = x
            self.shapes[-1][1].position_y = y 
            self.shapes[-1][2].position_x = x + 1
            self.shapes[-1][2].position_y = y
            self.shapes[-1][3].position_x = x + 2
            self.shapes[-1][3].position_y = y
            
            self.shapes[-1][0].version = 2

        elif self.shapes[-1][0].brick == "J" and self.shapes[-1][0].version == 2:
            x = self.shapes[-1][0].position_x
            y = self.shapes[-1][0].position_y
            
            self.shapes[-1][0].position_x = x
            self.shapes[-1][0].position_y = y - 1
            self.shapes[-1][1].position_x = x
            self.shapes[-1][1].position_y = y 
            self.shapes[-1][2].position_x = x
            self.shapes[-1][2].position_y = y + 1
            self.shapes[-1][3].position_x = x + 1
            self.shapes[-1][3].position_y = y + 1
            
            self.shapes[-1][0].version = 3
            
        elif self.shapes[-1][0].brick == "J" and self.shapes[-1][0].version == 3:
            x = self.shapes[-1][0].position_x
            y = self.shapes[-1][0].position_y
            
            if x < 1:
                x = 1
            
            self.shapes[-1][0].position_x = x + 1
            self.shapes[-1][0].position_y = y
            self.shapes[-1][1].position_x = x + 1
            self.shapes[-1][1].position_y = y + 1 
            self.shapes[-1][2].position_x = x
            self.shapes[-1][2].position_y = y + 1
            self.shapes[-1][3].position_x = x - 1
            self.shapes[-1][3].position_y = y + 1
            
            self.shapes[-1][0].version = 4

        elif self.shapes[-1][0].brick == "J" and self.shapes[-1][0].version == 4:
            x = self.shapes[-1][0].position_x
            y = self.shapes[-1][0].position_y
            
            if x < 1:
                x = 1
            
            self.shapes[-1][0].position_x = x - 1
            self.shapes[-1][0].position_y = y
            self.shapes[-1][1].position_x = x
            self.shapes[-1][1].position_y = y 
            self.shapes[-1][2].position_x = x
            self.shapes[-1][2].position_y = y + 1
            self.shapes[-1][3].position_x = x
            self.shapes[-1][3].position_y = y + 2
            
            self.shapes[-1][0].version = 1
        
        elif self.shapes[-1][0].brick == "Z" and self.shapes[-1][0].version == 1:
            x = self.shapes[-1][0].position_x
            y = self.shapes[-1][0].position_y
            
            self.shapes[-1][0].position_x = x 
            self.shapes[-1][0].position_y = y + 2
            self.shapes[-1][1].position_x = x
            self.shapes[-1][1].position_y = y + 1 
            self.shapes[-1][2].position_x = x + 1
            self.shapes[-1][2].position_y = y + 1
            self.shapes[-1][3].position_x = x + 1
            self.shapes[-1][3].position_y = y
            
            self.shapes[-1][0].version = 2
            
        elif self.shapes[-1][0].brick == "Z" and self.shapes[-1][0].version == 2:
            x = self.shapes[-1][0].position_x
            y = self.shapes[-1][0].position_y
            
            if x < 1:
                x = 1
            
            self.shapes[-1][0].position_x = x - 1
            self.shapes[-1][0].position_y = y - 2
            self.shapes[-1][1].position_x = x
            self.shapes[-1][1].position_y = y - 2
            self.shapes[-1][2].position_x = x
            self.shapes[-1][2].position_y = y - 1
            self.shapes[-1][3].position_x = x + 1
            self.shapes[-1][3].position_y = y - 1
            
            self.shapes[-1][0].version = 1
        
        elif self.shapes[-1][0].brick == "S" and self.shapes[-1][0].version == 1:
            x = self.shapes[-1][0].position_x
            y = self.shapes[-1][0].position_y
            
            if x < 1:
                x = 1
            
            self.shapes[-1][0].position_x = x - 1
            self.shapes[-1][0].position_y = y + 1
            self.shapes[-1][1].position_x = x
            self.shapes[-1][1].position_y = y + 1 
            self.shapes[-1][2].position_x = x
            self.shapes[-1][2].position_y = y
            self.shapes[-1][3].position_x = x + 1
            self.shapes[-1][3].position_y = y
            
            self.shapes[-1][0].version = 2
        
        elif self.shapes[-1][0].brick == "S" and self.shapes[-1][0].version == 2:
            x = self.shapes[-1][0].position_x
            y = self.shapes[-1][0].position_y
            
            self.shapes[-1][0].position_x = x
            self.shapes[-1][0].position_y = y - 1
            self.shapes[-1][1].position_x = x
            self.shapes[-1][1].position_y = y 
            self.shapes[-1][2].position_x = x + 1
            self.shapes[-1][2].position_y = y
            self.shapes[-1][3].position_x = x + 1
            self.shapes[-1][3].position_y = y + 1
            
            self.shapes[-1][0].version = 1
        
        elif self.shapes[-1][0].brick == "E" and self.shapes[-1][0].version == 1:
            x = self.shapes[-1][0].position_x
            y = self.shapes[-1][0].position_y
            
            if x < 1:
                x = 1
            
            self.shapes[-1][0].position_x = x
            self.shapes[-1][0].position_y = y
            self.shapes[-1][1].position_x = x - 1
            self.shapes[-1][1].position_y = y + 1 
            self.shapes[-1][2].position_x = x
            self.shapes[-1][2].position_y = y + 1
            self.shapes[-1][3].position_x = x + 1
            self.shapes[-1][3].position_y = y + 1
            
            self.shapes[-1][0].version = 2
        
        elif self.shapes[-1][0].brick == "E" and self.shapes[-1][0].version == 2:
            x = self.shapes[-1][0].position_x
            y = self.shapes[-1][0].position_y
            
            self.shapes[-1][0].position_x = x
            self.shapes[-1][0].position_y = y
            self.shapes[-1][1].position_x = x + 1
            self.shapes[-1][1].position_y = y - 1
            self.shapes[-1][2].position_x = x + 1
            self.shapes[-1][2].position_y = y
            self.shapes[-1][3].position_x = x + 1
            self.shapes[-1][3].position_y = y + 1
            
            self.shapes[-1][0].version = 3
            
        elif self.shapes[-1][0].brick == "E" and self.shapes[-1][0].version == 3:
            x = self.shapes[-1][0].position_x
            y = self.shapes[-1][0].position_y
            
            if x < 1:
                x = 1
            
            self.shapes[-1][0].position_x = x
            self.shapes[-1][0].position_y = y
            self.shapes[-1][1].position_x = x - 1
            self.shapes[-1][1].position_y = y - 1 
            self.shapes[-1][2].position_x = x 
            self.shapes[-1][2].position_y = y - 1
            self.shapes[-1][3].position_x = x + 1
            self.shapes[-1][3].position_y = y - 1
            
            self.shapes[-1][0].version = 4
            
        elif self.shapes[-1][0].brick == "E" and self.shapes[-1][0].version == 4:
            x = self.shapes[-1][0].position_x
            y = self.shapes[-1][0].position_y
            
            self.shapes[-1][0].position_x = x
            self.shapes[-1][0].position_y = y
            self.shapes[-1][1].position_x = x - 1
            self.shapes[-1][1].position_y = y - 1 
            self.shapes[-1][2].position_x = x - 1
            self.shapes[-1][2].position_y = y
            self.shapes[-1][3].position_x = x - 1
            self.shapes[-1][3].position_y = y + 1
            
            self.shapes[-1][0].version = 1
      
        
    def fall(self, dt):
        self.time += dt
        
        if self.time >= self.game_speed:
            self.time = 0
            for i in self.shapes[-1]:
                i.position_y -= 1  
                
                
    def size_change(self, window_width):
        self.unit = window_width / 10
        
        for i in self.shapes:
            for j in i:
                j.pos = (j.position_x * self.unit, j.position_y * self.unit)
                j.size = (self.unit, self.unit) 
    
    
    def collisions_bottom(self):
        for i in self.shapes[0:-1]:
            for j in i:
                for k in self.shapes[-1]:
                    if j.position_y + 1 == k.position_y and j.position_x == k.position_x:
                        for j in self.shapes[-1]:
                            j.active = False
        for i in self.shapes[-1]:
            if i.active == True:                        
                if i.position_y == 0:
                    for j in self.shapes[-1]:
                        j.active = False                 
            else:
                self.new_shape()
                self.delete_row()
                return True
    
    
    def collisions_right(self):
        for i in self.shapes[-1]:
            if i.position_x == 9:
                return True
            for j in self.shapes[0:-1]:
                for k in j:
                    if i.position_x + 1 == k.position_x and i.position_y == k.position_y:
                        return True
        return False
    
    
    def collisions_left(self):
        for i in self.shapes[-1]:
            if i.position_x == 0:
                return True
            for j in self.shapes[0:-1]:
                for k in j:
                    if i.position_x - 1 == k.position_x and i.position_y == k.position_y:
                        return True
        return False
             
    
    def move_right(self):
        if not self.collisions_right():
            for i in self.shapes[-1]:
                i.position_x += 1
                
                
    def move_left(self):
        if not self.collisions_left():
            for i in self.shapes[-1]:
                i.position_x -= 1
    
    
    def delete_row(self):
        rows = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        
        for i in self.shapes[0:-1]:
            for j in i: 
                rows[j.position_y] += 1
        
        for i in range(20):
            if rows[i] == 10:
                for j in self.shapes[0:-1]:
                    for k in j: 
                        if k.position_y == i:
                            self.canvas.remove(k)
                            j.remove(k)
                for j in self.shapes[0:-1]:
                    for k in j: 
                        if k.position_y == i:
                            self.canvas.remove(k)
                            j.remove(k)
                for j in self.shapes[0:-1]:
                    for k in j: 
                        if k.position_y == i:
                            self.canvas.remove(k)
                            j.remove(k)
                for j in self.shapes[0:-1]:
                    for k in j: 
                        if k.position_y == i:
                            self.canvas.remove(k)
                            j.remove(k)
                        elif k.position_y > i:
                            k.position_y -= 1
                self.delete_row()
                    
                
    def new_shape(self): 
        shape = []
         
        with self.canvas:      
            if self.r == 1:
                Color(0, 0.25, 0.3)
                shape.append(Shape(4, 20, "I", 1, size = (0, 0)))
                shape.append(Shape(4, 21, "I", 1, size = (0, 0)))
                shape.append(Shape(4, 22, "I", 1, size = (0, 0)))
                shape.append(Shape(4, 23, "I", 1, size = (0, 0)))
            elif self.r == 2:
                Color(1, 0.5, 0)
                shape.append(Shape(4, 20, "O", 1, size = (0, 0)))
                shape.append(Shape(5, 20, "O", 1, size = (0, 0)))
                shape.append(Shape(4, 21, "O", 1, size = (0, 0)))
                shape.append(Shape(5, 21, "O", 1, size = (0, 0)))
            elif self.r == 3:
                Color(0.5, 0.7, 0.5)
                shape.append(Shape(4, 20, "L", 1, size = (0, 0)))
                shape.append(Shape(4, 21, "L", 1, size = (0, 0)))
                shape.append(Shape(4, 22, "L", 1, size = (0, 0)))
                shape.append(Shape(5, 20, "L", 1, size = (0, 0)))
            elif self.r == 4:
                Color(0.95, 0.35, 0.5)
                shape.append(Shape(4, 20, "J", 1, size = (0, 0)))
                shape.append(Shape(5, 20, "J", 1, size = (0, 0)))
                shape.append(Shape(5, 21, "J", 1, size = (0, 0)))
                shape.append(Shape(5, 22, "J", 1, size = (0, 0)))
            elif self.r == 5:
                Color(0.45, 0.2, 0.5)
                shape.append(Shape(4, 20, "Z", 1, size = (0, 0)))
                shape.append(Shape(5, 20, "Z", 1, size = (0, 0)))
                shape.append(Shape(5, 21, "Z", 1, size = (0, 0)))
                shape.append(Shape(6, 21, "Z", 1, size = (0, 0)))
            elif self.r == 6:
                Color(0.9, 0.75, 0.2)
                shape.append(Shape(4, 20, "S", 1, size = (0, 0)))
                shape.append(Shape(4, 21, "S", 1, size = (0, 0)))
                shape.append(Shape(5, 21, "S", 1, size = (0, 0)))
                shape.append(Shape(5, 22, "S", 1, size = (0, 0)))
            else:
                Color(1, 0.35, 0.3)
                shape.append(Shape(4, 20, "E", 1, size = (0, 0)))
                shape.append(Shape(4, 21, "E", 1, size = (0, 0)))
                shape.append(Shape(4, 22, "E", 1, size = (0, 0)))
                shape.append(Shape(5, 21, "E", 1, size = (0, 0)))
            
        self.shapes.append(shape)
    
        self.r = random.randint(1, 7)             
        
    
class Shape(Rectangle):
    position_x = 0
    position_y = 0
    active = True
    brick = ""
    version = 1
    
    def __init__(self, position_x, position_y, brick, version, **kwargs):
        super().__init__(**kwargs)
        
        self.position_x = position_x
        self.position_y = position_y
        self.brick = brick
        self.version = version
      
    
class App(BoxLayout):
    points = 0
    game_over_state = False
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.orientation = 'horizontal'
        
        self._keyboard = Window.request_keyboard(self.keyboard_closed, self)
        self._keyboard.bind(on_key_down = self.on_key_down)
        self._keyboard.bind(on_key_up = self.on_key_up)
        
        self.tetris = TetrisWidget()
        self.panel = Panel()
        
        self.add_widget(self.tetris)
        self.add_widget(self.panel)
        
        Clock.schedule_interval(self.update, 1/120)


    def on_key_down(self, keyboard, keycode, text, modifiers):
        if keycode[1] == "left":
            self.tetris.move_left()
        if keycode[1] == "right":
            self.tetris.move_right()
        if keycode[1] == "up":
            self.tetris.rotate()
        if keycode[1] == "down":
            self.tetris.game_speed = 0.1
        return True
    
    
    def on_key_up(self, keyboard, keycode):
        if keycode[1] == "down":
            self.tetris.game_speed = 0.5
        return True
    
    
    def keyboard_closed(self):
        self._keyboard.unbind(on_key_down = self.on_key_down)
        self._keyboard.unbind(on_key_up = self.on_key_up)
        self._keyboard = None
    

    def update(self, dt):
        if not self.game_over_state:
            if self.tetris.game_speed == 0.1:
                self.points += 1
            
            self.panel.points.text = str(self.points)
            
            self.tetris.update_game(self.tetris.width, dt) 
            self.panel.update(self.tetris.r)  
            self.is_over()   
        

    def is_over(self):
        if not self.game_over_state:
            for i in self.tetris.shapes:
                for j in i:
                    if j.position_y > 20 and j.active == False:   
                        self.game_over_state = True
                        
                        self.game_over = GameOver()
                        
                        self.add_widget(self.game_over)
                        
                        self.panel.seg1.size = (0, 0)
                        self.panel.seg2.size = (0, 0)
                        self.panel.seg3.size = (0, 0)
                        self.panel.seg4.size = (0, 0)
                        break
                    
    
    def new_game(self):
        self.remove_widget(self.game_over)
        self.tetris.clear_widgets()
        self.tetris.shapes.clear()
        self.tetris.canvas.clear()
        self.tetris.__init__() 
        
        self.game_over_state = False
        self.points = 0

    
KivyTetrisApp().run()