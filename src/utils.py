import argparse
import yaml
import logging
import os

def parse_config(func) -> dict:
    """ Loads config and parses it to a function."""
    def wrapper(*args, **kwargs):
        parser = argparse.ArgumentParser()
        parser.add_argument('--config')
        filename = vars(parser.parse_args())['config']
        try:
            with open(filename, 'r') as file:
                config = yaml.load(file, Loader=yaml.FullLoader)
        except Exception:
            raise ValueError("Unable to load configuration")
        rv = func(config)
        return rv
    return wrapper

def LoggingConfig(folder):
    filename = os.path.join(folder, 'history.log')
    os.system(f'touch {filename}')
    logging.basicConfig(filename=filename,
                            level=logging.INFO,
                            format="%(asctime)s:%(levelname)s - %(msg)s")

          