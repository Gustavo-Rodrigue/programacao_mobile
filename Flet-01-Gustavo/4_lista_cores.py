#Página que cria uma lista suspensa para selecionar cores.

import flet as ft

def main(page: ft.Page):
    page.title = "Seletor de Cores"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Container que mudará de cor (como uma caixa colorida)
    caixa_colorida = ft.Container(
        content=ft.Text(
            "Escolha uma cor! 🎨",
            color=ft.Colors.WHITE,
            size=30,
            text_align=ft.TextAlign.CENTER
        ),
        bgcolor=ft.Colors.GREY,  # Cor inicial
        width=350,
        height=150,
        border_radius=20,  # Bordas arredondadas
        alignment=ft.alignment.center  # Centralizar o texto dentro da caixa
    )

    def cor_selecionada(evento):
        """
        Esta função é executada sempre que o usuário escolhe uma cor.
        """
        # Pegando qual cor foi selecionada
        cor_escolhida = evento.control.value

        # Dicionário com as cores disponíveis
        cores_disponiveis = {
            "Azul": ft.Colors.BLUE,
            "Verde": ft.Colors.GREEN,
            "Vermelho": ft.Colors.RED,
            "Roxo": ft.Colors.PURPLE,
            "Laranja": ft.Colors.ORANGE,
            "Rosa": ft.Colors.PINK,
            "Amarelo": ft.Colors.YELLOW,
            "Cinza": ft.Colors.GREY,
            "Preto": ft.Colors.BLACK,
            "Branco": ft.Colors.WHITE

        }

        # Mudando a cor da caixa
        caixa_colorida.bgcolor = cores_disponiveis[cor_escolhida]
        caixa_colorida.content.value = f"Cor selecionada: {cor_escolhida} ✨"

        # Se a cor escolhida for branco ou amarelo, o texto fica preto, senão fica branco
        if cor_escolhida == "Branco" or cor_escolhida == "Amarelo":
            caixa_colorida.content.color = ft.Colors.BLACK
        else:
            caixa_colorida.content.color = ft.Colors.WHITE

        page.update()

    # Criando a lista suspensa (dropdown)
    seletor_cor = ft.Dropdown(
        label="Escolha uma cor",
        width=200,
        options=[
            ft.dropdown.Option("Azul"),
            ft.dropdown.Option("Verde"),
            ft.dropdown.Option("Vermelho"),
            ft.dropdown.Option("Roxo"),
            ft.dropdown.Option("Laranja"),
            ft.dropdown.Option("Rosa"),
            ft.dropdown.Option("Amarelo"),
            ft.dropdown.Option("Cinza"),
            ft.dropdown.Option("Preto"),
            ft.dropdown.Option("Branco")
        ],
        on_change=cor_selecionada  # Função que será executada quando escolher
    )

    # Adicionando elementos à página dentro de uma coluna centralizada
    page.add(
        ft.Column(
            [
                ft.Text("Seletor de Cores Mágico! ✨", size=30, weight=ft.FontWeight.BOLD),
                seletor_cor,
                caixa_colorida
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )

ft.app(target=main)
