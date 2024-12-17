class ComplexNumber:
    __re = 0
    __img = 0

    def __init__(self, real_part=0.0, img_part=0.0):
        self.re = real_part
        self.img = img_part

    def __repr__(self):
        return f"ComplexNumber(re={self.re}, img={self.img}"

    def __str__(self):
        return f"{self.re} + {self.img}i"

    def __eq__(self, other):
        return self.re == other.re and self.img == other.img

    def __lt__(self, other):
        return self.re < other.re and self.img < other.img

    def __gt__(self, other):
        return self.re > other.re and self.img > other.img


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


if __name__ == '__main__':
    c1 = ComplexNumber(2,3)
    print(c1)           # prints __str__
    print([c1])         # prints __repr__


# python "mluvi" binarne, nevi jak vyprintovat citelne vystup, proto vyuziva
# metody __repr__ a __str__
