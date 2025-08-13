from slim_gsgp.main_slim import slim
import torch

X_train = torch.rand((100, 3))
y_train = torch.rand((100,))

pop_sizes = [50, 100]
p_inflates = [0.1, 0.5]

for pop_size in pop_sizes:
    for p_inflate in p_inflates:
        run_name = f"nested_pop{pop_size}_inflate{int(p_inflate*100)}"
        print(f"\n--- Execução: {run_name} ---")
        slim(
            X_train=X_train,
            y_train=y_train,
            dataset_name=run_name,
            pop_size=pop_size,
            n_iter=10,
            p_inflate=p_inflate,
            log_path=f"./log/{run_name}.log",
            seed=74
        )