import numpy as np
import time
import matplotlib.pyplot as plt


def aos_sum(data):
    """Sum x + y for Array of Structures (AoS)."""
    return sum(p[0] + p[1] for p in data)


def soa_sum(x, y):
    """Sum x + y for Structure of Arrays (SoA)."""
    return np.sum(x + y)


def bench_once(n):
    """Run one benchmark for n elements."""
    # AoS: array of pairs
    aos_data = np.random.rand(n, 2)
    # SoA: two separate arrays
    x = np.random.rand(n)
    y = np.random.rand(n)

    # Time AoS
    t0 = time.perf_counter()
    s1 = aos_sum(aos_data)
    t1 = time.perf_counter() - t0

    # Time SoA
    t0 = time.perf_counter()
    s2 = soa_sum(x, y)
    t2 = time.perf_counter() - t0

    return t1, t2


def benchmark(sizes, runs=5):
    """Run multiple benchmarks for different sizes."""
    results = []
    for n in sizes:
        aos_times, soa_times = [], []
        for _ in range(runs):
            t1, t2 = bench_once(n)
            aos_times.append(t1)
            soa_times.append(t2)

        results.append({
            "n": n,
            "aos_mean": np.mean(aos_times),
            "soa_mean": np.mean(soa_times)
        })
    return results


def main():
    sizes = [100_000, 200_000, 400_000, 800_000]
    results = benchmark(sizes)

    # Print results in table format
    print(f"{'Size':>10} | {'AoS (s)':>10} | {'SoA (s)':>10} | Speedup")
    print("-" * 45)
    for r in results:
        speedup = r['aos_mean'] / r['soa_mean']
        print(f"{r['n']:>10} | {r['aos_mean']:>10.6f} | {r['soa_mean']:>10.6f} | {speedup:>7.2f}x")

    # Plot results
    plt.figure(figsize=(8, 5))
    plt.plot([r['n'] for r in results], [r['aos_mean'] for r in results], marker="o", label="AoS")
    plt.plot([r['n'] for r in results], [r['soa_mean'] for r in results], marker="o", label="SoA")
    plt.xlabel("Number of elements")
    plt.ylabel("Execution time (seconds)")
    plt.title("AoS vs SoA Performance in HPC Optimization")
    plt.legend()
    plt.grid(True)
    plt.savefig("benchmark_results.png")
    plt.show()


if __name__ == "__main__":
    main()
