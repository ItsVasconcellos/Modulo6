# Drawing Turtle

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)

## Descrição

O pacote drawing_turtle foi uma atividade ponderada realizada com o intuito de utilizar o turtlesim para criar um desenho. Para isso, foram utilizados comandos como: `spawn`,`kill`,`setPen`. O pacote realiza um desenho, o qual se assemelha com o escudo do palmeiras.

### Vídeo demo

[Vídeo demonstração da aplicação!](https://youtu.be/jdG3csXaiEs)

## Pré-requisitos

- ROS 2
- Python 3.8+
- turtlesim

Caso nao tenha os pré-requisitos listados, recomendo seguir [esse tutorial](https://rmnicola.github.io/m6-ec-encontros/E01/ros) para instalar todas os requisitos.

## Instalação

1. Clone o repositório em sua máquina:

```bash
git clone https://github.com/ItsVasconcellos/Modulo6
```

2. Abra o repositório em um terminal e entre na pasta meu_workspace:
```bash
cd meu_workspace
```

3. Após isso, execute o comando a seguir para executar a build do pacote ros:
```bash 
colcon build
```

4. Crie o local_setup para seu terminal
```bash
source install/local_setup.bash
```

5. Rode o comando a baixo:
```bash 
ros2 run turtlesim turtlesim_node 
```

6. Repita os passos 2,3,4 e por fim execute o comando: 
```bash 
ros2 run drawing_turtle drawing_turtle
```