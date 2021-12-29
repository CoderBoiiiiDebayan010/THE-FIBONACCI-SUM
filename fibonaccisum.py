from tkinter import * 

root = Tk()

root.title("The Fibonacci Series")
root.geometry("400x500")

enter = Entry(root)
label_series = Label(root, text="Fibonacci Series :")
label_sum = Label(root)

def Fibonacci():
    input = int(enter.get())
    sum = 0
    sum2 = 0
    first_no = 0
    second_no = 1
    counter = 1
    while(counter <= input):
        label_series["text"] += str(sum) + " "
        label_sum["text"] = "The Fibonacci Sum" + str(sum2)
        counter += 1
        first_no = second_no
        second_no = sum
        sum = first_no + second_no
        sum2 = sum + sum2

btn = Button(root, text="Show the Fibonacci Series", command=Fibonacci, bg='Yellow', fg='Black')
 
btn.pack()
label_series.pack()
label_sum.pack()
enter.pack()

        

root.mainloop()