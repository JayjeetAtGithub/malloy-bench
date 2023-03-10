import os
import shutil

import duckdb
import pandas

if __name__ == "__main__":
    # create dir for raw dataset
    shutil.rmtree("/mnt/data/dataset", ignore_errors=True)
    os.makedirs("/mnt/data/dataset", exist_ok=True)

    # create dir for uid appended dataset
    shutil.rmtree("/mnt/data/dataset_uid", ignore_errors=True)
    os.makedirs("/mnt/data/dataset_uid", exist_ok=True)
    
    for i in range(1, 10001):
        filepath = f"/mnt/data/dataset/hep.{i}.parquet"
        shutil.copy("hep.parquet", filepath)
        print("Wrote ", filepath)
    
    for i in range(1, 10001):
        sql = f"""
            SELECT gen_random_uuid()::varchar AS uid, * FROM '/mnt/data/dataset/hep.{i}.parquet'
        """
        df = duckdb.sql(sql).df()
        filepath = f"/mnt/data/dataset_uid/hep.uid.{i}.parquet"
        df.to_parquet(filepath)
        print("Wrote ", filepath)
