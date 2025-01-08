# 2. Multi-objective BO: Optimizing Epoxy Formulations

Perform multi-objective optimization to simultaneously optimize tensile strength
and glass transition temperature of a sustainability-focused epoxy formulation.

##�� The Assignment

### 🎯 Task Context

Epoxy thermosets are of interest in many engineering applications for their high 
tensile strength and glass transition temperature (the temperature where a material 
becomes rubbery). However, many commercially available formulations rely on components
derived from fossil fuels that require chemically intensive refinement processes. In
this assignment, we will leverage Bayesian optimization to identify a sustainable 
epoxy formulation that balances the tradeoff between tensile strength and glass 
transition temperature.

### 🧪 Materials & Constraints

To facilitate the development of a new sustainable epoxy, you have selected three 
epoxy resins and three amine curing agents that are noted for being sourced from 
renewable feedstocks. These are organized in the table below which lists the compounds
and their respective bio-contents (a measure of sustainability).

| Component | Biocontent | Component Type | Description |
|-----------|------------|----------------|-------------|
| E_A       | 17         | Epoxy Resin    | Renewable source based |
| E_B       | 20         | Epoxy Resin    | Bio-derived |
| E_C       | 30         | Epoxy Resin    | High sustainability |
| A_A       | 10         | Amine Curing   | Standard curing agent |
| A_B       | 50         | Amine Curing   | High bio-content |
| A_C       | 25         | Amine Curing   | Medium sustainability |

Looking through the literature, you observe that most epoxy formulations are reported
with the sum of the weight fractions of epoxy components between 0.5 at the low end
and 0.95 at the highest. Additionally, as this is a formulation, you expect that the
weight fraction of all components must sum to 1.0.

#### Key Constraints:
- Total epoxy fraction: 0.5 ≤ Σ(E_A + E_B + E_C) ≤ 0.95
- Total mass balance: Σ(all components) = 1.0
- Experimental budget: 40 trials

Your task is to use Honegumi to develop an optimization script to help you identify a
set of pareto optimal parameters that balance the tradeoff between the tensile
strength and yield strength of an epoxy materail. Your experimental budget is
limited to 40 experiments. A synthetic objective function has been provided that will
serve as a proxy for real experimental measurements. The individual tasks for this assignment are listed below along with some helpful tips and guides for how to approach the problem.

### 📝 Detailed Tasks

#### **TASK A:** Use Honegumi to set up and run the optimization problem.

In this problem you are expected to use [Honegumi](https://honegumi.readthedocs.io/en/latest/) to generate a code template for this problem which you will then modify to meet the problem criteria. For some specific examples of this check out the [tutorials](https://honegumi.readthedocs.io/en/latest/tutorials.html) page on the Honegumi website.

> **Note:** In this assignment, we will be performing the optimization loop twice and have given the ax_client a unique name during the first part to differentiate it.

To complete this problem, you are given access to a synthetic objective function that will be used as a proxy for real experimental observations called `measure_epoxy()`, which is stored in the `./utils.py` file. This function takes in six variables: `E_A`, `E_B`, `E_C`, `A_A`, `A_B`, `A_C` and returns the measured tensile strenght and glass transition temperature of the epoxy. These are the parameters you should specify when setting up your optimization problem.

#### **TASK B:** Report solutions that maximize each individual objective.

Now that you have completed the optimization, you can visuaize the pareto optimal 
solutions using the visualization tools provided in Honegumi. Note that indiviual
objectives are maximized at either end of the pareto front. Assign the parameters for
the solution with the highest strength value as a dictionary to a variable named
`max_strength_params` and the parameters for the solution with the highest glass
transition temperature as a dictionary to a variable named `max_glass_t_params`. Next 
assign the maximum strength and maximum glass transition temperature found to a
variables named `max_strength` and `max_glass_t` respectively. Note that these are
expected to come from different points.

#### **TASK C:** Report the number of optimal solutions that meet sustainability targets.

First create a variable called `num_pareto_optimal` and assign the total number of 
solutions found on the pareto front to it. Next, create a variable called 
`num_pareto_sustainable` and assign the number of pareto solutions with a weighted
biocontent greater than 20 to it. The weighted biocontent is simply the sum of the 
biocontents of each component weighted by their mass fraction. 

Given an epoxy formulation and the biocontents given above. The biocontent of the formulation is calculated as:

### **TASK D:** Apply custom thresholds to the optimization problem.

In many scenarios, we have some notion of outcome constraints before running our 
optimization. For example, we might know that the application will demand glass 
transition temperature in excess of 85 C. We can directly specify this constraint in 
our multi-objective optimization problem to only target solutions that are predicted 
to be above this threshold. Use honegumi to devise a new script that applies a
threshold of 85 C to the glass transition temperature target and a threshold of 75 MPa
to the strength target. Keep the parameters and budget identical.

### **TASK E:** Report the number of optimal solutions that meet sustainability targets.

As in TASK C, report the number of pareto optimal solutions found with the new
outcome constraints and the number of those solutions that meet the sustainability
targets. Assign these values to the variables `num_pareto_optimal_thresh` and 
`num_pareto_sustainable_thresh` respectively.

### **TASK F:** Compute the tradeoff between strength and glass transition temperature.

Within the threshold of interest, how many degrees of glass transition temperature do 
we need to give up in order to increse our strength by 1 MPa? Assume that the pareto 
front is sufficiently linear in this region such that you can approximate the tradeoff
as the slope of a linear fit. Assign the tradeoff to a variable named `tradeoff`.

It is recommended to use a function in a python library for computing the linear regression coefficients here such as `scipy.stats.linregress()`.

## Setup command

See `postCreateCommand` from [`devcontainer.json`](.devcontainer/devcontainer.json).

## Run command
`pytest`

## Notes
- pip's install path is not included in the PATH var by default, so without installing via `sudo -H`, pytest would be unaccessible.
