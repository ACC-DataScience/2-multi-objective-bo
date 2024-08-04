# ======================================================================================
# ASSIGNMENT 2: Optimizing an Epoxy Formulation

# Your assignment is to use Honegumi to develop an optimization script to help you
# identify a set of pareto optimal parameters that balance the tradeoff between
# the tensile strength and yield strength of an epoxy materials. Your
# experimental budget is limited to 40 experiments. A synthetic objective
# function has been provided that will serve as a proxy for real experimental
# measurements. Refer to the README for specifics regarding each task.
# ======================================================================================

from utils import set_seeds, measure_epoxy_old

set_seeds()  # setting the random seed for reproducibility

# --------------------------------------------------------------------------------------
# TASK A: Use Honegumi to set up and run the optimization problem.
# --------------------------------------------------------------------------------------

import numpy as np
from ax.service.ax_client import AxClient, ObjectiveProperties

ax_client_full = AxClient(random_seed=42)  # ensure reproducibility

# TODO: Your Code Goes Here

# --------------------------------------------------------------------------------------
# TASK B: Report solutions that maximize each individual objective.
# --------------------------------------------------------------------------------------

# TODO: Your Code Goes Here

# --------------------------------------------------------------------------------------
# TASK C: Report the number of optimal solutions that meet sustainability targets.
# --------------------------------------------------------------------------------------

# TODO: Your Code Goes Here

# --------------------------------------------------------------------------------------
# TASK D: Apply custom thresholds to the optimization problem.
# --------------------------------------------------------------------------------------

import numpy as np
from ax.service.ax_client import AxClient, ObjectiveProperties

ax_client_thresh = AxClient(random_seed=42)  # ensure reproducibility

# TODO: Your Code Goes Here

# --------------------------------------------------------------------------------------
# TASK E: Report the number of optimal solutions that meet sustainability targets.
# --------------------------------------------------------------------------------------

# TODO: Your Code Goes Here

# --------------------------------------------------------------------------------------
# TASK F: Compute the tradeoff between strength and glass transition temperature.
# --------------------------------------------------------------------------------------

# TODO: Your Code Goes Here
