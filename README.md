# malloy-bench

Converting the queries [here](https://github.com/RumbleDB/iris-hep-benchmark-bigquery/tree/master/queries) to Malloy and measuring performance improvement. 
Till now, I could only convert Q1, Q2, Q3, and Q4 queries to Malloy.

## How to use this repo ?

1. The `malloy_query` dir contains the Malloy version (and malloy to sql converted version) of the queries in the `sql_query` dir.
2. `hep.parquet` is the dataset used for this project.
3. For this benchmark, I replicate the `hep.parquet` file 10000 times using the `create_dataset.py` script.
4. `bench.py` is my little script to run the benchmarks.

```bash
// to run a single query
python3 bench.py q /mnt/data/dataset_uid {query_no} 

// to run all the queries for `r` reps and plot the results
python3 bench.py e2e /mnt/data/dataset_uid {r}
```
