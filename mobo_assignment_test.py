import os
import warnings
from utils import set_seeds, measure_epoxy_old
import numpy as np
from ax.service.ax_client import AxClient, ObjectiveProperties
import matplotlib.pyplot as plt
from ax.modelbridge.cross_validation import cross_validate, compute_diagnostics
from ax.core.observation import ObservationFeatures
import pytest


@pytest.fixture(scope="session")
def get_namespace():
    script_fname = "mobo_assignment.py"
    script_content = open(script_fname).read()

    namespace = {}
    exec(script_content, namespace)
    return namespace


def test_task_a(get_namespace):

    running_ax_client = get_namespace["ax_client_full"]
    user_op_params = running_ax_client.experiment.parameters

    # assert that len op_params is 4
    assert len(user_op_params) == 5, "Expected 5 parameters, got {}".format(
        len(user_op_params)
    )

    # assert that op_params contains ['time', 'temperature', 'v_prct', 'process']
    assert all(
        [param in ["EA", "EB", "EC", "AA", "AB"] for param in user_op_params]
    ), "Expected parameters named ['EA', 'EB'', 'EC', 'AA', 'AB''], got {}".format(
        user_op_params.keys()
    )

    # assert that the ax_client budget is 25
    assert (
        len(running_ax_client.get_trials_data_frame()) == 40
    ), "Expected optimization budget of 40 trials, got {}".format(
        len(running_ax_client.get_trials_data_frame())
    )


def test_task_b(get_namespace):

    user_max_strength = get_namespace["max_strength"]
    user_max_glass_t = get_namespace["max_glass_t"]

    # assert that max_strength is greater than 125
    assert user_max_strength > 125, "Expected max_strength > 125, got {}".format(
        user_max_strength
    )

    # assert that max_glass_t is greater than 110
    assert user_max_glass_t > 110, "Expected max_glass_t > 110, got {}".format(
        user_max_glass_t
    )


def test_task_c(get_namespace):

    user_pareto_optimal = get_namespace["num_pareto_optimal"]
    user_pareto_sustainable = get_namespace["num_pareto_sustainable"]

    # assert that num_pareto_optimal is 15
    assert user_pareto_optimal == 15, "Expected num_pareto_optimal: 15, got {}".format(
        user_pareto_optimal
    )

    # assert that num_pareto_sustainable is 6
    assert (
        user_pareto_sustainable == 6
    ), "Expected num_pareto_sustainable: 6, got {}".format(user_pareto_sustainable)


def test_task_d(get_namespace):

    running_ax_client = get_namespace["ax_client_thresh"]
    user_op_params = running_ax_client.experiment.parameters

    # assert that len op_params is 4
    assert len(user_op_params) == 5, "Expected 5 parameters, got {}".format(
        len(user_op_params)
    )

    # assert that op_params contains ['time', 'temperature', 'v_prct', 'process']
    assert all(
        [param in ["EA", "EB", "EC", "AA", "AB"] for param in user_op_params]
    ), "Expected parameters named ['EA', 'EB'', 'EC', 'AA', 'AB''], got {}".format(
        user_op_params.keys()
    )

    # assert that the ax_client budget is 25
    assert (
        len(running_ax_client.get_trials_data_frame()) == 40
    ), "Expected optimization budget of 40 trials, got {}".format(
        len(running_ax_client.get_trials_data_frame())
    )

    user_obj_thresh_1 = (
        running_ax_client.experiment.optimization_config.objective_thresholds[0].bound
    )
    user_obj_thresh_2 = (
        running_ax_client.experiment.optimization_config.objective_thresholds[1].bound
    )

    # assert that the user obj thresholds is one of 75, 85
    assert user_obj_thresh_1 in [
        75,
        85,
    ], "Expected objective threshold: 75 or 85, got {}".format(user_obj_thresh_1)

    assert user_obj_thresh_2 in [
        75,
        85,
    ], "Expected objective threshold: 75 or 85, got {}".format(user_obj_thresh_2)


def test_task_e(get_namespace):

    user_pareto_optimal_thresh = get_namespace["num_pareto_optimal_thresh"]
    user_pareto_sustainable_thresh = get_namespace["num_pareto_sustainable_thresh"]

    # assert that num_pareto_optimal is 15
    assert (
        user_pareto_optimal_thresh >= 12
    ), "Expected num_pareto_optimal_thresh: 12, got {}".format(
        user_pareto_optimal_thresh
    )

    # assert that num_pareto_sustainable is 6
    assert (
        user_pareto_sustainable_thresh >= 12
    ), "Expected num_pareto_sustainable_thresh: 12, got {}".format(
        user_pareto_sustainable_thresh
    )


def test_task_f(get_namespace):

    user_tradeoff = get_namespace["tradeoff"]

    # assert that tradeoff is greater than 0.5
    assert user_tradeoff < -0.5, "Expected tradeoff < -0.5, got {}".format(
        user_tradeoff
    )
