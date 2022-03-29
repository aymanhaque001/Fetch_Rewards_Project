
# A seperate class for image. Stores the corner points and dimensions.

class image:
    def __init__(self, dim, cPnts):
        self.row = dim[0]
        self.column = dim[1]
        self.dimensions = [self.row, self.column]
        self.corner_points = cPnts

    def change_dimensions(self, c, v):
        self.rows, self.columns = c, v


# A seperate class for image generation

class ImageGeneration:
    def __init__(self, image):
        self.cPnts = image.corner_points
        self.row = image.row
        self.column = image.column

    def validate_corner_points(self):
        ValidityFlag = False
        Ref_x, Ref_y = self.cPnts[0][0], self.cPnts[0][1]
        Final_X, Final_y = float('-inf'), float('-inf')

        for i in range(1, len(self.cPnts)):
            if self.cPnts[i][0] == Ref_x and self.cPnts[i][1] != Ref_y:
                Final_y = self.cPnts[i][1]
            elif self.cPnts[i][1] == Ref_y and self.cPnts[i][0] != Ref_x:
                Final_X = self.cPnts[i][0]

        if (Final_X, Final_y) in set(self.cPnts):
            ValidityFlag = True

        if ValidityFlag == True:
            return True
        else:
            raise Exception(
                "Error : Invalid Coordinates for Corner Points. Try again!")

    def settingbounds(self):
        max_y = max([i[1] for i in self.cPnts])
        upperblock = []
        lowerblock = []

        for i in self.cPnts:
            if i[1] == max_y:
                upperblock.append(i)
            else:
                lowerblock.append(i)

        return upperblock, lowerblock

    def matrix_generation(self):
        print(self.row)
        if self.validate_corner_points() == True:
            up, low = self.settingbounds()
            x_inc = (abs(up[0][0] - up[1][0]) / (self.column-1))
            y_inc = (abs(up[0][1] - low[0][1]) / (self.row-1))
            x_inc = round(x_inc, 2)
            y_inc = round(y_inc, 2)

            solution = []

            x = up[0][0]
            y = up[0][1]

            for i in range(self.row):
                p = []
                for j in range(self.column):
                    p.append([x, y])
                    x = x + x_inc
                solution.append(p)
                y = y - y_inc
                x = up[0][0]

            return solution
