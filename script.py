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

TEXTO = """A Lei nº 10.436/2002 representa um passo muito importante para a comunidade surda no Brasil, pois foi a lei que reconheceu oficialmente a Língua Brasileira de Sinais (Libras) como meio legal de comunicação e expressão. A partir desse reconhecimento, a Libras passou a ser considerada uma língua legítima da comunidade surda, fortalecendo sua identidade cultural e linguística e abrindo caminho para políticas públicas voltadas à acessibilidade, como a formação de intérpretes e o ensino da Libras em cursos de formação de professores.

Já a Lei nº 14.191/2021 complementa esse avanço ao incluir a educação bilíngue de surdos como uma modalidade específica dentro da Lei de Diretrizes e Bases da Educação Nacional (LDB). Essa lei garante que estudantes surdos possam aprender utilizando a Libras como primeira língua e o português escrito como segunda língua, desde a educação infantil até outros níveis de ensino. Dessa forma, busca-se garantir uma educação mais adequada às necessidades linguísticas desses estudantes e promover maior igualdade de oportunidades no processo educacional.

Assim, é possível perceber que as duas leis se complementam: a Lei nº 10.436/2002 reconhece e valoriza a Libras como língua da comunidade surda, enquanto a Lei nº 14.191/2021 assegura que essa língua seja efetivamente utilizada no ambiente escolar, garantindo direitos linguísticos e educacionais mais amplos às pessoas surdas.

Fontes:
BRASIL. Lei nº 10.436, de 24 de abril de 2002.
BRASIL. Lei nº 14.191, de 3 de agosto de 2021.
Ministério dos Direitos Humanos e da Cidadania; Instituto Nacional de Educação de Surdos (INES)."""


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