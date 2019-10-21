class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def get_xy(self):
        return self.__x, self.__y

    def add(self, a, b):
        pt = Point(self.__x + a, self.__y + b)
        return pt


class Rectangle:
    def __init__(self, left_top, width, height):
        self.__left_top = left_top
        self.__right_bottom = left_top.add(width, height)

    def get(self):
        return self.__left_top, self.__right_bottom

    def get_lt(self):
        return self.__left_top
