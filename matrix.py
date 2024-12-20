class Matrix:

    def __init__(self,matrix_):
        self.matrix_ = matrix_

    def __str__(self):
        result = ""
        for i in self.matrix_:
            for j in i:
                result += f"{j} "
            result += "\n"
        return result

    def __eq__(self, other):
        return self.matrix_ == other.matrix_

    def transpose(self):
        result = []
        for i in range(len(self.matrix_[0])):
            new_row = []
            for j in range(len(self.matrix_)):
                new_row.append(self.matrix_[j][i])
            result.append(new_row)
        return Matrix(result)

    def add(self,other):
        if len(self.matrix_) == len(other.matrix_) and len(self.matrix_[0]) == len(other.matrix_[0]):
            result = []
            for i in range(len(self.matrix_)):
                new_row = []
                for j in range(len(self.matrix_[0])):
                    new_row.append(self.matrix_[i][j] + other.matrix_[i][j])
                result.append(new_row)
            return Matrix(result)
        raise ValueError

    def minus(self,other):
        if len(self.matrix_) == len(other.matrix_) and len(self.matrix_[0]) == len(other.matrix_[0]):
            result = []
            for i in range(len(self.matrix_)):
                new_row = []
                for j in range(len(self.matrix_[0])):
                    new_row.append(self.matrix_[i][j] - other.matrix_[i][j])
                result.append(new_row)
            return Matrix(result)
        raise ValueError



if __name__ == "__main__":
    m1 = Matrix([[1,2,5,6],[3,4,6,7],[5,6,6,8]])
    m2 = Matrix([[1,2,5,6],[3,4,6,7],[5,6,6,8]])
    print(m1)

    print(m1.transpose())

    m3 = m1.add(m2)
    print(m3)

    m3 = m1.minus(m2)
    print(m3)