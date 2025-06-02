import sys
import os
import logging
import logging.handlers
LOGGING_LEVEL_MAIN = logging.DEBUG
LOGGING_LEVEL_STREAM = logging.DEBUG
LOGGING_LEVEL_FILE = logging.INFO

sys.path.append('../')

# создаём формировщик логов (formatter):
formatter = logging.Formatter('%(asctime)s %(levelname)s %(filename)s %(message)s')

# Подготовка имени файла для логирования
log_path = os.path.dirname(os.path.abspath(__file__))
log_path = os.path.join(log_path, 'logs.log')

# создаём потоки вывода логов
stream_handler = logging.StreamHandler(sys.stderr)
stream_handler.setFormatter(formatter)
stream_handler.setLevel(LOGGING_LEVEL_STREAM)

file_handler = logging.FileHandler(log_path)
file_handler.setFormatter(formatter)
file_handler.setLevel(LOGGING_LEVEL_FILE)

# создаём регистратор и настраиваем его
logger = logging.getLogger('project_logger')
logger.setLevel(LOGGING_LEVEL_MAIN)
logger.addHandler(stream_handler)
logger.addHandler(file_handler)

# отладка
if __name__ == '__main__':
    logger.critical('Критическая ошибка')
    logger.error('Ошибка')
    logger.warning('Предупреждение')
    logger.info('Информационное сообщение')
    logger.debug('Отладочная информация')
