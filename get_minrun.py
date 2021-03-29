import keras
import json as js
import numpy as np
from __utils_get_and_parse_data import normalize_data

def get_minrun_from_builded_model(array_size,
                                  path_to_data="data.json",
                                  model_name="standard_model"):
    def LoadDataConfig(path_to_data):
        data = {}
        with open(path_to_data) as f:
            data = js.load(f)
        return float(data["std"]), float(data["mean"])

    mean, std = LoadDataConfig(path_to_data)
    norm_len = np.asarray([normalize_data(size, mean, std) for size in array_size])
    model = keras.models.load_model(model_name)
    minruns = model.predict(norm_len)
    return [min(array_size[i], max(1, abs(int(minruns[i][0] / 6)))) for i in range(len(array_size))]

