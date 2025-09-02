# App Multi-página com Flet
# Este script cria um aplicativo com múltiplas páginas, navegação e gerenciamento de estado

import flet as ft

def main(page: ft.Page):
    page.title = "App Multi-página"
    page.padding = 0
    page.scroll = ft.ScrollMode.AUTO

    pagina_atual = "home"

    dados_usuario = {
        "nome": "Estudante Flet",
        "nivel": "Iniciante",
        "pontos": 150,
        "configuracoes": {
            "modo_escuro": False,
            "notificacoes": True,
            "som": True
        }
    }

    # --- NOVAS PÁGINAS ---
    # Removido: Página de Ajuda

    # --- Página de Estatísticas com referências para atualização dinâmica ---
    stats_pontos = ft.Text(str(dados_usuario["pontos"]), size=22, weight=ft.FontWeight.BOLD, color=ft.Colors.TEAL_700)
    stats_nivel = ft.Text(dados_usuario["nivel"], size=22, weight=ft.FontWeight.BOLD, color=ft.Colors.TEAL_700)

    conteudo_stats = ft.Container(
        content=ft.Column(
            [
                ft.Icon(ft.Icons.BAR_CHART, size=60, color=ft.Colors.TEAL_400),
                ft.Text("Estatísticas", size=26, weight=ft.FontWeight.BOLD, color=ft.Colors.TEAL_900),
                ft.Text("Veja seu desempenho no app!", size=16, color=ft.Colors.TEAL_700),
                ft.Container(height=20),
                ft.Row([
                    ft.Container(
                        content=ft.Column([
                            ft.Text("Pontos", size=14, color=ft.Colors.TEAL_900),
                            stats_pontos
                        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                        bgcolor=ft.Colors.TEAL_50, border_radius=12, padding=16
                    ),
                    ft.Container(
                        content=ft.Column([
                            ft.Text("Nível", size=14, color=ft.Colors.TEAL_900),
                            stats_nivel
                        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                        bgcolor=ft.Colors.TEAL_50, border_radius=12, padding=16
                    )
                ], alignment=ft.MainAxisAlignment.CENTER, spacing=30)
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=15
        ),
        padding=40,
        visible=False
    )

    # --- FIM NOVAS PÁGINAS ---

    def atualizar_nivel():
        pontos = dados_usuario["pontos"]
        if pontos < 1000:
            dados_usuario["nivel"] = "Iniciante"
        elif pontos < 2000:
            dados_usuario["nivel"] = "Intermediário"
        elif pontos < 3000:
            dados_usuario["nivel"] = "Avançado"
        else:
            dados_usuario["nivel"] = "Mestre"

    def mudar_pagina(nova_pagina):
        nonlocal pagina_atual
        pagina_atual = nova_pagina

        conteudo_home.visible = False
        conteudo_perfil.visible = False
        conteudo_config.visible = False
        conteudo_sobre.visible = False
        conteudo_stats.visible = False

        # Atualiza o nível antes de mostrar as páginas
        atualizar_nivel()
        # Atualiza os dados do stats sempre que trocar de página
        stats_pontos.value = str(dados_usuario["pontos"])
        stats_nivel.value = dados_usuario["nivel"]

        if pagina_atual == "home":
            conteudo_home.visible = True
        elif pagina_atual == "perfil":
            conteudo_perfil.visible = True
        elif pagina_atual == "config":
            conteudo_config.visible = True
        elif pagina_atual == "sobre":
            conteudo_sobre.visible = True
        elif pagina_atual == "stats":
            conteudo_stats.visible = True

        atualizar_barra_navegacao()
        page.update()

    def ir_home(e): mudar_pagina("home")
    def ir_perfil(e): mudar_pagina("perfil")
    def ir_config(e): mudar_pagina("config")
    def ir_sobre(e): mudar_pagina("sobre")
    def ir_stats(e): mudar_pagina("stats")

    # Novo cabeçalho com gradiente e botão de ação
    cabecalho = ft.Container(
        content=ft.Row(
            [
                ft.Icon(ft.Icons.STAR, size=36, color=ft.Colors.AMBER_400),
                ft.Text("Meu App Moderno", size=28, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE, font_family="Arial"),
                ft.Container(expand=True),
                ft.IconButton(icon=ft.Icons.BAR_CHART, icon_color=ft.Colors.TEAL_100, tooltip="Estatísticas", on_click=ir_stats)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=10
        ),
        gradient=ft.LinearGradient(
            begin=ft.alignment.top_left,
            end=ft.alignment.bottom_right,
            colors=[ft.Colors.INDIGO_700, ft.Colors.PURPLE_400]
        ),
        padding=ft.padding.symmetric(vertical=28, horizontal=20),
        alignment=ft.alignment.center
    )

    def criar_item_navegacao(icone, label, pagina_nome, on_click_func, cor_ativa, cor_inativa):
        return ft.GestureDetector(
            content=ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Icon(icone, size=28, color=cor_inativa),
                        ft.Text(label, size=12, text_align=ft.TextAlign.CENTER, color=cor_inativa)
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=2
                ),
                padding=ft.padding.symmetric(vertical=10, horizontal=18),
                border_radius=16,
                bgcolor=ft.Colors.TRANSPARENT,
                animate=ft.Animation(200, ft.AnimationCurve.EASE_OUT)
            ),
            on_tap=on_click_func
        )

    # Itens de navegação com novas cores
    item_home = criar_item_navegacao(ft.Icons.HOME, "Início", "home", ir_home, ft.Colors.PINK_700, ft.Colors.PINK_200)
    item_perfil = criar_item_navegacao(ft.Icons.PERSON, "Perfil", "perfil", ir_perfil, ft.Colors.CYAN_700, ft.Colors.CYAN_200)
    item_config = criar_item_navegacao(ft.Icons.SETTINGS, "Config", "config", ir_config, ft.Colors.LIME_700, ft.Colors.LIME_200)
    item_sobre = criar_item_navegacao(ft.Icons.INFO, "Sobre", "sobre", ir_sobre, ft.Colors.AMBER_700, ft.Colors.AMBER_200)
    item_stats = criar_item_navegacao(ft.Icons.BAR_CHART, "Stats", "stats", ir_stats, ft.Colors.TEAL_700, ft.Colors.TEAL_200)

    itens_nav = [
        (item_home, "home", ft.Colors.PINK_700, ft.Colors.PINK_200),
        (item_perfil, "perfil", ft.Colors.CYAN_700, ft.Colors.CYAN_200),
        (item_config, "config", ft.Colors.LIME_700, ft.Colors.LIME_200),
        (item_sobre, "sobre", ft.Colors.AMBER_700, ft.Colors.AMBER_200),
        (item_stats, "stats", ft.Colors.TEAL_700, ft.Colors.TEAL_200)
    ]

    def atualizar_barra_navegacao():
        for item, pagina_nome, cor_ativa, cor_inativa in itens_nav:
            container = item.content
            icone = container.content.controls[0]
            texto = container.content.controls[1]
            if pagina_atual == pagina_nome:
                container.bgcolor = cor_inativa
                container.border = ft.border.all(2, cor_ativa)
                icone.color = cor_ativa
                texto.color = cor_ativa
                texto.weight = ft.FontWeight.BOLD
            else:
                container.bgcolor = ft.Colors.TRANSPARENT
                container.border = None
                icone.color = cor_inativa
                texto.color = cor_inativa
                texto.weight = ft.FontWeight.NORMAL

    # HOME
    conteudo_home = ft.Container(
        content=ft.Column(
            [
                ft.Icon(ft.Icons.HOME, size=100, color=ft.Colors.PINK_700),
                ft.Text("Bem-vindo ao App Moderno! 🎉", size=34, weight=ft.FontWeight.BOLD, color=ft.Colors.PINK_900),
                ft.Text("Navegue pelas páginas usando a barra colorida abaixo.", size=18, text_align=ft.TextAlign.CENTER, color=ft.Colors.PINK_400),
                ft.Container(height=20),
                ft.ElevatedButton("Ir para Estatísticas", icon=ft.Icons.BAR_CHART, bgcolor=ft.Colors.TEAL_400, color=ft.Colors.WHITE, on_click=ir_stats)
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=18
        ),
        padding=50,
        visible=True
    )

    # PERFIL
    def adicionar_pontos(e):
        dados_usuario["pontos"] += 100
        atualizar_nivel()
        texto_pontos.value = f"Pontos: {dados_usuario['pontos']} ⭐"
        stats_pontos.value = str(dados_usuario["pontos"])
        stats_nivel.value = dados_usuario["nivel"]
        page.update()

    texto_pontos = ft.Text(f"Pontos: {dados_usuario['pontos']} ⭐", size=20, color=ft.Colors.CYAN_900)

    conteudo_perfil = ft.Container(
        content=ft.Column(
            [
                ft.CircleAvatar(
                    content=ft.Icon(ft.Icons.PERSON, size=70, color=ft.Colors.WHITE),
                    bgcolor=ft.Colors.CYAN_700,
                    radius=70
                ),
                ft.Text(dados_usuario["nome"], size=28, weight=ft.FontWeight.BOLD, color=ft.Colors.CYAN_900),
                ft.Text(f"Nível: {dados_usuario['nivel']}", size=18, color=ft.Colors.CYAN_600),
                texto_pontos,
                ft.Container(height=20),
                ft.Row([
                    ft.ElevatedButton(
                        "Ganhar Pontos! 🎯",
                        on_click=adicionar_pontos,
                        bgcolor=ft.Colors.CYAN_400,
                        color=ft.Colors.WHITE
                    ),
                    ft.ElevatedButton(
                        "Configurações",
                        icon=ft.Icons.SETTINGS,
                        bgcolor=ft.Colors.LIME_400,
                        color=ft.Colors.WHITE,
                        on_click=ir_config
                    )
                ], alignment=ft.MainAxisAlignment.CENTER, spacing=16)
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=15
        ),
        padding=40,
        visible=False
    )

    # CONFIGURAÇÕES
    def alternar_modo_escuro(e):
        dados_usuario["configuracoes"]["modo_escuro"] = e.control.value

    def alternar_notificacoes(e):
        dados_usuario["configuracoes"]["notificacoes"] = e.control.value

    def alternar_som(e):
        dados_usuario["configuracoes"]["som"] = e.control.value

    conteudo_config = ft.Container(
        content=ft.Column(
            [
                ft.Icon(ft.Icons.SETTINGS, size=65, color=ft.Colors.LIME_700),
                ft.Text("Configurações ⚙️", size=26, weight=ft.FontWeight.BOLD, color=ft.Colors.LIME_900),
                ft.Container(height=20),
                ft.Switch(
                    label="Modo escuro",
                    value=dados_usuario["configuracoes"]["modo_escuro"],
                    on_change=alternar_modo_escuro,
                    active_color=ft.Colors.LIME_400
                ),
                ft.Switch(
                    label="Notificações",
                    value=dados_usuario["configuracoes"]["notificacoes"],
                    on_change=alternar_notificacoes,
                    active_color=ft.Colors.LIME_400
                ),
                ft.Switch(
                    label="Som",
                    value=dados_usuario["configuracoes"]["som"],
                    on_change=alternar_som,
                    active_color=ft.Colors.LIME_400
                ),
                ft.Container(height=30),
                ft.ElevatedButton("Voltar ao Início", icon=ft.Icons.HOME, bgcolor=ft.Colors.PINK_200, color=ft.Colors.PINK_900, on_click=ir_home)
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=17
        ),
        padding=40,
        visible=False
    )

    # SOBRE
    conteudo_sobre = ft.Container(
        content=ft.Column(
            [
                ft.Icon(ft.Icons.INFO, size=65, color=ft.Colors.AMBER_700),
                ft.Text("Sobre o App", size=26, weight=ft.FontWeight.BOLD, color=ft.Colors.AMBER_900),
                ft.Container(height=20),
                ft.Text("Versão: 2.0.0", size=17, color=ft.Colors.AMBER_800),
                ft.Text("Desenvolvido com Flet", size=17, color=ft.Colors.AMBER_800),
                ft.Text("Python + Interface Mobile", size=17, color=ft.Colors.AMBER_800),
                ft.Container(height=20),
                ft.Text(
                    "Este app demonstra navegação entre páginas, gerenciamento de estado, estatísticas e central de ajuda!",
                    size=15,
                    text_align=ft.TextAlign.CENTER,
                    color=ft.Colors.GREY_600
                ),
                ft.Container(height=30),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=15
        ),
        padding=40,
        visible=False
    )

    # Estrutura principal
    page.add(
        ft.Container(
            content=ft.Column(
                [
                    cabecalho,
                    ft.Container(
                        content=ft.Stack(
                            [
                                conteudo_home,
                                conteudo_perfil,
                                conteudo_config,
                                conteudo_sobre,
                                conteudo_stats
                            ]
                        ),
                        expand=True,
                        padding=ft.padding.only(bottom=90)
                    ),
                    ft.Container(
                        content=ft.Row(
                            [
                                item_home, item_perfil, item_config, item_sobre, item_stats
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_AROUND,
                            vertical_alignment=ft.CrossAxisAlignment.CENTER
                        ),
                        bgcolor=ft.Colors.GREY_100,
                        padding=ft.padding.only(top=16, bottom=28),
                        border=ft.border.only(top=ft.border.BorderSide(2, ft.Colors.PINK_200)),
                        shadow=ft.BoxShadow(
                            spread_radius=0,
                            blur_radius=12,
                            color=ft.Colors.with_opacity(0.13, ft.Colors.PINK_700),
                            offset=ft.Offset(0, -2)
                        )
                    )
                ],
                spacing=0
            ),
            expand=True
        )
    )

    atualizar_barra_navegacao()

ft.app(target=main)