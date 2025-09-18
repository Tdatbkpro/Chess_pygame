class Move:
    def __init__(self, initial, final):
        self.initial = initial
        self.final = final

    def __str__(self):
        return f'({self.initial.row},{self.initial.col}) --> ({self.final.row}, {self.final.col})'
    
    def __eq__(self,orther):
        return self.initial == orther.initial and self.final == orther.final