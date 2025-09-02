# Página inicial do nosso primeiro app com Flet, um framework para construir apps web e mobile com Python.
# A página contem um texto simples.

import flet as ft

def main(page: ft.Page):
    """
    Função principal que será executada quando o app iniciar.
    O parâmetro 'page' representa a tela/página do nosso app.
    """

    # Configurações básicas da página
    page.title = "Meu Primeiro App Flet"  # Título que aparece na aba do navegador
    page.padding = 200   # Espaçamento interno da página
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Criando nosso primeiro elemento: um texto
    meu_texto = ft.Text(
        value="👋 Fala galerinha! (Primeiro app com Flet!)",  # O texto que será exibido
        size=40,  # Tamanho da fonte
        color=ft.Colors.PURPLE,  # Cor do texto
        weight=ft.FontWeight.BOLD,  # Texto em negrito
        text_align=ft.TextAlign.CENTER  # Centralizar o texto
    )

    # Adicionando o texto à nossa página
    page.add(meu_texto)

    # Vamos adicionar mais alguns elementos para tornar mais interessante
    page.add(
        ft.Text("Bem-vindo ao mundo do desenvolvimento mobile!", size=25),
        ft.Text("Com Flet, você pode criar apps incríveis! 🚀", size=25, color=ft.Colors.RED)
    )

# Esta linha inicia nosso aplicativo, chamando a função main
ft.app(target=main)