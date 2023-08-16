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

Exemplos de aplicação do tipo TODO List:
- [todoist](https://todoist.com/pt-BR)
- [Any.do](https://www.any.do/en)
- [Google Keep](https://keep.google.com/)

> ***IMPORTANTE:*** Para a construção da interface com o usuário, considerar uma experiência mínima de utilização do sistema. Para isso, considere o uso de ferramentas de generativas para auxiliar neste processo de criação das interfaces. Sugestões de leitura:
> - [Keep It Simple, but Sensational: o princípio KISS para impactar](https://harve.com.br/blog/marketing-digital-blog/keep-it-simple-but-sensational-o-principio-kiss-para-impactar/)


## Padrão de qualidade

***TODO***

## Instruções:

***TODO***
