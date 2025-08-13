import time
import psutil
import torch
from slim_gsgp.main_gp import gp
import os

os.makedirs("log", exist_ok=True)

X_train = torch.rand((100, 3))
y_train = torch.rand((100,))

# Track overall performance
total_start_time = time.time()
results = []

for i in range(10):
    print(f"\n--- Execução {i + 1} ---")

    # Memory before execution
    process = psutil.Process()
    mem_before = process.memory_info().rss / 1024 / 1024  # MB

    # Time measurement
    start_time = time.time()

    # GPU memory if available
    if torch.cuda.is_available():
        gpu_mem_before = torch.cuda.memory_allocated() / 1024 / 1024  # MB

    # Execute SLIM
    gp(
        X_train=X_train,
        y_train=y_train,
        dataset_name=f"simples_{i + 1}",
        pop_size=50,
        n_iter=50,
        log_path=f"./log/simples_run_{i + 1}.csv",
        seed=11 + i
    )

    # Calculate costs
    execution_time = time.time() - start_time
    mem_after = process.memory_info().rss / 1024 / 1024  # MB
    mem_used = mem_after - mem_before

    if torch.cuda.is_available():
        gpu_mem_after = torch.cuda.memory_allocated() / 1024 / 1024  # MB
        gpu_mem_used = gpu_mem_after - gpu_mem_before
    else:
        gpu_mem_used = 0

    # Store results
    run_stats = {
        'run': i + 1,
        'time_seconds': execution_time,
        'memory_mb': mem_used,
        'gpu_memory_mb': gpu_mem_used,
        'cpu_percent': psutil.cpu_percent()
    }
    results.append(run_stats)

    print(f"Time: {execution_time:.2f}s")
    print(f"Memory used: {mem_used:.2f} MB")
    if gpu_mem_used > 0:
        print(f"GPU memory used: {gpu_mem_used:.2f} MB")

# Overall statistics
total_time = time.time() - total_start_time
avg_time = sum(r['time_seconds'] for r in results) / len(results)
total_memory = sum(r['memory_mb'] for r in results)

print(f"\n--- Summary ---")
print(f"Total execution time: {total_time:.2f}s")
print(f"Average time per run: {avg_time:.2f}s")
print(f"Total memory used: {total_memory:.2f} MB")