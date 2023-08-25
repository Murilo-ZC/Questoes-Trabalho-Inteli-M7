<img src="../static/logo-inteli.png" alt="Logo do Inteli" style="height: 100%; width:50vp; display: block; margin-left: auto; margin-right: auto; margin-bottom:16px"/>

# Atividade 3: Deploy de modelo de Machine Learning na Nuvem

## Enunciado

Construção e deploy de um modelo de predição ou classificação criados pelos alunos. Este modelo deve ser deployado em uma nuvem comercial e uma API de acesso a ele deve ser desenvolvida.

> ***IMPORTANTE 1:*** Para está entrega, não é necessário construir uma interface de usuário para o modelo, como um frontend. Apenas a API de acesso ao modelo deve ser desenvolvida. 

***IMPORTANTE 2:*** Para está entrega, dois pontos são obrigatórios: 

1. A utilização do Python com o FastAPI para realizar a construção da API;
2. O deploy com o imagens de containers no DockerHub.

O estudante deve escolher um conjunto de dados dentre os relacionados abaixo. Qualquer conjunto diferente destes deve ser aprovado pelo professor. Toda a manipulação realizada com os dados deve ser descrita na documentação do projeto.

O conjunto de dados escolhido deve ser utilizado para a construção de um modelo de predição ou classificação. O modelo deve ser construído utilizando o Python e o framework de Machine Learning de preferência do estudante. A escolha do modelo deve ser justificada pelo estudante.

O ambiente de desenvolvimento deve ser documentado, assim como o ambiente de produção. Um video deve ser gravado apresentado o processo de utilização do modelo em produção.

> ***IMPORTANTE:*** Depois de gravado o comportamento do projeto em produção, o estudante deve remover os recursos alocados na nuvem comercial. Apenas o vídeo será utilizado para a avaliação do projeto, em conjunto com os códigos fontes desenvolvidos.

### Datasets sugeridos:

- [Flight Delay](https://www.kaggle.com/datasets/arvindnagaonkar/flight-delay)
- [Brazil: Total highway crashes 2010 - 2023](https://www.kaggle.com/datasets/liamarguedas/brazil-total-highway-crashes-2010-2023)
- [Customer Segmentation](https://www.kaggle.com/datasets/joebeachcapital/customer-segmentation)
- [Startups](https://www.kaggle.com/datasets/joebeachcapital/startups)
- [Phone Activity Detailed Data](https://www.kaggle.com/datasets/atharvaarya25/phone-usage-dataset)
- [Global YouTube Statistics 2023](https://www.kaggle.com/datasets/nelgiriyewithana/global-youtube-statistics-2023)

## Padrão de qualidade

Os pontos que serão avaliados na entrega do projeto:
1. ***(Até 1.0 ponto)*** Construção do dockerfile: o arquivo contem todas as informações necessárias para a construção da imagem dos containers para produção;
2. ***(Até 1.0 ponto)*** Publicação das Imagens para a API: a API foi publicada corretamente na cloud;
3. ***(Até 1.0 ponto)*** Documentação do ambiente de desenvolvimento: documentar o ambiente de desenvolvimento (não precisa estar dockerizado), seus requisitos e como executar o projeto. Exportar os notebooks temporários que foram utilizados em seu desenvolvimento;
4. ***(Até 1.0 ponto)*** Documentação da API e seu funcionamento;
5. ***(Até 1.0 ponto)*** Descrever qual modelo de Machine Learning foi escolhido e justificar sua escolha: essa justificativa pode vir da comparação entre diversos modelos que foram previamente aplicados;
6. ***(Até 1.0 ponto)*** As instruções no arquivo README foram suficientes para executar a aplicação: as instruções no arquivo README foram suficientes para executar a aplicação APENAS SEGUINDO OS PASSOS CONTIDOS NO DOCUMENTO;
7. ***(Até 2.0 pontos)*** Treinamento do modelo;
8. ***(Até 2.0 pontos)*** Pré-processamento dos dados;

## Instruções:

A entrega do projeto deve ser realizada dentro de um repositório público do Github do estudante. Ao entregar a atividade no sistema da instituição, o estudante deve colocar o link para seu repositório.

O arquivo README do repositório deve conter as informações do estudante, o link para o Dockerhub onde a imagem está hospedada, o que foi desenvolvido (uma breve descrição de até 200 palavras) e o procedimento necessário para executar a aplicação (considerando que o container runtime já está instalado no sistema do usuário).

Deve ser entregue também um video demonstrando o funcionamento do modelo deployado.

## Prazo de Entrega:

O prazo oficial de entrega é até o dia 01/09/2023. Entretanto, entregas serão aceitas até o dia 10/09/2023 (23h59).