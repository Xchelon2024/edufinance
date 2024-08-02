def get_grade(self):
        if self.total >= 80:
            return 'A'
        elif self.total >= 70:
            return 'B'
        elif self.total >= 60:
            return 'C'
        elif self.total >= 50:
            return 'D'
        else:
            return 'F'