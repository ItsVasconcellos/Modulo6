# Robô Teleoperado - Pt.2

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)

### Vídeo demo

[Vídeo demonstração da aplicação!](https://youtu.be/ZL2YF-t-yMA)

## Pré-requisitos

- ROS 2
- Python 3.8+
- turtlesim
- WeBots
- RosBridge

Caso nao tenha os pré-requisitos listados, recomendo seguir [esse tutorial](https://rmnicola.github.io/m6-ec-encontros/E01/ros), junto com essa [outra página](https://rmnicola.github.io/m6-ec-encontros/rosbridge) para instalar todas os requisitos.

## Instalação

1. Clone o repositório em sua máquina:

```bash
git clone https://github.com/ItsVasconcellos/Modulo6
```

2. Abra o repositório em um terminal e entre na pasta meu_workspace:
```bash
cd turtlebot_pt2
```

3. Execute o webots (Caso não tenha instalado, siga [esse tutorial](https://rmnicola.github.io/m8-ec-encontros/sprint2/encontro4/nav2/#4-usando-o-simple-commander-api) )
```bash 
ros2 launch webots_ros2_turtlebot robot_launch.py
```

4. Em outro terminal, execute o script:
```bash
./run.sh
```

5. Serão necessários três abas de terminais para executar os pacotes:
```bash
ros2 run teleop_node teleop_node
```

6. Rode o pacote da webcam:
```bash 
ros2 launch webcam_node webcam
```

7. Por fim, execute o pacote do rosbridge:
```bash
ros2 launch rosbridge_server rosbridge_websocket_launch.xml
```

8. Por fim, abra o arquivo html e o execute: (Sugestão: Utilize live-server)
