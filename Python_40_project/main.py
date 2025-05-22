import logging
import logs.config_log  # Можно и без него, НО пусть будет для явного импорта!
from utils.decs import log

logger = logging.getLogger('project_logger')

@log
def print_something(something):
    print(something)


if __name__ == '__main__':

    print_something('hi!')

    logger.info('info')
    logger.warning('warner')
    logger.error('error')
    logger.critical('critical')