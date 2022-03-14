class Solution:
    def __init__(self):
        self.current_row = [1]
        self.triangle = []

    def generate(self, numRows: int):
        if numRows == 1 or (len(self.current_row) == 1 and numRows > 1):
            self.triangle.append(self.current_row.copy())
            self.current_row.append(1)
            if numRows == 1:
                return self.triangle
            else:
                return self.generate(numRows)
        elif numRows == 2 or (len(self.current_row) == 2 and numRows > 2):
            self.triangle.append(self.current_row.copy())
            self.current_row.insert(1, 2)
            if numRows == 2:
                return self.triangle
            else:
                return self.generate(numRows)
        elif len(self.current_row) <= numRows:
            self.triangle.append(self.current_row.copy())
            aux_row = self.current_row.copy()
            self.current_row = [1, 1]
            for i in range(1, len(aux_row)):
                self.current_row.insert(i, aux_row[i-1] + aux_row[i])
            return self.generate(numRows)
        else:
            return self.triangle

sol = Solution()
print(sol.generate(30))