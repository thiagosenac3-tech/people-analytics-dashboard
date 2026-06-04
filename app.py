"""Aplicação Streamlit — People Analytics Dashboard."""

import pandas as pd
import streamlit as st

import analysis as an
import charts as ch

# ── Configuração da página ─────────────────────────────────────────────────────

st.set_page_config(
    page_title="People Analytics | IBM HR",
    page_icon="📊",
    layout="wide",
)

# ── Injeção de CSS — Tema Storm ────────────────────────────────────────────────

st.markdown("""
<style>
.stApp { background-color: #141617; }
[data-testid="stSidebar"] {
    background-color: #0e1012;
    border-right: 1px solid rgba(255,255,255,0.06);
}
[data-testid="metric-container"] {
    background-color: #1e2225;
    border: 0.5px solid rgba(0,161,255,0.2);
    border-radius: 10px;
    padding: 16px 20px;
}
h1, h2, h3 { color: #ffffff !important; }
.stTabs [data-baseweb="tab"] { color: #8899aa; }
.stTabs [aria-selected="true"] { color: #00A1FF !important; }
</style>
""", unsafe_allow_html=True)

# ── Carregamento de dados ──────────────────────────────────────────────────────

@st.cache_data
def load_data() -> pd.DataFrame:
    """Carrega e retorna o dataset de attrition da IBM."""
    return pd.read_csv("data/WA_Fn-UseC_-HR-Employee-Attrition.csv")


df_full = load_data()

# ── Sidebar — filtros ──────────────────────────────────────────────────────────

with st.sidebar:
    st.title("📊 People Analytics")
    st.markdown("**IBM HR Attrition Dataset**")
    st.markdown("---")

    dept_sel = st.multiselect(
        "Departamento",
        options=sorted(df_full["Department"].unique()),
    )

    gender_sel = st.multiselect(
        "Gênero",
        options=sorted(df_full["Gender"].unique()),
    )

    nivel_range = st.slider(
        "Nível do Cargo",
        min_value=1, max_value=5, value=(1, 5),
    )

    st.markdown("---")
    st.caption("Desenvolvido por **Thiago Alexandre**")

# Aplica filtros (multiselect vazio = sem filtro)
df = df_full.copy()
if dept_sel:
    df = df[df["Department"].isin(dept_sel)]
if gender_sel:
    df = df[df["Gender"].isin(gender_sel)]
df = df[(df["JobLevel"] >= nivel_range[0]) & (df["JobLevel"] <= nivel_range[1])]

# ── Cabeçalho ─────────────────────────────────────────────────────────────────

st.title("People Analytics Dashboard — IBM HR")
st.markdown("*Análise de turnover, headcount e satisfação de 1.470 funcionários*")

# ── Abas ──────────────────────────────────────────────────────────────────────

tab_headcount, tab_turnover = st.tabs(["👥  HeadCount", "🔄  Turnover"])

# ══════════════════════════════════════════════════════════════════════════════
# Aba 1 — HeadCount
# ══════════════════════════════════════════════════════════════════════════════

with tab_headcount:

    # KPIs
    k1, k2, k3, k4 = st.columns(4)
    k1.metric("👥 Total de Funcionários", an.get_total_employees(df))
    k2.metric("🎂 Idade Média", f"{an.get_average_age(df)} anos")
    k3.metric("🏢 Tempo Médio na Empresa", f"{an.get_average_tenure(df)} anos")
    k4.metric("💰 Salário Médio", f"$ {an.get_average_salary(df):,.0f}")

    st.markdown("---")

    # Linha 1
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Headcount por Departamento")
        st.caption("Distribuição de funcionários entre as áreas da empresa.")
        st.pyplot(ch.chart_headcount_by_department(an.get_headcount_by_department(df)))

    with col2:
        st.subheader("Headcount por Cargo")
        st.caption("Top 8 cargos com maior número de funcionários.")
        st.pyplot(ch.chart_headcount_by_jobrole(an.get_headcount_by_jobrole(df)))

    # Linha 2
    col3, col4 = st.columns(2)

    with col3:
        st.subheader("Distribuição por Gênero")
        st.caption("Proporção de funcionários homens e mulheres.")
        st.pyplot(ch.chart_gender_donut(an.get_gender_distribution(df)))

    with col4:
        st.subheader("Headcount por Nível de Cargo")
        st.caption("Volume de funcionários em cada nível hierárquico (1 = júnior, 5 = sênior).")
        st.pyplot(ch.chart_headcount_by_joblevel(an.get_headcount_by_joblevel(df)))

    # Linha 3
    col5, col6 = st.columns(2)

    with col5:
        st.subheader("Headcount por Área de Formação")
        st.caption("Distribuição dos funcionários por background acadêmico.")
        st.pyplot(ch.chart_headcount_by_education(an.get_headcount_by_education(df)))

    with col6:
        st.subheader("Distribuição de Idade")
        st.caption("Perfil etário dos funcionários — identifica a faixa predominante.")
        st.pyplot(ch.chart_age_histogram(an.get_age_series(df)))

# ══════════════════════════════════════════════════════════════════════════════
# Aba 2 — Turnover
# ══════════════════════════════════════════════════════════════════════════════

with tab_turnover:

    # KPIs
    k1, k2, k3, k4 = st.columns(4)
    k1.metric("🔄 Taxa de Turnover", f"{an.get_attrition_rate(df)}%")
    k2.metric("🚪 Total de Saídas", an.get_total_attrition(df))
    k3.metric("😊 Satisfação Média", f"{an.get_average_satisfaction(df)} / 4")
    k4.metric("⏰ Com Hora Extra", f"{an.get_overtime_rate(df)}%")

    st.markdown("---")

    # Linha 1
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Turnover por Departamento")
        st.caption("Percentual de saída de funcionários em cada departamento.")
        st.pyplot(ch.chart_attrition_by_department(an.get_attrition_by_department(df)))

    with col2:
        st.subheader("Turnover por Cargo")
        st.caption("Top 8 cargos com maior taxa de turnover.")
        st.pyplot(ch.chart_attrition_by_jobrole(an.get_attrition_by_jobrole(df)))

    # Linha 2
    col3, col4 = st.columns(2)

    with col3:
        st.subheader("Turnover por Gênero")
        st.caption("Proporção de saídas entre funcionários homens e mulheres.")
        st.pyplot(ch.chart_attrition_by_gender(an.get_attrition_by_gender(df)))

    with col4:
        st.subheader("Turnover por Nível de Cargo")
        st.caption("Taxa de turnover em cada nível hierárquico — níveis júnior tendem a sair mais?")
        st.pyplot(ch.chart_attrition_by_joblevel(an.get_attrition_by_joblevel(df)))

    # Linha 3
    col5, col6 = st.columns(2)

    with col5:
        st.subheader("Satisfação Média: Ficou vs Saiu")
        st.caption("Comparação da satisfação no trabalho entre quem permaneceu e quem pediu demissão.")
        st.pyplot(ch.chart_satisfaction_vs_attrition(an.get_satisfaction_vs_attrition(df)))

    with col6:
        st.subheader("Hora Extra vs Turnover")
        st.caption("Funcionários que fazem hora extra têm maior probabilidade de sair?")
        st.pyplot(ch.chart_attrition_by_overtime(an.get_attrition_by_overtime(df)))
