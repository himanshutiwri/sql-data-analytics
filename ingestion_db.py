import pandas as pd
import os
from sqlalchemy import create_engine
import logging
import time

logging.basicConfig(
    filename="logs/ingestion_db.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="a"
)

engine = create_engine('sqlite:///inventory.db')

def ingest_db(df, table_name, engine, if_exists="replace"):
    """Ingest a DataFrame into SQLite table"""
    df.to_sql(table_name, con=engine, if_exists=if_exists, index=False)

def load_raw_data():
    """This function will load the CSVs as dataframe and ingest into db"""
    start = time.time()
    
    for file in os.listdir('data'):
        if file.endswith('.csv'):
            table_name = file[:-4]
            logging.info(f'Starting ingestion of {file} into table {table_name}')
            
            # Special handling for large sales.csv
            if file == 'sales.csv':
                chunksize = 50000  # adjust based on RAM
                first_chunk = True
                for chunk in pd.read_csv(f'data/{file}', chunksize=chunksize):
                    logging.info(f'Processing chunk with shape: {chunk.shape} from {file}')
                    if first_chunk:
                        ingest_db(chunk, table_name, engine, if_exists='replace')
                        first_chunk = False
                    else:
                        ingest_db(chunk, table_name, engine, if_exists='append')
            else:
                df = pd.read_csv(f'data/{file}')
                logging.info(f'Loaded {file} with shape: {df.shape}')
                ingest_db(df, table_name, engine, if_exists='replace')
    
    end = time.time()
    total_time = (end - start) / 60
    logging.info('--------------Ingestion Complete--------------')
    logging.info(f'Total Time Taken: {total_time:.2f} minutes')

if __name__ == '__main__':
    load_raw_data()
