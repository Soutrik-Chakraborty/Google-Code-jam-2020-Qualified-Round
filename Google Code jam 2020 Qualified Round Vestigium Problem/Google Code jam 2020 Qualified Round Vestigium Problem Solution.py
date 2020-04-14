import numpy as np

t = int(input())
for i in range(1, t + 1):
    N = int(input())
    arr = [];
    r = 0;
    c = 0;
    for j in range(1, N + 1):
        tmp = [int(s) for s in input().split(" ")]
        if len(tmp) != len(set(tmp)):
            r = r + 1;
        arr.append(tmp)
    matrix = np.array(arr);
    trace = matrix.diagonal().sum();
    transpose = matrix.transpose();
    for j in range(0, N):
        if len(transpose[j]) != len(set(transpose[j])):
            c = c + 1;
    print("Case #{}: {} {} {}".format(i, trace, r, c))