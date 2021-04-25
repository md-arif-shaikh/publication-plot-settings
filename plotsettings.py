from matplotlib import rc
from cycler import cycler
import matplotlib.pyplot as plt

# Axes
rc("axes", linewidth=0.5)
rc("axes", edgecolor="gray")
rc("axes.spines", top=False)
rc("axes.spines", right=False)

# Lines
rc("lines", linewidth=2)
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
           "#8c564b", "#e377c2", "#7f7f7f"]  # , "#bcbd22", "#17becf"]
)

# https://jfly.uni-koeln.de/html/manuals/pdf/color_blind.pdf
easy_colors = cycler(
    color=["#E69F00", "#56B4E9", "#009E73",
           "#F0E442", "#0072B2", "#D55E00", "#C979A7", "#000000"]
)

line_style_cycler = cycler(
    linestyle=['solid', 'dashed', 'dotted', 'dashdot',
               (0, (3, 1, 1, 1, 1, 1)),
               (0, (3, 1, 1, 1)),  (0, (5, 1)), (0, (1, 1))])

rc("axes", prop_cycle=d3_catagory10 + line_style_cycler)


def set(journal="APS",
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
    # https://www.elsevier.com/authors/policies-and-guidelines/artwork-and-media-instructions/artwork-sizing
    # https://www.springer.com/authors/manuscript+guidelines?SGWID=0-40162-6-1414342-0
    # https://cdn.journals.aps.org/files/styleguide-pr.pdf
    onecol_height = 3
    # margins
    labelsizes = {"APS": 10.0,
                  "APJ": 8.0,
                  "Elsevier": 8.0,
                  "Springer": 8.0,
                  "Presentation": 8.0,
                  "Notebook": 12.0}
    fontsizes = {"APS": 10.0,
                 "APJ": 8.0,
                 "Elsevier": 8.0,
                 "Springer": 8.0,
                 "Presentation": 8.0,
                 "Notebook": 12.0}
    figsizes = {"APS": {"onecol": (3.4, onecol_height * nrows),
                        "twocol": (7.0, onecol_height * nrows)},
                "APJ": {"onecol": (3.543, onecol_height * nrows),
                        "twocol": (7.48, onecol_height * nrows)},
                "Elsevier": {"onecol": (3.543, onecol_height * nrows),
                             "twocol": (7.48, onecol_height * nrows)},
                "Springer": {"onecol": (3.3, onecol_height * nrows),
                             "twocol": (6.93, onecol_height * nrows)},
                "Presentation": {"onecol": (3, 2),
                                 "twocol": (4.5, 2)},
                "Notebook": {"onecol": (6, 4),
                             "twocol": (10, 4)}
                }
    journals = ["APS", "APJ", "Elsevier", "Springer", "Presentation",
                "Notebook"]
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
