# People Analytics Dashboard — IBM HR

Dashboard interativo de People Analytics construído com Python, Pandas e Streamlit, usando o dataset público [IBM HR Analytics Employee Attrition & Performance](https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset).

## Demo

> Link do Streamlit Cloud: *(adicionar após o deploy)*

## Sobre o Projeto

Dashboard com duas abas analíticas para responder perguntas de negócio relevantes para a área de Pessoas:

**Aba HeadCount** — Visão geral do quadro de colaboradores ativos.

**Aba Turnover** — Análise de saída de colaboradores: quem sai, quando, e por quê.

## KPIs e Gráficos

### Aba HeadCount
| KPI | Descrição |
|-----|-----------|
| Total de Funcionários | Headcount com filtros aplicados |
| Idade Média | Média de Age |
| Tempo Médio na Empresa | Média de YearsAtCompany |
| Salário Médio | Média de MonthlyIncome |

Gráficos: Headcount por Departamento · Headcount por Cargo (Top 8) · Distribuição por Gênero · Headcount por Nível de Cargo · Headcount por Área de Formação · Distribuição de Idade

### Aba Turnover
| KPI | Descrição |
|-----|-----------|
| Taxa de Turnover | % de saídas (Attrition = Yes) |
| Total de Saídas | Contagem absoluta |
| Satisfação Média | Média de JobSatisfaction (1–4) |
| % com Hora Extra | % de OverTime = Yes |

Gráficos: Turnover por Departamento · Turnover por Cargo (Top 8) · Turnover por Gênero · Turnover por Nível de Cargo · Satisfação Ficou vs Saiu · Hora Extra vs Turnover

## Filtros Interativos

Aplicados simultaneamente em ambas as abas:
- **Departamento** — multiselect
- **Gênero** — multiselect
- **Nível do Cargo** — slider de range (1 a 5)

## Stack Técnica

```
Python 3.10+
Streamlit  — interface interativa com abas e sidebar
Pandas     — análise e transformação de dados
NumPy      — cálculos numéricos (médias, percentuais)
Matplotlib — visualização com tema dark personalizado
```

## Estrutura do Repositório

```
people-analytics-dashboard/
├── app.py              ← aplicação Streamlit (tabs + sidebar + CSS)
├── analysis.py         ← funções de análise com Pandas/NumPy
├── charts.py           ← funções de gráficos com Matplotlib (tema Storm)
├── requirements.txt    ← dependências para o Streamlit Cloud
├── .streamlit/
│   └── config.toml     ← tema dark Storm
└── data/
    └── WA_Fn-UseC_-HR-Employee-Attrition.csv
```

## Como Rodar Localmente

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Dataset

- **Fonte:** Kaggle — IBM HR Analytics Employee Attrition & Performance
- **Registros:** 1.470 funcionários, 35 colunas
- **Criado por:** Cientistas de dados da IBM (dataset fictício para fins educacionais)

---

Desenvolvido por **Thiago Alexandre** | [LinkedIn](https://linkedin.com) | [GitHub](https://github.com)
