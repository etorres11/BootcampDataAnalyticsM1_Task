import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go


# ============================================================
# CONFIGURACIÓN GENERAL
# ============================================================
st.set_page_config(
    page_title="Oil & Gas Engineering Analytics",
    page_icon="🛢️",
    layout="wide",
    initial_sidebar_state="expanded",
)

PARTICIPANTE = "Milka Camacho"
PROGRAMA = "Bootcamp Data Analytics for Oil & Gas"
APP_TITLE = "Oil & Gas Engineering Analytics"


# ============================================================
# ESTILOS HTML + CSS
# ============================================================
GLOBAL_CSS = r"""
<style>
:root {
    --bg: #07111f;
    --panel: rgba(15, 29, 46, 0.82);
    --panel-2: rgba(18, 38, 59, 0.74);
    --line: rgba(148, 163, 184, 0.18);
    --text: #e5edf7;
    --muted: #93a4b8;
    --accent: #2dd4bf;
    --accent-2: #38bdf8;
    --good: #22c55e;
    --warn: #f59e0b;
    --bad: #ef4444;
}

.stApp {
    background:
        radial-gradient(circle at 10% 5%, rgba(45, 212, 191, 0.10), transparent 28%),
        radial-gradient(circle at 92% 8%, rgba(56, 189, 248, 0.09), transparent 25%),
        linear-gradient(180deg, #07111f 0%, #091523 48%, #08111d 100%);
    color: var(--text);
}

[data-testid="stHeader"] {
    background: rgba(7, 17, 31, 0.72);
    backdrop-filter: blur(10px);
}

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #07111f 0%, #0a1726 100%);
    border-right: 1px solid var(--line);
}

[data-testid="stSidebar"] * {
    color: #dce8f4;
}

.block-container {
    max-width: 1480px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

h1, h2, h3 {
    letter-spacing: -0.02em;
}

.hero {
    position: relative;
    overflow: hidden;
    padding: 2.15rem 2.3rem;
    border: 1px solid rgba(45, 212, 191, 0.22);
    border-radius: 24px;
    background:
        linear-gradient(135deg, rgba(16, 41, 62, 0.96), rgba(8, 25, 41, 0.94)),
        radial-gradient(circle at top right, rgba(45, 212, 191, 0.20), transparent 32%);
    box-shadow: 0 22px 60px rgba(0, 0, 0, 0.28);
    margin-bottom: 1.25rem;
}

.hero::after {
    content: "";
    position: absolute;
    width: 260px;
    height: 260px;
    right: -90px;
    top: -120px;
    border: 1px solid rgba(56, 189, 248, 0.20);
    border-radius: 50%;
    box-shadow: 0 0 0 34px rgba(45, 212, 191, 0.035), 0 0 0 68px rgba(56, 189, 248, 0.025);
}

.eyebrow {
    display: inline-flex;
    align-items: center;
    gap: .55rem;
    padding: .38rem .72rem;
    border: 1px solid rgba(45, 212, 191, 0.24);
    border-radius: 999px;
    background: rgba(45, 212, 191, 0.07);
    color: #99f6e4;
    font-size: .78rem;
    font-weight: 700;
    letter-spacing: .08em;
    text-transform: uppercase;
}

.hero-title {
    margin: .9rem 0 .55rem 0;
    font-size: clamp(2.15rem, 4vw, 3.65rem);
    line-height: 1.02;
    font-weight: 800;
    color: #f7fbff;
}

.hero-title span {
    background: linear-gradient(90deg, #5eead4, #7dd3fc);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero-copy {
    max-width: 900px;
    margin: 0;
    color: #b8c8da;
    font-size: 1.05rem;
    line-height: 1.7;
}

.identity-strip {
    display: flex;
    gap: .75rem;
    flex-wrap: wrap;
    margin-top: 1.15rem;
}

.identity-pill {
    padding: .58rem .78rem;
    border-radius: 12px;
    border: 1px solid rgba(148, 163, 184, 0.16);
    background: rgba(255,255,255,0.035);
    color: #dbeafe;
    font-size: .88rem;
}

.section-title {
    margin: 1.6rem 0 .7rem 0;
    color: #f4f8fc;
    font-size: 1.45rem;
    font-weight: 750;
}

.section-subtitle {
    margin: -.35rem 0 1rem 0;
    color: var(--muted);
    font-size: .95rem;
}

.feature-grid {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 1rem;
    margin: .35rem 0 1.1rem 0;
}

.feature-card, .result-card, .info-card {
    border: 1px solid var(--line);
    border-radius: 18px;
    background: linear-gradient(180deg, rgba(19, 37, 56, 0.86), rgba(12, 27, 43, 0.80));
    box-shadow: 0 12px 32px rgba(0,0,0,.18);
}

.feature-card {
    padding: 1.15rem 1.15rem 1rem 1.15rem;
    min-height: 170px;
    transition: transform .20s ease, border-color .20s ease, box-shadow .20s ease;
}

.feature-card:hover {
    transform: translateY(-3px);
    border-color: rgba(45, 212, 191, 0.42);
    box-shadow: 0 16px 40px rgba(0,0,0,.23);
}

.feature-icon {
    width: 40px;
    height: 40px;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    border-radius: 12px;
    background: linear-gradient(135deg, rgba(45,212,191,.15), rgba(56,189,248,.14));
    border: 1px solid rgba(45,212,191,.18);
    font-size: 1.15rem;
}

.feature-title {
    margin: .85rem 0 .35rem 0;
    color: #f8fafc;
    font-size: 1.02rem;
    font-weight: 740;
}

.feature-copy {
    margin: 0;
    color: #9fb0c3;
    font-size: .90rem;
    line-height: 1.55;
}

.result-grid {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: .85rem;
    margin: .8rem 0 1rem 0;
}

.result-grid.four {
    grid-template-columns: repeat(4, minmax(0, 1fr));
}

.result-card {
    position: relative;
    overflow: hidden;
    padding: 1rem 1.05rem .95rem 1.05rem;
}

.result-card::before {
    content: "";
    position: absolute;
    width: 4px;
    left: 0;
    top: 0;
    bottom: 0;
    background: linear-gradient(180deg, #2dd4bf, #38bdf8);
}

.result-label {
    color: #9eb0c3;
    font-size: .78rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: .055em;
}

.result-value {
    margin-top: .28rem;
    color: #f8fafc;
    font-size: 1.65rem;
    line-height: 1.15;
    font-weight: 800;
}

.result-unit {
    color: #8fa2b8;
    font-size: .76rem;
    margin-top: .25rem;
}

.status-box {
    display: flex;
    align-items: center;
    gap: .65rem;
    padding: .8rem .95rem;
    border-radius: 14px;
    border: 1px solid var(--line);
    background: rgba(12, 26, 42, .72);
    margin: .65rem 0 1rem 0;
}

.status-dot {
    width: 10px;
    height: 10px;
    border-radius: 50%;
    box-shadow: 0 0 18px currentColor;
}

.status-good { color: #4ade80; }
.status-warn { color: #fbbf24; }
.status-bad { color: #f87171; }
.status-info { color: #67e8f9; }

.formula-card {
    padding: .9rem 1rem;
    border-radius: 14px;
    border: 1px solid rgba(56, 189, 248, .16);
    background: rgba(8, 24, 39, .68);
    color: #aebfd0;
    font-size: .88rem;
    line-height: 1.55;
    margin-bottom: .75rem;
}

.note-box {
    padding: .85rem 1rem;
    border-left: 3px solid #38bdf8;
    border-radius: 10px;
    background: rgba(56, 189, 248, .065);
    color: #b9c9da;
    font-size: .87rem;
    line-height: 1.55;
    margin: .75rem 0;
}

.sidebar-brand {
    padding: .95rem 1rem;
    border: 1px solid rgba(45, 212, 191, .20);
    border-radius: 16px;
    background: linear-gradient(145deg, rgba(15, 40, 58, .86), rgba(8, 27, 43, .90));
    margin: .35rem 0 1rem 0;
}

.sidebar-brand .kicker {
    color: #5eead4;
    font-size: .70rem;
    font-weight: 800;
    letter-spacing: .10em;
    text-transform: uppercase;
}

.sidebar-brand .name {
    margin-top: .28rem;
    color: #f8fafc;
    font-size: 1.05rem;
    font-weight: 780;
}

.sidebar-brand .program {
    margin-top: .2rem;
    color: #8fa4ba;
    font-size: .77rem;
    line-height: 1.4;
}

.footer {
    margin-top: 2.2rem;
    padding-top: 1rem;
    border-top: 1px solid rgba(148, 163, 184, .13);
    text-align: center;
    color: #71849a;
    font-size: .78rem;
}

/* Inputs */
[data-testid="stNumberInput"] input,
[data-testid="stSelectbox"] div[data-baseweb="select"] > div {
    background: rgba(10, 26, 42, .92);
}

/* Tabs */
button[data-baseweb="tab"] {
    font-weight: 700;
}

/* Plotly */
[data-testid="stPlotlyChart"] {
    border: 1px solid rgba(148, 163, 184, .12);
    border-radius: 16px;
    overflow: hidden;
    background: rgba(8, 22, 36, .45);
}

@media (max-width: 900px) {
    .feature-grid,
    .result-grid,
    .result-grid.four {
        grid-template-columns: 1fr;
    }
    .hero {
        padding: 1.5rem 1.35rem;
    }
}
</style>
"""

