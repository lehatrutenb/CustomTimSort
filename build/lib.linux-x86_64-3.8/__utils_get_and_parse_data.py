import json
import logging
import numpy as np
import pandas as pd
from collections import namedtuple
from sklearn.model_selection import train_test_split

TRAIN = 6171
EXAM = 500

data_params = namedtuple("data",
                         ["train", "train_labels", "test",
                          "test_labels", "exam", "exam_labels"])
l1_l2_params = namedtuple("reg_params", ["l1", "l2"])
params = namedtuple("parameters", ["epochs", "optimizer", "loss", "metrics",
                                   "regularizer", "dropout", "layer",
                                   "neirons", "reg_params", "activation"])

logging.basicConfig(filename="logs.log", level=logging.INFO)


def normalize_data(data, mean, std):
    return (data - mean) / std


def renormalize_data(data, mean, std):
    return data * std + mean


def get_parsed_data(file_name):
    """Parse data from file"""

    pairs = pd.read_csv(file_name)["DataPairs"]
    pairs = [eval(pair) for pair in pairs]
    X = np.asarray([pair[0] * 1.0 for pair in pairs])
    y = np.asarray([pair[1] * 1.0 for pair in pairs])

    all_data = train_test_split(X, y, test_size=0.3, shuffle=False)

    data = data_params
    data.train, test_exam, data.train_labels, test_exam_labels = all_data
    all_data = train_test_split(test_exam, test_exam_labels,
                                test_size=0.45, random_state=40)
    data.test, data.exam, data.test_labels, data.exam_labels = all_data

    logging.info('Len test: ' + str(len(data.test)))
    logging.info('Len train: ' + str(len(data.train)))
    logging.info('Len validate: ' + str(len(data.exam)))

    data.test = np.array_split(data.test, 4)
    data.test_labels = np.array_split(data.test_labels, 4)

    mean = data.train.mean(axis=0)
    data.train -= mean
    std = data.train.std(axis=0)
    data.train /= std

    data.test = normalize_data(data.test, mean, std)
    data.exam = normalize_data(data.exam, mean, std)

    data_p = {'mean': mean, 'std': std}
    with open('data.json', 'w') as f_write:
        json.dump(data_p, f_write)

    return data


def config_parameters(file_name):
    """Read parameters from config"""
    with open(file_name) as f:
        parameters_dict = json.load(f)

    l1 = parameters_dict["reg_params"]["l1"]
    l2 = parameters_dict["reg_params"]["l2"]
    parameters_dict["reg_params"] = l1_l2_params(l1, l2)
    parameters = params(**parameters_dict)
    return parameters

