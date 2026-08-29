# Academic Projects

Trabalhos e projetos acadêmicos desenvolvidos durante o curso de **Engenharia de Software** na
**Universidade Estadual de Maringá (UEM)**.

Este repositório reúne, em um só lugar, os trabalhos que antes estavam espalhados em
repositórios separados. Cada pasta corresponde a uma disciplina e contém o código como foi
entregue.

---

## Disciplinas

| Disciplina | Pasta | Sobre o trabalho | Linguagem |
|---|---|---|---|
| Fundamentos de Algoritmos | [`fundamentos-de-algoritmos/`](./fundamentos-de-algoritmos) | Exercícios e implementações dos algoritmos base da disciplina, incluindo leitura e processamento de dados a partir de arquivo CSV. | Python |
| Estrutura de Dados | [`estrutura-de-dados/trabalho-1/`](./estrutura-de-dados/trabalho-1) | Primeiro trabalho prático, com implementação e manipulação de arranjos e das estruturas de dados estudadas em aula. | Python |
| Estrutura de Dados | [`estrutura-de-dados/trabalho-2/`](./estrutura-de-dados/trabalho-2) | Segundo trabalho prático, avançando sobre as estruturas e a análise de complexidade. | Python |
| Programação Funcional | [`programacao-funcional/`](./programacao-funcional) | Cerca de 50 exercícios no paradigma funcional: imutabilidade, funções puras, recursão, pattern matching, ordenação e árvore de busca. | Gleam, Racket |
| Organização e Recuperação de Dados | [`organizacao-e-recuperacao-de-dados/`](./organizacao-e-recuperacao-de-dados) | Implementação de registros e compressão de dados, tratando organização de arquivos e recuperação da informação sobre uma base de filmes. | Python |

> As descrições acima resumem o escopo de cada disciplina.

**Programação Orientada a Objetos** é mantida em repositório próprio:
[Medical-clinic-management-system](https://github.com/JocaMgtt0/Medical-clinic-management-system) `Java`

---

## Estrutura

```
academic-projects/
├── fundamentos-de-algoritmos/
├── estrutura-de-dados/
│   ├── trabalho-1/
│   └── trabalho-2/
├── programacao-funcional/
└── organizacao-e-recuperacao-de-dados/
```

---

## Como executar

**Python**

```bash
cd fundamentos-de-algoritmos
python nome-do-arquivo.py
```

Alguns scripts leem arquivos de dados da própria pasta (`medals.csv`, `filmes.dat`), então rode
sempre de dentro do diretório do trabalho.

**Racket**

```bash
racket programacao-funcional/nome-do-arquivo.rkt
```

**Gleam**

Os arquivos `.gleam` são módulos soltos de exercícios, sem projeto Gleam configurado. Para
executar, copie o módulo desejado para dentro de um projeto criado com `gleam new`.

---

## Observação

Este é código acadêmico, escrito dentro do escopo e do prazo de cada disciplina. Ele mostra
minha evolução ao longo do curso, e não necessariamente como eu escreveria hoje. Para projetos
onde apliquei o que aprendi em contextos reais, veja os
[repositórios fixados no meu perfil](https://github.com/JocaMgtt0).

---

<p align="center">
  <sub>Engenharia de Software &nbsp;|&nbsp; Universidade Estadual de Maringá (UEM)</sub>
</p>
