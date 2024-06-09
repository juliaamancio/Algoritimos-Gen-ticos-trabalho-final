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
[1] Otimização Evolutiva Multiobjetivo: Implementação do
Algoritmo NSGA-II José Ignacio Herrera [FEEC/UNICAMP] XXIX Congresso de Iniciação Científica da UNICAMP – 2021
[2] A Fast and Elitist Multiobjective Genetic Algorithm:
NSGA-II Kalyanmoy Deb, Associate Member, IEEE, Amrit Pratap, Sameer Agarwal, and T. Meyarivan IEEE TRANSACTIONS ON EVOLUTIONARY COMPUTATION, VOL. 6, NO. 2, APRIL 2002
[3] Um Estudo dos Parˆametros do Algoritmo NSGA-II com o
operador SBX em Problemas de Otimiza¸c˜ao Estrutural
Multiobjetivo
Dˆenis E. C. Vargas1
Instituto Federal de Educa¸c˜ao, Ciˆencia e Tecnologia do Sudeste de Minas Gerais, IF Sudeste MG,
campus Rio Pomba, MG
Proceeding Series of the Brazilian Society of Computational and Applied Mathematics, v. 6, n. 2, 2018.
Trabalho apresentado no XXXVIII CNMAC, Campinas - SP, 2018.
[4] DOKUZ EYLÜL UNIVERSITY
GRADUATE SCHOOL OF NATURAL AND APPLIED SCIENCES
GENETIC ALGORITHM BASED OUTLIER
DETECTION USING INFORMATION CRITERION by Özlem GÜRÜNLÜ ALMA June, 2009 İZMİR







