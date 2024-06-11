import random
import copy as c

def cria_gene(valor_min, valor_max):
        
    gene = random.uniform(valor_min, valor_max)
    
    return gene

def cria_candidato(valor_min, valor_max, n):

    candidato = []
    for _ in range(n):
        candidato.append(cria_gene(valor_min, valor_max))
    return candidato

def cria_populacao(tamanho, valor_min, valor_max, n = 2):
    populacao = []
    for _ in range(tamanho):
        populacao.append(cria_candidato(valor_min, valor_max, n))
        
    return populacao

def funcoes_objetivo(candidato):

    f1 = candidato[0]**2 + candidato[1]**2
    f2 = (candidato[0] -  5)**2 + (candidato[1] -  5)**2
    
    return [f1, f2]
    
def funcoes_objetivo_populacao(populacao):
    
    fitness = []
    
    for candidato in populacao:
        fitness.append(funcoes_objetivo(candidato))
    
    return fitness

def verifica_dominancia(candidato_1, candidato_2):
    '''Verifica se o individuo 1 domina o 2'''
    
    pontuacao = 0
    domina = None
    
    objetivos_candidato_1 = funcoes_objetivo(candidato_1)
    objetivos_candidato_2 = funcoes_objetivo(candidato_2)
    
    for o_1, o_2 in zip(objetivos_candidato_1, objetivos_candidato_2):
        if o_1 <= o_2:
            pontuacao += 1
            if o_1 < o_2:
                pontuacao += 1
    
    if pontuacao > 2:
        domina = True
    else:
        domina = False
        
    return domina

def fast_non_dominated_sort(populacao):
    
    numero_dominam = []
    rank = {}
    nao_dominados = [] #lista de manos que não são dominados
    todos_os_dominados = [] #lista que tem como elementos listas que armazenam todos os individuos dominados por cada individuo
    
    for i in range(len(populacao)):
        dominam = 0
        dominados = [] #dominados pelo individuo_1        
        for j in range(len(populacao)):
            
            if i != j:
                
                individuo_1 = populacao[i]
                individuo_2 = populacao[j]

                if verifica_dominancia(individuo_1, individuo_2) == True:
                    dominados.append(tuple(individuo_2))
                elif verifica_dominancia(individuo_2, individuo_1) == True:
                    dominam += 1
    
        if dominam == 0:
            rank[tuple(individuo_1)] = [i, 1] #individuos não dominados tem rank 1
            nao_dominados.append(tuple(individuo_1))
            
        numero_dominam.append(dominam)
        todos_os_dominados.append(dominados)
        
    guarda_nao_dominados = nao_dominados.copy()
    guarda_todos_os_dominados = todos_os_dominados.copy()
    guarda_numero_dominam = numero_dominam.copy()

    contador_rank = 1
    valor_rank = 0
    todas_as_frentes = [] #lista que tem como elementos outras listas, cada uma armazenando todos os individuos das diferentes frentes. Essa lista fica ordenada na ordem de dominancia, começando pelos itens não dominados.
    frente = nao_dominados #inicializamos a primeira frente como os elementos não dominados.

    while frente != []:
        
        nova_frente = []
        
        for individuo_1 in frente:
            
            indice_1 = populacao.index(list(individuo_1)) #as listas: populacao, todos_os_dominados e numero_dominam estão acopladas pelos seus indices.
            
            for individuo_2 in todos_os_dominados[indice_1]:
                indice_2 = populacao.index(list(individuo_2))
                
                numero_dominam[indice_2] -= 1 #toda vez que um individuo está na lista de dominados, ele é penalizado, isso garante que TODOS que estão fora dos não dominados vão receber o rank adequado, mesmo que ele seja dominados por muitos. Ex: de 6 individuos 5 estão na mesma dominancia mas só um é dominado por todos, seu rank ainda será 2 porque ele perde 1 a cada vez q aparece em dominados.
                
                if numero_dominam[indice_2] == 0:#OBS: um individuo pode ser dominado por um conjunto de elementos não-dominados menor que o conjunto de TODOS os elementos não-dominados.
                    valor_rank = contador_rank + 1
                    nova_frente.append(individuo_2)
                
                rank[tuple(individuo_2)] = [indice_2, valor_rank]
            
        contador_rank += 1
        frente_listas = [list(tupla) for tupla in frente]
        todas_as_frentes.append(frente_listas)
        frente = nova_frente
        
    rank = dict(sorted(rank.items(), key = lambda item: item[1][1]))
    
    return rank, todas_as_frentes

