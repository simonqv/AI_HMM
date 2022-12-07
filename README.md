# AI_HMM
## Question 1 This problem can be formulated in matrix form. Please specify the initial probability vector π, the transition probability matrix A and the observation probability matrix B.
π
```
0.5 0.5
```
A
```
0.5 0.5
0.5 0.5
```
B
```
0.9 0.1
0.5 0.5
```

## Question 2 What is the result of this operation?
Probability that we will do a certain transition.


## Question 3 What is the result of this operation?
Probability of us observing a certain state.


## Question 4 Why is it valid to substitute O1:t = o1:t with Ot = ot when we condition on the state Xt = xi?
Because we recursively compute alpha, each column is based on the column before it, and thus at time step t, we have already computed
the P(O1:t-1 | xi). For all states i.

## Question 5 How many values are stored in the matrices δ and δidx respectively?
Both are t*i. t is timesteps and i is number of states.

## Question 6 Why we do we need to divide by the sum over the final α values for the di-gamma function?
To prevent underflow.
