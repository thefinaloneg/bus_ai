import multiprocessing as mp
import time_difference


stop_list = ["iu", "it", "isr", "unimpl"]

if __name__ == '__main__':
    with mp.Pool() as pool:
        pool.map(time_difference.bulk_difference, stop_list)