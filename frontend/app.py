import numpy as np
import streamlit as st
import pandas as pd
import joblib
import os
import textwrap

# ==========================================
# CONFIGURATION
# ==========================================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

st.set_page_config(
    page_title="Laptop Price Estimator",
    layout="wide"
)


# ==========================================
# CUSTOM DARK THEME
# ==========================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

:root {
    --background: #0b0f19;
    --surface: #161b26;
    --surface-hover: #1c2332;
    --border: #262d3d;
    --text: #f1f5f9;
    --muted: #929bad;
    --accent: #6366f1;
    --accent-light: #8b5cf6;
}

/* GLOBAL */

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background: var(--background);
    color: var(--text);
}

header[data-testid="stHeader"] {
    background: transparent;
}

.main .block-container {
    max-width: 1120px;
    padding: 2rem 2.5rem 1rem;
}

/* HIDE STREAMLIT CLUTTER */

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

[data-testid="stDeployButton"],
.stDeployButton {
    display: none !important;
}

[data-testid="stToolbar"] {
    display: none !important;
}

/* TYPOGRAPHY */

h1, h2, h3, h4 {
    color: var(--text) !important;
    font-family: 'Inter', sans-serif !important;
}

h1 {
    font-size: 2.65rem !important;
    font-weight: 800 !important;
    letter-spacing: -1.8px;
    margin-bottom: 8px !important;
}

h2 {
    font-size: 1.35rem !important;
    font-weight: 700 !important;
}

h3 {
    font-size: 1rem !important;
    font-weight: 600 !important;
}

p {
    color: var(--muted);
}

/* HERO */

.hero-label {
    color: #818cf8;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 2px;
    margin-bottom: 12px;
}

