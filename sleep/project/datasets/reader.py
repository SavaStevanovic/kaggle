import pandas as pd

class Reader:
    read_map = {
        "csv": lambda x: pd.read_csv(x),
        "parquet": lambda x: pd.read_parquet(x)
    }

    @staticmethod
    def read(path: str):
        return Reader.read_map[path.split(".")[-1]](path)