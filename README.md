# Script EAD — Digitação automática

Script em Python que simula digitação tecla a tecla em qualquer campo de texto. Útil quando **copiar e colar (Ctrl+V / Cmd+V) não funciona** no destino — por exemplo em provas, redações ou formulários de plataformas EAD que bloqueiam colagem.

## O que faz

- Digita o conteúdo da variável `TEXTO` no `script.py` caractere por caractere.
- Dá 3 segundos para você posicionar o cursor no campo antes de começar.
- Permite ajustar a velocidade da digitação via argumento na linha de comando.

## Requisitos

- Python 3.7+
- Dependência: `pynput`

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/eduardofrois/script-ead.git
   cd script-ead
   ```

2. Crie um ambiente virtual (recomendado):
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # Linux/macOS
   # ou: venv\Scripts\activate  # Windows
   ```

3. Instale a dependência:
   ```bash
   pip install -r requirements.txt
   ```

## Uso

1. Abra a página/aba onde está o campo de texto (prova, redação, etc.).
2. Execute o script:
   ```bash
   python script.py
   ```
   No macOS/Linux, se precisar:
   ```bash
   python3 script.py
   ```
3. Nos **3 segundos** de contagem, **clique no campo** onde o texto deve aparecer.
4. Não use teclado nem mouse enquanto o script estiver digitando.

### Ajustar velocidade

O intervalo entre cada tecla é **0,02 segundos** por padrão.

- Mais devagar (ex.: 0,05 s entre teclas):
  ```bash
  python script.py 0.05
  ```
- Mais rápido (ex.: 0,01 s):
  ```bash
  python script.py 0.01
  ```

## Como mudar o texto

Edite a variável `TEXTO` no arquivo `script.py`. É uma string de várias linhas (triple-quoted); basta substituir pelo conteúdo desejado. Quebras de linha são respeitadas (Enter é simulado).

## Estrutura do repositório

```
script-ead/
├── script.py          # Script principal
├── requirements.txt   # Dependência (pynput)
├── .gitignore
└── README.md
```

## Observações

- O script envia as teclas para a **janela que estiver em foco**. Certifique-se de que o cursor está no campo certo antes do fim da contagem.
- Em alguns sistemas pode ser necessário conceder permissão de “Acessibilidade” ou “Controle do computador” para o terminal/IDE que executa o script.
- Use por sua conta e risco; verifique as regras da plataforma antes de usar em provas ou atividades avaliativas.

## Licença

Uso livre para fins educacionais e pessoais.
