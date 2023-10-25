import numpy as np
import matplotlib.pyplot as plt
xvals=np.arange(0,1,0.001)
def sHash(x):
    num=0
    charsX=str(x)
    for x in charsX:
        if x!=".":
            num+=int(x)
    return num
yvals=np.fromiter(map(sHash,xvals),float)
plt.scatter(xvals,yvals)
plt.title("simple hash")
plt.show()