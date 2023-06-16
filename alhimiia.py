from tkinter import*
from random import randint

window=Tk()
window.geometry('600x600')

class Fire:
    image=PhotoImage(file='C:\\Users\\alena\\Desktop\\snake\\fire.png')

    def __add__(self,Earth):
        return Clay
    
class Clay:
    image=PhotoImage(file='C:\\Users\\alena\\Desktop\\snake\\clay.png')
                     
class Water:
    image=PhotoImage(file='C:\\Users\\alena\\Desktop\\snake\\water.png')
    
class Earth:
    image=PhotoImage(file='C:\\Users\\alena\\Desktop\\snake\\earth.png')

    def __add__(self,Fire):
        return Clay
    
class Wind:
    image=PhotoImage(file='C:\\Users\\alena\\Desktop\\snake\\wind.png')

canvas=Canvas(window,width=600,height=600)
canvas.pack()

elements=[Fire(),Earth(),Water(),Wind()]

for i in elements:
    img=canvas.create_image(randint(50,550),randint(50,550),image=i.image)
def move(event):
    img_id=canvas.find_overlapping(event.x,event.y,event.x+10,event.y+10)

    if len(images_id)==2:
       i_id_1,i_id_1=images_id[0],images_id[1]
       elem_1=elements[i_id_1 - 1]
       elem_2=elements[i_id_2 - 1]

       new_element=elem_1+elem_2
       if new_elem:
          if new_elem not in elements:
            canvas.create-image(event.x,event.y,image=new_elem.image)
            elements.append(new_elem)
           
canvas.coords(img_id,event.x,event.y)


window.bind('<B1-Motion>',move)
window.mainloop()
