import turtle


def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)


def draw_koch_snowflake(order, size=300):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-size / 2, 0)
    t.pendown()

    # draw three sides of the triangle
    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)  # turn right to make the triangle

    window.mainloop()


if __name__ == "__main__":
    draw_koch_snowflake(6)
