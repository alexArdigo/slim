from sklearn.model_selection import KFold

from slim_gsgp.config.gp_config import *
from slim_gsgp.main_gp import gp  # import the slim_gsgp library
from slim_gsgp.datasets.data_loader import load_airfoil  # import the loader for the dataset PPB
from slim_gsgp.evaluators.fitness_functions import rmse  # import the rmse fitness metric
from slim_gsgp.utils.graphic import build_graphic
from slim_gsgp.utils.utils import train_test_split  # import the train-test split function

seed = 1111

# Load the PPB dataset
X, y = load_airfoil(X_y=True)

cv = KFold(n_splits=10, random_state=seed, shuffle=True)

data_cv = [[train_ix, test_ix] for train_ix, test_ix in cv.split(X, y)]

# Split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, p_test=0.4)

# Split the test set into validation and test sets
X_val, X_test, y_val, y_test = train_test_split(X_test, y_test, p_test=0.5)


local_var = {
    "dataset_name": "airfoil",
    "pop_size": 50,  # size of the population of candidate solutions.
    "n_iter": 100,
    "p_xo": .9,  # probability of applying the cross-over genetic operator to candidate solutions.
    "elitism": True,
    "n_elites": 1,
    "max_depth": 7,
    "init_depth": 4,
    "log_path": "./log/gp_airfoil.csv",
    "seed": seed,
    "log_level": 2,
    "verbose": 1,
    "minimization": True,
    "fitness_function": "rmse",
    "initializer": "grow",
    "n_jobs": 1,
    "prob_const": .9,
    "tree_functions": list(FUNCTIONS.keys()),
    "tree_constants": [float(key.replace("constant_", "").replace("_", "-")) for key in CONSTANTS],
    "tournament_size": 2,
    "test_elite": True
}

# Apply the GP algorithm
final_tree = gp(X_train=X_train, y_train=y_train,
                X_test=X_val, y_test=y_val,
                **local_var)

# Show the best individual structure at the last generation
final_tree.print_tree_representation()

# Get the prediction of the best individual on the test set
predictions = final_tree.predict(X_test)

# Compute and print the RMSE on the test set
print(float(rmse(y_true=y_test, y_pred=predictions)))

build_graphic(local_var.get("log_path"), local_var.get("dataset_name"))
