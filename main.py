from graphics import Window, Line, Point


def main():
    win = Window(800, 600)
    line = Line(Point(50,50), Point(100,50))
    win.draw_line(line,'black')
    line = Line(Point(50,50), Point(50,100))
    win.draw_line(line,'black')
    win.wait_for_close()


if __name__ == "__main__":
    main()