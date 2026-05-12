import timeit
import numpy as np
import matplotlib.pyplot as plt

def test_cache_speed(max_size=2**20, step=2**12):
    sizes = []
    times = []

    for size in range(2**10, max_size, step):
        # Create a large array
        arr = np.ones(size, dtype=np.int64)

        # Time the read/write operation
        def read_write():
            for i in range(len(arr)):
                arr[i] *= 1

        # Measure time
        time_taken = timeit.timeit(read_write, number=1)
        sizes.append(size)
        times.append(time_taken)

    return sizes, times

def plot_results(sizes, times):
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, times, marker='o')
    plt.xscale('log', base=2)
    plt.yscale('log', base=2)
    plt.xlabel('Array Size (bytes)')
    plt.ylabel('Time (seconds)')
    plt.title('Cache Speed Test')
    plt.grid(True, which="both", ls="--")
    plt.show()

if __name__ == "__main__":
    sizes, times = test_cache_speed()
    plot_results(sizes, times)