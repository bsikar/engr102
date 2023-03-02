"""
A simple module to help make games with turtle graphics.
"""

import turtle


class TurtleGame(turtle._Screen):
    """A class to help draw with turtle graphics."""

    def __init__(
        self,
        width: int,
        height: int,
        background: str = "white",
        title: str = "Turtle Game",
    ) -> None:
        """Initialize the screen."""
        self.screen = turtle.Screen()
        self.screen.setup(width, height)
        self.screen.title(title)
        self.screen.setworldcoordinates(5, height, width, 5)
        self.screen.tracer(0)
        self.screen.bgcolor(background)
        self.bgcolor = background
        self.mouse_click_pos = None
        self.screen.cv._rootwindow.resizable(False, False)
        self.screen.cv._rootwindow.wm_attributes("-topmost", 1)

    def update(self) -> None:
        """Update the screen."""
        self.mouse_click_pos = None
        self.get_mouse_click_pos()
        self.screen.update()

    def get_mouse_click_pos(self) -> tuple:
        """Get the position of the mouse when clicked."""
        self._mouse_click_pos()
        return self.mouse_click_pos

    def _mouse_click_pos(self) -> None:
        """Update the mouse click position variable."""
        ws = self.screen.getcanvas()

        def helper_mouse_click_pos(event):
            self.mouse_click_pos = (event.x, event.y)

        ws.bind("<Button-1>", helper_mouse_click_pos)

    def make_grid(
        self,
        rows: int,
        columns: int,
        width: int,
        height: int,
        color: str = "black",
        thickness: int = 1,
    ) -> None:
        """Draw a grid on the screen."""
        row_size = height / rows
        column_size = width / columns
        for i in range(rows + 1):
            self.draw_line(
                0, i * row_size, width, i * row_size, color=color, width=thickness
            )
        for i in range(columns + 1):
            self.draw_line(
                i * column_size,
                0,
                i * column_size,
                height,
                color=color,
                width=thickness,
            )

    def make_circle_grid(
        self,
        rows: int,
        columns: int,
        width: int,
        height: int,
        color: str = "black",
        thickness: int = 1,
        filled: bool = True,
    ) -> None:
        """Draw a grid of circles on the screen."""
        row_size = height / rows
        column_size = width / columns
        radius = min(row_size, column_size) / 2
        for i in range(rows):
            for j in range(columns):
                self.draw_circle(
                    j * column_size + column_size / 2,
                    i * row_size,
                    radius,
                    color,
                    thickness,
                    filled,
                )

    def draw_line(
        self, x1: int, y1: int, x2: int, y2: int, color: str = "black", width: int = 1
    ) -> None:
        """Draw a line on the screen."""
        line = turtle.Turtle()
        line.hideturtle()
        line.penup()
        line.goto(x1, y1)
        line.pendown()
        line.color(color)
        line.width(width)
        line.goto(x2, y2)
        line.penup()
        line.goto(0, 0)

    def draw_circle(
        self,
        x: int,
        y: int,
        radius: int,
        color: str = "black",
        thickness: int = 1,
        filled: bool = True,
    ) -> None:
        """Draw a circle on the screen."""
        circle = turtle.Turtle()
        circle.hideturtle()
        circle.penup()
        circle.goto(x, y)
        circle.pendown()
        circle.color(color)
        circle.width(thickness)
        if filled:
            circle.begin_fill()
        circle.circle(radius)
        if filled:
            circle.end_fill()
        circle.penup()
        circle.goto(0, 0)

    def draw_rectangle(
        self,
        x: int,
        y: int,
        width: int,
        height: int,
        color: str = "black",
        thickness: int = 1,
        filled: bool = True,
    ) -> None:
        """Draw a rectangle on the screen."""
        rectangle = turtle.Turtle()
        rectangle.hideturtle()
        rectangle.penup()
        rectangle.goto(x, y)
        rectangle.pendown()
        rectangle.color(color)
        rectangle.width(thickness)
        if filled:
            rectangle.begin_fill()
        rectangle.goto(width, y)
        rectangle.goto(width, height)
        rectangle.goto(x, height)
        rectangle.goto(x, y)
        if filled:
            rectangle.end_fill()
        rectangle.penup()
        rectangle.goto(0, 0)

    def draw_square(
        self,
        size: int,
        x: int,
        y: int,
        color: str = "black",
        thickness: int = 1,
        filled: bool = True,
    ) -> None:
        """Draw a square on the screen."""
        self.draw_rectangle(x, y, x + size, y + size, color, thickness, filled)

    def draw_text(
        self,
        text: str,
        x: int,
        y: int,
        color: str = "black",
        font: str = "Arial",
        size: int = 12,
        align: str = "center",
    ) -> None:
        """Draw text on the screen."""
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(x, y)
        t.color(color)
        t.write(text, font=(font, size, "normal"), align=align)
        t.penup()
        t.goto(0, 0)

    def clear(self):
        """Clears the screen."""
        # XXX : this is a hack to clear the screen, its not the best way to do it
        self.draw_rectangle(
            0, 0, self.screen.window_width(), self.screen.window_height(), self.bgcolor
        )
