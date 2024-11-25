import numpy as np
import matplotlib.pyplot as plt
for q in range(3):
    with open ("signal0"+str(q+1)+".dat","r") as f:
        x=np.array(f.read().split('\n'),dtype=np.float64)
        a=int(x.shape[0])
        y=np.arange(a,dtype=np.float64)
        plt.plot(y,x,label="raw signal",color="orange")
        for i in range(a):
            if i>8:
                s=(x[i-9:i+1].sum())
                y[i]=s/10
            else:
                s=(x[0:i+1].sum())
                y[i]=s/(i+1)
        x=np.arange(a,dtype=np.float64)
        plt.plot(x,y,label="after filter")
        plt.grid()
        plt.legend()
        plt.savefig(str(q+1)+".png")
        plt.show()

