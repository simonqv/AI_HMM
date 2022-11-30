from la import *
import math

tran = parse_matrix_from_line()
emis = parse_matrix_from_line()
init = parse_matrix_from_line()

seq = list(map(int, input().split()[1:]))
print(seq)
print("-"*20)
ans = 1
for i, s in enumerate(seq):
    t = emis
    for _ in range(i+1):
        t *= t
    state_prob = init * t
    print(state_prob.data[0][s])
    ans *= state_prob.data[0][s]
print(ans)
