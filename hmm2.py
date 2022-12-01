from la import *
import math


def argmax(l):
    return l.index(max(l))


tran = parse_matrix_from_line()
emis = parse_matrix_from_line()
init = parse_matrix_from_line()
seq = list(map(int, input().split()[1:]))

d_mat = Matrix(len(seq), init.cols)
d_idx_mat = Matrix(len(seq), init.cols)
n_states = init.cols

for i in range(n_states):
    d_mat[0][i] = init[0][i] * emis[i][seq[0]]

for t in range(1, len(seq)):
    for i in range(n_states):
        d_mat[t][i] = max([ tran[j][i]*d_mat[t-1][j]*emis[i][seq[t]] for j in range(n_states) ])
        d_idx_mat[t][i] = argmax([ tran[j][i]*d_mat[t-1][j]*emis[i][seq[t]] for j in range(n_states) ])

out = []
out.append(argmax(d_mat[-1]))
for t in reversed(range(len(seq)-1)):
    out.append(d_idx_mat[t+1][out[-1]])

print(*list(reversed(out)))
