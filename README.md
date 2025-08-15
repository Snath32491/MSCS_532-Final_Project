HPC Optimization: Array of Structures (AoS) vs Structure of Arrays (SoA)

Project Overview
This project explores High Performance Computing (HPC) optimization techniques by comparing two data layouts:

- Array of Structures (AoS) → `[[x1, y1], [x2, y2], ...]`  
- Structure of Arrays (SoA) → `x = [x1, x2, ...], y = [y1, y2, ...]`  

The focus is on **benchmarking performance** when summing large datasets, highlighting the benefits of vectorization and memory-friendly access patterns.

Techniques Applied
- AoS (Array of Structures):
  - Stored data as an `N x 2` NumPy array.
  - Used a Python loop to iterate and sum values.
  - Simple and intuitive but slow due to Python loop overhead.

- SoA (Structure of Arrays):
  - Split data into separate NumPy arrays (`x`, `y`).
  - Applied vectorized NumPy operations (`np.sum(x + y)`).
  - Exploits low-level C optimizations and SIMD instructions.


Problems Encountered
- Floating-point precision differences  
  Small rounding errors triggered failed assertions, so strict equality checks were removed.
  
-Timing variability 
  Benchmarks fluctuated due to OS background processes. Solved by averaging across 5 runs.

- Python loop overhead in AoS  
  Showed how row-wise iteration becomes a bottleneck for large datasets.


Results and Performance Gains
- SoA outperformed AoS significantly:
  - 15–20× faster for arrays of 100k to 800k elements.
- Scaling remained linear in both cases, but SoA’s slope was much smaller.
- Demonstrated the power of data layout + vectorization for HPC workloads.


Conclusion
This project confirms that:
- Data structure choice directly impacts performance.
- Re-structuring from AoS → SoA enables massive speedups with minimal code changes.
- Vectorization and memory-friendly access are key to **HPC and scientific computing efficiency.


Repository Contents
- hpc_optimization.py → Benchmarking script.
- Final Project_High Performance Optimization Techniques → Project Report.
- README.md → Project documentation.


How to Run
1. Clone or download the repository.
2. Run the script with Python:
   ```bash
   python hpc_optimization.py
