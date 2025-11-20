## Simulador de Gerenciamento de Memória (Python)

Este projeto em Python simula as estratégias clássicas de alocação e desalocação de memória: **First Fit, Best Fit** e **Worst Fit**. O ambiente de memória é representado por uma matriz bidimensional.

### Estrutura do Projeto

O código é implementado em um único script Python (`tde3.py`) e utiliza a biblioteca `sympy` (embora `X` seja usado como um marcador e não um símbolo matemático, e a biblioteca `random` para inicializar o estado da memória).

### Representação da Memória

A memória é representada por uma **matriz bidimensional**.
* **Espaço Alocado:** Marcado com o símbolo `X` (simbolizado como `sp.symbols('X')`).
* **Espaço Livre:** Marcado com um espaço em branco `' '`.

A alocação inicial da matriz (`matriz(lin, col)`) preenche-a aleatoriamente com `X` ou `' '`.

### Funcionalidades do Menu

O usuário interage com o sistema através de um menu de console:

1.  **Criar Matriz (`matriz(lin, col)`):**
    * Solicita o número de linhas e colunas (devem ser maiores que zero).
    * Inicializa e exibe a matriz com alocação aleatória.
2.  **Alocação First Fit (`ffit()`):**
    * **Estratégia:** Encontra e utiliza o **primeiro bloco** de espaço livre que seja **suficientemente grande** para o tamanho requisitado (`d`).
    * **Lógica:** Percorre a memória sequencialmente até encontrar um espaço livre de tamanho `>= d`.
3.  **Alocação Best Fit (`bfit()`):**
    * **Estratégia:** Busca o bloco de espaço livre que seja o **mais adequado** para o tamanho requisitado (`d`), ou seja, o menor bloco que ainda atenda à necessidade (tamanho $n, n+1, n+2, \dots$).
    * **Lógica:** O código incrementa o tamanho desejado (`d = d + 1`) em um *loop* `while L == []:` até encontrar o bloco mais próximo.
4.  **Alocação Worst Fit (`wfit()`):**
    * **Estratégia:** Aloca a memória na região com o **maior espaço livre** disponível, desde que seja grande o suficiente para o tamanho requisitado.
    * **Lógica:** O código procura o maior bloco livre (sem quebrar o *loop*) e o usa para a alocação, incrementando o tamanho desejado (`d = d + 1`) para forçar o sistema a encontrar blocos maiores disponíveis antes de alocar.
5.  **Desalocação (`des()`):**
    * O usuário informa as coordenadas de **início e fim (linha e coluna)** para a região a ser liberada (desalocada).
    * **Validação:** Garante que todas as coordenadas estejam dentro dos limites da matriz e que a linha inicial não seja maior que a linha final.
    * **Ação:** Define as posições dentro do intervalo como espaço livre (`' '`).

### Operação no Console

O programa é executado em um *loop* infinito (`while True`), permitindo que o usuário realize múltiplas operações sequencialmente:

1.  O menu é exibido.
2.  O usuário seleciona uma opção (1 a 5).
3.  Se a opção for de alocação/desalocação, a matriz é exibida antes e depois da operação.

***
**NOTA SOBRE IMPLEMENTAÇÃO:**
As implementações de **Best Fit** e **Worst Fit** no código focam em encontrar *algum* bloco que satisfaça a condição, mas a lógica de busca do bloco *mais adequado* (Best Fit) ou *pior* (Worst Fit) pode estar simplificada em relação aos algoritmos clássicos que mapeiam todos os buracos livres.
