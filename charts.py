"""Funções de geração de gráficos com Matplotlib — tema Storm."""

import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import pandas as pd

# ── Paleta Storm ───────────────────────────────────────────────────────────────
COR_PRINCIPAL  = "#00A1FF"
COR_SECUNDARIA = "#0050EB"
COR_SERIE = ["#00A1FF", "#009FEF", "#008CEE", "#0078ED", "#0050EB", "#0641C8", "#0B31A5"]
COR_DESTAQUE   = "#8BC7F7"
COR_SAIU       = "#00A1FF"
COR_FICOU      = "#0B31A5"
COR_TEXTO      = "#8899aa"
FUNDO_GRAFICO  = "#1e2225"


def _storm(fig: plt.Figure, ax: plt.Axes, title: str) -> None:
    """Aplica o tema Storm em gráficos de barras e histogramas."""
    fig.patch.set_facecolor(FUNDO_GRAFICO)
    ax.set_facecolor(FUNDO_GRAFICO)
    ax.tick_params(colors=COR_TEXTO, labelcolor=COR_TEXTO, labelsize=9)
    ax.spines["bottom"].set_color((1.0, 1.0, 1.0, 0.08))
    ax.spines["left"].set_color((1.0, 1.0, 1.0, 0.08))
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.set_title(title, color="#ffffff", fontsize=12, fontweight="bold", pad=10)
    ax.xaxis.label.set_color(COR_TEXTO)
    ax.yaxis.label.set_color(COR_TEXTO)


def _storm_donut(fig: plt.Figure, ax: plt.Axes, title: str) -> None:
    """Aplica o tema Storm em gráficos de rosca."""
    fig.patch.set_facecolor(FUNDO_GRAFICO)
    ax.set_facecolor(FUNDO_GRAFICO)
    ax.set_title(title, color="#ffffff", fontsize=12, fontweight="bold", pad=10)


def _bar_labels(ax: plt.Axes, bars, fmt: str = "%.0f") -> None:
    """Adiciona rótulos nas barras com a cor de texto Storm."""
    for lbl in ax.bar_label(bars, fmt=fmt, padding=5):
        lbl.set_color(COR_TEXTO)
        lbl.set_fontsize(9)


# ── Gráficos — Aba HeadCount ──────────────────────────────────────────────────

def chart_headcount_by_department(df: pd.DataFrame) -> plt.Figure:
    """Barra horizontal — headcount por departamento."""
    fig, ax = plt.subplots(figsize=(8, 3.5))
    colors = COR_SERIE[:len(df)]
    bars = ax.barh(df["Department"], df["Count"], color=colors)
    _bar_labels(ax, bars)
    ax.set_xlim(0, df["Count"].max() * 1.2)
    ax.set_xlabel("Funcionários")
    _storm(fig, ax, "Headcount por Departamento")
    fig.tight_layout()
    plt.close(fig)
    return fig


def chart_headcount_by_jobrole(df: pd.DataFrame) -> plt.Figure:
    """Barra horizontal — headcount por cargo (top 8)."""
    fig, ax = plt.subplots(figsize=(8, 4.5))
    colors = COR_SERIE[:len(df)]
    bars = ax.barh(df["JobRole"], df["Count"], color=colors)
    _bar_labels(ax, bars)
    ax.set_xlim(0, df["Count"].max() * 1.2)
    ax.set_xlabel("Funcionários")
    _storm(fig, ax, "Headcount por Cargo (Top 8)")
    fig.tight_layout()
    plt.close(fig)
    return fig


def chart_gender_donut(df: pd.DataFrame) -> plt.Figure:
    """Rosca — proporção de funcionários por gênero."""
    fig, ax = plt.subplots(figsize=(6, 5))
    wedgeprops = {"width": 0.5, "edgecolor": FUNDO_GRAFICO, "linewidth": 2}
    colors = COR_SERIE[:len(df)]
    ax.pie(
        df["Count"], labels=df["Gender"], colors=colors,
        wedgeprops=wedgeprops, autopct="%1.1f%%",
        textprops={"color": "#e8eaf0", "fontsize": 9},
    )
    _storm_donut(fig, ax, "Distribuição por Gênero")
    fig.tight_layout()
    plt.close(fig)
    return fig


def chart_headcount_by_joblevel(df: pd.DataFrame) -> plt.Figure:
    """Barra vertical — headcount por nível de cargo (1-5)."""
    fig, ax = plt.subplots(figsize=(6, 4))
    colors = COR_SERIE[:len(df)]
    bars = ax.bar(df["JobLevel"].astype(str), df["Count"], color=colors, width=0.6)
    _bar_labels(ax, bars)
    ax.set_ylim(0, df["Count"].max() * 1.2)
    ax.set_xlabel("Nível do Cargo")
    ax.set_ylabel("Funcionários")
    ax.yaxis.set_major_locator(mticker.MaxNLocator(integer=True))
    _storm(fig, ax, "Headcount por Nível de Cargo")
    fig.tight_layout()
    plt.close(fig)
    return fig


def chart_headcount_by_education(df: pd.DataFrame) -> plt.Figure:
    """Barra horizontal — headcount por área de formação."""
    fig, ax = plt.subplots(figsize=(8, 4.5))
    colors = COR_SERIE[:len(df)]
    bars = ax.barh(df["EducationField"], df["Count"], color=colors)
    _bar_labels(ax, bars)
    ax.set_xlim(0, df["Count"].max() * 1.2)
    ax.set_xlabel("Funcionários")
    _storm(fig, ax, "Headcount por Área de Formação")
    fig.tight_layout()
    plt.close(fig)
    return fig


