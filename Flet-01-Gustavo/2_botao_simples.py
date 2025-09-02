# Página que cria um botão simples que, ao ser clicado, muda o texto exibido na tela.

import flet as ft

def main(page: ft.Page):
    page.title = "Meu Primeiro Botão"
    page.padding = 20
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Criando um texto que será modificado pelo botão
    mensagem = ft.Text(
        value="Clique no botão abaixo! 👇",
        size=20,
        text_align=ft.TextAlign.CENTER
    )

    def botao_clicado(evento):
        """
        Esta função será executada sempre que o botão for clicado.
        O parâmetro 'evento' contém informações sobre o clique.
        """
        # Mudando o texto da mensagem
        mensagem.value = "EI! Por que você clicou? 😲"
        mensagem.color = ft.Colors.GREEN

        # IMPORTANTE: Sempre que modificamos elementos da interface,
        # precisamos chamar page.update() para que as mudanças apareçam na tela
        page.update()

    def botao_clicado2(evento):
        """
        Esta função será executada sempre que o botão for clicado.
        O parâmetro 'evento' contém informações sobre o clique.
        """
        # Mudando o texto da mensagem
        mensagem.value = "Se clicar no outro tem surpresa 😲"
        mensagem.color = ft.Colors.GREEN

        # IMPORTANTE: Sempre que modificamos elementos da interface,
        # precisamos chamar page.update() para que as mudanças apareçam na tela
        page.update()


    # Criando nosso botão
    meu_botao = ft.ElevatedButton(
        text="Clique em mim!",  # Texto que aparece no botão
        on_click=botao_clicado2,  # Função que será executada no clique
        width=200,  # Largura do botão
        height=50,  # Altura do botão
        bgcolor=ft.Colors.PURPLE,  # Cor de fundo
        color=ft.Colors.WHITE # Cor do texto
 
    )
    # Criando nosso botão
    meu_botao2 = ft.ElevatedButton(
        text="Clique em mim!",  # Texto que aparece no botão
        on_click=botao_clicado,  # Função que será executada no clique
        width=200,  # Largura do botão
        height=50,  # Altura do botão
        bgcolor=ft.Colors.PURPLE,  # Cor de fundo
        color=ft.Colors.WHITE  # Cor do texto
    )


    # Adicionando os elementos à página
    page.add(mensagem)
    page.add(meu_botao)
    page.add(meu_botao2)

ft.app(target=main)
