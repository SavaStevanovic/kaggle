from torch.utils.data import Dataset
from datasets.reader import Reader

class SleepDataset(Dataset):
    def __init__(self, data_path: str, event_path: str):
        self._event_data = Reader.read(event_path)
        self._data = Reader.read(data_path)
        self._data_info = self._data.merge(self._event_data, how="left", on=["step", "series_id", "timestamp"])
        self._data_groups = self._data_info["series_id"].unique().tolist()

    def __len__(self):
        return len(self._data_groups)

    def __getitem__(self, idx):
        return self._data_info[self._data_info["series_id"] == self._data_groups[idx]]