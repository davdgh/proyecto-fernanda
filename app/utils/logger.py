import logging
import os

# 1. Crear la carpeta de logs si no existe
if not os.path.exists('logs'):
    os.makedirs('logs')

# 2. Definir el nombre del archivo (puede ser fijo o por fecha)
log_filename = f"logs/app.log"

# 3. Configurar el formato: [Fecha y Hora] | [Nivel] | [Mensaje]
log_format = "[%(asctime)s] | %(levelname)s | %(message)s"
date_format = "%Y-%m-%d %H:%M:%S"

logging.basicConfig(
    level=logging.DEBUG,
    format=log_format,
    datefmt=date_format,
    handlers=[
        logging.FileHandler(log_filename), # Guarda en archivo
        logging.StreamHandler()           # También muestra en consola
    ]
)

logger = logging.getLogger(__name__)