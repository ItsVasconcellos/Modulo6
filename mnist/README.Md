# Projeto MNIST

Este é um projeto que utiliza o conjunto de dados MNIST para treinar e testar modelos de aprendizado de máquina para reconhecimento de dígitos escritos à mão.

## Descrição

O conjunto de dados MNIST é composto por imagens de dígitos escritos à mão, cada uma com tamanho 28x28 pixels. O objetivo deste projeto é desenvolver um modelo de aprendizado de máquina capaz de identificar corretamente o dígito representado em cada imagem.

## Funcionalidades

- Carregar o conjunto de dados MNIST
- Pré-processar as imagens para melhorar a qualidade dos dados
- Treinar um modelo de aprendizado de máquina utilizando diferentes algoritmos
- Avaliar o desempenho do modelo utilizando métricas como acurácia e matriz de confusão
- Realizar previsões em novas imagens de dígitos escritos à mão

## Instalação

1. Clone este repositório em sua máquina local.
2. Execute o arquivo `src/backend.py` para iniciar o treinamento e teste do modelo.

## Demonstração

https://youtu.be/YQ0OVXnX7xM

## Rotas 

1. Rota inicial (/)

- Método: GET
- Descrição: Carrega a página inicial (index.html).
- Parâmetros: Nenhum
- Retorno:
    Renderiza o template index.html, passando a variável prediction obtida da sessão do usuário (se disponível). Essa variável provavelmente exibe o dígito previsto anteriormente.

2. Rota de previsão (/predict)

- Método: POST (Aceita envios de formulário)
- Descrição: Recebe uma imagem enviada pelo usuário, processa-a e gera uma previsão usando o modelo modelo_mnist.h5.
- Parâmetros:
    image (arquivo): Arquivo de imagem enviado pelo usuário (formato aceito: imagem).
- Retorno:
    Caso haja erro (imagem não enviada): Dicionário JSON com a chave error contendo a mensagem "Nenhuma imagem enviada" e código de status HTTP 400 (Erro de Solicitação Inválida).
    Caso a imagem seja enviada com sucesso: Renderiza o template index.html, passando a variável prediction contendo a classe prevista pelo modelo e deixando a variável prediction_linear como None.

3. Rota de previsão linear (/predict-linear)

- Método: POST (Aceita envios de formulário)
- Descrição: Recebe uma imagem enviada pelo usuário, processa-a e gera uma previsão usando o modelo linear modelo_mnist_linear.h5.
- Parâmetros:
    image (arquivo): Arquivo de imagem enviado pelo usuário (formato aceito: imagem).
- Retorno:
    Caso haja erro (imagem não enviada): Dicionário JSON com a chave error contendo a mensagem "Nenhuma imagem enviada" e código de status HTTP 400 (Erro de Solicitação Inválida).
    Caso a imagem seja enviada com sucesso: Renderiza o template index.html, deixando a variável prediction como None e passando a variável prediction_linear contendo a classe prevista pelo modelo linear.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request com melhorias, correções de bugs ou novas funcionalidades.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
