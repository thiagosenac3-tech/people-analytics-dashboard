"""Funções de análise de dados com Pandas e NumPy."""

import numpy as np
import pandas as pd


# ── KPIs — Aba HeadCount ──────────────────────────────────────────────────────

def get_total_employees(df: pd.DataFrame) -> int:
    """Retorna o total de funcionários no DataFrame filtrado."""
    return len(df)


def get_average_age(df: pd.DataFrame) -> float:
    """Retorna a idade média dos funcionários."""
    return round(float(np.mean(df["Age"])), 1)


def get_average_tenure(df: pd.DataFrame) -> float:
    """Retorna o tempo médio de empresa em anos (YearsAtCompany)."""
    return round(float(np.mean(df["YearsAtCompany"])), 1)


def get_average_salary(df: pd.DataFrame) -> float:
    """Retorna o salário mensal médio."""
    return round(float(np.mean(df["MonthlyIncome"])), 0)


# ── KPIs — Aba Turnover ───────────────────────────────────────────────────────

def get_attrition_rate(df: pd.DataFrame) -> float:
    """Retorna a taxa de turnover (%) — proporção de Attrition='Yes'."""
    return round(float(np.sum(df["Attrition"] == "Yes") / len(df) * 100), 1)


def get_total_attrition(df: pd.DataFrame) -> int:
    """Retorna o total absoluto de saídas (Attrition = Yes)."""
    return int(np.sum(df["Attrition"] == "Yes"))


def get_average_satisfaction(df: pd.DataFrame) -> float:
    """Retorna a satisfação média no trabalho (escala 1-4)."""
    return round(float(np.mean(df["JobSatisfaction"])), 2)


def get_overtime_rate(df: pd.DataFrame) -> float:
    """Retorna o percentual de funcionários que fazem hora extra."""
    return round(float(np.sum(df["OverTime"] == "Yes") / len(df) * 100), 1)


# ── Dados para gráficos — Aba HeadCount ───────────────────────────────────────

def get_headcount_by_department(df: pd.DataFrame) -> pd.DataFrame:
    """Conta funcionários por departamento, ordenado crescente para barh."""
    counts = df["Department"].value_counts().reset_index()
    counts.columns = ["Department", "Count"]
    return counts.sort_values("Count")


def get_headcount_by_jobrole(df: pd.DataFrame) -> pd.DataFrame:
    """Conta funcionários por cargo — top 8, ordenado crescente para barh."""
    counts = df["JobRole"].value_counts().nlargest(8).reset_index()
    counts.columns = ["JobRole", "Count"]
    return counts.sort_values("Count")


def get_gender_distribution(df: pd.DataFrame) -> pd.DataFrame:
    """Contagem por gênero para o gráfico de rosca."""
    counts = df["Gender"].value_counts().reset_index()
    counts.columns = ["Gender", "Count"]
    return counts


def get_headcount_by_joblevel(df: pd.DataFrame) -> pd.DataFrame:
    """Conta funcionários por nível de cargo (JobLevel 1-5), ordenado."""
    counts = df["JobLevel"].value_counts().sort_index().reset_index()
    counts.columns = ["JobLevel", "Count"]
    return counts


def get_headcount_by_education(df: pd.DataFrame) -> pd.DataFrame:
    """Conta funcionários por área de formação, ordenado crescente para barh."""
    counts = df["EducationField"].value_counts().reset_index()
    counts.columns = ["EducationField", "Count"]
    return counts.sort_values("Count")


def get_age_series(df: pd.DataFrame) -> pd.Series:
    """Retorna a série de idades para o histograma."""
    return df["Age"]


# ── Dados para gráficos — Aba Turnover ────────────────────────────────────────

def get_attrition_by_department(df: pd.DataFrame) -> pd.DataFrame:
    """Taxa de turnover (%) por departamento, ordenado crescente."""
    grouped = df.groupby("Department")["Attrition"].apply(
        lambda s: round((s == "Yes").sum() / len(s) * 100, 1)
    ).reset_index()
    grouped.columns = ["Department", "AttritionRate"]
    return grouped.sort_values("AttritionRate")


def get_attrition_by_jobrole(df: pd.DataFrame) -> pd.DataFrame:
    """Taxa de turnover (%) — top 8 cargos com maior taxa, ordenado crescente."""
    grouped = df.groupby("JobRole")["Attrition"].apply(
        lambda s: round((s == "Yes").sum() / len(s) * 100, 1)
    ).reset_index()
    grouped.columns = ["JobRole", "AttritionRate"]
    return grouped.nlargest(8, "AttritionRate").sort_values("AttritionRate")


def get_attrition_by_gender(df: pd.DataFrame) -> pd.DataFrame:
    """Contagem de saídas por gênero para o gráfico de rosca."""
    exits = df[df["Attrition"] == "Yes"]["Gender"].value_counts().reset_index()
    exits.columns = ["Gender", "Count"]
    return exits


def get_attrition_by_joblevel(df: pd.DataFrame) -> pd.DataFrame:
    """Taxa de turnover (%) por nível de cargo (JobLevel 1-5)."""
    grouped = df.groupby("JobLevel")["Attrition"].apply(
        lambda s: round((s == "Yes").sum() / len(s) * 100, 1)
    ).reset_index()
    grouped.columns = ["JobLevel", "AttritionRate"]
    return grouped.sort_values("JobLevel")


def get_satisfaction_vs_attrition(df: pd.DataFrame) -> pd.DataFrame:
    """Satisfação média de quem ficou (No) e quem saiu (Yes)."""
    grouped = (
        df.groupby("Attrition")["JobSatisfaction"]
        .mean()
        .round(2)
        .reset_index()
    )
    grouped.columns = ["Attrition", "AvgSatisfaction"]
    return grouped


def get_attrition_by_overtime(df: pd.DataFrame) -> pd.DataFrame:
    """Taxa de turnover (%) por grupo de hora extra (Yes/No)."""
    grouped = df.groupby("OverTime")["Attrition"].apply(
        lambda s: round((s == "Yes").sum() / len(s) * 100, 1)
    ).reset_index()
    grouped.columns = ["OverTime", "AttritionRate"]
    return grouped
