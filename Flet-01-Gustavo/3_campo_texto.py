# Página que demonstra o uso de um campo de texto para entrada do usuário.
# O usuário pode digitar seu nome, e o app responderá com uma saudação personalizada

import flet as ft

def main(page: ft.Page):
    page.title = "Campo de Texto"
    page.padding = ft.padding.only(top=40, left=20, right=20, bottom=20)  # Padding superior para área segura
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    # Criando um campo onde o usuário pode digitar
    campo_nome = ft.TextField(
        label="Digite seu nome aqui",  # Texto de orientação
        width=300,  # Largura do campo
        border_color=ft.Colors.BLUE  # Cor da borda
    )

    # Texto que mostrará a resposta
    resposta = ft.Text(
        value="",  # Inicialmente vazio
        size=18,
        text_align=ft.TextAlign.CENTER
    )

    def processar_nome(evento):
        """
        Função que pega o texto digitado pelo usuário e faz algo com ele.
        """
        # Pegando o valor digitado no campo
        nome_digitado = campo_nome.value

        # Verificando se o usuário realmente digitou algo
        if nome_digitado == "" or nome_digitado is None:
            resposta.value = "⚠️ Não sabe ler cara? Escreve teu nome ai!"
            resposta.color = ft.Colors.RED
        elif len(nome_digitado) < 2:
            resposta.value = "⚠️ Escreve seu nome direito ai meu fi!"
            resposta.color = ft.Colors.ORANGE
        else:
            resposta.value = f"✅ Olá, {nome_digitado}! Prazer em conhecê-lo(a)!"
            resposta.color = ft.Colors.GREEN

        # Atualizando a interface
        page.update()

    # Botão para processar o nome
    botao_ok = ft.ElevatedButton(
        text="Confirmar",
        on_click=processar_nome,
        width=150
    )

    # Adicionando elementos à página
    page.add(
        ft.Text("Vamos nos conhecer! 😉", size=25, weight=ft.FontWeight.BOLD),
        campo_nome,
        botao_ok,
        resposta
    )

ft.app(target=main)
