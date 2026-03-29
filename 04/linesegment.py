class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"


class LineSegment:
    def __init__(self, *args):
        # TH1: Không đối số → mặc định d1(8,5), d2(1,0)
        if len(args) == 0:
            self.__d1 = Point(8, 5)
            self.__d2 = Point(1, 0)

        elif len(args) == 2 and isinstance(args[0], Point) and isinstance(args[1], Point):
            self.__d1 = args[0]
            self.__d2 = args[1]

        elif len(args) == 4:
            x1, y1, x2, y2 = args
            self.__d1 = Point(x1, y1)
            self.__d2 = Point(x2, y2)

        elif len(args) == 1 and isinstance(args[0], LineSegment):
            other = args[0]
            self.__d1 = Point(other.__d1.x, other.__d1.y)
            self.__d2 = Point(other.__d2.x, other.__d2.y)

        else:
            raise ValueError("Tham số không hợp lệ")

    def __repr__(self):
        return f"LineSegment({self.__d1}, {self.__d2})"

    # Getter (nếu cần truy cập)
    def get_d1(self):
        return self.__d1

    def get_d2(self):
        return self.__d2
