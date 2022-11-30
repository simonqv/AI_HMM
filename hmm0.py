from la import *

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

if __name__ == "__main__":
    tran = parse_matrix_from_line()
    emis = parse_matrix_from_line()
    init = parse_matrix_from_line()
    # print(tran)
    # print(emis)
    # print(init)
    out = init * (tran * emis)
    # print(out)
    output_matrix(out)
