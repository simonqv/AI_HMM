import math

class Matrix:
    def __init__(self, rows, cols, d=None):
        self.rows = rows
        self.cols = cols
        self.data = []
        for h in range(rows):
            self.data.append([])
            for w in range(cols):
                if d is None:
                    self.data[-1].append(0)
                else:
                    self.data[-1].append(d[h*cols + w])

    def __mul__(self, other):
        out = Matrix(self.rows, other.cols)
        for i in range(self.rows):
            for j in range(other.cols):
                for k in range(other.rows):
                    out.data[i][j] += self.data[i][k] * other.data[k][j]
        return out

    def __str__(self):
        out = ""
        for r in self.data:
            out += str(r) + "\n"
        return out


def parse_matrix_from_line():
    inp = input().split()
    h = int(inp[0])
    w = int(inp[1])
    a = Matrix(h, w, list(map(float, inp[2:])))
    return a

def output_matrix(m):
    print(m.rows, m.cols, end=" ")
    for r in m.data:
        print(*[round(e, 5) for e in r], end=" ")
    print()

