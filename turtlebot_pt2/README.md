# Robô Teleoperado 

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)

### Vídeo demo

[Vídeo demonstração da aplicação!](https://youtu.be/qZqdl7lqa1E)

## Pré-requisitos

- ROS 2
- Python 3.8+
- turtlesim
- WeBots

Caso nao tenha os pré-requisitos listados, recomendo seguir [esse tutorial](https://rmnicola.github.io/m6-ec-encontros/E01/ros) para instalar todas os requisitos.

## Instalação

1. Clone o repositório em sua máquina:

```bash
git clone https://github.com/ItsVasconcellos/Modulo6
```

2. Abra o repositório em um terminal e entre na pasta meu_workspace:
```bash
cd semana3
```

3. Crie um ambiente virtual
```bash
python -m venv venv
```

4. Baixe os requisitos necessários 
```bash
pip install -r requirements.txt
```

5. Execute o webots (Caso não tenha instalado, siga [esse tutorial](https://rmnicola.github.io/m8-ec-encontros/sprint2/encontro4/nav2/#4-usando-o-simple-commander-api) )

```bash 
ros2 launch webots_ros2_turtlebot robot_launch.py
```

6. Execute o script:
```bash
./run.sh
```

7. Por fim, execute o arquivo cli.py
```bash
python3 cli.py
```