# Atividade 1: Criando o ambiente para a execução de uma aplicação containerizada (former: Criando uma conta em uma núvem comercial)

## Enunciado

Os estudantes devem criar uma aplicação em Python utilizam algum framework Web (sugesre-se o Flask ou o Fastapi), para apresentar uma página HTML com o currículo do estudante. A aplicação deve ser containerizada e deve ser possível executá-la em um container Docker. O estudante deve descrever o que foi necessário para realizar o desenvolvimento da aplicação e containerização. O estudante deve ainda descrever como executar a aplicação em um container Docker.

## O que foi desenvolvido

Foi desenvolvido uma aplicação em Python utilizando o framework Flask, para apresentar uma página HTML com o currículo. Para a execução da aplicação foi criado um arquivo Dockerfile, que contém todas as informações necessárias para a construção da imagem. A imagem foi construída e publicada no Dockerhub. A aplicação foi executada em um container Docker e apresenta a página HTML com o currículo.

## Estrutura das pastas

 <pre><code>
ponderada_1/
│
├── Solução/
│   │
│   ├──app/
│   │   │
│   │   ├── static/
│   |   |    |── estilo.css
│   |   |    └── Foto-Jean.jpeg
|   |   |
│   |   |── templates/
│   │   |   |── index.html
│   │   ├── requirements.txt
│   │   └── main.py
│   │
|   ├── venv/
│   │
└── └── Dockerfile
 </code></pre>

 ## Instrução de uso da Aplicação

Primeiramente, é necessário clonar a imagem do [Dockerhub](https://hub.docker.com/repository/docker/jeanrothstein/ponderada1/general):

<pre><code>
docker pull jeanrothstein/ponderada1:latest
</code></pre>

Após isso, é necessário executar a imagem com a porta 80:
<pre><code>
docker run -p 80:80 ponderada1
</code></pre>
Por fim, o servidor estará rodando na porta 80, e para acessar a página basta digitar no navegador: http://localhost:80/