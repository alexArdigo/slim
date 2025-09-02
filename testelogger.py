from Logger import Logger
import time

def test_logger():
    params_gp = {
        "popsize": 10,
        "mutation_rate": 0.1,
        "generations": 5
    }

    logger_gp = Logger(algorithm="GP", params=params_gp)

    for gen in range(1, params_gp["generations"] + 1):
        best_fitness = 100 / gen
        avg_fitness = sum([100 / i for i in range(1, gen + 1)]) / gen
        diversity = gen * 0.2
        logger_gp.log_generation(
            generation=gen,
            best_fitness=best_fitness,
            avg_fitness=avg_fitness,
            diversity=diversity
        )
        time.sleep(0.05)

    for row in logger_gp.get_log():
        print(row)

if __name__ == "__main__":
    test_logger()

