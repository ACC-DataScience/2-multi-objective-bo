import numpy as np
import torch
import random


def set_seeds(seed: int = 42):
    """Set random seeds for reproducibility."""
    np.random.seed(seed)
    torch.manual_seed(seed)
    random.seed(seed)


def measure_epoxy_old(EA, EB, EC, AA, AB, AC):
    """
    Synthetic objective function for estimating the tensile strength and glass transition
    temperature of a sustainable epoxy formulation.

    Parameters:
    -----------
    EA : float
        Weight fraction of epoxy resin E_A.
    EB : float
        Weight fraction of epoxy resin E_B.
    EC : float
        Weight fraction of epoxy resin E_C.
    AA : float
        Weight fraction of amine curing agent A_A.
    AB : float
        Weight fraction of amine curing agent A_B.
    AC : float
        Weight fraction of amine curing agent A_C.

    Returns:
    --------
    dict
        Dictionary with the estimated properties of the epoxy formulation
    """

    def gauss(x, mean, std):
        return np.exp(-(((x - mean) / std) ** 2))

    def wave(x, period, amplitude):
        return np.sin(2 * np.pi * x / period) * amplitude / 2 + amplitude / 2

    # first compute strength
    EA_eff = gauss(EA, 0.46, 0.12) + wave(EA, 0.5, 0.11)
    # EA_eff = gauss(EA, 0.46, 0.2) + wave(EA, 0.5, 0.05)
    EB_eff = gauss(EB, 0.22, 0.1) + wave(EB, 0.3, 0.05)
    EC_eff = gauss(EC, 0.04, 0.4) + wave(EC, 0.2, 0.05)

    AA_eff = gauss(AA, 0.16, 0.6) + wave(AA, 0.4, 0.05)
    AB_eff = gauss(AB, 0.05, 0.3) + wave(AB, 0.8, 0.05)
    AC_eff = gauss(AC, 0.09, 0.5) + wave(AC, 0.6, 0.05)

    strength = EA_eff * EB_eff * EC_eff * AA_eff * AB_eff * AC_eff

    # now compute the Tg
    EA_eff = gauss(EA, 0.64, 0.12) + wave(EA, 0.5, 0.05)
    EB_eff = gauss(EB, 0.01, 0.2) + wave(EB, 0.3, 0.05)
    EC_eff = gauss(EC, 0.12, 0.3) + wave(EC, 0.1, 0.05)

    AA_eff = gauss(AA, 0.05, 0.3) + wave(AA, 0.9, 0.05)
    AB_eff = gauss(AB, 0.08, 0.4) + wave(AB, 0.7, 0.05)
    AC_eff = gauss(AC, 0.1, 0.34) + wave(AC, 0.9, 0.05)

    glass_t = EA_eff * EB_eff * EC_eff * AA_eff * AB_eff * AC_eff

    return {"strength": strength * 57 + 63, "glass_t": glass_t * 36 + 75}


# def measure_epoxy(EA, EB, EC, AA, AB, AC):
#     """
#     Synthetic objective function for estimating the tensile strength and glass transition
#     temperature of a sustainable epoxy formulation.

#     Parameters:
#     -----------
#     EA : float
#         Weight fraction of epoxy resin E_A.
#     EB : float
#         Weight fraction of epoxy resin E_B.
#     EC : float
#         Weight fraction of epoxy resin E_C.
#     AA : float
#         Weight fraction of amine curing agent A_A.
#     AB : float
#         Weight fraction of amine curing agent A_B.
#     AC : float
#         Weight fraction of amine curing agent A_C.

#     Returns:
#     --------
#     dict
#         Dictionary with the estimated properties of the epoxy formulation
#     """

#     def gauss(x, mean, std):
#         return np.exp(-((x - mean) / std) ** 2)

#     def wave(x, period, amplitude):
#         return np.sin(2*np.pi*x/period) * amplitude/2 + amplitude/2

#     # first compute strength
#     EA_eff = gauss(EA, 0.46, 0.12) + gauss(EA, 0.9, 0.05) / 5 + gauss(EA, 0.1, 0.05) / 5
#     EB_eff = gauss(EB, 0.22, 0.09) + gauss(EB, 0.5, 1) / 5
#     EC_eff = gauss(EC, 0.04, 0.4) + gauss(EC, 0.9, 0.05) / 5

#     AA_eff = gauss(AA, 0.16, 0.6) + gauss(AA, 0.9, 0.1) / 5
#     AB_eff = gauss(AB, 0.05, 0.3) + gauss(AB, 0.8, 0.1) / 5
#     AC_eff = gauss(AC, 0.09, 0.5) + gauss(AC, 0.9, 0.1) / 5

#     strength = EA_eff * EB_eff * EC_eff * AA_eff * AB_eff * AC_eff

#     # now compute the Tg
#     EA_eff = gauss(EA, 0.64, 0.12) + gauss(EA, 0.1, 0.08) / 5
#     EB_eff = gauss(EB, 0.01, 0.2) + gauss(EB, 0.5, 1) / 5
#     EC_eff = gauss(EC, 0.12, 0.3) + gauss(EC, 0.8, 0.1) / 5

#     AA_eff = gauss(AA, 0.05, 0.3) + gauss(AA, 0.6, 0.08) / 5
#     AB_eff = gauss(AB, 0.08, 0.4) + gauss(AB, 0.8, 0.08) / 5
#     AC_eff = gauss(AC, 0.1, 0.34) + gauss(AC, 0.85, 0.2) / 5

#     glass_t = EA_eff * EB_eff * EC_eff * AA_eff * AB_eff * AC_eff

#     return {"strength": strength * 57 + 63, "glass_t": glass_t * 36 + 75}
