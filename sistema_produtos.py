# ======================================================
# DESAFIO SPRINT 4
# SISTEMA DE PRODUTOS
# ======================================================


def ler_quantidade_produtos():
    """Lê e valida a quantidade de produtos."""

    while True:
        try:
            quantidade = int(
                input("Quantos produtos deseja cadastrar? ")
            )

            if quantidade <= 0:
                print("Digite uma quantidade maior que zero.")
                continue

            return quantidade

        except ValueError:
            print("Digite um número inteiro válido.")


def ler_preco():
    """Lê e valida o preço de um produto."""

    while True:
        try:
            preco = float(
                input("Preço do produto: R$ ")
            )

            if preco <= 0:
                print("O preço deve ser maior que zero.")
                continue

            return preco

        except ValueError:
            print("Digite um preço válido.")


def cadastrar_produtos():
    """Cadastra produtos utilizando lista e append()."""

    produtos = []

    quantidade_produtos = ler_quantidade_produtos()

    print("\n===== CADASTRO DE PRODUTOS =====")

    for indice in range(quantidade_produtos):

        print(
            f"\nProduto {indice + 1}"
        )

        nome = input(
            "Nome do produto: "
        ).strip()

        while nome == "":
            print("O nome não pode ficar vazio.")

            nome = input(
                "Nome do produto: "
            ).strip()

        preco = ler_preco()

        categoria = input(
            "Categoria do produto: "
        ).strip()

        while categoria == "":
            print("A categoria não pode ficar vazia.")

            categoria = input(
                "Categoria do produto: "
            ).strip()

        produto = {
            "nome": nome,
            "preco": preco,
            "categoria": categoria
        }

        produtos.append(produto)

    return produtos


def filtrar_produtos(produtos):
    """Filtra os produtos por um valor informado."""

    print("\n===== FILTRAGEM POR PREÇO =====")

    while True:
        try:
            valor_limite = float(
                input("Digite o valor para filtragem: R$ ")
            )

            break

        except ValueError:
            print("Digite um valor válido.")

    print("\nEscolha o tipo de filtragem:")
    print("1 - Produtos acima do valor")
    print("2 - Produtos abaixo do valor")

    while True:

        opcao = input(
            "Opção: "
        ).strip()

        if opcao == "1":

            produtos_filtrados = [
                produto
                for produto in produtos
                if produto["preco"] > valor_limite
            ]

            tipo_filtro = "acima"

            break

        if opcao == "2":

            produtos_filtrados = [
                produto
                for produto in produtos
                if produto["preco"] < valor_limite
            ]

            tipo_filtro = "abaixo"

            break

        print("Escolha 1 ou 2.")

    return produtos_filtrados, valor_limite, tipo_filtro


def ordenar_produtos(produtos):
    """Ordena produtos de forma crescente e decrescente."""

    # Cópia da lista para não alterar a lista original.
    produtos_crescente = produtos.copy()

    # sort() modifica a própria lista.
    produtos_crescente.sort(
        key=lambda produto: produto["preco"]
    )

    # sorted() cria uma nova lista.
    produtos_decrescente = sorted(
        produtos,
        key=lambda produto: produto["preco"],
        reverse=True
    )

    return produtos_crescente, produtos_decrescente


def obter_categorias_unicas(produtos):
    """Cria um conjunto com categorias sem repetição."""

    categorias_unicas = set()

    for produto in produtos:
        categorias_unicas.add(
            produto["categoria"]
        )

    return categorias_unicas


def calcular_estatisticas(produtos):
    """Calcula menor preço, maior preço e média."""

    precos = [
        produto["preco"]
        for produto in produtos
    ]

    menor_preco = min(precos)

    maior_preco = max(precos)

    media_precos = (
        sum(precos) / len(precos)
    )

    # Tupla imutável.
    estatisticas = (
        menor_preco,
        maior_preco,
        media_precos
    )

    return estatisticas


def exibir_lista_produtos(titulo, produtos):
    """Exibe uma lista de produtos formatada."""

    print(f"\n===== {titulo} =====")

    if not produtos:
        print("Nenhum produto encontrado.")
        return

    for produto in produtos:

        print(
            f"Nome: {produto['nome']} | "
            f"Preço: R$ {produto['preco']:.2f} | "
            f"Categoria: {produto['categoria']}"
        )


def exibir_relatorio_final(
    produtos,
    produtos_filtrados,
    valor_limite,
    tipo_filtro,
    produtos_crescente,
    produtos_decrescente,
    categorias_unicas,
    estatisticas
):
    """Exibe o relatório final utilizando f-strings."""

    print("\n")
    print("=" * 55)
    print("RELATÓRIO FINAL")
    print("=" * 55)

    exibir_lista_produtos(
        "TODOS OS PRODUTOS",
        produtos
    )

    print(
        f"\nProdutos com preço {tipo_filtro} "
        f"de R$ {valor_limite:.2f}:"
    )

    if produtos_filtrados:

        for produto in produtos_filtrados:

            print(
                f"- {produto['nome']} "
                f"| R$ {produto['preco']:.2f}"
            )

    else:

        print(
            "Nenhum produto encontrado para esse filtro."
        )

    exibir_lista_produtos(
        "PREÇO CRESCENTE",
        produtos_crescente
    )

    exibir_lista_produtos(
        "PREÇO DECRESCENTE",
        produtos_decrescente
    )

    print("\n===== CATEGORIAS ÚNICAS =====")

    for categoria in categorias_unicas:

        print(
            f"- {categoria}"
        )

    menor_preco, maior_preco, media_precos = estatisticas

    print("\n===== ESTATÍSTICAS =====")

    print(
        f"Menor preço: R$ {menor_preco:.2f}"
    )

    print(
        f"Maior preço: R$ {maior_preco:.2f}"
    )

    print(
        f"Média dos preços: R$ {media_precos:.2f}"
    )

    print("\n")
    print("=" * 55)
    print("FIM DO RELATÓRIO")
    print("=" * 55)


def main():
    """Executa o sistema de produtos."""

    print(
        "===== SISTEMA DE PRODUTOS ====="
    )

    produtos = cadastrar_produtos()

    (
        produtos_filtrados,
        valor_limite,
        tipo_filtro
    ) = filtrar_produtos(produtos)

    (
        produtos_crescente,
        produtos_decrescente
    ) = ordenar_produtos(produtos)

    categorias_unicas = (
        obter_categorias_unicas(produtos)
    )

    estatisticas = (
        calcular_estatisticas(produtos)
    )

    exibir_relatorio_final(
        produtos,
        produtos_filtrados,
        valor_limite,
        tipo_filtro,
        produtos_crescente,
        produtos_decrescente,
        categorias_unicas,
        estatisticas
    )


if __name__ == "__main__":
    main()
