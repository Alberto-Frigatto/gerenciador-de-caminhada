# Gerenciador de caminhada

Sistema para gerenciar o seu exercício, oferecendo informações e estatísticas

## Créditos

**Autor**: Alberto Frigatto

**Email**: albertofrigatto.comercial@gmail.com

**LinkedIn**: [Clique aqui](https://www.linkedin.com/in/alberto-frigatto-de-andrade-ferreira-a72022251/)


## Índices

- [Iniciando](#iniciando)
- [Funcionalidades](#funcionalidades)

## iniciando

Instale o Python na versão 3.11.2. [Clique aqui para baixar](https://www.python.org/downloads/)

Baixe o projeto via GitHub

```
git clone https://github.com/Alberto-Frigatto/gerenciador-de-caminhada.git
```

Estando na pasta do projeto, ative o ambiente virtual e execute o projeto

```
python -m venv .venv
.venv/scripts/activate
pip install -r requirements.txt
python main.py
```

## Funcionalidades

- [1 - Visualizar caminhadas](#1---visualizar-caminhadas)
- [3 - Excluir caminhada](#3---excluir-caminhada)
- [2 - Cadastrar caminhada](#2---cadastrar-caminhada)
- [4 - Tempo médio das caminhadas](#4---tempo-médio-das-caminhadas)
- [5 - Desvio padrão dos tempos das caminhadas](#5---desvio-padrão-dos-tempos-das-caminhadas)
- [6 - Quilometragem total](#6---quilometragem-total)
- [7 - Quilometragem total mensal](#8---quilometragem-total-mensal)
- [8 - Gráfico da quilometragem total mensal](#10---gráfico-da-quilometragem-total-mensal)
- [9 - Gráfico dos tempos das caminhadas](#11---gráfico-dos-tempos-das-caminhadas)
- [10 - Sair](#12---sair)

### 1 - Visualizar caminhadas

Exibirá todas as caminhadas cadastradas com as informações separadas por colunas:

- Data
- Distância
- Duração

### 2 - Cadastrar caminhada

Irá solicitar as informações de **Data** *(dd/mm/aaaa)*, **Distância** *(Km)* e **Duração** *(min)* para cadastrar uma caminhada e uma confirmação para cadastramento. Ao tentar cadastrar, se for detectada alguma irregularidade nos dados será exibida uma mensagem apontando a irregularidade e o processo para cadastrar uma caminhada recomeça.

### 3 - Excluir caminhada

Exibirá as caminhadas cadastradas, solicitará o índice da caminhada e uma confirmação para exclusão

### 4 - Tempo médio das caminhadas

Exibirá seu tempo médio em minutos

### 5 - Desvio padrão dos tempos das caminhadas

Exibirá o desvio padrão dos tempos das caminhadas

### 6 - Quilometragem total

Exibirá a quilometragem total somando todas as distâncias das caminhadas

### 7 - Quilometragem total mensal

Exibirá o quanto você andou por mês

### 8 - Gráfico da quilometragem total mensal

Exibirá o gráfico do quanto você andou por mês

### 9 - Gráfico dos tempos das caminhadas

Exibirá o gráfico dos tempos de suas caminhadas

### 10 - Sair

Salvará e encerrará o app

<br />

**Obrigado por usar meu projeto :)**
