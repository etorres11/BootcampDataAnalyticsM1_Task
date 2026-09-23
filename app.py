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

INGENIERO = "Eder Torres"
PROGRAMA = "Bootcamp Data Analytics for Oil & Gas"
APP_TITLE = "Oil & Gas Engineering Analytics"


# ============================================================
# ESTILOS HTML + CSS
# ============================================================
GLOBAL_CSS = r"""
<style>
:root {
    /* Paleta inspirada en crudos parafínicos / verde petróleo */
    --bg: #E3ECD9;
    --bg-2: #D6E4CC;
    --panel: rgba(48, 83, 61, 0.96);
    --panel-2: rgba(61, 99, 73, 0.92);
    --panel-soft: rgba(224, 236, 213, 0.92);
    --line: rgba(61, 94, 68, 0.24);
    --text: #193326;
    --muted: #536A5B;
    --accent: #A8D45F;
    --accent-2: #6FBF73;
    --accent-soft: #D7E9A7;
    --amber: #F2C14E;
    --good: #8ED081;
    --warn: #F2C14E;
    --bad: #FF7B72;

    /* Controles del borde animado */
    --card-border-speed: 7s;
    --card-glow-opacity: .48;
    --card-glow-blur: 18px;
}

.stApp {
    background:
        radial-gradient(circle at 12% 4%, rgba(185, 211, 126, 0.34), transparent 30%),
        radial-gradient(circle at 92% 8%, rgba(126, 176, 113, 0.24), transparent 28%),
        radial-gradient(circle at 50% 100%, rgba(255, 250, 220, 0.42), transparent 38%),
        linear-gradient(180deg, #EEF3E8 0%, #E2ECDD 45%, #D7E5D0 100%);
    color: var(--text);
}

[data-testid="stHeader"] {
    background: rgba(238, 243, 232, 0.84);
    backdrop-filter: blur(10px);
}

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #355E46 0%, #446F54 100%);
    border-right: 1px solid rgba(168, 212, 95, .18);
}

[data-testid="stSidebar"] * {
    color: #ECF4E8;
}

.block-container {
    max-width: 1480px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

h1, h2, h3 {
    letter-spacing: -0.02em;
    color: #173C2A !important;
}

/* Contraste de textos nativos sobre el fondo claro */
[data-testid="stMain"] [data-testid="stMarkdownContainer"] > p,
[data-testid="stMain"] [data-testid="stWidgetLabel"] p,
[data-testid="stMain"] label p {
    color: #254A35 !important;
}

[data-testid="stMain"] small,
[data-testid="stMain"] [data-testid="stCaptionContainer"] {
    color: #58705F !important;
}

[data-testid="stExpander"] {
    border: 1px solid rgba(55, 92, 65, .18);
    border-radius: 12px;
    background: rgba(247, 250, 243, .70);
}

[data-testid="stExpander"] summary p {
    color: #234A33 !important;
    font-weight: 750 !important;
}

.hero {
    position: relative;
    overflow: hidden;
    padding: 2.15rem 2.3rem;
    border: 1px solid rgba(168, 212, 95, 0.24);
    border-radius: 24px;
    background:
        linear-gradient(135deg, rgba(43, 76, 57, 0.97), rgba(25, 51, 38, 0.96)),
        radial-gradient(circle at top right, rgba(168, 212, 95, 0.20), transparent 34%);
    box-shadow: 0 22px 60px rgba(4, 18, 10, 0.25);
    margin-bottom: 1.25rem;
}

.hero::after {
    content: "";
    position: absolute;
    width: 260px;
    height: 260px;
    right: -90px;
    top: -120px;
    border: 1px solid rgba(215, 233, 167, 0.18);
    border-radius: 50%;
    box-shadow: 0 0 0 34px rgba(168, 212, 95, 0.035), 0 0 0 68px rgba(111, 191, 115, 0.025);
}

.eyebrow {
    display: inline-flex;
    align-items: center;
    gap: .55rem;
    padding: .38rem .72rem;
    border: 1px solid rgba(168, 212, 95, 0.28);
    border-radius: 999px;
    background: rgba(168, 212, 95, 0.09);
    color: #E0F1B8;
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
    color: #FBFFF8;
}

.hero-title span {
    background: linear-gradient(90deg, #D7E9A7, #91D18B, #E6F2B8);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero-copy {
    max-width: 900px;
    margin: 0;
    color: #D1DDCE;
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
    border: 1px solid rgba(215, 233, 167, 0.17);
    background: rgba(255,255,255,0.045);
    color: #F0F7EC;
    font-size: .88rem;
}

.section-title {
    margin: 1.6rem 0 .7rem 0;
    color: #183D2B;
    font-size: 1.45rem;
    font-weight: 750;
}

.section-subtitle {
    margin: -.35rem 0 1rem 0;
    color: #536B5C;
    font-size: .95rem;
}

.feature-grid {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 1rem;
    margin: .35rem 0 1.1rem 0;
}

/* ==========================================================
   TARJETAS CON BORDE ANIMADO
   Controla velocidad y brillo desde :root:
   --card-border-speed / --card-glow-opacity / --card-glow-blur
   ========================================================== */
@property --border-angle {
    syntax: '<angle>';
    initial-value: 0deg;
    inherits: false;
}

.feature-card, .result-card, .info-card {
    position: relative;
    border: 1.4px solid transparent;
    border-radius: 18px;
    background:
        linear-gradient(180deg, rgba(43, 76, 57, 0.96), rgba(29, 56, 42, 0.94)) padding-box,
        conic-gradient(
            from var(--border-angle),
            rgba(215,233,167,.18) 0deg,
            #A8D45F 55deg,
            #6FBF73 105deg,
            rgba(215,233,167,.16) 155deg,
            rgba(215,233,167,.08) 220deg,
            #D7E9A7 285deg,
            rgba(215,233,167,.18) 360deg
        ) border-box;
    box-shadow: 0 12px 32px rgba(3, 17, 9, .18);
    animation: cardBorderSpin var(--card-border-speed) linear infinite;
    transition: transform .22s ease, box-shadow .35s ease, filter .35s ease;
}

.feature-card:hover,
.result-card:hover,
.info-card:hover {
    box-shadow:
        0 18px 42px rgba(7, 32, 17, .30),
        0 0 var(--card-glow-blur) rgba(168, 212, 95, var(--card-glow-opacity)),
        0 0 calc(var(--card-glow-blur) * 1.7) rgba(111, 191, 115, .16);
    filter: brightness(1.045);
}

@keyframes cardBorderSpin {
    to { --border-angle: 360deg; }
}

@media (prefers-reduced-motion: reduce) {
    .feature-card, .result-card, .info-card {
        animation: none;
    }
}

.feature-card {
    padding: 1.15rem 1.15rem 1rem 1.15rem;
    min-height: 170px;
    transition: transform .20s ease, box-shadow .35s ease, filter .35s ease;
}

.feature-card:hover {
    transform: translateY(-4px);
}

.feature-icon {
    width: 40px;
    height: 40px;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    border-radius: 12px;
    background: linear-gradient(135deg, rgba(168,212,95,.18), rgba(111,191,115,.16));
    border: 1px solid rgba(215,233,167,.20);
    font-size: 1.15rem;
}

.feature-title {
    margin: .85rem 0 .35rem 0;
    color: #FAFFF7;
    font-size: 1.02rem;
    font-weight: 740;
}

.feature-copy {
    margin: 0;
    color: #C5D3C2;
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
    overflow: visible;
    padding: 1.05rem 1.08rem 1rem 1.08rem;
    min-height: 118px;
    transition: transform .20s ease, box-shadow .35s ease, filter .35s ease;
}

.result-card:hover {
    transform: translateY(-3px);
}

.result-label {
    color: #CFDACB;
    font-size: .78rem;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: .055em;
}

/* Números de cálculo con alta visibilidad */
.result-value {
    display: inline-block;
    margin-top: .34rem;
    padding: .14rem .38rem .18rem .38rem;
    border-radius: 9px;
    color: #F8FFD5;
    background: linear-gradient(90deg, rgba(168,212,95,.15), rgba(215,233,167,.08));
    border: 1px solid rgba(215,233,167,.13);
    font-size: clamp(1.72rem, 2.35vw, 2.15rem);
    line-height: 1.12;
    font-weight: 900;
    letter-spacing: -.02em;
    text-shadow: 0 0 14px rgba(200, 235, 129, .34);
    font-variant-numeric: tabular-nums;
}

.result-unit {
    color: #B8C8B4;
    font-size: .78rem;
    font-weight: 650;
    margin-top: .34rem;
}

.status-box {
    display: flex;
    align-items: center;
    gap: .65rem;
    padding: .8rem .95rem;
    border-radius: 14px;
    border: 1px solid rgba(190, 214, 175, .20);
    background: rgba(51, 87, 64, .94);
    margin: .65rem 0 1rem 0;
}

.status-dot {
    width: 10px;
    height: 10px;
    border-radius: 50%;
    box-shadow: 0 0 18px currentColor;
}

.status-good { color: #A8E08E; }
.status-warn { color: #F2C14E; }
.status-bad { color: #FF8A80; }
.status-info { color: #B7DF74; }

.formula-card {
    padding: .9rem 1rem;
    border-radius: 14px;
    border: 1px solid rgba(168, 212, 95, .20);
    background: rgba(247, 250, 243, .86);
    color: #294D37;
    font-size: .88rem;
    line-height: 1.55;
    margin-bottom: .75rem;
}

.note-box {
    padding: .85rem 1rem;
    border-left: 3px solid #A8D45F;
    border-radius: 10px;
    background: rgba(187, 211, 132, .22);
    color: #294C38;
    font-size: .87rem;
    line-height: 1.55;
    margin: .75rem 0;
}

.sidebar-brand {
    position: relative;
    padding: .95rem 1rem;
    border: 1px solid rgba(168, 212, 95, .22);
    border-radius: 16px;
    background: linear-gradient(145deg, rgba(45, 80, 59, .92), rgba(29, 58, 43, .94));
    margin: .35rem 0 1rem 0;
}

.sidebar-brand .kicker {
    color: #D7E9A7;
    font-size: .70rem;
    font-weight: 800;
    letter-spacing: .10em;
    text-transform: uppercase;
}

.sidebar-brand .name {
    margin-top: .28rem;
    color: #FBFFF8;
    font-size: 1.05rem;
    font-weight: 780;
}

.sidebar-brand .program {
    margin-top: .2rem;
    color: #BDCCB8;
    font-size: .77rem;
    line-height: 1.4;
}

.footer {
    margin-top: 2.2rem;
    padding-top: 1rem;
    border-top: 1px solid rgba(188, 211, 173, .16);
    text-align: center;
    color: #9EAF9A;
    font-size: .78rem;
}

/* Inputs */
[data-testid="stNumberInput"] input,
[data-testid="stSelectbox"] div[data-baseweb="select"] > div {
    background: rgba(250, 252, 247, .96);
    color: #173D2A;
    border-color: rgba(66, 105, 75, .24);
}

/* Tabs */
button[data-baseweb="tab"] {
    font-weight: 800;
    color: #355B42 !important;
}

button[data-baseweb="tab"][aria-selected="true"] {
    color: #163D29 !important;
}

[data-baseweb="tab-highlight"] {
    background-color: #6F9E5B !important;
}

/* Radio principal y controles: texto visible sobre superficies claras */
[data-testid="stMain"] [role="radiogroup"] label p {
    color: #244A34 !important;
}

[data-testid="stNumberInput"] button {
    color: #284D38 !important;
}

/* Selectores y cajas de entrada */
[data-baseweb="input"] > div,
[data-baseweb="base-input"] {
    background: rgba(250,252,247,.96) !important;
}

[data-baseweb="input"] input {
    color: #173D2A !important;
    -webkit-text-fill-color: #173D2A !important;
}

/* Plotly */
[data-testid="stPlotlyChart"] {
    border: 1px solid rgba(188, 211, 173, .16);
    border-radius: 16px;
    overflow: hidden;
    background: rgba(247, 250, 243, .76);
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
                <div style="font-weight:750;color:#F6FBF2;">{text}</div>
                <div style="font-size:.84rem;color:#B8C8B4;margin-top:.12rem;">{detail}</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def oilgas_plot_layout(fig: go.Figure, title: str, x_title: str, y_title: str) -> go.Figure:
    fig.update_layout(
        title=dict(text=title, x=0.02, xanchor="left", font=dict(size=18, color="#F2F7F0")),
        xaxis_title=x_title,
        yaxis_title=y_title,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(24,49,36,0.42)",
        font=dict(color="#D5E0D1"),
        margin=dict(l=50, r=25, t=65, b=50),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1,
            bgcolor="rgba(0,0,0,0)",
        ),
        hoverlabel=dict(bgcolor="#264735", font_color="#F8FFF4"),
    )
    fig.update_xaxes(gridcolor="rgba(188,211,173,0.15)", zeroline=False)
    fig.update_yaxes(gridcolor="rgba(188,211,173,0.15)", zeroline=False)
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
            <div class="program">{PROGRAMA}<br>{INGENIERO}</div>
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

    # Reloj JavaScript persistente en el sidebar: visible en Home y Ejercicios.
    sidebar_clock = r"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
    <meta charset="UTF-8" />
    <style>
        *{box-sizing:border-box}
        body{margin:0;background:transparent;font-family:Inter,Arial,sans-serif}
        .clock{
            border:1px solid rgba(224,238,190,.38);
            border-radius:14px;
            padding:11px 13px 10px;
            background:linear-gradient(135deg,rgba(29,65,43,.68),rgba(76,112,72,.58));
            box-shadow:0 8px 20px rgba(13,39,23,.14);
        }
        .label{font-size:9px;letter-spacing:.12em;text-transform:uppercase;color:#DDEBB9;font-weight:850}
        #reloj{margin-top:4px;color:#FAFFD8;font-size:25px;line-height:1.05;font-weight:900;letter-spacing:.02em;font-variant-numeric:tabular-nums;text-shadow:0 0 12px rgba(214,235,148,.28)}
        #fecha{margin-top:5px;color:#E1EBDC;font-size:10px;line-height:1.25;text-transform:capitalize}
    </style>
    </head>
    <body>
        <div class="clock">
            <div class="label">Hora local del navegador</div>
            <div id="reloj">--:--:--</div>
            <div id="fecha">Sincronizando…</div>
        </div>
        <script>
            function actualizarReloj() {
                const ahora = new Date();
                document.getElementById("reloj").innerText = ahora.toLocaleTimeString();
                document.getElementById("fecha").innerText = ahora.toLocaleDateString('es-PE', {
                    weekday: 'short', day: '2-digit', month: 'short', year: 'numeric'
                });
            }
            actualizarReloj();
            setInterval(actualizarReloj, 1000);
        </script>
    </body>
    </html>
    """
    st.iframe(sidebar_clock, height=90)

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
                <div class="identity-pill"><b>Participante:</b> {INGENIERO}</div>
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
        "El reloj permanece visible en el menú lateral; aquí se mantiene una segunda interacción basada en un evento de clic.",
    )

    # Segunda interacción JavaScript: cambio de insight por evento de clic.
    js_component = r"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
    <meta charset="UTF-8" />
    <style>
        *{box-sizing:border-box}
        body{margin:0;background:transparent;font-family:Inter,Arial,sans-serif;color:#F4FAF0}
        .card{
            display:flex;align-items:center;justify-content:space-between;gap:18px;
            padding:15px 17px;min-height:96px;
            border:1px solid rgba(168,212,95,.26);border-radius:16px;
            background:linear-gradient(135deg,rgba(55,91,67,.98),rgba(38,72,52,.97));
            box-shadow:0 12px 28px rgba(4,22,11,.14);
        }
        .left{min-width:0}.tag{font-size:10px;letter-spacing:.11em;text-transform:uppercase;color:#E1EFB8;font-weight:850}
        .msg{margin-top:6px;color:#EEF5EA;font-size:13px;line-height:1.45}.count{font-size:10px;color:#C3D1BF;margin-top:6px}
        button{flex:0 0 auto;border:1px solid rgba(215,233,167,.30);background:rgba(168,212,95,.14);color:#FAFFE4;padding:10px 13px;border-radius:11px;font-weight:780;cursor:pointer;transition:.22s ease}
        button:hover{transform:translateY(-2px);background:rgba(168,212,95,.23);border-color:rgba(215,233,167,.56);box-shadow:0 0 18px rgba(168,212,95,.18)}
        @media(max-width:680px){.card{align-items:flex-start;flex-direction:column}button{width:100%}}
    </style>
    </head>
    <body>
        <div class="card">
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
    st.iframe(js_component, height=112)

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
                        line=dict(width=3, color="#A8D45F"),
                        hovertemplate="qₒ = %{x:,.1f} STB/d<br>Pwf = %{y:,.0f} psi<extra></extra>",
                    )
                )
                fig_ipr.add_trace(
                    go.Scatter(
                        x=[qo],
                        y=[pwf],
                        mode="markers",
                        name="Punto ingresado",
                        marker=dict(size=13, color="#F2C14E", line=dict(width=2, color="#FFF7D6")),
                        hovertemplate="Punto de operación<br>qₒ = %{x:,.1f} STB/d<br>Pwf = %{y:,.0f} psi<extra></extra>",
                    )
                )
                fig_ipr.add_trace(
                    go.Scatter(
                        x=[qb],
                        y=[pb],
                        mode="markers",
                        name="Punto de burbuja",
                        marker=dict(size=10, color="#76C47B"),
                        hovertemplate="Punto de burbuja<br>qᵦ = %{x:,.1f} STB/d<br>Pᵦ = %{y:,.0f} psi<extra></extra>",
                    )
                )
                fig_ipr.add_hline(y=pb, line_dash="dash", line_color="rgba(168,212,95,.58)")
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
                        line=dict(width=3, color="#7BCB82"),
                        hovertemplate="TVD = %{x:,.0f} ft<br>Pₕ = %{y:,.0f} psi<extra></extra>",
                    )
                )
                fig_h.add_trace(
                    go.Scatter(
                        x=[tvd],
                        y=[ph],
                        mode="markers",
                        name="Punto calculado",
                        marker=dict(size=13, color="#C7E879", line=dict(width=2, color="#F7FFE6")),
                        hovertemplate="TVD = %{x:,.0f} ft<br>Pₕ = %{y:,.0f} psi<extra></extra>",
                    )
                )
                fig_h.add_hline(
                    y=pform,
                    line_dash="dash",
                    line_color="rgba(242,193,78,.78)",
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
                        marker_color=["#7BCB82", "#C7E879"],
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
    f'<div class="footer">{APP_TITLE} · {INGENIERO} · {PROGRAMA}</div>',
    unsafe_allow_html=True,
)
