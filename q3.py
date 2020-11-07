# Hit the Target Game
import math
import turtle

# Named constants
SCREEN_WIDTH = 600  # Screen width
SCREEN_HEIGHT = 600  # Screen height

TARGET_CENTER_X = 100  # Target's center X
TARGET_CENTER_Y = 250  # Target's center Y
TARGET_RADIUS = 30  # radius of the target

PROJECTILE_SPEED = 1  # Projectile's animation speed

# Setup the window.
turtle.setup(SCREEN_WIDTH, SCREEN_HEIGHT)

pen = turtle.Pen()

# Draw the target.
pen.hideturtle()
pen.speed(0)
pen.penup()

# Centre to draw the circle (TARGET_CENTER_X, TARGET_CENTER_Y-TARGET_RADIUS)
pen.goto(TARGET_CENTER_X, TARGET_CENTER_Y-TARGET_RADIUS)
pen.pendown()
pen.circle(TARGET_RADIUS)
pen.penup()

while True:
    pen.hideturtle()
    pen.speed(0)
    pen.home()
    pen.showturtle()
    pen.speed(PROJECTILE_SPEED)
    angle = int(input("Enter the projectile's angle: "))
    if angle == -1: exit(0)
    distance = int(input("Enter the launch distance: "))
    if distance == -1: exit(0)

    # Set the heading.
    pen.setheading(angle)

    # Launch the projectile.
    pen.pendown()
    pen.forward(distance)

    xcor = pen.xcor()
    ycor = pen.ycor()

    # Check if target hit?
    distance_to_center = math.sqrt((xcor - TARGET_CENTER_X) ** 2 + (ycor - TARGET_CENTER_Y) ** 2)
    if distance_to_center <= TARGET_RADIUS:
        print ("Target hit!")
        exit(0)
    else:
        print("You missed the target. Try again!")