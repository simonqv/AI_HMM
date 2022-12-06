from la import *
import sys


# Init variables
tran = parse_matrix_from_line()
emis = parse_matrix_from_line()
init = parse_matrix_from_line()
seq = list(map(int, input().split()[1:]))

n_states = init.cols

alpha_mat = Matrix(len(seq), n_states)
beta_mat = Matrix(len(seq),n_states)

di_gamma = [Matrix(n_states,n_states) for _ in range(len(seq))]
gamma = Matrix(len(seq),n_states)

scale = [0]*len(seq)


def alpha_pass():
    # Forward pass
    for i in range(n_states):
        alpha_mat[0][i] = init[0][i] * emis[i][seq[0]]
    scale[0] = 1/sum(alpha_mat[0])
    for i in range(n_states):
        alpha_mat[0][i] *= scale[0]

    for t in range(1, len(seq)):
        for i in range(n_states):
            t_prob = sum( alpha_mat[t-1][j]*tran[j][i] for j in range(n_states) )
            alpha_mat[t][i] = t_prob * emis[i][seq[t]]
        scale[t] = 1/sum(alpha_mat[t])
        for i in range(n_states):
            alpha_mat[t][i] *= scale[t]


def beta_pass():
    # Backwards pass
    for i in range(n_states):
        beta_mat[-1][i] = 1 * scale[-1]

    for t in reversed(range(len(seq)-1)):
        for i in range(n_states):
            beta_mat[t][i] = sum( beta_mat[t+1][j] * emis[j][seq[t+1]] * tran[i][j] for j in range(n_states) )
            beta_mat[t][i] *= scale[t]


def calc_gamma():
    sum_alpha = sum(alpha_mat[-1])  # Might be wrong
    for t in range(len(seq)-1):
        for i in range(n_states):
            gamma[t][i] = 0
            for j in range(n_states):
                alpha = alpha_mat[t][i]
                a = tran[i][j]
                b = emis[j][seq[t+1]]
                beta = beta_mat[t+1][j]
                di_gamma[t][i][j] = (alpha*a*b*beta) / sum_alpha
                gamma[t][i] += di_gamma[t][i][j]


def reestimate():
    # Reestimate transmission matrix
    # 2.35 typ
    for i in range(n_states):
        for j in range(n_states):
            sum_di_gamma = sum( di_gamma[t][i][j] for t in range(len(seq)) )
            sum_gamma = sum( gamma[t][i] for t in range(len(seq)) )
            tran[i][j] = sum_di_gamma / sum_gamma

    # Reestimate emission matrix
    # b estimates. 2.36
    for j in range(n_states):
        for k in range(emis.cols):

            sum_gamma_denominator = 0
            sum_gamma_numerator = 0

            for t in range(len(seq)):
                indicator = lambda _k: 1 if _k == seq[t] else 0

                sum_gamma_numerator += gamma[t][j]*indicator(k)
                sum_gamma_denominator += gamma[t][j]

            emis[j][k] = sum_gamma_numerator / sum_gamma_denominator

    # Reestimate initial probability matrix
    # new pi. 2.37
    for i in range(n_states):
        init[0][i] = gamma[0][i]


sum_scale = math.inf
iter = 0
while True:
    print("\r" + str(iter) + ": " + str(sum(scale)), end="", file=sys.stderr)
    iter+=1

    alpha_pass()
    beta_pass()
    calc_gamma()
    reestimate()

    new_sum_scale = sum(map(math.log, scale))
    if new_sum_scale+1e-3 >= sum_scale:
        break
    sum_scale = new_sum_scale

print("", file=sys.stderr)


output_matrix(tran)
output_matrix(emis)
