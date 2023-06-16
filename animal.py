from tkinter import*

window = Tk()
window.geometry = ('800x500')
canvas = Canvas(window,width=800,height=500,bg='white')
canvas.pack()

class Animal:
    def __init__(self,animal_color):
        self.animal_color = animal_color
        self.height = 200
        self.width = 20
        self.animal = None

    def create_neck(self,x,y):
        h = self.height
        w = self.width
        self_neck = canvas.create_rectangle (x+20,y,x+50,y+200,fill=self.animal_color,outline='')

    def create_body(self,x,y):
         h = self.height
         w = self.width
         self_body = canvas.create_rectangle (x+20,y,x+200,y+50,fill=self.animal_color,outline='')

    def create_leg_1(self,x,y):
         h = self.height
         w = self.width
         self_leg_1 =canvas.create_rectangle(x+20,y,x+50,y+110,fill=self.animal_color,outline='')

    def create_leg_2(self,x,y):
         h = self.height
         w = self.width
         self_leg_2 =canvas.create_rectangle(x+20,y,x+50,y+110,fill=self.animal_color,outline='')

    def create_head(self,x,y):
         h = self.height
         w = self.width
         self_head=canvas.create_polygon(x-30,y+5,x+w,y,x+w/2,h-140,fill=self.animal_color,outline='')

    def create_ear(self,x,y):
         h = self.height
         w = self.width
         self_ear=canvas.create_polygon(x,y,x+w,y,x+w/2,h-175,fill=self.animal_color,outline='')
         
    def create_spot_1(self,x,y):
         h = self.height
         w = self.width
         self_spot_1=canvas.create_rectangle(x+15,y,x,y+15,fill=self.animal_color,outline='')

    def create_spot_2(self,x,y):
         h = self.height
         w = self.width
         self_spot_2=canvas.create_rectangle(x+15,y,x,y+15,fill=self.animal_color,outline='')

    def create_spot_3(self,x,y):
         h = self.height
         w = self.width
         self_spot_3=canvas.create_rectangle(x+15,y,x,y+15,fill=self.animal_color,outline='')

    def create_spot_4(self,x,y):
         h = self.height
         w = self.width
         self_spot_4=canvas.create_rectangle(x+15,y,x,y+15,fill=self.animal_color,outline='')

    def create_spot_5(self,x,y):
         h = self.height
         w = self.width
         self_spot_5=canvas.create_rectangle(x+15,y,x,y+15,fill=self.animal_color,outline='')

    def create_spot_6(self,x,y):
         h = self.height
         w = self.width
         self_spot_6=canvas.create_rectangle(x+15,y,x,y+15,fill=self.animal_color,outline='')

    def create_spot_7(self,x,y):
         h = self.height
         w = self.width
         self_spot_7=canvas.create_rectangle(x+15,y,x,y+15,fill=self.animal_color,outline='')

    def create_spot_8(self,x,y):
         h = self.height
         w = self.width
         self_spot_8=canvas.create_rectangle(x+15,y,x,y+15,fill=self.animal_color,outline='')
              
animal_neck = Animal('yellow')
animal_body = Animal('yellow')
animal_leg_1 = Animal('yellow')
animal_leg_2 = Animal('yellow')
animal_head = Animal('yellow')
animal_ear=Animal('goldenrod3')
animal_spot_2=Animal('goldenrod3')
animal_spot_1=Animal('goldenrod3')
animal_spot_3=Animal('goldenrod3')
animal_spot_4=Animal('goldenrod3')
animal_spot_5=Animal('goldenrod3')
animal_spot_6=Animal('goldenrod3')
animal_spot_7=Animal('goldenrod3')
animal_spot_8=Animal('goldenrod3')
animal_neck.create_neck(50,60)
animal_body.create_body(50,210)
animal_leg_1.create_leg_1(70,210)
animal_leg_2.create_leg_2(175,210)
animal_head.create_head(60,95)
animal_ear.create_ear(80,60)
animal_spot_1.create_spot_1(80,90)
animal_spot_2.create_spot_2(75,130)
animal_spot_3.create_spot_3(80,175)
animal_spot_4.create_spot_4(85,220)
animal_spot_5.create_spot_5(100,265)
animal_spot_6.create_spot_6(155,230)
animal_spot_7.create_spot_7(195,265)
animal_spot_8.create_spot_8(225,225)

window.mainloop()
