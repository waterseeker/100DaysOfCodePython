import tkinter

# A Tkinter window is kind of like a turtle Screen
window = tkinter.Tk()
# you can change the title of the window like this...
window.title("My First GUI Program")
# the window will scale to include everything you put in it.
# but if you don't have much in the window and want it to be a certain size, you can set a minimum size
window.minsize(width=500, height=300)

# You can create components to put inside the window
# with tkinter, you have to create a component and then set it's position for it to show on the window
# to make a Label...
my_label = tkinter.Label(text="I Am a Label!", font=("Arial", 24, "bold"))
# the easiest way to position a component on the screen is to use pack()
# it will automatically center the component horizontally on the screen
# pack takes some optional parameters. One is expand.
# If you set this to True, it will center the component vertically too.
my_label.pack()

another_label = tkinter.Label(text="Some text", font=("Arial", 24, "bold"))
another_label.pack(side="left")
# you can change properties of the component by using dictionary syntax like...
another_label["text"] = "Changed Text"
# or by using the .config() method like...
another_label.config(text="Changed text again.")

# mainloop will keep the tkinter window on the screen, otherwise it is closed once there are no more instructions to
# run. This is sort of like how the exitonclick method on a turtle Screen works.
# The call to mainloop needs to be at the end of your program
window.mainloop()
