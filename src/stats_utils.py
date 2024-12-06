import cProfile
import pstats
from timeit import timeit

def run_profiler(func, *args, **kwargs):
    profiler = cProfile.Profile()
    profiler.enable()

    result = func(*args, **kwargs)

    stats = pstats.Stats(profiler)
    stats.strip_dirs()
    stats.sort_stats('cumulative')
    stats.print_stats()

    profiler.disable()
    profiler.dump_stats("resultado.prof")

    exec_time = timeit(lambda: func(*args, **kwargs), number=1)
    print(f"Tempo de execução: {exec_time:.5f} segundos")

    return result
