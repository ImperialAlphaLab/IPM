
class point():

    #modification 20-mars :added spaces
    def __init__(self, *args):
        self.L = [0,0,0]
        self.Dim = 0
        for i, j in enumerate(args):
            self.L[i]=j
            self.Dim = i+1
        self.X = self.L[0]
        self.Y = self.L[1]
        self.Z = self.L[2]

    def _avx(self, value):
        self.L[0] += value
        self.X = self.L[0]

    def _avy(self, value):
        self.L[1] += value
        self.Y = self.L[1]

    def _avz(self, value):
        self.L[2] += value
        self.Z = self.L[2]
        
    def _xyz(self):
        return (self.L[0], self.L[1], self.L[2])

    def _dim(self):
        return self.Dim

    def _avi(self, i, value):
        self.L[i] += value
        self.X = self.L[0]
        self.Y = self.L[1]
        self.Z = self.L[2]
