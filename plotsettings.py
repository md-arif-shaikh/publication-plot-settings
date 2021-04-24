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

# Ticks
rc("xtick", labelsize=8)
rc("ytick", labelsize=8)

# Legend
rc("legend", frameon=False)
rc("legend", loc="upper right")

# Grid
rc("grid", linestyle="solid")
rc("grid", linewidth=0.5)
rc("grid", alpha=0.5)

# TeX
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

# Figure size
# onecol_width = 4.2519699737097
# onecol_height = 2.627861962896592
onecol_width = 3.4  # (Phys Rev)
twocol_width = 7  # (Phys Rev)
onecol_height = 3
# margins
left_margin = 0.15  # / onecol_width
right_margin = 0.95  # / onecol_width
bottom_margin = 0.15  # / onecol_height
top_margin = 0.95  # / onecol_height
rc("figure.subplot", bottom=bottom_margin)
rc("figure.subplot", right=right_margin)
rc("figure.subplot", left=left_margin)
rc("figure.subplot", top=top_margin)


def set(journal="PRD",
        fig_type="onecol",
        nrows=1,
        ncols=1,
        sharex=False,
        sharey=False):
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

    rc("figure", figsize=figsizes[journal][fig_type])
    rc("axes", labelsize=labelsizes[journal])
    rc("axes", titlesize=labelsizes[journal])
    rc("legend", fontsize=fontsizes[journal])

    fig, ax = plt.subplots(nrows, ncols, sharex=sharex, sharey=sharey)
    return fig, ax
