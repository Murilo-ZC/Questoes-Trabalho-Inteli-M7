<img src="../static/logo-inteli.png" alt="Logo do Inteli" style="height: 100%; width:50vp; display: block; margin-left: auto; margin-right: auto; margin-bottom:16px"/>

# Atividade 1: Criando o ambiente para a execução de uma aplicação containerizada (former: Criando uma conta em uma núvem comercial)

## Enunciado

Este autoestudo tem por objetivo verificar se o estudante consegue criar uma aplicação e um container para executá-la. Espera-se que os estudantes possam criar suas imagens e descrever o que foi necessário para realizar seu desenvolvimento. Espera-se ainda que os estudantes possam buscar as informações complementares para o desenvolvimento da aplicação.

| ***ESCLARECIMENTO:*** Quem iniciou a atividade com nuvem comercial pode continuar seu desenvolvimento utilizando a solução de nuvem comercial. Contudo, os pontos avaliados não demandam sua utilização.

Os estudantes devem criar uma aplicação em Python utilizam algum framework Web (sugesre-se o Flask ou o Fastapi), para apresentar uma página HTML com o currículo do estudante. Alguns modelos de páginas podem ser encontrados em:
- [Exemplo de currículo de programador júnior](https://www.kickresume.com/pt/centro-de-ajuda/programador-junior-1-amostra-de-curriculo/)
- [Eu sou Mario Souto, prazer!](https://mariosouto.com/sobre/)

A aplicação deve ser containerizada e deve ser possível executá-la em um container Docker. O estudante deve descrever o que foi necessário para realizar o desenvolvimento da aplicação e containerização. O estudante deve ainda descrever como executar a aplicação em um container Docker.

O dockerfile deve conter as seguintes informações:
- A imagem base deve ser a imagem oficial do Python (a escolha do estudante)
- A imagem deve instalar o framework web escolhido
- A imagem deve copiar o código fonte da aplicação para o container
- A imagem deve expor a porta 80
- A imagem deve executar o comando para iniciar a aplicação
- A imagem deve estar publicada no Dockerhub

| ***old:*** Este autoestudo tem por objetivo verificar se o aluno estudante conseguiu criar sua conta em uma nuvem comercial e se ele possui os conhecimentos mínimos para realizar sua manipulação. 

## Padrão de qualidade

Os pontos que serão avaliados na entrega do projeto:
1. ***(Até 3.0 pontos)*** Construção do dockerfile: o arquivo contem todas as informações necessárias para a construção da imagem
2. ***(Até 1.0 pontos)*** A imagem foi construída sem problemas: com o arquivo fonte fornecido, foi possível construir a imagem
3. (Até 2.0 pontos) A imagem foi publicada no Dockerhub: a imagem está disponível no Dockerhub
4. ***(Até 1.0 ponto)*** A aplicação foi executada em um container Docker: a aplicação foi executada em um container Docker
5. ***(Até 2.0 pontos)*** As instruções no arquivo README foram suficientes para executar a aplicação: as instruções no arquivo README foram suficientes para executar a aplicação APENAS SEGUINDO OS PASSOS CONTIDOS NO DOCUMENTO.
6. ***(Até 1.0 ponto)*** A aplicação apresenta o currículo do estudante: a aplicação apresenta o currículo do estudante

## Instruções:

A entrega do projeto deve ser realizada dentro de um repositório público do Github do estudante. Ao entregar a atividade no sistema da instituição, o estudante deve colocar o link para seu repositório.
O arquivo README do repositório deve conter as informações do estudante, o link para o Dockerhub onde a imagem está hospedada, o que foi desenvolvido (uma breve descrição de até 200 palavras) e o procedimento necessário para executar a aplicação (considerando que o container runtime já está instalado no sistema do usuário).

## Prazo de Entrega:

As entregas serão consideradas até as 23h59 do dia 13/08/2023. Será considerado o último commit antes do prazo de entrega.
