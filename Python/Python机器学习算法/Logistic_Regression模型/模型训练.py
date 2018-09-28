def lr_train_bgd(feature, label, maxCycle, alpha):
    n = np.shape(feature)[1]
    w = np.mat(np.ones(n, 1))
    i = 0
    while i<= maxCycle:
        i += 1
        h = sig(feature * w)
        err = label - h
        if i % 100 == 0:
            print("\t---------iter=" + str(i) + ", train error reate= " + str(error_rate(h, label)))
        w = w + alpha * feature.T * err
    return w

def error_rate(h, label):
    m = np.shape(h)[0]

    sum_err = 0.0
    for i in xrange(m):
        if h[i, 0] > 0 and (1 - h[i,0]) > 0:
            sum_err -= (label[i,0] * np.log(h[i,0])) + (1-label[i,0]) * np.log(1-h[i,0])
        else:
            sum_err -= 0
    return sum_err

def main():

