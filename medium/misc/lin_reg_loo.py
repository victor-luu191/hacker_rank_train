# You may do imports here
import numpy as np

def linearRegressionLoo(obs_A, obs_B):
    error_sum = 0.
    loo = lambda arr, idx: arr[:idx] + arr[(idx + 1):]
    n = len(obs_A)
    for i in range(n):
        A_train = loo(obs_A, i)
        B_train = loo(obs_B, i)
        mean_A = sum(A_train) / (n - 1.0)
        mean_B = sum(B_train) / (n - 1.0)

        slope = sum(np.multiply(A_train, np.subtract(B_train, mean_B))) / sum(
            np.multiply(A_train, np.subtract(A_train, mean_A)))

        intercept = mean_B - slope * mean_A
        pred_B = slope * obs_A[i] + intercept
        error_sum += (pred_B - obs_B[i])**2

    ans = error_sum / float(n)
    return ans

if __name__ == '__main__':
    x = [0,2,3]
    y = [1,2,1]

    print(linearRegressionLoo(x, y))
