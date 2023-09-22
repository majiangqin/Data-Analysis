import numpy as np


def calculate(alist):
    if len(alist) >= 9:
        calculations = {}
        alist = np.array(alist)
        alist = alist.reshape(3, 3)
        calculations['mean'] = []
        mean1 = list(np.mean(alist, axis=0))
        calculations['mean'].append(mean1)
        mean2 = list(np.mean(alist, axis=1))
        calculations['mean'].append(mean2)
        mean3 = np.mean(alist)
        calculations['mean'].append(mean3)

        calculations['variance'] = []
        var1 = list(np.var(alist, axis=0))
        calculations['variance'].append(var1)
        var2 = list(np.var(alist, axis=1))
        calculations['variance'].append(var2)
        var3 = np.var(alist)
        calculations['variance'].append(var3)

        calculations['standard deviation'] = []
        std1 = list(np.std(alist, axis=0))
        calculations['standard deviation'].append(std1)
        std2 = list(np.std(alist, axis=1))
        calculations['standard deviation'].append(std2)
        std3 = np.std(alist)
        calculations['standard deviation'].append(std3)

        calculations['max'] = []
        max1 = list(np.max(alist, axis=0))
        calculations['max'].append(max1)
        max2 = list(np.max(alist, axis=1))
        calculations['max'].append(max2)
        max3 = np.max(alist)
        calculations['max'].append(max3)

        calculations['min'] = []
        min1 = list(np.min(alist, axis=0))
        calculations['min'].append(min1)
        min2 = list(np.min(alist, axis=1))
        calculations['min'].append(min2)
        min3 = np.min(alist)
        calculations['min'].append(min3)

        calculations['sum'] = []
        sum1 = list(np.sum(alist, axis=0))
        calculations['sum'].append(sum1)
        sum2 = list(np.sum(alist, axis=1))
        calculations['sum'].append(sum2)
        sum3 = np.sum(alist)
        calculations['sum'].append(sum3)

        return calculations
    else:
        raise ValueError("List must contain nine numbers.")
