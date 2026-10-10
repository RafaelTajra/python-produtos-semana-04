# ======================================================
# VERSÃO EQUIVALENTE EM PORTUGOL
# ======================================================
#
# Este arquivo demonstra a mesma lógica do programa
# sistema_produtos.py utilizando conceitos de Portugol.
#
# Todo o código está comentado para que o arquivo continue
# sendo um arquivo Python válido e possa ser executado
# sem gerar erros.
#
#
# ======================================================
# 1. DECLARAÇÃO DE VETORES
# ======================================================
#
# programa
# {
#
#     funcao inicio()
#     {
#
#         inteiro quantidade
#         inteiro i
#
#         cadeia nomes[100]
#         real precos[100]
#         cadeia categorias[100]
#
#
#         escreva("Quantos produtos deseja cadastrar? ")
#         leia(quantidade)
#
#
# ======================================================
# 2. CADASTRO DE PRODUTOS
# ======================================================
#
#         para (i = 0; i < quantidade; i++)
#         {
#
#             escreva("\nProduto ", i + 1, "\n")
#
#             escreva("Nome: ")
#             leia(nomes[i])
#
#             escreva("Preço: ")
#             leia(precos[i])
#
#             escreva("Categoria: ")
#             leia(categorias[i])
#
#         }
#
#
# ======================================================
# 3. FILTRAGEM POR PREÇO
# ======================================================
#
#         real valor_limite
#         inteiro opcao
#
#
#         escreva("\nDigite o valor para filtragem: ")
#         leia(valor_limite)
#
#
#         escreva("\n1 - Produtos acima do valor")
#         escreva("\n2 - Produtos abaixo do valor")
#
#         leia(opcao)
#
#
#         para (i = 0; i < quantidade; i++)
#         {
#
#             se (opcao == 1)
#             {
#
#                 se (precos[i] > valor_limite)
#                 {
#
#                     escreva(
#                         "\n",
#                         nomes[i],
#                         " - R$ ",
#                         precos[i]
#                     )
#
#                 }
#
#             }
#
#
#             senao se (opcao == 2)
#             {
#
#                 se (precos[i] < valor_limite)
#                 {
#
#                     escreva(
#                         "\n",
#                         nomes[i],
#                         " - R$ ",
#                         precos[i]
#                     )
#
#                 }
#
#             }
#
#         }
#
#
# ======================================================
# 4. ORDENAÇÃO CRESCENTE - BUBBLE SORT
# ======================================================
#
#         inteiro j
#         real preco_auxiliar
#         cadeia nome_auxiliar
#         cadeia categoria_auxiliar
#
#
#         para (i = 0; i < quantidade - 1; i++)
#         {
#
#             para (j = 0; j < quantidade - 1 - i; j++)
#             {
#
#                 se (precos[j] > precos[j + 1])
#                 {
#
#                     preco_auxiliar = precos[j]
#
#                     precos[j] = precos[j + 1]
#
#                     precos[j + 1] = preco_auxiliar
#
#
#                     nome_auxiliar = nomes[j]
#
#                     nomes[j] = nomes[j + 1]
#
#                     nomes[j + 1] = nome_auxiliar
#
#
#                     categoria_auxiliar = categorias[j]
#
#                     categorias[j] = categorias[j + 1]
#
#                     categorias[j + 1] = categoria_auxiliar
#
#                 }
#
#             }
#
#         }
#
#
#         escreva("\nProdutos em ordem crescente:")
#
#
#         para (i = 0; i < quantidade; i++)
#         {
#
#             escreva(
#                 "\n",
#                 nomes[i],
#                 " - R$ ",
#                 precos[i]
#             )
#
#         }
#
#
# ======================================================
# 5. ORDENAÇÃO DECRESCENTE - BUBBLE SORT
# ======================================================
#
#         para (i = 0; i < quantidade - 1; i++)
#         {
#
#             para (j = 0; j < quantidade - 1 - i; j++)
#             {
#
#                 se (precos[j] < precos[j + 1])
#                 {
#
#                     preco_auxiliar = precos[j]
#
#                     precos[j] = precos[j + 1]
#
#                     precos[j + 1] = preco_auxiliar
#
#
#                     nome_auxiliar = nomes[j]
#
#                     nomes[j] = nomes[j + 1]
#
#                     nomes[j + 1] = nome_auxiliar
#
#
#                     categoria_auxiliar = categorias[j]
#
#                     categorias[j] = categorias[j + 1]
#
#                     categorias[j + 1] = categoria_auxiliar
#
#                 }
#
#             }
#
#         }
#
#
#         escreva("\nProdutos em ordem decrescente:")
#
#
#         para (i = 0; i < quantidade; i++)
#         {
#
#             escreva(
#                 "\n",
#                 nomes[i],
#                 " - R$ ",
#                 precos[i]
#             )
#
#         }
#
#
# ======================================================
# 6. SIMULAÇÃO DE CONJUNTO DE CATEGORIAS
# ======================================================
#
#         cadeia categorias_unicas[100]
#
#         inteiro quantidade_categorias_unicas = 0
#
#         logico repetida
#
#
#         para (i = 0; i < quantidade; i++)
#         {
#
#             repetida = falso
#
#
#             para (
#                 j = 0;
#                 j < quantidade_categorias_unicas;
#                 j++
#             )
#             {
#
#                 se (
#                     categorias[i]
#                     == categorias_unicas[j]
#                 )
#                 {
#
#                     repetida = verdadeiro
#
#                 }
#
#             }
#
#
#             se (repetida == falso)
#             {
#
#                 categorias_unicas[
#                     quantidade_categorias_unicas
#                 ] = categorias[i]
#
#
#                 quantidade_categorias_unicas++
#
#             }
#
#         }
#
#
#         escreva("\nCategorias únicas:")
#
#
#         para (
#             i = 0;
#             i < quantidade_categorias_unicas;
#             i++
#         )
#         {
#
#             escreva(
#                 "\n",
#                 categorias_unicas[i]
#             )
#
#         }
#
#
# ======================================================
# 7. ESTATÍSTICAS
# ======================================================
#
#         real menor_preco
#         real maior_preco
#         real soma
#         real media
#
#
#         menor_preco = precos[0]
#
#         maior_preco = precos[0]
#
#         soma = 0
#
#
#         para (i = 0; i < quantidade; i++)
#         {
#
#             se (precos[i] < menor_preco)
#             {
#
#                 menor_preco = precos[i]
#
#             }
#
#
#             se (precos[i] > maior_preco)
#             {
#
#                 maior_preco = precos[i]
#
#             }
#
#
#             soma = soma + precos[i]
#
#         }
#
#
#         media = soma / quantidade
#
#
# ======================================================
# 8. RELATÓRIO FINAL
# ======================================================
#
#         escreva("\n\n===== RELATÓRIO FINAL =====")
#
#
#         para (i = 0; i < quantidade; i++)
#         {
#
#             escreva(
#                 "\nProduto: ",
#                 nomes[i],
#                 " | Preço: R$ ",
#                 precos[i],
#                 " | Categoria: ",
#                 categorias[i]
#             )
#
#         }
#
#
#         escreva(
#             "\n\nMenor preço: R$ ",
#             menor_preco
#         )
#
#
#         escreva(
#             "\nMaior preço: R$ ",
#             maior_preco
#         )
#
#
#         escreva(
#             "\nMédia dos preços: R$ ",
#             media
#         )
#
#
#     }
#
# }
#
#
# ======================================================
# COMPARAÇÃO COM PYTHON
# ======================================================
#
# PYTHON:
#
# produtos.append(...)
#
# PORTUGOL:
#
# O valor é colocado manualmente na próxima posição
# disponível do vetor.
#
#
# PYTHON:
#
# set(categorias)
#
# PORTUGOL:
#
# É necessário percorrer o vetor e comparar manualmente
# cada categoria para impedir valores duplicados.
#
#
# PYTHON:
#
# lista.sort()
#
# PORTUGOL:
#
# A ordenação foi implementada manualmente utilizando
# Bubble Sort e dois laços para.
#
#
# PYTHON:
#
# min(), max(), sum() e len()
#
# PORTUGOL:
#
# Os valores são calculados manualmente utilizando
# variáveis acumuladoras, comparações e laços.
