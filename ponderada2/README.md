<img src="../static/logo-inteli.png" alt="Logo do Inteli" style="height: 100%; width:50vp; display: block; margin-left: auto; margin-right: auto; margin-bottom:16px"/>

# Atividade 2: Criação de uma aplicação protegida com CRUD

## Enunciado

Esta atividade tem por objetivo desenvolver um projeto web que possibilite os usuários registrarem dados em um banco de dados. O deploy do banco, da API do backend e do frontend deve acontecer utilizando uma aplicação com multiplos containers. A aplicação não precisa utilizar frameworks, pode ser realizada utilizando os primitivos presentes na linguagem de programação escolhida.

> ***ESCLARECIMENTO:*** Quem iniciou a atividade com nuvem comercial pode continuar seu desenvolvimento utilizando a solução de nuvem comercial. Contudo, os pontos avaliados não demandam sua utilização. ***NÃO SERÃO PREJUDICADOS QUEM OPTAR POR REALIZAR O DESENVOLVIMENTO APENAS LOCAL.*** Portanto, onde lia-se *utilizando uma nuvem comercial*, considerar apenas ***utilizando uma aplicação com multiplos containers***.

> ***PONTO DE ATENÇÃO:*** Nas atividades anteriores, foi considerado o processo de criação de um ambiente virtual para a criação do arquivo *requiments.txt*, para todos que escolherem utilizar Python como sua linguagem padrão. Nesta atividade, escrever apenas o arquivo *requirements.txt*, sem a criação do ambiente virtual. Para este projeto, espera-se encontrar no ***MÍNIMO*** a aplicação dividida em 2 containers, sendo que o recomendado é a sua divisão em 3 containers.

### Divisão do projeto em containers:

- Para os projetos que vão trabalhar com 2 containers:
    - Container da aplicação (interface e backend);
    - Container do banco de dados.

- Para os projetos que vão trabalhar com 3 containers:
    - Container da interface com o usuário (frontend da aplicação);
    - Container do sistema de API (backend da aplicação);
    - Container do banco de dados.

A escolha de uma das estratégias está totalmente vinculada a experiência que o estudante deseja praticar. De qualquer forma, será encessário justificar a escolha da arquitetura utilizada para a solução. Esperá-se encontrar na entrega do projeto:

- Arquitetura da solução utilizada (no arquivo README do projeto) e a justificativa de sua escolha;
- Um arquivo docker-compose para o lançamento da aplicação;
- Instruções para lançar a aplicação;
- Instruções para utilizar a aplicação;
- Uma descrição da estrutura de dados utilizada para armazenar os dados no banco de dados;
- Uma tela de login para entrar no sistema;
- Uma tela para ver os dados cadastrados;
- Uma tela para cadastrar novas entradas de dados.

O projeto consiste em um TODO List, onde o usuário deve se cadastrar no sistema (considerar o usuário **teste**, com a senha **teste123**) para ter acesso a suas notas e adicionar novas notas. ***NÃO É NECESSÁRIO REALIZAR A IMPLEMENTAÇÃO DE CADASTRO DE USUÁRIOS OU TELA/FUNCIONALIDADE DE RECUPERAÇÃO DE SENHA.***

A imagem do banco de dados que será utilizada pode ser de qualquer banco de dados **RELACIONAL**. A aplicação pode ser desenvolvida em Python ou em JavaScript.

Exemplos de aplicação do tipo TODO List:
- [todoist](https://todoist.com/pt-BR)
- [Any.do](https://www.any.do/en)
- [Google Keep](https://keep.google.com/)

> ***IMPORTANTE:*** Para a construção da interface com o usuário, considerar uma experiência mínima de utilização do sistema. Para isso, considere o uso de ferramentas de generativas para auxiliar neste processo de criação das interfaces. Sugestões de leitura:
> - [Keep It Simple, but Sensational: o princípio KISS para impactar](https://harve.com.br/blog/marketing-digital-blog/keep-it-simple-but-sensational-o-principio-kiss-para-impactar/)


## Padrão de qualidade

Os pontos que serão avaliados na entrega do projeto:
1. ***(Até 1.0 ponto)*** Construção do dockerfile: o arquivo contem todas as informações necessárias para a construção da imagem dos containers;
2. ***(Até 1.0 ponto)*** Publicação das Imagens no DockerHub: todas as imagens construídas para a aplicação estão publicadas no DockerHub;
3. ***(Até 1.0 ponto)*** Construção do docker-compose: o arquivo contem todas as informações necessárias para lançar os containers da aplicação;
4. ***(Até 1.0 ponto)*** A arquitetura da solução foi apresentada: a arquitetura utilizada foi apresentada e sua escolha foi justificada pelo estudante;
5. ***(Até 1.0 ponto)*** A aplicação foi executada em um conjunto de containers Docker;
6. ***(Até 1.0 ponto)*** As instruções no arquivo README foram suficientes para executar a aplicação: as instruções no arquivo README foram suficientes para executar a aplicação APENAS SEGUINDO OS PASSOS CONTIDOS NO DOCUMENTO;
7. ***(Até 1.0 ponto)*** A aplicação apresenta uma tela de login;
8. ***(Até 1.0 ponto)*** A aplicação apresenta uma tela com as notas enviadas pelo usuário;
9. ***(Até 1.0 ponto)*** A aplicação protege as rotas da tela de login para apresentar elas apenas para usuário logados no sistema;
10. ***(Até 1.0 ponto)*** A estrutura de pastas utilizada no projeto foi apresentada no arquivo README do projeto.


## Instruções:

A entrega do projeto deve ser realizada dentro de um repositório público do Github do estudante. Ao entregar a atividade no sistema da instituição, o estudante deve colocar o link para seu repositório.
O arquivo README do repositório deve conter as informações do estudante, o link para o Dockerhub onde a imagem está hospedada, o que foi desenvolvido (uma breve descrição de até 200 palavras) e o procedimento necessário para executar a aplicação (considerando que o container runtime já está instalado no sistema do usuário).

## Prazo de Entrega:

As entregas serão consideradas até as 23h59 do dia 27/08/2023. Será considerado o último commit antes do prazo de entrega.
