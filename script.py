#!/usr/bin/env python3
"""
Script para digitar o texto automaticamente (simula digitação).
Use quando copiar/colar não funcionar no campo de destino.
"""

import time
import sys

try:
    from pynput.keyboard import Controller, Key
except ImportError:
    print("Instalando dependência: pynput")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pynput"])
    from pynput.keyboard import Controller, Key

TEXTO = """teste que vai ser digitado!"""


def digitar_texto(intervalo_entre_teclas=0.02):
    """Simula a digitação do texto caractere por caractere."""
    teclado = Controller()
    print("Digitação iniciará em 3 segundos. Coloque o cursor no campo de texto!")
    for i in range(3, 0, -1):
        print(f"  {i}...")
        time.sleep(1)
    print("Digitação em andamento. Não mexa no teclado/mouse.")
    for char in TEXTO:
        if char == "\n":
            teclado.press(Key.enter)
            teclado.release(Key.enter)
        else:
            teclado.type(char)
        time.sleep(intervalo_entre_teclas)
    print("Concluído.")


if __name__ == "__main__":
    intervalo = 0.02
    if len(sys.argv) > 1:
        try:
            intervalo = float(sys.argv[1])
        except ValueError:
            pass
    digitar_texto(intervalo_entre_teclas=intervalo)