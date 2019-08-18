import logging
import os
import configparser
import pytz

logger = logging.getLogger('bustag')

DATA_PATH = './data/'
CONFIG_FILE = 'config.ini'
APP_CONFIG = {}


def setup_logging():
    logger.addHandler(logging.StreamHandler())
    logger.setLevel(logging.DEBUG)


def get_data_path(file):
    file_path = os.path.join(DATA_PATH, file)
    return file_path


def load_config():
    config_path = get_data_path(CONFIG_FILE)
    conf = configparser.ConfigParser()
    conf.read(config_path)
    for section in conf.sections():
        for key in conf.options(section):
            value = conf.get(section, key)
            key = section + '.' + key
            APP_CONFIG[key.lower()] = value


def to_localtime(utc_dt):
    local_tz = pytz.timezone('Asia/Shanghai')
    local_dt = utc_dt.replace(tzinfo=pytz.utc).astimezone(local_tz)
    format = '%Y-%m-%d %H:%M:%S'
    local_dt = local_tz.normalize(local_dt)
    return local_dt.strftime(format)


def init():
    setup_logging()
    load_config()


init()
