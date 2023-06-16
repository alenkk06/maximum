from tkinter import*

window = Tk()
window.geometry('800x600')

canvas = Canvas(window,width=800,height=600,bg='white')
canvas.pack()

#canvas.create_polygon(10,260,60,200,110,260, fill= 'blue',outline = '')
#canvas.create_rectangle(20,260,100,360, fill='yellow',outline='')
#canvas.create_rectangle(30,290,90,330,fill='pink',outline='')

class House:
    def __init__(self,roof_color, wall_color,number):
        self.number = number
        self.roof_color = roof_color
        self.wall_color = wall_color
        self.height = 200
        self.width = 220
        self.roof = None
        self.wall = None

    def build_house(self, x, y):
        h = self.height
        w = self.width

        self.roof = canvas.create_polygon(x,y,x+w,y,x + w/2,h-200, fill=self.roof_color,outline = '')
        self.wall = canvas.create_rectangle(x+30,y,x+190,y+150, fill=self.wall_color,outline='')
        
    def print_info(self):
        print('Дом номер:',str(self.number))
        print('Цвет крыши:',str(self.roof_color))
        print('Цвет стен:',str(self.wall_color))

house_1 = House('chocolate1','OliveDrab1',1)
house_2 = House('blue','red',2)
house_1.build_house(20,50)
house_2.build_house(300,50)

house_1.print_info()
house_2.print_info()
window.mainloop()
