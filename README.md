# 🚀 Atividades Flet - Programação Mobile

Este repositório reúne atividades práticas desenvolvidas em Python com o framework [Flet](https://flet.dev/), explorando conceitos de interface gráfica, lógica e interação.  
Cada atividade possui um print ilustrativo e uma explicação detalhada do funcionamento e das interações possíveis.

---

## 📑 Índice

- [1. 👋 Primeiro App](#1-👋-primeiro-app-1_primeiro_apppy)
- [2. 🟢 Botão Simples](#2-🟢-botão-simples-2_botao_simplespy)
- [3. 📝 Campo de Texto](#3-📝-campo-de-texto-3_campo_textopy)
- [4. 🎨 Lista de Cores](#4-🎨-lista-de-cores-4_lista_corespy)
- [5. 🧩 Layout Básico](#5-🧩-layout-básico-5_layout_basicopy)
- [5a. 🧞‍♂️ Desafio 1 - Criador de Perfil](#5a-🧞‍♂️-desafio-1---criador-de-perfil-5a_desafio1py)
- [6. 🔢 Contador Completo](#6-🔢-contador-completo-6_contadorpy)
- [7. 🧮 Calculadora Simples](#7-🧮-calculadora-simples-7_calculadorapy)
- [8. ⚙️ Painel de Configuração](#8-⚙️-painel-de-configuração-8_painel_confpy)
- [9. 🦁 Galeria de Animais com Filtros](#9-🦁-galeria-de-animais-com-filtros-9_galeria_cardspy)
- [10. 📱 App Multi-página](#10-📱-app-multi-página-10_app_multipaginapy)
- [10a. 🛒 Desafio 2 - Loja Virtual Mini](#10a-🛒-desafio-2---loja-virtual-mini-10a_desafio2py)
- [Como executar](#como-executar)
- [Sobre](#sobre)

---

## 1. 👋 Primeiro App (`1_primeiro_app.py`)

**Descrição:**  
Página inicial que exibe uma mensagem de boas-vindas centralizada.  
Demonstra como configurar título, alinhamento e adicionar textos com diferentes estilos.

**Funcionamento:**  
- Ao abrir, mostra um texto grande roxo e mensagens de boas-vindas.
- Não há interação, serve para apresentar o básico do Flet.

<img width="1856" height="813" alt="Captura de tela 2025-09-01 162805" src="https://github.com/user-attachments/assets/1ca3c2bf-54ca-4a7d-b840-2c0e800df714" />

---

## 2. 🟢 Botão Simples (`2_botao_simples.py`)

**Descrição:**  
Página com dois botões que mudam o texto exibido ao serem clicados.

**Funcionamento:**  
- Inicialmente, aparece a mensagem:  
  `"Clique no botão abaixo! 👇"`
- Ao clicar no primeiro botão, a mensagem muda para:  
  `"Se clicar no outro tem surpresa 😲"`
- Ao clicar no segundo botão, a mensagem muda para:  
  `"EI! Por que você clicou? 😲"`
- O texto muda de cor ao clicar.

**Prints:**  
- Antes do clique:  
<img width="1637" height="708" alt="Captura de tela 2025-09-01 162830" src="https://github.com/user-attachments/assets/c8d6b38e-1c95-457a-a4d0-0f2c8747807a" />
- Após clicar em um dos botões:
<img width="1815" height="764" alt="Captura de tela 2025-09-01 162836" src="https://github.com/user-attachments/assets/ca0faa82-5eaa-44ee-98a5-0d3a2d339f75" />
- Após clicar no segundo botão:
<img width="1762" height="751" alt="Captura de tela 2025-09-01 162841" src="https://github.com/user-attachments/assets/9038dfd8-3a43-484a-bb2b-8d2ef8ea8528" />

---

## 3. 📝 Campo de Texto (`3_campo_texto.py`)

**Descrição:**  
Permite ao usuário digitar seu nome e receber uma resposta personalizada.

**Funcionamento:**  
- O usuário digita o nome e clica em "Confirmar".
- Se o campo estiver vazio, aparece:  
  `"⚠️ Não sabe ler cara? Escreve teu nome ai!"` (em vermelho)
- Se o nome for muito curto, aparece:  
  `"⚠️ Escreve seu nome direito ai meu fi!"` (em laranja)
- Se o nome for válido, aparece:  
  `"✅ Olá, [nome]! Prazer em conhecê-lo(a)!"` (em verde)

**Prints:**  
- Campo vazio:  
<img width="1839" height="796" alt="Captura de tela 2025-09-01 162912" src="https://github.com/user-attachments/assets/dab6e98a-f6c4-4c26-b41f-dd22e7c9e6a2" />
- Nome inválido:  
<img width="1871" height="812" alt="Captura de tela 2025-09-01 162919" src="https://github.com/user-attachments/assets/7fb4b769-e7bf-4d80-8122-7aee6ea8c2d6" />
- Enviar campo sem nome:
<img width="1859" height="805" alt="Captura de tela 2025-09-01 162934" src="https://github.com/user-attachments/assets/b6ba8b15-e3df-4f05-becd-508ce4f6fd39" />
- Nome válido:
<img width="1775" height="781" alt="Captura de tela 2025-09-01 162927" src="https://github.com/user-attachments/assets/95f066e9-1bfb-4a9b-93e5-09197ab726a2" />


---

## 4. 🎨 Lista de Cores (`4_lista_cores.py`)

**Descrição:**  
Permite escolher uma cor em uma lista suspensa e ver uma caixa mudar de cor.

**Funcionamento:**  
- O usuário seleciona uma cor no dropdown.
- A caixa colorida muda para a cor escolhida.
- O texto dentro da caixa também muda de cor para garantir contraste (preto para amarelo/branco, branco para as demais).

**Prints:**  
- Antes da seleção:  
<img width="1890" height="839" alt="Captura de tela 2025-09-01 163002" src="https://github.com/user-attachments/assets/0510610a-4bd5-4393-a1e2-f014fd0f2143" />
- Dropdown aberto:
<img width="1883" height="848" alt="Captura de tela 2025-09-01 163009" src="https://github.com/user-attachments/assets/f3bac05c-59dc-44c8-85e9-d111f2ea891c" />
- Após selecionar "Rosa":  
<img width="1897" height="856" alt="Captura de tela 2025-09-01 163015" src="https://github.com/user-attachments/assets/b761a470-4c57-4779-9f91-a6da799aafc4" />

---

## 5. 🧩 Layout Básico (`5_layout_basico.py`)

**Descrição:**  
Demonstra o uso de layouts Column e Row para organizar botões e caixas coloridas.

**Funcionamento:**  
- Mostra uma linha com três botões centralizados.
- Abaixo, duas caixas coloridas empilhadas em coluna.
- Não há interação, serve para mostrar organização visual.

**Print:**  
<img width="1893" height="857" alt="Captura de tela 2025-09-01 163050" src="https://github.com/user-attachments/assets/9de35536-a3df-46e3-9b5d-c08cdcee2785" />


---

## 5a. 🧞‍♂️ Desafio 1 - Criador de Perfil (`5a_desafio1.py`)

**Descrição:**  
Formulário para criar um perfil de usuário com validação.

**Funcionamento:**  
- O usuário preenche nome, idade, escola/universidade e hobby.
- Ao clicar em "Criar Perfil":
  - Se faltar algum campo ou houver erro, aparece uma mensagem de erro em vermelho.
  - Se tudo estiver correto, aparece um cartão com o perfil criado, mostrando nome, idade, categoria (Jovem, Adulto, Experiente), escola e hobby.
- O botão "Limpar" apaga todos os campos e esconde o cartão.

**Prints:**  
- Formulário:  
<img width="1885" height="829" alt="Captura de tela 2025-09-01 163131" src="https://github.com/user-attachments/assets/fcd4c63d-5d20-47d4-8cde-940b584bc058" />
- Perfil criado:  
<img width="1879" height="847" alt="Captura de tela 2025-09-01 163146" src="https://github.com/user-attachments/assets/dc02e13a-a285-46db-a758-9f5f48f244c4" />

---

## 6. 🔢 Contador Completo (`6_contador.py`)

**Descrição:**  
Contador com botões para incrementar, decrementar, resetar e alterar o valor em passos de 1 ou 5.

**Funcionamento:**  
- Botões "+" e "-" aumentam ou diminuem em 1.
- Botões "+5" e "-5" aumentam ou diminuem em 5.
- O botão "Reset" zera o contador.
- O texto muda de cor: verde para valores positivos, vermelho para negativos, roxo para zero.
- Mensagem abaixo indica o estado do contador.

**Prints:**  
- Valor zero:  
<img width="1841" height="828" alt="Captura de tela 2025-09-01 163435" src="https://github.com/user-attachments/assets/8afad5ad-0ef2-4367-90cb-bcdc20c27a3c" />
- Valor positivo:  
<img width="1870" height="815" alt="Captura de tela 2025-09-01 163444" src="https://github.com/user-attachments/assets/0e7cd6e3-cb72-4806-aef8-d2d966277283" />
- Valor negativo:  
<img width="1906" height="852" alt="Captura de tela 2025-09-02 095701" src="https://github.com/user-attachments/assets/19ac7256-4880-4c84-a6e0-c177fb27d8d0" />

---

## 7. 🧮 Calculadora Simples (`7_calculadora.py`)

**Descrição:**  
Calculadora com operações básicas, porcentagem e potenciação, além de tratamento de erros.

**Funcionamento:**  
- O usuário digita dois números, escolhe a operação e clica em "Calcular".
- Mostra o resultado formatado.
- Se tentar dividir por zero, exibe erro em vermelho.
- Se digitar valores inválidos, exibe erro.
- O botão "Limpar" apaga todos os campos e mostra mensagem de campos limpos.

**Prints:**  
- Antes do cálculo:  
<img width="1849" height="811" alt="Captura de tela 2025-09-02 080643" src="https://github.com/user-attachments/assets/6138fdc3-1246-4764-831b-158d6b280469" />
- Resultado de uma divisão:  
<img width="1889" height="839" alt="Captura de tela 2025-09-02 080738" src="https://github.com/user-attachments/assets/dbfdcad3-8433-462c-a0e7-acbafe56bc33" />
- Erro de divisão por zero:  
<img width="1878" height="857" alt="Captura de tela 2025-09-02 100031" src="https://github.com/user-attachments/assets/197ba5d1-0ef0-4745-af36-daffcdc769b7" />


---

## 8. ⚙️ Painel de Configuração (`8_painel_conf.py`)

**Descrição:**  
Permite configurar o estilo de um texto (cor, tamanho, negrito, itálico, sublinhado, riscado) e o fundo, com preview em tempo real.

**Funcionamento:**  
- O usuário pode ativar/desativar negrito, itálico, sublinhado, riscado.
- Pode escolher cor do texto e do fundo.
- O texto de preview muda instantaneamente conforme as opções.

**Print:**  

- Configuração Padrão:
<img width="1858" height="850" alt="Captura de tela 2025-09-02 080856" src="https://github.com/user-attachments/assets/1a9091eb-814b-401e-a76e-07ad5aa350ba" />
- Configurações alteradas:
<img width="1881" height="842" alt="Captura de tela 2025-09-02 080908" src="https://github.com/user-attachments/assets/22352199-9b98-4920-bbf1-7cba9ed093f5" />


---

## 9. 🦁 Galeria de Animais com Filtros (`9_galeria_cards.py`)

**Descrição:**  
Exibe uma galeria de cards de animais, com filtros por categoria, tamanho, sociabilidade e busca por nome.

**Funcionamento:**  
- O usuário pode filtrar por categoria (Doméstico, Selvagem, Aquático), tamanho, sociabilidade e buscar pelo nome.
- Os cards exibem emoji, nome, descrição e cor de fundo personalizada.
- O contador mostra quantos animais estão sendo exibidos.

**Print:**  
- Galeria sem filtros:
<img width="1887" height="826" alt="Captura de tela 2025-09-02 080945" src="https://github.com/user-attachments/assets/ee8270e1-5b5e-448f-ae3f-feca5ea712c2" />
- Galeria com filtros:
<img width="1910" height="852" alt="Captura de tela 2025-09-02 080955" src="https://github.com/user-attachments/assets/8e5d5299-1a0b-4af1-a1d0-672f88ccfb2e" />


---

## 10. 📱 App Multi-página (`10_app_multipagina.py`)

**Descrição:**  
App com navegação entre várias páginas (Home, Perfil, Configurações, Sobre, Estatísticas), barra de navegação colorida e gerenciamento de estado do usuário.

**Funcionamento:**  
- **Home:** Mensagem de boas-vindas e botão para estatísticas.
- **Perfil:** Mostra nome, nível, pontos e permite ganhar pontos. O nível muda automaticamente conforme a pontuação.
- **Configurações:** Alterna modo escuro, notificações e som.
- **Sobre:** Informações do app.
- **Estatísticas:** Mostra pontos e nível atualizados em tempo real.
- Barra de navegação fixa na parte inferior para trocar de página.

**Prints:**  
- Página Home:  
<img width="1914" height="853" alt="Captura de tela 2025-09-02 081106" src="https://github.com/user-attachments/assets/85aa64f2-07cb-481a-9fac-fd19925890dd" />
- Página Perfil:  
<img width="1917" height="828" alt="Captura de tela 2025-09-02 081117" src="https://github.com/user-attachments/assets/39c184c7-eef9-472b-ad0b-07fcb82e7161" />

---

## 10a. 🛒 Desafio 2 - Loja Virtual Mini (`10a_desafio2.py`)

**Descrição:**  
Simula uma loja virtual com produtos de várias categorias, filtros, busca, carrinho de compras com agrupamento de itens e finalização de compra.

**Funcionamento:**  
- O usuário pode filtrar produtos por categoria (incluindo "Brinquedos"), faixa de preço e busca por nome.
- Ao clicar em um produto, ele é adicionado ao carrinho.
- O carrinho agrupa produtos iguais e mostra a quantidade (ex: "Livro x3").
- É possível remover itens individualmente.
- O botão "Finalizar Compra" limpa o carrinho e mostra mensagem de sucesso.

**Prints:**  
- Produtos e filtros:
<img width="1907" height="873" alt="Captura de tela 2025-09-02 081148" src="https://github.com/user-attachments/assets/a9f9238e-4b6f-406f-ba8f-99e4b81dfd8b" />
- Carrinho com agrupamento:  
<img width="1911" height="858" alt="Captura de tela 2025-09-02 081157" src="https://github.com/user-attachments/assets/09f4c114-1269-459b-ba6b-b005010ba744" />


## Como executar

1. Crie um ambiente virtual (recomendado):
   ```
   python -m venv .venv
   ```
2. Ative o ambiente virtual:
   ```
   .venv\Scripts\activate
   ```
3. Instale o Flet Desktop:
   ```
   pip install flet-desktop
   ```
4. Execute o arquivo desejado:
   ```
   flet run --web nome_do_arquivo.py
   ```

---

## Sobre

Essas atividades fazem parte do aprendizado de interfaces gráficas e lógica de programação usando Flet e Python.  
Sinta-se à vontade para explorar, modificar e criar novas ideias a partir destes exemplos!
Caso queira visualizar melhor as imagens de solução e as imagens com os exemplos de códigos simples, visualize as pastas dentro do arquivo `Fleet-01-Gustavo`