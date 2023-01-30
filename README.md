# Servidor de Nomes Distribuído
## Objetivo
  O projeto tem como objetivo implementar um servidor de nomes estruturados de comunicação cliente-servidor de maneira síncrona, single thread, stateless e recursivo. Um servidor de nomes tem como função armazenar informações referentes a entidades; no caso deste trabalho, foi definido que o projeto seria similar ao modelo DNS (Domain Name Server), cujo objetivo do servidor seria armazenar URLs e traduzir os seus respectivos endereços IPs mediante solicitação do cliente.


## Estrutura
  O resolver cliente é capaz de se conectar apenas com o servidor local, fazendo uma requisição e aguardando a resposta. Este servidor de nomes local contém um arquivo de cache com poucos nomes, caso ele consiga resolver, o hostname retorna o IP do servidor desejado, caso contrário, o local requisita para o servidor raiz que contém outro arquivo com uma coleção maior para resolver nomes em específico; se este também não conseguir resolver, é feita uma avaliação do hostname para identificar para qual outro servidor mandar(.br ou . us), que por sua vez possuem a mesma estrutura de resolução de nomes do raiz porém com uma coleção de nomes focada apenas no domínio que o servidor se propõe; entretanto caso não sejam capaz de resolver, retornam o código 404 para os servidores anteriores sequencialmente até o resolver. Essa estrutura do servidor de nomes é conhecida como recursiva.
  A conexão entre os servidores é feita através do módulo socket que foi configurado para utilizar UDP e IPV4. <br><br>

## Desenvolvedores
| [<img src="https://avatars.githubusercontent.com/u/80076522?s=400&u=3342a0dfdb1a853f8666e88bdda42b0d2554dddb&v=4" width=115><br><sub>Victor Hugo Alves</sub>](https://github.com/VictorHugoMA) |  [<img src="https://avatars.githubusercontent.com/u/80076882?v=4" width=115><br><sub>Pedro Henrique Santana</sub>](https://github.com/PeSantanna) |  [<img src="https://avatars.githubusercontent.com/u/54860118?v=4" width=115><br><sub>André Alcântara</sub>](https://github.com/andreoalcantara) | [<img src="https://avatars.githubusercontent.com/u/122176833?v=4" width=115><br><sub>Gustavo Ramos</sub>](https://github.com/guxtavoramoz) |
| :---: | :---: | :---: | :---: 