def distancia_de_aglomeracao(frente):
    
    tamanho = len(frente)
    distancias = [0] * tamanho
    fitness = funcoes_objetivo_populacao(frente) #nao dominados e fitness são acoplados por indice
    fitness_ordenado = []

    for i in range(tamanho):

        fitness_ordenado.append([frente[i], fitness[i]])

    for k in range(len(fitness[0])):

        fitness_ordenado = sorted(fitness_ordenado, key = lambda item: item[1][k])
        distancias[0] = float('inf')
        distancias[tamanho-1] = float('inf')
        f_min = fitness_ordenado[0][1][k]
        f_max = fitness_ordenado[tamanho-1][1][k]

        for l in range(1, tamanho - 1):
            distancias[l] += (fitness_ordenado[l+1][1][k] - fitness_ordenado[l-1][1][k])/(f_max - f_min)

    return distancias, fitness_ordenado

def aplica_elitismo(rank, todas_as_frentes):
    
    conta_frentes = 1
    distancias_frentes = {}
    fitness_ordenado_dict = {}
    informacoes = c.deepcopy(rank)
    
    for frente in todas_as_frentes:
        
        distancias, fitness_ordenado = distancia_de_aglomeracao(frente)
                
        distancias_frentes[conta_frentes] = distancias
        conta_frentes += 1
        fitness_ordenado_dict[conta_frentes] = fitness_ordenado
        
        for valor in fitness_ordenado:

            index = fitness_ordenado.index(valor)
            chave = tuple(valor[0])
            informacoes[chave].append(distancias[index])
        
    informacoes = dict(sorted(informacoes.items(), key = lambda item: (item[1][1], -item[1][-1])))
    
    return informacoes


def operador_comparacao_de_superlotacao(individuo_1, individuo_2, informacoes):
 
    individuo_1 = tuple(individuo_1)
    individuo_2 = tuple(individuo_2)
    
    #informacoes[individuo_x][0] é o indice do individuo na populacao
    #[...][1] é o rank de Pareto
    #[...][2] é o valor de crowding-distance
    
    if informacoes[individuo_1][1] < informacoes[individuo_2][1]:
        return True
    elif (informacoes[individuo_1][1] == informacoes[individuo_2][1]) and (informacoes[individuo_1][-1] > informacoes[individuo_2][-1]):
        return True
    else:
        return False
                                                                                                                   
def torneio_binario(informacoes):
    
    selecionados = []
    populacao = list(informacoes.keys())
    tamanho_populacao = len(informacoes.keys())
    
    for _ in range(tamanho_populacao):
        
        competidor_1, competidor_2 = random.sample(populacao, 2)
        
        if operador_comparacao_de_superlotacao(competidor_1, competidor_2, informacoes):
            selecionados.append(list(competidor_1))
        else:
            selecionados.append(list(competidor_2))
            
    return selecionados
    
def cruzamento_blx_alpha(pai, mae, chance_de_cruzamento, valor_min, valor_max, alpha = 0, num_filhos = 2):
    
    if random.random() < chance_de_cruzamento:
    
        filhos = []
        
        for _ in range(num_filhos):
            filho = []
            
            for gene_pai, gene_mae in zip(pai, mae):
                
                beta = random.uniform(alpha, alpha+1)
                gene_filho = gene_pai + beta * (gene_mae - gene_pai)
                if valor_min <= gene_filho <= valor_max:
                    filho.append(gene_filho)
                else:
                    gene_filho = random.choice([gene_pai, gene_mae])
                    filho.append(gene_filho)
            
            filhos.append(filho)
                
        return *filhos,
    
    else:
        return pai, mae
    
def mutacao_sucessiva_BINH1(populacao, chance_de_mutacao, chance_mutacao_gene, valor_min, valor_max, taxa_perturbacao = 0.5):
    
    for individuo in populacao:
        if random.random() < chance_de_mutacao:
            for gene in range(len(individuo)):
                if random.random() < chance_mutacao_gene:
                    perturbacao = taxa_perturbacao * individuo[gene]
                    mutacao = random.uniform(-perturbacao, perturbacao)
                    novo_valor = individuo[gene] + mutacao

                    while not (valor_min <= novo_valor <= valor_max):
                        mutacao = random.uniform(-perturbacao, perturbacao)
                        novo_valor = individuo[gene] + mutacao

                    individuo[gene] = novo_valor