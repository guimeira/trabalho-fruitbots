# Trabalho de Programação - FruitBots
![FruitBots](/imagem.png?raw=true)
Este repositório contém os arquivos para um trabalho final que passei para meus alunos da disciplina de Algoritmos e Estruturas de Dados no Instituto Federal do Espírito Santo.
O trabalho é uma versão do desafio apresentado no site [fruitbots.org](http://fruitbots.org/), onde dois robôs disputam para decidir quem tem a melhor estratégia para coletar frutas.
Este trabalho exercita conceitos básicos de programação como condicionais, loops e uso de estruturas de dados como listas e dicionários. Além disso, por não haver uma solução "correta", isso incentiva os alunos a usarem a criatividade ao desenvolverem suas estratégias. A realização de um pequeno torneio ao final do trabalho também cria uma competição saudável e divertida entre os alunos.

## Regras do jogo:
A arena de jogo é populada aleatoriamente com 5 melancias, 3 bananas e uma maçã.
A cada rodada cada um dos oponentes deve se movimentar em uma de 4 direções: para cima, para baixo, para a direita ou para a esquerda.
Ao se movimentar para uma casa ocupada por uma fruta, o robô automaticamente coleta aquela fruta (esta regra difere da regra do FruitBots original, onde coletar a fruta gasta uma jogada).
Se ambos os robôs capturam uma fruta ao mesmo tempo, cada um recebe 0.5 fruta.
Vence o robô que obtiver a maior quantidade de frutas no maior número de categorias.

## Instruções:
Este repositório contém uma implementação em Python do jogo, em `trabalho.py`, além de implementações básicas para os dois oponentes em `robo-0.py` e `robo-1.py`. O aluno deve modificar um dos robôs. Para iniciar o programa, execute o arquivo `trabalho.py` usando um interpretador Python 3.
A interface gráfica é feita com Tk, que está disponível por padrão na maioria das instalações do Python e não deve requerer nenhuma instalação adicional.

## Documentação:
O código possui alguns comentários para facilitar a compreensão de alunos que queiram entender como o jogo funciona internamente. O arquivo `robo-0.py` apresenta uma descrição detalhada de todos os parâmetros da função a ser implementada pelos alunos.
Na pasta `docs` há um PDF com slides que usei para apresentar o trabalho.
Um vídeo da aula explicando o trabalho também está disponível no YouTube:
[![Video](https://img.youtube.com/vi/EnxGcpZni3c/0.jpg)](https://www.youtube.com/watch?v=EnxGcpZni3c)

## Torneio
Na aula final da disciplina foi feita a apresentação dos trabalhos. Após a apresentação, fizemos um pequeno torneio onde os robôs competiram entre si.
Na pasta `docs` há uma planilha do LibreOffice Calc que permite organizar um pequeno torneio com 8 competidores.
Na pasta `Resultados` da planilha é possível preencher o nome dos grupos, e o nome dos robôs. Há uma coluna aleatória próxima aos nomes que pode ser usada para misturar a ordem dos grupos. Para isso, basta selecionar a as três colunas (aleatória, grupo e robô) e ordenar pela coluna aleatória.
Também na pasta `Resultados` da planilha, há as etapas da competição. Ao marcar um `X` (maiúsculo) no time vencedor, todo o restante da planilha é atualizado, incluindo as chaves do campeonato na pasta `Chaves`.

## Perguntas frequentes (que ninguém perguntou):
**Por que não usar a implementação original do FruitBots?**
Apesar de o site aceitar robôs em Python, a [versão standalone](https://github.com/scribd/robot-fruit-hunt) do jogo suporta apenas Javascript. Como a disciplina foi dada em Python, foi preciso criar uma nova implementação.

**Posso usar esse trabalho com meus alunos?**
Claro! Também adoraria saber o resultado do uso deste trabalho em outras turmas. Fique à vontade para usar a página de Issues para relatar sua experiência, ou sugerir melhorias.

