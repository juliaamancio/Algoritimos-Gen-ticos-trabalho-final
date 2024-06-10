# Algoritimos Genéticos: Trabalho final
Este repositório é referente à matérias de Redes Neurais e Algoritmos Genéticos do curso de Ciência e Tecnologia na Ilum Escola de Ciência. Matéria ministrada pelo professor Daniel Roberto Cassar.

## Equipe 
Davi José, Gabriel Torquato e Júlia Amancio. :D

### Organização do repositório:
* __Readme__: Contém as informações gerais sobre o trabalho abordado, levando em conta objetivo, apresentação do dataset, descrição do repositórios e bibliotecas, além das referências bibliográficas.
* __script_original__: Contém o Script em que estão presentes todas as funções utilizadas no notebook principal.
* __notebook_original__: Nesse notebook, há a apresentação do problema utilizado e o uso das funções contidas no script, além dos resultados obtidos.

### Recomendação de leitura:
* __1) Script original__
* __2) Notebook_original__

### Objetivo do trabalho: 
A proposta do trabalho é utilizar Nondominated Sorting Genetic Algorithm II (NSGA II), que se consiste em um algoritmo evolutivo multiobjetivo. Para isso, foi selecionado o problema BINH1, sendo ele referente a duas funções matemáticas: 
$$f_1(x) = x_1^2 + x_2^2$$ 

$$f_2(x) = (x_1 - 5)^2 + (x_2 - 5)^2$$

em que $x_1$ e $x_2$ são duas variáveis as quais estão restritas ao intervalo

$$ -5 \leq x_i \leq 10$$ 

sendo i = 1,2. O objetivo resume-se à minimização das duas funções através do algoritmo genético, encontrando e retornando um conjunto de valores que apresentam a característica de "não dominados", isto é, os melhores valores possíveis e bem distribuídos que possa atender ao problema multiobjetivo em questão.

### Estratégias adotadas para a execução do trabalho:
O trabalho foi baseado essencialmente no artigo "A Fast and Elitist Multiobjective Genetic Algorithm: NSGA-II", em que trata do algoritmo por meio de 3 pseudocódigos para executar a lógica por trás do modelo. Dessa maneira, esses pseudocódigos foram traduzidos para códigos em Python a fim de poder ser aplicado em uma população fixa. 

#### Funções definidas:
* detalhar cada funcao

### Bibliotecas utilizadas 
* detalhar as bibliotecas

### Referências bibliográficas:
[1] HERRERA, José Ignacio. Otimização Evolutiva Multiobjetivo: Implementação do Algoritmo NSGA-II. In: XXIX Congresso de Iniciação Científica da UNICAMP, 2021, Campinas. Campinas: FEEC/UNICAMP, 2021.
[2] DEB, Kalyanmoy; PRATAP, Amrit; AGARWAL, Sameer; MEYARIVAN, T. A fast and elitist multiobjective genetic algorithm: NSGA-II. IEEE Transactions on Evolutionary Computation, v. 6, n. 2, p. 182-197, abr. 2002.
[3] VARGAS, Dênis E. C. Um estudo dos parâmetros do algoritmo NSGA-II com o operador SBX em problemas de otimização estrutural multiobjetivo. Proceeding Series of the Brazilian Society of Computational and Applied Mathematics, v. 6, n. 2, 2018. Trabalho apresentado no XXXVIII CNMAC, Campinas - SP, 2018. Rio Pomba: Instituto Federal de Educação, Ciência e Tecnologia do Sudeste de Minas Gerais, campus Rio Pomba, 2018.
[4] GÜRÜNLÜ ALMA, Özlem. Genetic algorithm based outlier detection using information criterion. 2009. Dissertação (Mestrado) - Dokuz Eylül University, Graduate School of Natural and Applied Sciences, İzmir, 2009.







