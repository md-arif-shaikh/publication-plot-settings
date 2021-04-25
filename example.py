import numpy as np
import plotsettings as plts

x = np.arange(-np.pi, np.pi, 0.01)
fig, ax = plts.set("PRD")
for idx in range(5):
    ax.plot(x, np.sin(x + idx), label=r"$i = %.f$" % idx)
ax.set_xlabel(r"$\theta$")
ax.set_ylabel(r"$\sin(\theta + i)$")
ax.legend(loc="upper left")
ax.grid()
fig.savefig("./figs/PRD.pdf")