.hero-title {
    font-family: 'Inter', sans-serif;
    font-size: 43px;
    font-weight: 800;
    letter-spacing: -2px;
    line-height: 1.2;
    background: linear-gradient(90deg, #ffffff, #a5b4fc, #8b5cf6);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero-description {
    color: #929bad;
    font-size: 14px;
    margin-top: 10px;
}

/* SECTION HEADINGS */

.section-heading {
    color: #f1f5f9;
    font-size: 17px;
    font-weight: 700;
    margin-bottom: 4px;
}

.section-description {
    color: #929bad;
    font-size: 12px;
    margin-bottom: 20px;
}

/* CARDS */

div[data-testid="stVerticalBlockBorderWrapper"] {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 20px;
    box-shadow: 0 8px 25px rgba(0, 0, 0, 0.12);
    transition: border-color 0.2s ease;
}

/* INPUT LABELS */

div[data-testid="stSelectbox"] label,
div[data-testid="stNumberInput"] label {
    color: #cbd5e1 !important;
    font-size: 12px !important;
    font-weight: 600 !important;
}

/* SELECTBOX */

div[data-baseweb="select"] > div {
    background: #101622 !important;
    border: 1px solid #30394b !important;
    border-radius: 8px !important;
    min-height: 43px;
    transition: border-color 0.2s ease;
}

div[data-baseweb="select"] > div:hover {
    border-color: var(--accent) !important;
}

div[data-baseweb="select"] span {
    color: #f1f5f9 !important;
}

/* SELECTBOX DROPDOWN */

div[data-baseweb="popover"] {
    background: #161b26 !important;
    border: 1px solid var(--border) !important;
}

div[data-baseweb="menu"] {
    background: #161b26 !important;
}

div[role="option"] {
    background: #161b26 !important;
    color: #f1f5f9 !important;
}

div[role="option"]:hover {
    background: #252d40 !important;
}

/* NUMBER INPUT */

div[data-testid="stNumberInput"] input {
    background: #101622 !important;
    color: #f1f5f9 !important;
    border: 1px solid #30394b !important;
    border-radius: 8px !important;
}

div[data-testid="stNumberInput"] button {
    background: #1c2332 !important;
    color: #cbd5e1 !important;
    border-color: #30394b !important;
}

/* FOCUS */

div[data-baseweb="select"]:focus-within,
div[data-testid="stNumberInput"] input:focus {
    border-color: var(--accent) !important;
    box-shadow: 0 0 0 2px rgba(99, 102, 241, 0.18) !important;
}

/* PREDICTION BUTTON */

.stButton > button {
    width: 100%;
    height: 52px;
    border: none;
    border-radius: 9px;
    color: white;
    font-family: 'Inter', sans-serif;
    font-size: 14px;
    font-weight: 700;
    background: linear-gradient(100deg, #6366f1, #8b5cf6);
    box-shadow: 0 5px 18px rgba(99, 102, 241, 0.2);
    transition: all 0.2s ease;
}

.stButton > button:hover {
    color: white;
    border: none;
    transform: translateY(-2px);
    box-shadow: 0 8px 25px rgba(99, 102, 241, 0.35);
}

.stButton > button:active {
    transform: translateY(0);
}

/* RESULT CARD */

.result-card {
    background: linear-gradient(135deg, #191f32, #211b38);
    border: 1px solid #454078;
    border-radius: 14px;
    padding: 30px;
    margin-top: 20px;
    animation: fadeIn 0.5s ease;
    box-shadow: 0 8px 35px rgba(99, 102, 241, 0.10);
}

.result-label {
    color: #a5b4fc;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 1.8px;
}

.result-price {
    color: #ffffff;
    font-size: 42px;
    font-weight: 800;
    letter-spacing: -1.5px;
    margin: 12px 0 5px;
}

.result-caption {
    color: #a1a1b5;
    font-size: 12px;
}

/* ANIMATION */

@keyframes fadeIn {
    from {
        opacity: 0        ;
        transform: translateY(10px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

/* CAPTIONS */

.stCaption {
    color: var(--muted);
}

/* FOOTER */

.footer {
    text-align: center;
    color: #647084;
    font-size: 11px;
    padding: 25px 0 10px;
    border-top: 1px solid var(--border);
    margin-top: 40px;
}

/* DIVIDERS */

hr {
    border-color: var(--border) !important;
    margin: 18px 0 !important;
}

</style>
""", unsafe_allow_html=True)


# ==========================================
# LOAD TRAINED MODELS
# ==========================================

@st.cache_resource
def load_models():

    return {
        "Linear Regression": joblib.load(
            os.path.join(BASE_DIR, "models", "linear_regression.pkl")
        ),

        "Decision Tree": joblib.load(
            os.path.join(BASE_DIR, "models", "decision_tree.pkl")
        ),

        "Random Forest": joblib.load(
            os.path.join(BASE_DIR, "models", "random_forest.pkl")
        )
    }


models = load_models()


# ==========================================
# LOAD PROCESSED DATASET
# ==========================================

@st.cache_data
def load_dataset():

    return pd.read_csv(
        os.path.join(BASE_DIR, "dataset", "processed_laptops.csv")
    )


df = load_dataset()


# ==========================================
# HERO HEADER
# ==========================================

st.markdown("""
<div class="hero-label">LAPTOP VALUATION PLATFORM</div>

<div class="hero-title">
    Used Laptop Price Estimator
</div>

<div class="hero-description">
    Estimate the resale value of a laptop using its hardware
    specifications and machine learning.
</div>
""", unsafe_allow_html=True)


st.markdown("<br>", unsafe_allow_html=True)


# ==========================================
# LAPTOP SPECIFICATIONS
# ==========================================

st.markdown("""
<div class="section-heading">Laptop specifications</div>
<div class="section-description">
    Enter the details of the laptop you want to evaluate.
</div>
""", unsafe_allow_html=True)


col1, col2 = st.columns(2, gap="medium")


# DEVICE INFORMATION

with col1:

    with st.container(border=True):

        st.markdown("### Device information")

        brand = st.selectbox(
            "Brand",
            sorted(df["Brand"].dropna().unique())
        )

        available_models = sorted(
            df.loc[df["Brand"] == brand, "Model_Family"]
            .dropna().unique()
        )

        model_family = st.selectbox(
            "Model",
            available_models
        )

        condition = st.selectbox(
            "Condition",
            sorted(df["Condition"].dropna().unique())
        )

        ram = st.selectbox(
            "RAM",
            sorted(df["RAM_GB"].dropna().unique()),
            format_func=lambda x: f"{x} GB"
        )


# HARDWARE SPECIFICATIONS

with col2:

    with st.container(border=True):

        st.markdown("### Hardware specifications")

        processor = st.selectbox(
            "Processor",
            sorted(df["Processor_Family"].dropna().unique())
        )

        generation_category = st.selectbox(
            "Processor generation",
            sorted(df["Generation_Category"].dropna().unique())
        )

        generation_number = st.number_input(
            "Generation number (0 if not applicable)",
            min_value=0,
            max_value=20,
            value=0
        )

        hdd = st.selectbox(
            "HDD storage",
            sorted(df["HDD_GB"].dropna().unique()),
            format_func=lambda x: f"{x} GB"
        )

        ssd = st.selectbox(
            "SSD storage",
            sorted(df["SSD_GB"].dropna().unique()),
            format_func=lambda x: f"{x} GB"
        )


# ==========================================
# PREDICTION SETTINGS
# ==========================================

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<div class="section-heading">Prediction settings</div>
<div class="section-description">
    Select the machine learning algorithm for your estimation.
</div>
""", unsafe_allow_html=True)


selected_model = st.selectbox(
    "Prediction algorithm",
    list(models.keys())
)


# ==========================================
# PREDICTION
# ==========================================

st.markdown("<br>", unsafe_allow_html=True)


if st.button("Estimate Price", use_container_width=True):

    input_data = pd.DataFrame([{
        "Brand": brand,
        "Processor_Family": processor,
        "Generation_Category": generation_category,
        "Generation_Number": generation_number if generation_number != 0 else np.nan,
        "RAM_GB": ram,
        "HDD_GB": hdd,
        "SSD_GB": ssd,
        "Condition": condition,
        "Model_Family": model_family
    }])

    try:

        selected_algorithm = models[selected_model]

        prediction = selected_algorithm.predict(input_data)[0]

        result_html = f"""
        <div class="result-card">
            <div class="result-label">
                ESTIMATED RESALE VALUE
            </div>

            <div class="result-price">
                ₦{prediction:,.0f}
            </div>

            <div class="result-caption">
                Prediction generated using {selected_model}.
                Actual market prices may vary.
            </div>
        </div>
        """

        st.html(result_html)
    except Exception as e:

        st.error(f"Prediction failed: {e}")


# ==========================================
# FOOTER
# ==========================================

st.markdown("""
<div class="footer">
    Used Laptop Price Estimator
    <br>
    Machine Learning Project
</div>
""", unsafe_allow_html=True)