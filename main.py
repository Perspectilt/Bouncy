import tkinter
import res
import physics

# Basic stuff
root = tkinter.Tk()
root.geometry('1024x768')
canvas = tkinter.Canvas(root, width=1024, height=768)
root.title('Bouncy')

canvas.pack()

# Create a ball and a container
ball_1 = res.Ball(canvas, pos_x=100, pos_y=665, radius=50, mass=1)
container_1 = res.Container(canvas, pos_x=0, pos_y=0, width=1024, height=768)

# Add the object and the boundaries to their respective global lists
objects = [ball_1]
boundaries = [container_1]

# Applying gravity to all objects
physics.apply_gravity(objects)

for n in range(1000):         # <-- Temp measure
    physics.physics(root, objects, boundaries, log=True)        # Apply physics to objects and boundaries

# root.after(1, physics(root, objects, boundaries))         # The part that doesnt work :(
# root.mainloop()
