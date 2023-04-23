import yaml

def loader(filename: str) -> dict:
    with open(filename, 'r') as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
    return config