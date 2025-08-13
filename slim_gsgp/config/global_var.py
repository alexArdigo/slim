from slim_gsgp.config.gp_config import *

global_var = {
    "dataset_name": None,
    "pop_size": gp_parameters["pop_size"],
    "n_iter": 100,
    "p_xo": gp_parameters['p_xo'],
    "elitism": gp_solve_parameters["elitism"],
    "n_elites": gp_solve_parameters["n_elites"],
    "max_depth": gp_solve_parameters["max_depth"],
    "init_depth": gp_pi_init["init_depth"],
    "log_path": None,
    "seed": gp_parameters["seed"],
    "log_level": gp_solve_parameters["log"],
    "verbose": gp_solve_parameters["verbose"],
    "minimization": True,
    "fitness_function": gp_solve_parameters["ffunction"],
    "initializer": gp_parameters["initializer"],
    "n_jobs": gp_solve_parameters["n_jobs"],
    "prob_const": gp_pi_init["p_c"],
    "tree_functions": list(FUNCTIONS.keys()),
    "tree_constants": [float(key.replace("constant_", "").replace("_", "-")) for key in CONSTANTS],
    "tournament_size": 2,
    "test_elite": gp_solve_parameters["test_elite"]
}
