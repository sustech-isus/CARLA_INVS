#!/usr/bin/env python3
from pathlib import Path

CARLA_PATH = Path('~/CARLA').expanduser()
ROOT_PATH  = Path(__file__).parent

#for gen_data
LOG_PATH   = ROOT_PATH / 'log'
RAW_DATA_PATH  = ROOT_PATH / 'raw_data'
COOK_DATA_PATH = ROOT_PATH / 'dataset'
#https://carla.readthedocs.io/en/latest/core_map/#changing-the-map
TOWN_MAP = ['Town01', 'Town02', 'Town03', 'Town04', 'Town05'][1]
