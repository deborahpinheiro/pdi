import services.reception as reception
import services.loader as loader
import utils


def exec(source_id):
    
    df_raw = reception.process_source(source_id)

    loader.process_data(df_raw, source_id)

    utils.report_resource_usage()

if __name__ == "__main__":
    
    exec(1)