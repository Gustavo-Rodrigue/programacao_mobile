# Painel de Configuração com Flet
# Este script cria uma interface gráfica para configurar o estilo e as cores de um texto de exemplo

import flet as ft

def main(page: ft.Page):
    page.title = "Painel de Configuração"
    page.padding = ft.padding.only(top=40, left=20, right=20, bottom=20)
    
    # Área de preview
    area_preview = ft.Container(
        content=ft.Text("Texto de exemplo para configurar 🎨", size=25, color=ft.Colors.BLACK),
        bgcolor=ft.Colors.WHITE, padding=25, border_radius=10,
        border=ft.border.all(2, ft.Colors.GREY_300), width=350, height=150,
        alignment=ft.alignment.center
    )
    
    # Controles
    switch_negrito = ft.Switch(label="Negrito", value=False)
    switch_italico = ft.Switch(label="Itálico", value=False)
    checkbox_sublinhado = ft.Checkbox(label="Sublinhado", value=False)
    checkbox_rachurado = ft.Checkbox(label="Riscado", value=False)
    slider_tamanho = ft.Slider(min=12, max=32, value=16, divisions=4, label="Tamanho: {value}px")
    dropdown_cor = ft.Dropdown(
        label="Cor texto", width=150, value="Preto",
        options=[ft.dropdown.Option("Preto"), ft.dropdown.Option("Azul"), 
                ft.dropdown.Option("Verde"), ft.dropdown.Option("Vermelho"), ft.dropdown.Option("Roxo"), ft.dropdown.Option("Laranja")]
    )
    dropdown_fundo = ft.Dropdown(
        label="Cor fundo", width=150, value="Branco",
        options=[ft.dropdown.Option("Branco"), ft.dropdown.Option("Cinza Claro"), 
                ft.dropdown.Option("Azul Claro"), ft.dropdown.Option("Verde Claro"), ft.dropdown.Option("Rosa Claro"), ft.dropdown.Option("Amarelo Claro") ]
    )
    
    def aplicar_config(e):
        texto = area_preview.content
        
        # Estilo do texto
        texto.size = slider_tamanho.value
        texto.weight = ft.FontWeight.BOLD if switch_negrito.value else ft.FontWeight.NORMAL
        texto.italic = switch_italico.value
        texto.style = ft.TextStyle(decoration=ft.TextDecoration.UNDERLINE) if checkbox_sublinhado.value else None
        texto.style = ft.TextStyle(decoration=ft.TextDecoration.LINE_THROUGH) if checkbox_rachurado.value else None

        # Cores
        cores_texto = {"Preto": ft.Colors.BLACK, "Azul": ft.Colors.BLUE, "Verde": ft.Colors.GREEN, 
                      "Vermelho": ft.Colors.RED, "Roxo": ft.Colors.PURPLE, "Laranja": ft.Colors.ORANGE}
        cores_fundo = {"Branco": ft.Colors.WHITE, "Cinza Claro": ft.Colors.GREY_200, 
                      "Azul Claro": ft.Colors.BLUE_100, "Verde Claro": ft.Colors.GREEN_100, "Rosa Claro": ft.Colors.PINK_100, "Amarelo Claro": ft.Colors.YELLOW_100}
        
        texto.color = cores_texto[dropdown_cor.value]
        area_preview.bgcolor = cores_fundo[dropdown_fundo.value]
        page.update()
    
    # Conectar eventos
    for controle in [switch_negrito, switch_italico, checkbox_sublinhado, checkbox_rachurado, slider_tamanho, dropdown_cor, dropdown_fundo]:
        controle.on_change = aplicar_config
    
    # Interface
    page.add(
        ft.Column([
            ft.Text("⚙️ Painel de Configuração", size=25, weight=ft.FontWeight.BOLD),
            ft.Text("Configure o texto abaixo:", size=18),
            area_preview,
            ft.Divider(),
            ft.Row([
                ft.Column([
                    ft.Text("📝 Estilo", size=18, weight=ft.FontWeight.BOLD),
                    switch_negrito, switch_italico, checkbox_sublinhado, checkbox_rachurado,
                    ft.Text(f"Tamanho: {slider_tamanho.value}px"), slider_tamanho
                ], spacing=10),
                ft.Column([
                    ft.Text("🎨 Cores", size=18, weight=ft.FontWeight.BOLD),
                    dropdown_cor, dropdown_fundo
                ], spacing=10)
            ], alignment=ft.MainAxisAlignment.CENTER, vertical_alignment=ft.CrossAxisAlignment.START)
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=20)
    )

ft.app(target=main)