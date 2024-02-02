import pandas as pd


def rename_columns(df: pd.DataFrame) -> pd.DataFrame:
    # mappings :: {old_name: new_name}
    mappings = {
            "Name": "Host Name",
            "Host": "Host Name",
            "hostname": "Host Name",
            "IP": "IP Address",
            "IPAddress": "IP Address",
            "Dept": "Department",
            "Operating System": "OS",
        }
    return df.rename(columns=mappings)


def reorder_columns(df):
    return df.sort_index(axis=1)


def normalize(file_name) -> list[pd.DataFrame]:
    return reorder_columns(rename_columns(pd.read_csv(file_name)))


def merge(dfs: list[pd.DataFrame]) -> pd.DataFrame:
    return pd.concat(dfs, ignore_index=True)


def process_files(file_names, output):
    result_df = merge([normalize(name) for name in file_names])
    result_df.to_csv(path_or_buf=output,
                     columns=['Host Name',
                              'IP Address',
                              'Department',
                              'OS',
                              'Function'],
                     sep=',',
                     index=False)
