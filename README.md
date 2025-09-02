# Atividades Flet - Programação Mobile

Este repositório reúne atividades práticas desenvolvidas em Python com o framework [Flet](https://flet.dev/), explorando conceitos de interface gráfica, lógica e interação.  
Cada atividade possui um print ilustrativo e uma explicação detalhada do funcionamento e das interações possíveis.

---

## 1. Primeiro App (`1_primeiro_app.py`)

**Descrição:**  
Página inicial que exibe uma mensagem de boas-vindas centralizada.  
Demonstra como configurar título, alinhamento e adicionar textos com diferentes estilos.

**Funcionamento:**  
- Ao abrir, mostra um texto grande roxo e mensagens de boas-vindas.
- Não há interação, serve para apresentar o básico do Flet.

![Print Primeiro App](https://raw.githubusercontent.com/seu-usuario/seu-repo/main/prints/1_primeiro_app.png)

---

## 2. Botão Simples (`2_botao_simples.py`)

**Descrição:**  
Página com dois botões que mudam o texto exibido ao serem clicados.

**Funcionamento:**  
- Inicialmente, aparece a mensagem:  
  `"Clique no botão abaixo! 👇"`
- Ao clicar no primeiro botão, a mensagem muda para:  
  `"Se clicar no outro tem surpresa 😲"`
- Ao clicar no segundo botão, a mensagem muda para:  
  `"EI! Por que você clicou? 😲"`
- O texto muda de cor para verde ao clicar.

**Prints:**  
- Antes do clique:  
  ![Print Botão Simples - Antes](https://raw.githubusercontent.com/seu-usuario/seu-repo/main/prints/2_botao_simples_antes.png)
- Após clicar em um dos botões:  
  ![Print Botão Simples - Depois](https://raw.githubusercontent.com/seu-usuario/seu-repo/main/prints/2_botao_simples_depois.png)

---

## 3. Campo de Texto (`3_campo_texto.py`)

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
  ![Print Campo de Texto - Erro](https://raw.githubusercontent.com/seu-usuario/seu-repo/main/prints/3_campo_texto_erro.png)
- Nome válido:  
  ![Print Campo de Texto - Ok](https://raw.githubusercontent.com/seu-usuario/seu-repo/main/prints/3_campo_texto_ok.png)

---

## 4. Lista de Cores (`4_lista_cores.py`)

**Descrição:**  
Permite escolher uma cor em uma lista suspensa e ver uma caixa mudar de cor.

**Funcionamento:**  
- O usuário seleciona uma cor no dropdown.
- A caixa colorida muda para a cor escolhida.
- O texto dentro da caixa também muda de cor para garantir contraste (preto para amarelo/branco, branco para as demais).

**Prints:**  
- Antes da seleção:  
  ![Print Lista de Cores - Inicial](https://raw.githubusercontent.com/seu-usuario/seu-repo/main/prints/4_lista_cores_inicial.png)
- Após selecionar "Azul":  
  ![Print Lista de Cores - Azul](https://raw.githubusercontent.com/seu-usuario/seu-repo/main/prints/4_lista_cores_azul.png)

---

## 5. Layout Básico (`5_layout_basico.py`)

**Descrição:**  
Demonstra o uso de layouts Column e Row para organizar botões e caixas coloridas.

**Funcionamento:**  
- Mostra uma linha com três botões centralizados.
- Abaixo, duas caixas coloridas empilhadas em coluna.
- Não há interação, serve para mostrar organização visual.

**Print:**  
![Print Layout Básico](https://raw.githubusercontent.com/seu-usuario/seu-repo/main/prints/5_layout_basico.png)

---

## 5a. Desafio 1 - Criador de Perfil (`5a_desafio1.py`)

**Descrição:**  
Formulário para criar um perfil de usuário com validação.

**Funcionamento:**  
- O usuário preenche nome, idade, escola/universidade e hobby.
- Ao clicar em "Criar Perfil":
  - Se faltar algum campo ou houver erro, aparece uma mensagem de erro em vermelho.
  - Se tudo estiver correto, aparece um cartão com o perfil criado, mostrando nome, idade, categoria (Jovem, Adulto, Experiente), escola e hobby.
- O botão "Limpar" apaga todos os campos e esconde o cartão.

**Prints:**  
- Formulário preenchido:  
  ![Print Criador de Perfil - Formulário](https://raw.githubusercontent.com/seu-usuario/seu-repo/main/prints/5a_desafio1_form.png)
- Perfil criado:  
  ![Print Criador de Perfil - Cartão](https://raw.githubusercontent.com/seu-usuario/seu-repo/main/prints/5a_desafio1_cartao.png)

---

## 6. Contador Completo (`6_contador.py`)

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
  ![Print Contador - Zero](https://raw.githubusercontent.com/seu-usuario/seu-repo/main/prints/6_contador_zero.png)
- Valor positivo:  
  ![Print Contador - Positivo](https://raw.githubusercontent.com/seu-usuario/seu-repo/main/prints/6_contador_positivo.png)
- Valor negativo:  
  ![Print Contador - Negativo](https://raw.githubusercontent.com/seu-usuario/seu-repo/main/prints/6_contador_negativo.png)

---

## 7. Calculadora Simples (`7_calculadora.py`)

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
  ![Print Calculadora - Inicial](https://raw.githubusercontent.com/seu-usuario/seu-repo/main/prints/7_calculadora_inicial.png)
- Resultado de uma soma:  
  ![Print Calculadora - Soma](https://raw.githubusercontent.com/seu-usuario/seu-repo/main/prints/7_calculadora_soma.png)
- Erro de divisão por zero:  
  ![Print Calculadora - Erro](https://raw.githubusercontent.com/seu-usuario/seu-repo/main/prints/7_calculadora_erro.png)

---

## 8. Painel de Configuração (`8_painel_conf.py`)

**Descrição:**  
Permite configurar o estilo de um texto (cor, tamanho, negrito, itálico, sublinhado, riscado) e o fundo, com preview em tempo real.

**Funcionamento:**  
- O usuário pode ativar/desativar negrito, itálico, sublinhado, riscado.
- Pode escolher cor do texto e do fundo.
- O texto de preview muda instantaneamente conforme as opções.

**Print:**  
![Print Painel de Configuração](https://raw.githubusercontent.com/seu-usuario/seu-repo/main/prints/8_painel_conf.png)

---

## 9. Galeria de Animais com Filtros (`9_galeria_cards.py`)

**Descrição:**  
Exibe uma galeria de cards de animais, com filtros por categoria, tamanho, sociabilidade e busca por nome.

**Funcionamento:**  
- O usuário pode filtrar por categoria (Doméstico, Selvagem, Aquático), tamanho, sociabilidade e buscar pelo nome.
- Os cards exibem emoji, nome, descrição e cor de fundo personalizada.
- O contador mostra quantos animais estão sendo exibidos.

**Print:**  
![Print Galeria de Animais](https://raw.githubusercontent.com/seu-usuario/seu-repo/main/prints/9_galeria_cards.png)

---

## 10. App Multi-página (`10_app_multipagina.py`)

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
  ![Print App Multi-página - Home](https://raw.githubusercontent.com/seu-usuario/seu-repo/main/prints/10_app_multipagina_home.png)
- Página Perfil:  
  ![Print App Multi-página - Perfil](https://raw.githubusercontent.com/seu-usuario/seu-repo/main/prints/10_app_multipagina_perfil.png)
- Página Estatísticas:  
  ![Print App Multi-página - Stats](https://raw.githubusercontent.com/seu-usuario/seu-repo/main/prints/10_app_multipagina_stats.png)

---

## 10a. Desafio 2 - Loja Virtual Mini (`10a_desafio2.py`)

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
  ![Print Loja Virtual Mini - Produtos](https://raw.githubusercontent.com/seu-usuario/seu-repo/main/prints/10a_desafio2_produtos.png)
- Carrinho com agrupamento:  
  ![Print Loja Virtual Mini - Carrinho](https://raw.githubusercontent.com/seu-usuario/seu-repo/main/prints/10a_desafio2_carrinho.png)

---

> **Observação:**  
> Se você está visualizando localmente, coloque suas imagens na pasta `prints/` e ajuste os caminhos conforme necessário.  
> Para exibir imagens no GitHub, substitua `seu-usuario/seu-repo` pelo caminho real do seu repositório.

---

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
