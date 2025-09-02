import flet as ft

def main(page: ft.Page):
    # Define o título da página, alinhamento e tema inicial
    page.title = "Calculadora IMC"
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT  # Começa no tema claro
    page.padding = ft.padding.only(top=100, right=50, left=50)

    # Função para retornar as cores de acordo com o tema atual
    def get_colors():
        if page.theme_mode == ft.ThemeMode.DARK:
            return {
                "titulo": ft.Colors.PURPLE_500,
                "btn_calc": ft.Colors.PURPLE_500,
                "btn_limpar": ft.Colors.PURPLE_200,
                "btn_text": ft.Colors.BLACK,
                "resultado": ft.Colors.WHITE,
                "tema_label": ft.Colors.WHITE,  # cor do texto do switch no escuro
                "ativa_color": ft.Colors.PURPLE_200,  # cor da borda do switch no escuro
                "border_color": ft.Colors.PURPLE_400  # cor da borda do switch no escuro
            }
        else:
            return {
                "titulo": ft.Colors.ORANGE_900,
                "btn_calc": ft.Colors.ORANGE_900,
                "btn_limpar": ft.Colors.ORANGE,
                "btn_text": ft.Colors.BLACK,
                "resultado": ft.Colors.BLACK,
                "tema_label": ft.Colors.BLACK,  # cor do texto do switch no claro
                "ativa_color": ft.Colors.ORANGE_200,  # cor da borda do switch no claro
                "border_color": ft.Colors.ORANGE_400  # cor da borda do switch no claro
            }

    colors = get_colors()  # Inicializa as cores conforme o tema inicial

    # Função chamada ao alternar o switch de tema
    def tema_alternar(e):
        if tema.value:
            page.theme_mode = ft.ThemeMode.DARK
        else:
            page.theme_mode = ft.ThemeMode.LIGHT
        # Atualiza as cores dos componentes para refletir o novo tema
        atualizar_cores()
        page.update()

    # Atualiza as cores dos widgets dinâmicos conforme o tema
    def atualizar_cores():
        nonlocal colors
        colors = get_colors()
        titulo.color = colors["titulo"]
        btn_calcular.bgcolor = colors["btn_calc"]
        btn_calcular.color = colors["btn_text"]
        btn_limpar.bgcolor = colors["btn_limpar"]
        btn_limpar.color = colors["btn_text"]
        resultado.color = colors["resultado"]
        tema.label_style = ft.TextStyle(color=colors["tema_label"], size=18)  # atualiza cor do texto do switch
        tema.active_color = colors["ativa_color"]  # atualiza cor da borda do switch
        peso.border_color = colors["border_color"]  # atualiza cor da borda do switch
        altura.border_color = colors["border_color"]

    # Switch para alternar o tema, maior, texto preto (inicial) e cor de borda dinâmica
    tema = ft.Switch(
        label="Tema",
        on_change=tema_alternar,
        scale=1.5,
        label_style=ft.TextStyle(color=colors["tema_label"], size=18),
        active_color=colors["ativa_color"]
    )

     # Campos de entrada com cor de fundo e label customizados

    peso = ft.TextField(
        label=" 🏋️‍♂️ Peso (kg)",
        width=600,
        keyboard_type=ft.KeyboardType.NUMBER,
        fill_color=ft.Colors.GREY_200,
        color=ft.Colors.BLACK,
        label_style=ft.TextStyle(color=ft.Colors.GREY_600),
        border_color=colors["border_color"],  # cor da borda do switch no escuro
        border_width=3
    )
    altura = ft.TextField(
        label="📏 Altura (m)",
        width=600,
        keyboard_type=ft.KeyboardType.NUMBER,
        fill_color=ft.Colors.GREY_200,
        color=ft.Colors.BLACK,
        label_style=ft.TextStyle(color=ft.Colors.GREY_600),
        border_color=colors["border_color"],  # cor da borda do switch no claro
        border_width=3
    )

    # Widgets que terão cor dinâmica (precisam ser variáveis para atualizar)
    titulo = ft.Text("Calculadora de IMC", size=60, color=colors["titulo"], text_align=ft.TextAlign.CENTER)
    resultado = ft.Text(value="Seu resultado aparecerá aqui", size=30, text_align=ft.TextAlign.CENTER, color=colors["resultado"])
    btn_calcular = ft.ElevatedButton(
        "Calcular",
        on_click=lambda e: calcular_imc(e),
        bgcolor=colors["btn_calc"],
        color=colors["btn_text"],
        width=160,
        height=60,
        style=ft.ButtonStyle(
        text_style=ft.TextStyle(size=22, weight=ft.FontWeight.BOLD)  # ⬅️ controla o tamanho e peso da fonte
    )
    )
    btn_limpar = ft.ElevatedButton(
        "Limpar",
        on_click=lambda e: limpar(e),
        bgcolor=colors["btn_limpar"],
        color=colors["btn_text"],
        width=160,
        height=60,
        style=ft.ButtonStyle(
        text_style=ft.TextStyle(size=22, weight=ft.FontWeight.BOLD)  # ⬅️ controla o tamanho e peso da fonte
    )
    )

    # Função para calcular o IMC e atualizar o resultado
    def calcular_imc(e):
        try:
            p: float = float(peso.value.replace(",", "."))
            a: float = float(altura.value.replace(",", "."))
            imc: float = p / (a ** 2)

            if p <= 0 or a <= 0:
                resultado.value = "Peso e altura devem ser maiores que zero."
                resultado.color = ft.Colors.RED
            elif a > 3 or a < 0.5:  # Altura maior que 3 metros é improvável
                resultado.value = "Por favor, insira uma altura válida. Utilize valores em metros (ex: 1.75)."
                resultado.color = ft.Colors.RED
            else:
                 # Classificação do IMC com cores diferentes
                if imc < 18.5:
                    resultado.value = f"Seu IMC é {imc:.2f}. Você está abaixo do peso."
                    resultado.color = ft.Colors.YELLOW_500
                elif 18.5 <= imc < 24.9:
                    resultado.value = f"Seu IMC é {imc:.2f}. Você está com peso normal."
                    resultado.color = ft.Colors.GREEN
                elif 25 <= imc < 29.9:
                    resultado.value = f"Seu IMC é {imc:.2f}. Você está com sobrepeso."
                    resultado.color = ft.Colors.ORANGE
                else:
                    resultado.value = f"Seu IMC é {imc:.2f}. Você está com obesidade."
                    resultado.color = ft.Colors.RED_900
        except ValueError:
            resultado.value = "Por favor, insira valores válidos."
            resultado.color = ft.Colors.RED

        page.update()

    # Função para limpar os campos e restaurar as cores do resultado
    def limpar(e):
        peso.value = ""
        altura.value = ""
        resultado.value = "Seu resultado aparecerá aqui"
        atualizar_cores()  # Garante que a cor do resultado volta ao padrão do tema
        page.update()

    # Layout principal da página
    page.add(
        ft.Column(
            controls=[
                # Switch de tema alinhado à direita e topo
                ft.Row(
                    controls=[tema],
                    alignment=ft.MainAxisAlignment.END,
                    vertical_alignment=ft.CrossAxisAlignment.START,
                    expand=False,
                ),
                titulo,
                ft.Container(height=10),  # Espaço abaixo do título
                peso,
                altura,
                ft.Row(
                    controls=[
                        btn_calcular,
                        ft.Container(width=20),  # Espaço entre os botões
                        btn_limpar
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                resultado
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=25
        )
    )


ft.app(target=main)