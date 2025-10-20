import time
current_seconds = time.time()
print(f"Current time in seconds since epoch: {current_seconds}")

def matvec_basic (A,x):
    result = []
    for row in A:
        s = 0
        for i in range(len(x)): 
            s += row[i] * x[i]
            result.append(s)
            return result
        current_seconds2 = time.time()
print(f"Current time in seconds since epoch: {current_seconds}")

def matvec_listcomp(A,x):
            return [sum(a*b for a, b in zip(row, x)) for row in A]
        
import numpy as np
def matvec_numpy(A,x):
            return np.dot(A,x)
current_seconds4 = time.time()
print(f"Current time in seconds since epoch: {current_seconds}")