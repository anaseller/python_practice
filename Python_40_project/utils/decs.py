"""Декораторы"""

import sys
import logging
sys.path.append('../')
from logs import config_log


# Метод определения модуля, источника запуска.
# Метод find() возвращает индекс первого вхождения искомой подстроки,
# если он найден в данной строке.
# Если его не найдено, - возвращает -1.


def log(func_to_log):
    def log_saver(*args, **kwargs):
        logger = logging.getLogger('project_logger')
        ret = func_to_log(*args, **kwargs)
        logger.info(f'Была вызвана функция {func_to_log.__name__} c параметрами {args}, {kwargs}. '
                     f'Вызов из модуля {func_to_log.__module__}')
        return ret
    return log_saver