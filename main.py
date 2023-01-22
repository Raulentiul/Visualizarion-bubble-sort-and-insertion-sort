from tkinter import *
import time

def main():
    ###we create the frame
    t = Tk()
    t.title('Visualization of Sorting Algorithms')
    t.geometry("1000x600")
    t.configure(bg='grey')
    frame = Frame(t)
    frame.pack(side=BOTTOM)

    ##this is where the animation time is programmed
    def tksleep(self, time: float) -> None:
        self.after(int(time * 1000), self.quit)
        self.mainloop()

    Misc.tksleep = tksleep

    def Bubblesort():

        ###we take the input from the text and convert it into a list of integers
        list = text_box.get(1.0, "end-1c")
        frame_list = Frame(t)
        list = list.split(" ")
        list = [int(i) for i in list]
        frame_list.pack()

        list_variables = []
        for i in range(len(list)):
            list_variables.append(StringVar(frame_list))

        ###here we create the buttons in which the numbers are written
        list_buttons = []
        for i in range(len(list)):
            list_buttons.append(Button(t, textvariable=list_variables[i], bg = "yellow",  height=4, width=8))
            list_buttons[i].pack(side = LEFT, expand=True)
            for i in range(len(list)):
                list_variables[i].set(str(list[i]))

        ##bubblesort
        for i in range(len(list)):
            for j in range(0, len(list) - i - 1):
                list_buttons[j].config(bg='blue')
                list_buttons[j + 1].config(bg='blue')
                t.tksleep(2)
                if list[j] > list[j + 1]:
                    list_buttons[j].config(bg='green')
                    list_buttons[j+1].config(bg='green')
                    list[j], list[j + 1] = list[j + 1], list[j]
                    t.tksleep(1)
                    list_variables[j].set(str(list[j]))
                    list_variables[j+1].set(str(list[j+1]))
                    list_buttons[j].config(bg='green')
                    list_buttons[j+1].config(bg='green')
                    t.tksleep(1)
                    list_buttons[j].config(bg='yellow')
                    list_buttons[j+1].config(bg='yellow')
                    t.tksleep(1)
                else:
                    list_buttons[j].config(bg='yellow')
                    list_buttons[j + 1].config(bg='yellow')


    def Insertionsort():

        ###we take the input from the text and convert it into a list of integers
        list = text_box.get(1.0, "end-1c")
        frame_list = Frame(t)
        list = list.split(" ")
        list = [int(i) for i in list]
        frame_list.pack()
        list_variables = []
        for i in range(len(list)):
            list_variables.append(StringVar(frame_list))

        ###here we create the buttons in which the numbers are written
        list_buttons = []
        for i in range(len(list)):
            list_buttons.append(Button(t, textvariable=list_variables[i], bg = "yellow",  height=4, width=8))
            list_buttons[i].pack(side = LEFT, expand=True)
        for i in range(len(list)):
            list_variables[i].set(str(list[i]))

        ##we assign a key
        for i in range(1, len(list)):
            key = list[i]
            j = i - 1

            for k in range(len(list)):
                if k == i or k == i + 1:
                    list_buttons[k].config(bg='blue')
                elif k <= j:
                    list_buttons[k].config(bg='green')
                else:
                    list_buttons[k].config(bg='yellow')

            t.tksleep(1)

            ###insertion
            while j >= 0 and key < list[j]:
                list[j+1] = list[j]
                for i in range (len(list)):
                    if i == j:
                        list_buttons[i].config(bg='pink')
                    elif i <= j:
                        list_buttons[i].config(bg='green')
                    else:
                        list_buttons[i].config(bg='yellow')
                j = j- 1
                t.tksleep(2)

            list[j+1] = key
            for i in range(len(list)):
                list_buttons[i].config(bg='yellow')

            t.tksleep(2)

            for i in range(len(list)):
                list_variables[i].set(str(list[i]))

            t.tksleep(3)

    ###here we add the buttons in the frame
    frame_buttons = Frame(t)
    frame_buttons.pack()
    button = Button(frame_buttons, text='Bubble sort', width=15, fg="black", bg='gray78', command=Bubblesort)
    button.pack(side=LEFT)
    button = Button(frame_buttons, text='Insertion sort', width=15, fg="black", bg='gray78', command=Insertionsort)
    button.pack(side=LEFT)

    ##here lies the Text frame
    text_box = Text(frame, height=4, width=50, bg='gray65', fg='black')
    text_box.pack(side=RIGHT)

    t.mainloop()

if __name__ == "__main__":
    main()



