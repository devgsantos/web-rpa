import logging
import sys
import os
import pytz

from typing import Union


from datetime import datetime

current_datetime = datetime.now(pytz.timezone('America/Sao_Paulo'))
year = current_datetime.year
month = current_datetime.month
day = current_datetime.day

# CONFIGURAÇÃO DO PATH DE PASTAS DO LOG
ROOT_DIR = os.getcwd()
LOG_PATH = os.path.join(ROOT_DIR, 'logs')
YEAR_PATH = os.path.join(LOG_PATH, str(year))
MONTH_PATH = os.path.join(YEAR_PATH, str(month))
DAY_PATH = os.path.join(MONTH_PATH, str(day))
day_folder = DAY_PATH

class Logger:

    @classmethod
    def setup_logger(self):
        try:
            if not os.path.exists(DAY_PATH):
                os.makedirs(DAY_PATH)

            logger = logging.getLogger()
            logger.setLevel(logging.INFO)
            formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')

            file_handler = logging.FileHandler(os.path.join(day_folder, f"{str(day)}_log.log"))
            file_handler.setLevel(logging.DEBUG)
            file_handler.setFormatter(formatter)

            logger.addHandler(file_handler)


        except Exception as e:
            self.create_log('ERROR', str(e))

    @classmethod
    def create_log(self, log_type: Union['INFO', 'WARNING', 'ERROR'], log_message: str):
        # VERIFICA SE O LOGGER JÁFOI CRIADO
        if not logging.getLogger().handlers:
            self.setup_logger()

        logger = logging.getLogger()
        if log_type == 'INFO':
            logger.info(log_message)
        if log_type == 'WARNING':
            logger.warning(log_message)
        if log_type == 'ERROR':
            logger.error(log_message)
