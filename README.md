# Sistema de Produtos - Semana 04

Projeto desenvolvido como Desafio Sprint 4 da disciplina de Desenvolvimento em Python.

## Objetivo

O objetivo do projeto é aplicar estruturas de dados fundamentais do Python através de um sistema de cadastro e análise de produtos.

Os principais conceitos utilizados são:

- listas;
- dicionários;
- tuplas;
- conjuntos;
- filtros;
- ordenação;
- funções;
- laços de repetição;
- entrada de dados;
- formatação utilizando f-strings.

Também foi desenvolvida uma versão equivalente da lógica em Portugol, demonstrando como as mesmas funcionalidades podem ser implementadas utilizando vetores e algoritmos manuais.

## Estrutura

```text
python-produtos-semana-04/
│
├── sistema_produtos.py
├── portugol_comentado.py
└── README.md
```

## Cadastro de produtos

O programa solicita ao usuário:

- nome;
- preço;
- categoria.

Cada produto é armazenado em um dicionário.

Os dicionários são adicionados a uma lista através do método:

```python
append()
```

## Filtragem por preço

O usuário informa um valor e pode escolher visualizar:

- produtos acima do valor informado;
- produtos abaixo do valor informado.

## Ordenação

O programa demonstra duas formas de ordenação.

### Crescente

É utilizado:

```python
sort()
```

O método `sort()` modifica a própria lista.

### Decrescente

É utilizado:

```python
sorted(..., reverse=True)
```

A função `sorted()` cria uma nova lista ordenada sem modificar a lista original.

## Categorias únicas

As categorias são armazenadas em um:

```python
set()
```

O conjunto elimina valores repetidos automaticamente.

Assim, se vários produtos pertencem à mesma categoria, ela aparece apenas uma vez no resultado.

## Estatísticas

O projeto calcula:

- menor preço;
- maior preço;
- média dos preços.

São utilizadas:

```python
min()
max()
sum()
len()
```

Os três resultados são armazenados em uma tupla:

```python
estatisticas = (
    menor_preco,
    maior_preco,
    media_precos
)
```

A tupla é adequada porque representa um conjunto de valores que não precisa ser alterado posteriormente.

## Relatório final

O relatório utiliza f-strings para apresentar os valores de maneira organizada.

Exemplo:

```python
print(
    f"Preço: R$ {produto['preco']:.2f}"
)
```

O formato:

```text
:.2f
```

faz com que os valores monetários sejam apresentados com duas casas decimais.

## Equivalência em Portugol

O arquivo:

```text
portugol_comentado.py
```

contém a versão lógica equivalente em Portugol.

O código está comentado para que o arquivo continue sendo válido como arquivo Python e não provoque erros de execução.

Na versão em Portugol são utilizados:

- vetores de tamanho fixo;
- laços `para`;
- comparações;
- variáveis auxiliares;
- Bubble Sort;
- verificação manual de valores repetidos.

## Bubble Sort

Como não é utilizado o `sort()` do Python na versão em Portugol, a ordenação é feita manualmente utilizando Bubble Sort.

O algoritmo compara elementos vizinhos e troca suas posições quando estão fora da ordem desejada.

São utilizados dois laços de repetição.

A mesma lógica é demonstrada tanto para ordem crescente quanto para ordem decrescente.

## Simulação de conjuntos

No Python, valores repetidos podem ser eliminados facilmente utilizando:

```python
set()
```

Na versão em Portugol, isso é feito manualmente.

Cada categoria é comparada com as categorias já armazenadas.

Somente categorias ainda não existentes são adicionadas ao vetor de categorias únicas.

## PEP 8

Os nomes das variáveis e funções utilizam `snake_case`, seguindo as recomendações de estilo da PEP 8.

Exemplos:

```python
produtos_filtrados
categorias_unicas
menor_preco
calcular_estatisticas
```

## Como executar

Abra o terminal na pasta do projeto e execute:

```bash
python sistema_produtos.py
```

Em alguns sistemas também pode ser necessário utilizar:

```bash
python3 sistema_produtos.py
```

Depois, siga as instruções exibidas no terminal para cadastrar os produtos e gerar o relatório.

## Autor

Rafael Tajra
