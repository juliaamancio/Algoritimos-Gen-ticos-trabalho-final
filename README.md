# Algoritmos Genéticos: Trabalho final
Este repositório é referente à matérias de Redes Neurais e Algoritmos Genéticos do curso de Ciência e Tecnologia na Ilum Escola de Ciência. Matéria ministrada pelo professor Daniel Roberto Cassar.

## Equipe 
Davi José, Gabriel Torquato e Júlia Amancio. :D

### Organização do repositório:
* __Readme__: Contém as informações gerais sobre o trabalho abordado, levando em conta objetivo, apresentação do dataset, descrição do repositórios e bibliotecas, além das referências bibliográficas.
* __Notebook didático__: 
* __Scripts__: Com um total de 3 scripts, cada um deles contém todas as funções utilizadas no notebook principal.
* __Notebooks de problemas__: Com um total de 3 problemas, há a apresentação do problema utilizado em cada um deles e o uso das funções contidas no script, além dos resultados obtidos.

### Recomendação de leitura:
* __1) Notebook didático__
* __2) Notebook do problema__
* __3) Script do problema__
* __4) Artigos de referência__

### Objetivo do trabalho: 
A proposta do trabalho é utilizar Nondominated Sorting Genetic Algorithm II (NSGA II), que se consiste em um algoritmo evolutivo multiobjetivo. Para isso, foi selecionado três problemas: o problema BINH1, o problema POLONI e o problema ZDT4. Com isso, será encontrado e retornado um conjunto de valores que apresentam a característica de "não dominados", isto é, os melhores valores possíveis e bem distribuídos que possa atender ao problema multiobjetivo em questão.

* __1) Problema BINH1__: refere-se a duas funções matemáticas:
$$f_1(x) = x_1^2 + x_2^2$$ 

$$f_2(x) = (x_1 - 5)^2 + (x_2 - 5)^2$$

em que $x_1$ e $x_2$ são duas variáveis as quais estão restritas ao intervalo

$$ -5 \leq x_i \leq 10$$ 

sendo i = 1,2. O objetivo resume-se à minimização das duas funções através do algoritmo genético, encontrando e retornando um conjunto de valores que apresentam a característica de "não dominados", isto é, os melhores valores possíveis e bem distribuídos que possa atender ao problema multiobjetivo em questão.

* __2) Problema POLONI__: refere-se a duas funções matemáticas:

$$f_1(x) = 1 + (A_1 - B_1)^2 + (A_2 - B_2)^2$$

$$f_2(x) = (x_1 + 3)^2 + (x_2 + 1)^2$$

Sendo os coeficientes:
$$A_1 = 0.5 sin(1) - 2 cos(1) + sin(2) - 1.5 cos(2)$$
$$B_1 = 0.5 sin(x_1) - 2 cos(x_1) + sin(x_2) - 1.5 cos(x_2)$$
$$A_2 = 1.5 sin(1) - cos(1) + 2 sin(2) - 0.5 cos(2)$$
$$B_2 = 1.5 sin(x_1) - cos(x_1) + 2 sin(x_2) - 0.5 cos(x_2)$$

em que $x_1$ e $x_2$ são duas variáveis as quais estão restritas ao intervalo

 $$ -\pi \leq x_i \leq \pi$$

sendo i = 1,2. O objetivo resume-se à minimização das duas funções através do algoritmo genético também aplicado. 

* __3) Problema ZDT4__: refere-se a duas funções matemáticas:
$$f_1(x) = x_1$$

$$f_2(x) = g(x) \big [ 1 - \sqrt{\frac{x_1}{g(x)}} \big ]$$

sendo 

$$g(x) = 1 + 10(n - 1) + \sum_{i=2}^{n} (x^2_i - 10cos(4\pi x_i))$$

em que $x_1$ e $x_i$ são variáveis as quais estão restritas ao intervalo


$$0 \leq x_1 \leq 1$$

$$-5 \leq x_i \leq 5$$ sendo (i = 2, ..., n)


### Estratégias adotadas para a execução do trabalho:
O trabalho foi baseado essencialmente no artigo "A Fast and Elitist Multiobjective Genetic Algorithm: NSGA-II", em que trata do algoritmo por meio de 3 pseudocódigos para executar a lógica por trás do modelo. Dessa maneira, esses pseudocódigos foram traduzidos para códigos em Python a fim de poder ser aplicado em uma população fixa. 

### Bibliotecas utilizadas 
* __Random:__ usada para gerar números pseudoaleatórios.
* __Copy:__ usada para criar cópias de objetos em Python. 

### Referências bibliográficas:
[1] HERRERA, José Ignacio. Otimização Evolutiva Multiobjetivo: Implementação do Algoritmo NSGA-II. In: XXIX Congresso de Iniciação Científica da UNICAMP, 2021, Campinas. Campinas: FEEC/UNICAMP, 2021.

[2] DEB, Kalyanmoy; PRATAP, Amrit; AGARWAL, Sameer; MEYARIVAN, T. A fast and elitist multiobjective genetic algorithm: NSGA-II. IEEE Transactions on Evolutionary Computation, v. 6, n. 2, p. 182-197, abr. 2002.

[3] VARGAS, Dênis E. C. Um estudo dos parâmetros do algoritmo NSGA-II com o operador SBX em problemas de otimização estrutural multiobjetivo. Proceeding Series of the Brazilian Society of Computational and Applied Mathematics, v. 6, n. 2, 2018. Trabalho apresentado no XXXVIII CNMAC, Campinas - SP, 2018. Rio Pomba: Instituto Federal de Educação, Ciência e Tecnologia do Sudeste de Minas Gerais, campus Rio Pomba, 2018.

[4] GÜRÜNLÜ ALMA, Özlem. Genetic algorithm based outlier detection using information criterion. 2009. Dissertação (Mestrado) - Dokuz Eylül University, Graduate School of Natural and Applied Sciences, İzmir, 2009.







