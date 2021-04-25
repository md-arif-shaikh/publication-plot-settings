from matplotlib import rc
from cycler import cycler
import matplotlib.pyplot as plt

# Axes
rc("axes", linewidth=0.5)
rc("axes", edgecolor="gray")
rc("axes.spines", top=False)
rc("axes.spines", right=False)

# Lines
rc("lines", linewidth=1.25)
rc("lines", markersize=5)

# Legend
rc("legend", frameon=True)
rc("legend", loc="upper right")

# Grid
rc("grid", linestyle="solid")
rc("grid", linewidth=0.5)
rc("grid", alpha=0.5)

# LaTeX
rc("text.latex", preamble=r"\usepackage{txfonts}")
rc("text", usetex=True)

# Fonts
rc("font", family="serif")
rc("font", serif="times")

# color and line style cycle
solarized = cycler(
    color=["#2aa198", "#cb4b16", "#268bd2", "#859900", "#b58900",
           "#d33682", "#6c71c4"])
# https://colorbrewer2.org/#type=qualitative&scheme=Dark2&n=8
dark2 = cycler(
    color=['#1b9e77', '#d95f02', '#7570b3', '#e7298a', '#66a61e',
           '#e6ab02', '#a6761d', '#666666']
)
d3_catagory10 = cycler(
    color=["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd",
           "#8c564b", "#e377c2", "#7f7f7f", "#bcbd22", "#17becf"]
)
line_style_cycler = cycler(
    linestyle=['-', '--', ':', '-.',
               '-', '--', ':', '-.',
               '-', '--'])

rc("axes", prop_cycle=d3_catagory10 + line_style_cycler)


def set(journal="PRD",
        fig_type="onecol",
        nrows=1,
        ncols=1,
        sharex=False,
        sharey=False,
        left=0.15,
        bottom=0.15,
        right=0.95,
        top=0.95,
        wspace=0.0,
        hspace=0.0,
        figsize=None):
    # Figure size
    # onecol_width = 4.2519699737097
    # onecol_height = 2.627861962896592
    cm_to_inch = 1/2.54
    onecol_width = 9 * cm_to_inch
    twocol_width = 19 * cm_to_inch
    onecol_height = 3
    # margins
    labelsizes = {"PRD": 10.0,
                  "APJ": 8.0,
                  "Presentation": 8.0,
                  "Notebook": 12.0}
    fontsizes = {"PRD": 10.0,
                 "APJ": 8.0,
                 "Presentation": 8.0,
                 "Notebook": 12.0}
    figsizes = {"PRD": {"onecol": (onecol_width, onecol_height * nrows),
                        "twocol": (twocol_width, onecol_height * nrows)},
                "APJ": {"onecol": (onecol_width, onecol_height * nrows),
                        "twocol": (twocol_width, onecol_height * nrows)},
                "Presentation": {"onecol": (3, 2),
                                 "twocol": (4.5, 2)},
                "Notebook": {"onecol": (6, 4),
                             "twocol": (10, 4)}
                }
    journals = ["PRD", "APJ", "Presentation", "Notebook"]
    fig_types = ["onecol", "twocol"]
    if journal not in journals:
        print(f"--- Journal should be one of {journals} ---")
    if fig_type not in fig_types:
        print(f"--- fig_type should be one of {fig_types} ---")

    if figsize is None:
        rc("figure", figsize=figsizes[journal][fig_type])
    else:
        rc("figure", figsize=figsize)
    rc("axes", labelsize=labelsizes[journal])
    rc("axes", titlesize=labelsizes[journal])
    rc("xtick", labelsize=labelsizes[journal])
    rc("ytick", labelsize=labelsizes[journal])
    rc("legend", fontsize=fontsizes[journal])
    rc("figure.subplot", bottom=bottom)
    rc("figure.subplot", right=right)
    rc("figure.subplot", left=left)
    rc("figure.subplot", top=top)
    rc("figure.subplot", wspace=wspace)
    rc("figure.subplot", hspace=hspace)

    fig, ax = plt.subplots(nrows, ncols, sharex=sharex, sharey=sharey)
    return fig, ax
