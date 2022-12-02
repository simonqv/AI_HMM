from la import *




tran = parse_matrix_from_line()
emis = parse_matrix_from_line()
init = parse_matrix_from_line()
seq = list(map(int, input().split()[1:]))

n_states = init.cols

a_mat = Matrix(len(seq), n_states)
beta_mat = Matrix(len(seq),n_states)


# Forward pass
for i in range(n_states):
    a_mat[0][i] = init[0][i] * emis[i][seq[0]]

for t in range(1, len(seq)):
    for i in range(n_states):
        t_prob = sum([ a_mat[t-1][j]*tran[j][i] for j in range(n_states)])
        a_mat[t][i] = t_prob * emis[i][seq[t]]

# Backwards pass
for i in range(n_states):
    beta_mat[-1][i] = 1

for t in reversed(range(len(seq)-1)):
    for i in range(n_states):
        beta_mat[t][i] = sum([beta_mat[t + 1][j] * emis[j][seq[t+1]] * tran[i][j] for j in range(n_states)])

di_gamma = [Matrix(n_states,n_states) for _ in range(len(seq))]

gamma = Matrix(len(seq),n_states)

sum_alpha = sum(a_mat[-1])
print(a_mat[-1])

for t in range(len(seq)-1):
    for i in range(n_states):
        for j in range(n_states):
            alpha = a_mat[t][i]
            a = tran[i][j]
            b = emis[j][seq[t+1]]
            beta = beta_mat[t+1][j]
            di_gamma[t][i][j] = (alpha*a*b*beta) / sum_alpha


        gamma[t][i] = sum(di_gamma[t][i])
    print(di_gamma[t])

for i in range(n_states):
    sum_gamma = sum([gamma[t][i] for t in range(len(seq))] )
    for j in range(n_states):
        sum_di_gamma = sum([di_gamma[t][i][j] for t in range(len(seq))])
        tran[i][j] = sum_di_gamma / sum_gamma



