import reception
import loader

source_id = 1

df_raw = reception.process_source(source_id)

loader.process_data(df_raw, source_id)
