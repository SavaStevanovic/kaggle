from datasets.sleep import SleepDataset


data = SleepDataset(
    "/Data/sequence/child-mind-institute-detect-sleep-states/train_series.parquet",
    "/Data/sequence/child-mind-institute-detect-sleep-states/train_events.csv",
)
len(data)
print(data[1])