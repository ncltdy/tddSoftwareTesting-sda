class ComplexNumber:
    __re = 0
    __img = 0

    def __init__(self, real_part=0.0, img_part=0.0):
        self.re = real_part
        self.img = img_part

    def __eq__(self, other):
        return self.re == other.re and self.img == other.img

    def __lt__(self, other):
        pass

    def __gt__(self, other):
        pass

    @property
    def re(self):
        return self.__re

    @re.setter
    def re(self, real_part):
        if isinstance(real_part, int) or isinstance(real_part, float):
            self.__re = real_part
        else:
            raise Exception

    @property
    def img(self):
        return self.__img

    @img.setter
    def img(self, img_part):
        if isinstance(img_part, int) or isinstance(img_part, float):
            self.__img = img_part
        else:
            raise Exception