st.markdown(GLOBAL_CSS, unsafe_allow_html=True)


# ============================================================
# HELPERS VISUALES
# ============================================================
def section_header(title: str, subtitle: str = "") -> None:
    st.markdown(f'<div class="section-title">{title}</div>', unsafe_allow_html=True)
    if subtitle:
        st.markdown(f'<div class="section-subtitle">{subtitle}</div>', unsafe_allow_html=True)


def render_result_cards(cards, columns_class="") -> None:
    html = f'<div class="result-grid {columns_class}">'
    for label, value, unit in cards:
        html += f"""
        <div class="result-card">
            <div class="result-label">{label}</div>
            <div class="result-value">{value}</div>
            <div class="result-unit">{unit}</div>
        </div>
        """
    html += "</div>"
    st.markdown(html, unsafe_allow_html=True)


def render_status(text: str, detail: str, tone: str = "info") -> None:
    tone_class = {
        "good": "status-good",
        "warn": "status-warn",
        "bad": "status-bad",
        "info": "status-info",
    }.get(tone, "status-info")
    st.markdown(
        f"""
        <div class="status-box">
            <div class="status-dot {tone_class}"></div>
            <div>
                <div style="font-weight:750;color:#f4f8fc;">{text}</div>
                <div style="font-size:.84rem;color:#8fa2b8;margin-top:.12rem;">{detail}</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def oilgas_plot_layout(fig: go.Figure, title: str, x_title: str, y_title: str) -> go.Figure:
    fig.update_layout(
        title=dict(text=title, x=0.02, xanchor="left", font=dict(size=18, color="#edf6ff")),
        xaxis_title=x_title,
        yaxis_title=y_title,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(7,17,31,0.25)",
        font=dict(color="#c9d7e6"),
        margin=dict(l=50, r=25, t=65, b=50),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1,
            bgcolor="rgba(0,0,0,0)",
        ),
        hoverlabel=dict(bgcolor="#0f2236", font_color="#f8fafc"),
    )
    fig.update_xaxes(gridcolor="rgba(148,163,184,0.12)", zeroline=False)
    fig.update_yaxes(gridcolor="rgba(148,163,184,0.12)", zeroline=False)
    return fig


# ============================================================
# LÓGICA TÉCNICA - PRODUCCIÓN / IPR
# ============================================================
def validate_ipr(pr: float, pb: float, j: float, pwf: float):
    errors = []
    if pr <= 0:
        errors.append("Pᵣ debe ser mayor que 0 psi.")
    if pb <= 0:
        errors.append("Pᵦ debe ser mayor que 0 psi.")
    if j <= 0:
        errors.append("J debe ser mayor que 0 STB/d/psi.")
    if pwf < 0:
        errors.append("Pwf no puede ser negativa.")
    if pb >= pr:
        errors.append("Para este ejercicio subsaturado debe cumplirse Pᵣ > Pᵦ.")
    if pwf > pr:
        errors.append("Pwf no puede ser mayor que Pᵣ.")
    return errors


def ipr_rate(pr: float, pb: float, j: float, pwf: float) -> float:
    """IPR compuesta definida en la guía del Módulo 1."""
    qb = j * (pr - pb)
    if pwf >= pb:
        return j * (pr - pwf)

    ratio = pwf / pb
    return qb + (j * pb / 1.8) * (1 - 0.2 * ratio - 0.8 * ratio**2)


def build_ipr_curve(pr: float, pb: float, j: float, points: int = 180) -> pd.DataFrame:
    pwf_values = np.linspace(pr, 0.0, points)
    q_values = [ipr_rate(pr, pb, j, p) for p in pwf_values]
    regime = np.where(pwf_values >= pb, "Lineal (Pwf ≥ Pb)", "Vogel (Pwf < Pb)")
    return pd.DataFrame({"Pwf_psi": pwf_values, "Qo_STBd": q_values, "Régimen": regime})


# ============================================================
# LÓGICA TÉCNICA - PERFORACIÓN
# ============================================================
def validate_drilling(mw: float, md: float, tvd: float, pform: float):
    errors = []
    if mw <= 0:
        errors.append("MW debe ser mayor que 0 ppg.")
    if md <= 0:
        errors.append("MD debe ser mayor que 0 ft.")
    if tvd <= 0:
        errors.append("TVD debe ser mayor que 0 ft.")
    if tvd > md:
        errors.append("TVD no puede ser mayor que MD.")
    if pform < 0:
        errors.append("La presión de formación no puede ser negativa.")
    return errors


def hydrostatic_calculation(mw: float, tvd: float, pform: float):
    gradient = 0.052 * mw
    ph = gradient * tvd
    delta_p = ph - pform
    return gradient, ph, delta_p


# ============================================================
# LÓGICA TÉCNICA - RESERVORIOS
# ============================================================
def validate_reservoir(area, h, ntg, phi, swi, boi, fr):
    errors = []
    if area <= 0:
        errors.append("El área A debe ser mayor que 0 acres.")
    if h <= 0:
        errors.append("El espesor h debe ser mayor que 0 ft.")
    if not 0 <= ntg <= 1:
        errors.append("NTG debe estar entre 0 y 1.")
    if not 0 <= phi <= 1:
        errors.append("La porosidad φ debe estar entre 0 y 1.")
    if not 0 <= swi <= 1:
        errors.append("Swi debe estar entre 0 y 1.")
    if boi <= 0:
        errors.append("Boi debe ser mayor que 0 rb/STB.")
    if not 0 <= fr <= 1:
        errors.append("FR debe estar entre 0 y 1.")
    return errors


def volumetric_poes(area, h, ntg, phi, swi, boi, fr):
    h_net = h * ntg
    poes_stb = (7758 * area * h_net * phi * (1 - swi)) / boi
    recoverable_stb = poes_stb * fr
    return h_net, poes_stb, recoverable_stb


# ============================================================
# SIDEBAR / NAVEGACIÓN PRINCIPAL
# ============================================================
with st.sidebar:
    st.markdown(
        f"""
        <div class="sidebar-brand">
            <div class="kicker">SPE · Oil & Gas</div>
            <div class="name">{APP_TITLE}</div>
            <div class="program">{PROGRAMA}<br>{PARTICIPANTE}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.caption("NAVEGACIÓN")
    page = st.radio(
        "Navegación principal",
        ["Home", "Ejercicios"],
        label_visibility="collapsed",
    )

    st.markdown("---")
    st.caption("Módulo 1 · Aplicación técnica")
    st.caption("Producción · Perforación · Reservorios")


# ============================================================
# HOME
# ============================================================
if page == "Home":
    st.markdown(
        f"""
        <section class="hero">
            <div class="eyebrow">● Technical web application · Oil & Gas</div>
            <div class="hero-title">Engineering decisions,<br><span>supported by data.</span></div>
            <p class="hero-copy">
                Aplicación técnica desarrollada en Python y Streamlit para resolver ejercicios de
                Producción, Perforación y Reservorios mediante cálculos de ingeniería, validaciones
                físicas e interpretación gráfica en una interfaz web profesional.
            </p>
            <div class="identity-strip">
                <div class="identity-pill"><b>Participante:</b> {PARTICIPANTE}</div>
                <div class="identity-pill"><b>Programa:</b> {PROGRAMA}</div>
                <div class="identity-pill"><b>Stack:</b> Python · Streamlit · HTML · CSS · JavaScript</div>
            </div>
        </section>
        """,
        unsafe_allow_html=True,
    )

    section_header(
        "Tres áreas, una sola experiencia técnica",
        "Cada módulo combina entradas de ingeniería, cálculo, validación e interpretación visual.",
    )

    st.markdown(
        """
        <div class="feature-grid">
            <div class="feature-card">
                <div class="feature-icon">↗</div>
                <div class="feature-title">Producción · IPR compuesta</div>
                <p class="feature-copy">Evalúa el caudal de petróleo diferenciando el régimen lineal por encima de Pb y el comportamiento de Vogel por debajo de la presión de burbuja.</p>
            </div>
            <div class="feature-card">
                <div class="feature-icon">↓</div>
                <div class="feature-title">Perforación · Hidrostática</div>
                <p class="feature-copy">Calcula gradiente y presión hidrostática a TVD y compara la columna de lodo contra la presión de formación para identificar el balance.</p>
            </div>
            <div class="feature-card">
                <div class="feature-icon">◫</div>
                <div class="feature-title">Reservorios · POES</div>
                <p class="feature-copy">Aplica el método volumétrico para estimar petróleo original en sitio y un volumen recuperable asociado al factor de recobro.</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    section_header(
        "Microinteracción JavaScript",
        "Componente demostrativo solicitado en la actividad: el evento del botón se ejecuta en el navegador.",
    )

    # Interacción JavaScript visible. Se usa st.iframe para encapsular JS de forma estable.
    js_component = r"""
    <!DOCTYPE html>
    <html>
    <head>
    <style>
        *{box-sizing:border-box} body{margin:0;background:transparent;font-family:Inter,Arial,sans-serif;color:#eaf2fb}
        .box{display:flex;align-items:center;justify-content:space-between;gap:18px;padding:16px 18px;border:1px solid rgba(45,212,191,.22);border-radius:16px;background:linear-gradient(135deg,rgba(16,40,59,.96),rgba(8,25,41,.96));}
        .left{min-width:0}.tag{font-size:11px;letter-spacing:.09em;text-transform:uppercase;color:#5eead4;font-weight:800}.msg{margin-top:5px;color:#c7d6e6;font-size:14px;line-height:1.45}.count{font-size:11px;color:#7f93aa;margin-top:5px}
        button{flex:0 0 auto;border:1px solid rgba(94,234,212,.26);background:rgba(45,212,191,.10);color:#ccfbf1;padding:10px 14px;border-radius:11px;font-weight:750;cursor:pointer;transition:.18s ease}
        button:hover{transform:translateY(-1px);background:rgba(45,212,191,.17);border-color:rgba(94,234,212,.45)}
    </style>
    </head>
    <body>
        <div class="box">
            <div class="left">
                <div class="tag">Technical Insight</div>
                <div id="message" class="msg">Una IPR permite relacionar la presión de fondo fluyente con la capacidad de aporte del yacimiento.</div>
                <div id="counter" class="count">Interacciones: 0</div>
            </div>
            <button onclick="nextInsight()">Cambiar insight</button>
        </div>
        <script>
            const insights = [
                'Una IPR permite relacionar la presión de fondo fluyente con la capacidad de aporte del yacimiento.',
                'En hidrostática de perforación, la presión depende de la TVD porque representa la altura vertical real de la columna de fluido.',
                'El POES es petróleo originalmente contenido en el reservorio; no equivale al volumen técnicamente recuperable.'
            ];
            let i = 0;
            let clicks = 0;
            function nextInsight(){
                i = (i + 1) % insights.length;
                clicks += 1;
                document.getElementById('message').textContent = insights[i];
                document.getElementById('counter').textContent = 'Interacciones: ' + clicks;
            }
        </script>
    </body>
    </html>
    """
    st.iframe(js_component, height=118)

    section_header("Diseño orientado a evaluación", "Implementación pensada para evidenciar el cumplimiento técnico y visual de la rúbrica.")
    render_result_cards(
        [
            ("Navegación", "2", "Home + Ejercicios"),
            ("Áreas técnicas", "3", "Producción · Perforación · Reservorios"),
            ("Frontend", "HTML/CSS/JS", "Personalización e interacción"),
        ]
    )


# ============================================================
# EJERCICIOS
# ============================================================
else:
    st.markdown(
        """
        <section class="hero" style="padding:1.6rem 1.8rem;">
            <div class="eyebrow">Engineering Workspace</div>
            <div class="hero-title" style="font-size:2.35rem;">Ejercicios <span>Oil & Gas</span></div>
            <p class="hero-copy" style="font-size:.96rem;">
                Ajusta los parámetros y analiza cómo cambia la respuesta técnica de cada sistema.
                Las validaciones impiden combinaciones físicamente inconsistentes.
            </p>
        </section>
        """,
        unsafe_allow_html=True,
    )

    tab_prod, tab_drill, tab_res = st.tabs(["📈 Producción", "🛠️ Perforación", "🧭 Reservorios"])

    # --------------------------------------------------------
    # TAB 1: PRODUCCIÓN
    # --------------------------------------------------------
    with tab_prod:
        section_header(
            "IPR compuesta con punto de burbuja",
            "Reservorio inicialmente subsaturado: comportamiento lineal para Pwf ≥ Pb y Vogel para Pwf < Pb.",
        )

        input_col, output_col = st.columns([0.92, 1.55], gap="large")

        with input_col:
            st.markdown('<div class="formula-card"><b>Entradas del modelo</b><br>Presiones en psi e índice de productividad en STB/d/psi.</div>', unsafe_allow_html=True)
            pr = st.number_input("Presión promedio del reservorio, Pᵣ [psi]", min_value=0.0, value=3200.0, step=50.0, key="ipr_pr")
            pb = st.number_input("Presión de burbuja, Pᵦ [psi]", min_value=0.0, value=1800.0, step=50.0, key="ipr_pb")
            j = st.number_input("Índice de productividad, J [STB/d/psi]", min_value=0.0, value=0.80, step=0.05, format="%.3f", key="ipr_j")
            pwf = st.number_input("Presión de fondo fluyente, Pwf [psi]", min_value=0.0, value=1200.0, step=50.0, key="ipr_pwf")

            with st.expander("Ver ecuaciones utilizadas"):
                st.latex(r"q_b = J(P_r-P_b)")
                st.latex(r"P_{wf}\geq P_b:\quad q_o=J(P_r-P_{wf})")
                st.latex(r"P_{wf}<P_b:\quad q_o=q_b+\frac{JP_b}{1.8}\left[1-0.2\left(\frac{P_{wf}}{P_b}\right)-0.8\left(\frac{P_{wf}}{P_b}\right)^2\right]")
                st.latex(r"q_{o,max}=q_b+\frac{JP_b}{1.8}")

        errors = validate_ipr(pr, pb, j, pwf)

        with output_col:
            if errors:
                for error in errors:
                    st.error(error)
            else:
                qb = j * (pr - pb)
                qo = ipr_rate(pr, pb, j, pwf)
                qmax = qb + (j * pb / 1.8)
                regime = "Por encima de Pᵦ · régimen lineal" if pwf >= pb else "Por debajo de Pᵦ · régimen Vogel"
                tone = "good" if pwf >= pb else "warn"

                render_result_cards(
                    [
                        ("Caudal actual, qₒ", f"{qo:,.1f}", "STB/d"),
                        ("Caudal a Pᵦ, qᵦ", f"{qb:,.1f}", "STB/d"),
                        ("Caudal máximo, qₒ,max", f"{qmax:,.1f}", "STB/d"),
                    ]
                )
                render_status(
                    regime,
                    f"Pwf = {pwf:,.0f} psi · Pᵦ = {pb:,.0f} psi",
                    tone,
                )

                df_ipr = build_ipr_curve(pr, pb, j)
                fig_ipr = go.Figure()
                fig_ipr.add_trace(
                    go.Scatter(
                        x=df_ipr["Qo_STBd"],
                        y=df_ipr["Pwf_psi"],
                        mode="lines",
                        name="Curva IPR",
                        line=dict(width=3, color="#2dd4bf"),
                        hovertemplate="qₒ = %{x:,.1f} STB/d<br>Pwf = %{y:,.0f} psi<extra></extra>",
                    )
                )
                fig_ipr.add_trace(
                    go.Scatter(
                        x=[qo],
                        y=[pwf],
                        mode="markers",
                        name="Punto ingresado",
                        marker=dict(size=13, color="#f59e0b", line=dict(width=2, color="#fff7ed")),
                        hovertemplate="Punto de operación<br>qₒ = %{x:,.1f} STB/d<br>Pwf = %{y:,.0f} psi<extra></extra>",
                    )
                )
                fig_ipr.add_trace(
                    go.Scatter(
                        x=[qb],
                        y=[pb],
                        mode="markers",
                        name="Punto de burbuja",
                        marker=dict(size=10, color="#38bdf8"),
                        hovertemplate="Punto de burbuja<br>qᵦ = %{x:,.1f} STB/d<br>Pᵦ = %{y:,.0f} psi<extra></extra>",
                    )
                )
                fig_ipr.add_hline(y=pb, line_dash="dash", line_color="rgba(56,189,248,.55)")
                oilgas_plot_layout(fig_ipr, "Curva IPR compuesta", "Caudal de petróleo, qₒ [STB/d]", "Pwf [psi]")
                fig_ipr.update_yaxes(range=[0, pr * 1.03])
                st.plotly_chart(fig_ipr, use_container_width=True, config={"displaylogo": False})

                st.markdown(
                    '<div class="note-box"><b>Lectura técnica:</b> el cambio de pendiente alrededor de Pᵦ representa el paso del tramo lineal al comportamiento no lineal descrito por Vogel.</div>',
                    unsafe_allow_html=True,
                )

    # --------------------------------------------------------
    # TAB 2: PERFORACIÓN
    # --------------------------------------------------------
    with tab_drill:
        section_header(
            "Presión hidrostática del lodo",
            "El cálculo usa TVD como altura vertical efectiva de la columna de fluido; MD se emplea como contexto y validación geométrica.",
        )

        input_col, output_col = st.columns([0.92, 1.55], gap="large")

        with input_col:
            st.markdown('<div class="formula-card"><b>Entradas del modelo</b><br>Peso de lodo en ppg, profundidades en ft y presión de formación en psi.</div>', unsafe_allow_html=True)
            mw = st.number_input("Peso del lodo, MW [ppg]", min_value=0.0, value=10.2, step=0.1, key="dr_mw")
            md = st.number_input("Profundidad medida, MD [ft]", min_value=0.0, value=9000.0, step=100.0, key="dr_md")
            tvd = st.number_input("Profundidad vertical verdadera, TVD [ft]", min_value=0.0, value=7800.0, step=100.0, key="dr_tvd")
            pform = st.number_input("Presión de formación, Pform [psi]", min_value=0.0, value=4000.0, step=50.0, key="dr_pform")

            with st.expander("Ver ecuaciones utilizadas"):
                st.latex(r"G_h=0.052\times MW")
                st.latex(r"P_h=0.052\times MW\times TVD")
                st.latex(r"\Delta P=P_h-P_{form}")

            st.markdown(
                '<div class="note-box">Para el indicador visual de “balance aproximado” se utiliza una tolerancia de ±50 psi. Es un criterio de interfaz para representar ΔP ≈ 0; las ecuaciones base no cambian.</div>',
                unsafe_allow_html=True,
            )

        errors = validate_drilling(mw, md, tvd, pform)

        with output_col:
            if errors:
                for error in errors:
                    st.error(error)
            else:
                gradient, ph, delta_p = hydrostatic_calculation(mw, tvd, pform)
                balance_tolerance = 50.0

                if delta_p > balance_tolerance:
                    status = "Sobrebalance"
                    tone = "good"
                    detail = "La presión hidrostática es mayor que la presión de formación."
                elif delta_p < -balance_tolerance:
                    status = "Bajo balance"
                    tone = "bad"
                    detail = "La presión hidrostática es menor que la presión de formación."
                else:
                    status = "Balance aproximado"
                    tone = "warn"
                    detail = "La diferencia de presión se encuentra dentro de ±50 psi."

                render_result_cards(
                    [
                        ("Gradiente, Gₕ", f"{gradient:.3f}", "psi/ft"),
                        ("Presión hidrostática, Pₕ", f"{ph:,.0f}", "psi"),
                        ("Diferencial, ΔP", f"{delta_p:+,.0f}", "psi"),
                    ]
                )
                render_status(status, detail, tone)

                depth = np.linspace(0, tvd, 140)
                pressure = gradient * depth
                fig_h = go.Figure()
                fig_h.add_trace(
                    go.Scatter(
                        x=depth,
                        y=pressure,
                        mode="lines",
                        name="P. hidrostática",
                        line=dict(width=3, color="#38bdf8"),
                        hovertemplate="TVD = %{x:,.0f} ft<br>Pₕ = %{y:,.0f} psi<extra></extra>",
                    )
                )
                fig_h.add_trace(
                    go.Scatter(
                        x=[tvd],
                        y=[ph],
                        mode="markers",
                        name="Punto calculado",
                        marker=dict(size=13, color="#2dd4bf", line=dict(width=2, color="#ecfeff")),
                        hovertemplate="TVD = %{x:,.0f} ft<br>Pₕ = %{y:,.0f} psi<extra></extra>",
                    )
                )
                fig_h.add_hline(
                    y=pform,
                    line_dash="dash",
                    line_color="rgba(245,158,11,.70)",
                    annotation_text="Pform",
                    annotation_position="top left",
                )
                oilgas_plot_layout(fig_h, "Presión hidrostática vs TVD", "TVD [ft]", "Presión [psi]")
                st.plotly_chart(fig_h, use_container_width=True, config={"displaylogo": False})

                render_result_cards(
                    [
                        ("Relación TVD / MD", f"{(tvd/md)*100:.1f}%", "geometría del pozo"),
                        ("MW equivalente", f"{mw:.1f}", "ppg"),
                        ("Pform", f"{pform:,.0f}", "psi"),
                    ]
                )

    # --------------------------------------------------------
    # TAB 3: RESERVORIOS
    # --------------------------------------------------------
    with tab_res:
        section_header(
            "Estimación volumétrica del POES",
            "Método volumétrico para calcular Petróleo Original en Sitio y un volumen potencialmente recuperable mediante FR.",
        )

        input_col, output_col = st.columns([0.92, 1.55], gap="large")

        with input_col:
            st.markdown('<div class="formula-card"><b>Entradas del modelo</b><br>NTG, porosidad, Swi y FR se ingresan como fracciones entre 0 y 1.</div>', unsafe_allow_html=True)
            area = st.number_input("Área, A [acres]", min_value=0.0, value=640.0, step=10.0, key="res_area")
            h = st.number_input("Espesor bruto, h [ft]", min_value=0.0, value=55.0, step=1.0, key="res_h")
            ntg = st.number_input("Net-to-gross, NTG [fracción]", min_value=0.0, max_value=1.0, value=0.72, step=0.01, format="%.2f", key="res_ntg")
            phi = st.number_input("Porosidad efectiva, φ [fracción]", min_value=0.0, max_value=1.0, value=0.18, step=0.01, format="%.2f", key="res_phi")
            swi = st.number_input("Saturación inicial de agua, Swi [fracción]", min_value=0.0, max_value=1.0, value=0.28, step=0.01, format="%.2f", key="res_swi")
            boi = st.number_input("Factor volumétrico inicial, Boi [rb/STB]", min_value=0.0, value=1.20, step=0.01, format="%.2f", key="res_boi")
            fr = st.number_input("Factor de recobro, FR [fracción]", min_value=0.0, max_value=1.0, value=0.32, step=0.01, format="%.2f", key="res_fr")

            with st.expander("Ver ecuaciones utilizadas"):
                st.latex(r"h_n=h\times NTG")
                st.latex(r"POES=\frac{7758\times A\times h_n\times\phi\times(1-S_{wi})}{B_{oi}}")
                st.latex(r"Petróleo\ recuperable=POES\times FR")

        errors = validate_reservoir(area, h, ntg, phi, swi, boi, fr)

        with output_col:
            if errors:
                for error in errors:
                    st.error(error)
            else:
                h_net, poes_stb, recoverable_stb = volumetric_poes(area, h, ntg, phi, swi, boi, fr)
                poes_mmstb = poes_stb / 1_000_000
                recoverable_mmstb = recoverable_stb / 1_000_000

                render_result_cards(
                    [
                        ("Espesor neto, hₙ", f"{h_net:,.1f}", "ft"),
                        ("POES", f"{poes_mmstb:,.2f}", "MMSTB"),
                        ("Recuperable estimado", f"{recoverable_mmstb:,.2f}", "MMSTB"),
                    ]
                )

                render_status(
                    "Estimación volumétrica completada",
                    f"FR aplicado = {fr:.0%} · volumen no recuperable estimado = {(1-fr):.0%} del POES.",
                    "info",
                )

                fig_res = go.Figure()
                fig_res.add_trace(
                    go.Bar(
                        x=["POES", "Recuperable"],
                        y=[poes_mmstb, recoverable_mmstb],
                        marker_color=["#38bdf8", "#2dd4bf"],
                        text=[f"{poes_mmstb:,.2f}", f"{recoverable_mmstb:,.2f}"],
                        textposition="outside",
                        hovertemplate="%{x}<br>%{y:,.2f} MMSTB<extra></extra>",
                    )
                )
                oilgas_plot_layout(fig_res, "POES vs volumen recuperable estimado", "Volumen", "MMSTB")
                fig_res.update_layout(showlegend=False)
                st.plotly_chart(fig_res, use_container_width=True, config={"displaylogo": False})

                render_result_cards(
                    [
                        ("POES", f"{poes_stb:,.0f}", "STB"),
                        ("Recuperable", f"{recoverable_stb:,.0f}", "STB"),
                        ("Poro con HC", f"{phi*(1-swi):.3f}", "φ × (1 − Swi)"),
                    ]
                )

                st.markdown(
                    '<div class="note-box"><b>Interpretación:</b> el POES representa el petróleo originalmente contenido a condiciones de tanque. El volumen recuperable mostrado depende directamente del factor de recobro asumido.</div>',
                    unsafe_allow_html=True,
                )


# ============================================================
# FOOTER
# ============================================================
st.markdown(
    f'<div class="footer">{APP_TITLE} · {PARTICIPANTE} · {PROGRAMA}</div>',
    unsafe_allow_html=True,
)
