import services.reception as reception
import services.loader as loader
import utils
from timeit import timeit
import cProfile
import pstats
from io import StringIO


def main(source_id):
    
    df_raw = reception.process_source(source_id)

    print(df_raw)

if __name__ == "__main__":
    profiler = cProfile.Profile()
    profiler.enable()

    main(1)

    profiler.disable()
    profiler.dump_stats("resultado.prof")

    exec_time = timeit(lambda: main(1), number=1)
    print(f"Tempo de execução: {exec_time:.5f} segundos")

   
