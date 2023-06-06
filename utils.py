import pandas as pd

def create_dict(keys, values):
    dict = {}
    for i in range(len(keys)):
        dict[keys[i]]=values[i]
    return dict


def save_csv(data, filename):
    frame = pd.DataFrame(data)
    frame.to_csv(filename, index=False)
