# CP02---PYTHON---Jogo-da-Velha

# 🎮 Jogo da Velha em Python

Este projeto implementa o clássico **Jogo da Velha (Tic-Tac-Toe)** em Python, utilizando uma **matriz 3x3** para representar o tabuleiro.  
O jogo foi desenvolvido para **dois jogadores**, com alternância de turnos e escolha livre entre os símbolos **X** e **O**.  

---

## 🧩 Objetivo

Criar um programa em Python que permita dois jogadores se enfrentarem em um jogo da velha interativo no terminal, exibindo o tabuleiro após cada jogada e determinando automaticamente se há um vencedor ou empate.

---

## 📜 Regras do Jogo

- O jogo é disputado em um **tabuleiro 3x3**.  
- Dois jogadores escolhem entre **X** e **O**.  
- Os jogadores **alternam suas jogadas**, marcando uma célula vazia do tabuleiro.  
- O jogo termina quando:
  - Um jogador completa **uma linha, coluna ou diagonal** com seu símbolo;  
  - Ou **todas as células forem preenchidas** sem vencedor (empate).

---

## 🧠 Estrutura do Programa

O programa foi estruturado em **funções** para facilitar a leitura e a manutenção do código, conforme o enunciado:

| Função | Descrição |
|--------|------------|
| `exibir_tabuleiro()` | Mostra o tabuleiro 3x3 atualizado após cada jogada |
| `verificar_vencedor()` | Verifica se algum jogador completou uma linha, coluna ou diagonal |
| `verificar_empate()` | Detecta se o tabuleiro está cheio sem vencedor |
| `jogada_valida()` | Garante que o jogador não jogue fora dos limites ou em uma célula ocupada |
| `jogar()` | Controla o fluxo principal do jogo, alternando entre os jogadores e verificando as condições de vitória ou empate |

---

## ⚙️ Instalação e Execução
# 1️⃣ Clonar o repositório
git clone https://github.com/PedroIavaroneCustodio/CP02---PYTHON---Jogo-da-Velha.git

# 2️⃣ Acessar a pasta do projeto
cd CP02---PYTHON---Jogo-da-Velha

# 3️⃣ Verificar se o Python 3 está instalado
python --version
# ou, dependendo do sistema
python3 --version

# 4️⃣ Executar o jogo
python jogo_da_velha.py
# ou, se precisar
python3 jogo_da_velha.py


### 🔹 Pré-requisitos

- **Python 3** instalado no sistema  
  (verifique com o comando abaixo)

```bash
python --version
ou
python3 --version

# 👨‍🏫 Professor
Fernando Timóteo Fernandes

# 👥 Integrantes
Pedro Iavarone — RM 567638
Rafael Tavares — RM 567357
Yuri Santos — RM 568512
Gabriel Muniz — RM 568237