import numpy as np
import plotsettings as plts

x = np.arange(-np.pi, np.pi, 0.01)
fig, ax = plts.set("APS", left=0.17)
for idx in range(5):
    ax.plot(x, np.sin(x + idx), label=r"$i = %.f$" % idx)
ax.set_xlabel(r"$\theta$")
ax.set_ylabel(r"$\sin(\theta + i)$")
ax.legend(loc="upper left")
ax.grid()
fig.savefig("../figs/APS.pdf")

fig, ax = plts.set("APS", fig_type="twocol", left=0.1)
for idx in range(5):
    ax.plot(x, np.sin(x + idx), label=r"$i = %.f$" % idx)
ax.set_xlabel(r"$\theta$")
ax.set_ylabel(r"$\sin(\theta + i)$")
ax.legend(loc="upper left")
ax.grid()
fig.savefig("../figs/APS_twocol.pdf")
