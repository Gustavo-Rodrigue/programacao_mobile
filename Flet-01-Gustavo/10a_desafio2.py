import flet as ft

def main(page: ft.Page):
    # Configurações iniciais
    page.title = "Loja Virtual Mini"
    page.padding = ft.padding.only(top=40, left=20, right=20, bottom=20)
    page.scroll = ft.ScrollMode.AUTO
    page.bgcolor = ft.Colors.GREY_50

    # Estado do carrinho
    carrinho = []
    total_carrinho = 0.0

    # Elementos da interface
    area_produtos = ft.GridView(
        expand=1,
        runs_count=2,
        max_extent=180,
        child_aspect_ratio=0.9,
        spacing=15,
        run_spacing=15
    )
    contador_carrinho = ft.Text("Carrinho (0)", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_700)
    total_texto = ft.Text("Total: R$ 0,00", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_700)
    lista_carrinho = ft.ListView(height=150, spacing=5)
    notificacao = ft.Text(size=14, color=ft.Colors.BLUE_600, text_align=ft.TextAlign.CENTER)

    # Lista de produtos (agora com mais itens e nova categoria "Brinquedos")
    produtos = [
        {"nome": "Smartphone", "preco": 899.99, "categoria": "Eletrônicos", "emoji": "📱", "cor": ft.Colors.BLUE_600},
        {"nome": "Notebook", "preco": 2499.99, "categoria": "Eletrônicos", "emoji": "💻", "cor": ft.Colors.PURPLE_600},
        {"nome": "Tênis", "preco": 299.99, "categoria": "Roupas", "emoji": "👟", "cor": ft.Colors.GREEN_600},
        {"nome": "Camiseta", "preco": 89.90, "categoria": "Roupas", "emoji": "👕", "cor": ft.Colors.ORANGE_600},
        {"nome": "Livro", "preco": 45.00, "categoria": "Educação", "emoji": "📚", "cor": ft.Colors.BROWN_600},
        {"nome": "Fone", "preco": 199.99, "categoria": "Eletrônicos", "emoji": "🎧", "cor": ft.Colors.RED_600},
        {"nome": "Relógio", "preco": 350.00, "categoria": "Acessórios", "emoji": "⌚", "cor": ft.Colors.TEAL_600},
        {"nome": "Óculos", "preco": 250.00, "categoria": "Acessórios", "emoji": "🕶️", "cor": ft.Colors.INDIGO_600},
        {"nome": "Mochila", "preco": 120.00, "categoria": "Acessórios", "emoji": "🎒", "cor": ft.Colors.BLUE_GREY_600},
        {"nome": "Copo Térmico", "preco": 59.90, "categoria": "Acessórios", "emoji": "🥤", "cor": ft.Colors.CYAN_600},
        {"nome": "Tablet", "preco": 1299.99, "categoria": "Eletrônicos", "emoji": "📝", "cor": ft.Colors.LIME_600},
        {"nome": "Jaqueta", "preco": 399.99, "categoria": "Roupas", "emoji": "🧥", "cor": ft.Colors.GREY_700},
        {"nome": "Caderno", "preco": 25.00, "categoria": "Educação", "emoji": "📒", "cor": ft.Colors.YELLOW_700},
        {"nome": "Caneta", "preco": 5.50, "categoria": "Educação", "emoji": "🖊️", "cor": ft.Colors.BLUE_900},
        {"nome": "Pulseira", "preco": 35.00, "categoria": "Acessórios", "emoji": "📿", "cor": ft.Colors.PINK_400},
        {"nome": "Boné", "preco": 49.90, "categoria": "Roupas", "emoji": "🧢", "cor": ft.Colors.LIGHT_BLUE_700},
        # Novos itens e nova categoria
        {"nome": "Lego", "preco": 199.90, "categoria": "Brinquedos", "emoji": "🧱", "cor": ft.Colors.YELLOW_800},
        {"nome": "Carrinho", "preco": 39.90, "categoria": "Brinquedos", "emoji": "🚗", "cor": ft.Colors.RED_400},
        {"nome": "Boneca", "preco": 59.90, "categoria": "Brinquedos", "emoji": "🪆", "cor": ft.Colors.PINK_200},
        {"nome": "Quebra-cabeça", "preco": 29.90, "categoria": "Brinquedos", "emoji": "🧩", "cor": ft.Colors.GREEN_400},
        {"nome": "Patins", "preco": 220.00, "categoria": "Brinquedos", "emoji": "🛼", "cor": ft.Colors.PURPLE_400},
        {"nome": "Garrafa", "preco": 19.90, "categoria": "Acessórios", "emoji": "🍼", "cor": ft.Colors.CYAN_200},
        {"nome": "Chaveiro", "preco": 9.90, "categoria": "Acessórios", "emoji": "🔑", "cor": ft.Colors.BROWN_400},
        {"nome": "Meia", "preco": 15.00, "categoria": "Roupas", "emoji": "🧦", "cor": ft.Colors.LIME_700},
        {"nome": "Agenda", "preco": 35.00, "categoria": "Educação", "emoji": "📔", "cor": ft.Colors.PINK_700},
        {"nome": "Mouse", "preco": 89.90, "categoria": "Eletrônicos", "emoji": "🖱️", "cor": ft.Colors.GREY_800}
    ]

    # Filtros
    filtro_categoria = ft.Dropdown(
        label="Categoria",
        label_style=ft.TextStyle(color=ft.Colors.BLACK),
        width=150,
        value="Todas",
        color=ft.Colors.BLACK,
        options=[
            ft.dropdown.Option("Todas"),
            ft.dropdown.Option("Eletrônicos"),
            ft.dropdown.Option("Roupas"),
            ft.dropdown.Option("Educação"),
            ft.dropdown.Option("Acessórios"),
            ft.dropdown.Option("Brinquedos")  # Nova categoria
        ]
    )
    filtro_preco = ft.Dropdown(
        label="Preço",
        label_style=ft.TextStyle(color=ft.Colors.BLACK),
        color=ft.Colors.BLACK,
        width=150,
        value="Todos",
        options=[
            ft.dropdown.Option("Todos"),
            ft.dropdown.Option("Até R$ 100"),
            ft.dropdown.Option("R$ 100-500"),
            ft.dropdown.Option("Acima R$ 500")
        ]
    )
    campo_busca = ft.TextField(
        label="Buscar produto",
        label_style=ft.TextStyle(color=ft.Colors.BLACK),
        color=ft.Colors.BLACK,
        width=200,
        prefix_icon=ft.Icons.SEARCH
    )

    # Funções principais
    def mostrar_notificacao(msg):
        notificacao.value = msg
        page.update()

    def atualizar_carrinho():
        # Agrupa produtos iguais e mostra quantidade
        contador_carrinho.value = f"Carrinho ({len(carrinho)})"
        total_texto.value = f"Total: R$ {total_carrinho:.2f}"
        lista_carrinho.controls.clear()
        # Agrupar por nome e preco
        agrupados = {}
        for item in carrinho:
            chave = (item["nome"], item["preco"])
            if chave in agrupados:
                agrupados[chave]["quantidade"] += 1
            else:
                agrupados[chave] = {"nome": item["nome"], "preco": item["preco"], "quantidade": 1}
        for i, ((nome, preco), info) in enumerate(agrupados.items()):
            linha = ft.Row([
                ft.Text(f"{nome} x{info['quantidade']}", expand=True, color=ft.Colors.BLACK),
                ft.Text(f"R$ {preco:.2f}", color=ft.Colors.BLACK),
                ft.IconButton(
                    ft.Icons.DELETE,
                    icon_color=ft.Colors.RED,
                    on_click=lambda e, n=nome, p=preco: remover_do_carrinho_nome_preco(n, p)
                )
            ], spacing=10)
            lista_carrinho.controls.append(linha)
        page.update()

    def adicionar_ao_carrinho(nome, preco):
        nonlocal total_carrinho
        carrinho.append({"nome": nome, "preco": preco})
        total_carrinho += preco
        atualizar_carrinho()
        mostrar_notificacao(f"✅ {nome} adicionado!")

    def remover_do_carrinho_nome_preco(nome, preco):
        nonlocal total_carrinho
        # Remove apenas um produto com o nome e preco correspondente
        for idx, item in enumerate(carrinho):
            if item["nome"] == nome and item["preco"] == preco:
                produto = carrinho.pop(idx)
                total_carrinho -= produto["preco"]
                break
        atualizar_carrinho()
        mostrar_notificacao(f"❌ {nome} removido")

    def criar_card_produto(nome, preco, categoria, emoji, cor):
        return ft.Container(
            content=ft.Column([
                ft.Text(emoji, size=40, text_align=ft.TextAlign.CENTER),
                ft.Text(
                    nome,
                    size=16,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.WHITE,
                    text_align=ft.TextAlign.CENTER,
                    max_lines=2,
                    overflow=ft.TextOverflow.ELLIPSIS
                ),
                ft.Text(
                    f"R$ {preco:.2f}",
                    size=14,
                    color=ft.Colors.WHITE70,
                    text_align=ft.TextAlign.CENTER
                )
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10
            ),
            bgcolor=cor,
            padding=20,
            border_radius=15,
            width=160,
            height=180,
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=8,
                color=ft.Colors.with_opacity(0.3, ft.Colors.BLACK)
            ),
            on_click=lambda e, n=nome, p=preco: adicionar_ao_carrinho(n, p),
            ink=True
        )

    def carregar_produtos(e=None):
        area_produtos.controls.clear()
        categoria = filtro_categoria.value
        preco_faixa = filtro_preco.value
        busca = (campo_busca.value or "").lower()
        for produto in produtos:
            # Filtro categoria
            if categoria != "Todas" and produto["categoria"] != categoria:
                continue
            # Filtro preço
            if preco_faixa == "Até R$ 100" and produto["preco"] > 100:
                continue
            elif preco_faixa == "R$ 100-500" and not (100 < produto["preco"] <= 500):
                continue
            elif preco_faixa == "Acima R$ 500" and produto["preco"] <= 500:
                continue
            # Filtro busca
            if busca and busca not in produto["nome"].lower():
                continue
            card = criar_card_produto(
                produto["nome"], produto["preco"], produto["categoria"], produto["emoji"], produto["cor"]
            )
            area_produtos.controls.append(card)
        page.update()

    def finalizar_compra(e):
        nonlocal total_carrinho
        if len(carrinho) > 0:
            carrinho.clear()
            total_carrinho = 0.0
            atualizar_carrinho()
            mostrar_notificacao("🎉 Compra finalizada! Obrigado!")
        else:
            mostrar_notificacao("⚠️ Carrinho vazio!")

    def limpar_filtros(e):
        filtro_categoria.value = "Todas"
        filtro_preco.value = "Todos"
        campo_busca.value = ""
        carregar_produtos()
        mostrar_notificacao("🧹 Filtros limpos!")
        page.update()

    # Eventos dos filtros
    for controle in [filtro_categoria, filtro_preco, campo_busca]:
        controle.on_change = carregar_produtos

    # Carrega produtos inicialmente
    carregar_produtos()

    # Interface
    page.add(
        ft.Column([
            ft.Text(
                "🛒 Loja Virtual Mini",
                size=28,
                weight=ft.FontWeight.BOLD,
                color=ft.Colors.BLUE_800,
                text_align=ft.TextAlign.CENTER
            ),
            ft.Text(
                "Encontre os melhores produtos!",
                size=14,
                color=ft.Colors.GREY_600,
                text_align=ft.TextAlign.CENTER
            ),
            # Filtros
            ft.Row(
                [filtro_categoria, filtro_preco],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=20
            ),
            ft.Row(
                [
                    campo_busca,
                    ft.ElevatedButton(
                        "🧹 Limpar Filtros",
                        on_click=limpar_filtros,
                        bgcolor=ft.Colors.ORANGE_400,
                        color=ft.Colors.WHITE,
                        height=40,
                        style=ft.ButtonStyle(
                            text_style=ft.TextStyle(size=12, weight=ft.FontWeight.BOLD)
                        )
                    )
                ]
            ),
            # Produtos
            ft.Container(
                content=area_produtos,
                height=400,
                border=ft.border.all(1, ft.Colors.GREY_300),
                border_radius=10,
                padding=10
            ),
            # Carrinho
            ft.Container(
                content=ft.Column([
                    ft.Row(
                        [contador_carrinho, total_texto],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                    ),
                    lista_carrinho,
                    ft.Row([
                        ft.ElevatedButton(
                            "🛒 Finalizar Compra",
                            on_click=finalizar_compra,
                            bgcolor=ft.Colors.GREEN,
                            color=ft.Colors.WHITE,
                            width=200
                        )
                    ], alignment=ft.MainAxisAlignment.CENTER),
                    notificacao
                ], spacing=10),
                bgcolor=ft.Colors.WHITE,
                padding=20,
                border_radius=10,
                shadow=ft.BoxShadow(
                    spread_radius=1,
                    blur_radius=3,
                    color=ft.Colors.with_opacity(0.1, ft.Colors.BLACK)
                )
            )
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=15
        )
    )

ft.app(target=main)