def chart_age_histogram(age_series: pd.Series) -> plt.Figure:
    """Histograma — distribuição etária dos funcionários."""
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.hist(age_series, bins=20, color=COR_PRINCIPAL, edgecolor=FUNDO_GRAFICO, linewidth=0.8)
    ax.set_xlabel("Idade")
    ax.set_ylabel("Funcionários")
    ax.yaxis.set_major_locator(mticker.MaxNLocator(integer=True))
    _storm(fig, ax, "Distribuição de Idade")
    fig.tight_layout()
    plt.close(fig)
    return fig


# ── Gráficos — Aba Turnover ───────────────────────────────────────────────────

def chart_attrition_by_department(df: pd.DataFrame) -> plt.Figure:
    """Barra horizontal — taxa de turnover (%) por departamento."""
    fig, ax = plt.subplots(figsize=(8, 3.5))
    colors = [COR_SAIU if v == df["AttritionRate"].max() else COR_SECUNDARIA
              for v in df["AttritionRate"]]
    bars = ax.barh(df["Department"], df["AttritionRate"], color=colors)
    _bar_labels(ax, bars, fmt="%.1f%%")
    ax.set_xlim(0, df["AttritionRate"].max() * 1.3)
    ax.set_xlabel("Taxa de Turnover (%)")
    _storm(fig, ax, "Turnover por Departamento")
    fig.tight_layout()
    plt.close(fig)
    return fig


def chart_attrition_by_jobrole(df: pd.DataFrame) -> plt.Figure:
    """Barra horizontal — taxa de turnover (%) por cargo (top 8)."""
    fig, ax = plt.subplots(figsize=(8, 4.5))
    colors = [COR_SAIU if v == df["AttritionRate"].max() else COR_SECUNDARIA
              for v in df["AttritionRate"]]
    bars = ax.barh(df["JobRole"], df["AttritionRate"], color=colors)
    _bar_labels(ax, bars, fmt="%.1f%%")
    ax.set_xlim(0, df["AttritionRate"].max() * 1.3)
    ax.set_xlabel("Taxa de Turnover (%)")
    _storm(fig, ax, "Turnover por Cargo (Top 8)")
    fig.tight_layout()
    plt.close(fig)
    return fig


def chart_attrition_by_gender(df: pd.DataFrame) -> plt.Figure:
    """Rosca — proporção de saídas por gênero."""
    fig, ax = plt.subplots(figsize=(6, 5))
    wedgeprops = {"width": 0.5, "edgecolor": FUNDO_GRAFICO, "linewidth": 2}
    colors = COR_SERIE[:len(df)]
    ax.pie(
        df["Count"], labels=df["Gender"], colors=colors,
        wedgeprops=wedgeprops, autopct="%1.1f%%",
        textprops={"color": "#e8eaf0", "fontsize": 9},
    )
    _storm_donut(fig, ax, "Turnover por Gênero")
    fig.tight_layout()
    plt.close(fig)
    return fig


def chart_attrition_by_joblevel(df: pd.DataFrame) -> plt.Figure:
    """Barra vertical — taxa de turnover (%) por nível de cargo."""
    fig, ax = plt.subplots(figsize=(6, 4))
    colors = [COR_SAIU if v == df["AttritionRate"].max() else COR_SECUNDARIA
              for v in df["AttritionRate"]]
    bars = ax.bar(df["JobLevel"].astype(str), df["AttritionRate"], color=colors, width=0.6)
    _bar_labels(ax, bars, fmt="%.1f%%")
    ax.set_ylim(0, df["AttritionRate"].max() * 1.3)
    ax.set_xlabel("Nível do Cargo")
    ax.set_ylabel("Taxa de Turnover (%)")
    _storm(fig, ax, "Turnover por Nível de Cargo")
    fig.tight_layout()
    plt.close(fig)
    return fig


def chart_satisfaction_vs_attrition(df: pd.DataFrame) -> plt.Figure:
    """Barra agrupada — satisfação média entre quem ficou e quem saiu."""
    fig, ax = plt.subplots(figsize=(6, 4))
    labels_map = {"No": "Ficou", "Yes": "Saiu"}
    df = df.copy()
    df["Label"] = df["Attrition"].map(labels_map)
    colors = [COR_FICOU if a == "No" else COR_SAIU for a in df["Attrition"]]
    bars = ax.bar(df["Label"], df["AvgSatisfaction"], color=colors, width=0.5)
    _bar_labels(ax, bars, fmt="%.2f")
    ax.set_ylim(0, 4.8)
    ax.set_ylabel("Satisfação Média (1–4)")
    _storm(fig, ax, "Satisfação Média: Ficou vs Saiu")
    fig.tight_layout()
    plt.close(fig)
    return fig


def chart_attrition_by_overtime(df: pd.DataFrame) -> plt.Figure:
    """Barra comparativa — taxa de turnover (%) com e sem hora extra."""
    fig, ax = plt.subplots(figsize=(6, 4))
    labels_map = {"Yes": "Faz Hora Extra", "No": "Não Faz"}
    df = df.copy()
    df["Label"] = df["OverTime"].map(labels_map)
    colors = [COR_SAIU if ot == "Yes" else COR_FICOU for ot in df["OverTime"]]
    bars = ax.bar(df["Label"], df["AttritionRate"], color=colors, width=0.5)
    _bar_labels(ax, bars, fmt="%.1f%%")
    ax.set_ylim(0, df["AttritionRate"].max() * 1.35)
    ax.set_ylabel("Taxa de Turnover (%)")
    _storm(fig, ax, "Hora Extra vs Turnover")
    fig.tight_layout()
    plt.close(fig)
    return fig
