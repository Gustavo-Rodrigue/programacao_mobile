---
# ⚖️ Flet-02 - Calculadora de IMC com Theme Switch

Aplicação feita com Python e Flet que calcula o **IMC (Índice de Massa Corporal)** a partir do peso e altura informados.  
Inclui também um **alternador de tema** (claro/escuro) para demonstrar o uso de `Switch` e `theme_mode` no Flet.

---

## ✨ Funcionalidades

- Campo para digitar **peso** (kg) e **altura** (m).
- Botão para **calcular IMC** e exibir a classificação:
  - Abaixo do peso
  - Peso normal
  - Sobrepeso
  - Obesidade
- Mensagens e cores reativas conforme o resultado.
- **Validação** de campos vazios ou inválidos.
- **Switch para alternar entre modo claro e escuro** com mudança automática de aparência.

---

## 🧠 Classificação do IMC

| IMC               | Classificação       | Cor         |
|-------------------|---------------------|-------------|
| Menor que 18.5    | Abaixo do peso      | Amarelo     |
| 18.5 a 24.9       | Peso normal         | Verde       |
| 25 a 29.9         | Sobrepeso           | Laranja     |
| 30 ou mais        | Obesidade           | Vermelho    |

---

## 📸 Exemplos

### 🌞 Tema Claro
<img width="1910" height="841" alt="Captura de tela 2025-09-02 151051" src="https://github.com/user-attachments/assets/ed4865aa-ab97-47d7-85a2-f5184870848d" />

### 🌚 Tema Escuro
<img width="1907" height="864" alt="Captura de tela 2025-09-02 151101" src="https://github.com/user-attachments/assets/7633212b-1b53-42d5-b750-115a522435f9" />

---

## 🧪 Como executar

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
