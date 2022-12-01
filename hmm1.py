from la import *
import math

tran = parse_matrix_from_line()
emis = parse_matrix_from_line()
init = parse_matrix_from_line()
seq = list(map(int, input().split()[1:]))

a_mat = Matrix(len(seq), init.cols)
n_states = init.cols

for i in range(n_states):
    a_mat[0][i] = init[0][i] * emis[i][seq[0]]

for t in range(1, len(seq)):
    for i in range(n_states):
        t_prob = sum([ a_mat[t-1][j]*tran[j][i] for j in range(n_states)])
        a_mat[t][i] = t_prob * emis[i][seq[t]]

print(sum(a_mat[-1]))
