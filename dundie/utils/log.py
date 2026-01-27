import os
import logging
from logging import handlers

LOG_LEVEL = os.getenv("LOG_LEVEL", "WARNING").upper()
# retorna um log com nome específico, e o cria, se necessário
log = logging.getLogger("dundie")
fmt = logging.Formatter(
        '%(asctime)s  %(name)s  %(levelname)s l:%(lineno)d f:%(filename)s: %(message)s'
    )
def get_logger(logfile="dundie.log"):
    """Returns a configured logger."""
    # ch = logging.StreamHandler() # Console/terminal/stderr
    # ch.setLevel(log_level)
    fh = handlers.RotatingFileHandler(
        "logfile",
        maxBytes=10**6,  # costuma-se usar maxBytes=10**6 , que é igual a 1MB
        backupCount=10
    )
    fh.setLevel(LOG_LEVEL)
    # formatação
    
    # ch.setFormatter(fmt)
    fh.setFormatter(fmt)
    # destino
    log.addHandler(fh)
    return log