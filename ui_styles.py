import streamlit as st

def apply_cyber_theme():
    st.markdown("""
    <style>
        /* Clean Enterprise Cloud SaaS Light-Slate Canvas */
        .stApp {
            background: linear-gradient(135deg, #F8FAFC 0%, #EEF2F6 50%, #E2E8F0 100%) !important;
            color: #0F172A !important;
            font-family: 'Inter', 'Segoe UI', sans-serif;
        }
        .block-container {
            padding-top: 2rem !important;
            padding-bottom: 2rem !important;
            max-width: 96% !important;
        }
        /* Fix All Text & Labels to Crisp Navy */
        h1, h2, h3, h4, p, label, .stMarkdown, .stRadio label {
            color: #0F172A !important;
        }
        /* Clean Light-Mode Code & Terminal Boxes */
        pre, code {
            white-space: pre-wrap !important;
            word-break: break-word !important;
            overflow-x: hidden !important;
            background-color: #FFFFFF !important;
            border: 1px solid #CBD5E1 !important;
            color: #1E293B !important;
            border-radius: 8px !important;
            box-shadow: 0 2px 6px rgba(15, 23, 42, 0.04);
        }
        /* Executive Enterprise Header Banner */
        .cyber-banner {
            background: linear-gradient(120deg, #0F172A 0%, #1E3A8A 60%, #0284C7 100%);
            padding: 20px 26px;
            border-radius: 14px;
            margin-bottom: 20px;
            box-shadow: 0 10px 25px rgba(15, 23, 42, 0.15);
        }
        .cyber-title { font-size: 1.7rem; font-weight: 800; color: #FFFFFF !important; margin: 0; }
        .cyber-sub { font-size: 0.9rem; color: #CBD5E1 !important; margin-top: 6px; }
        .badge-live {
            background: #10B981; color: #FFFFFF !important;
            padding: 4px 12px; border-radius: 20px;
            font-size: 0.72rem; font-weight: 700; margin-left: 10px;
        }
        /* Crisp White Glass KPI Cards */
        .kpi-card {
            background: #FFFFFF;
            border: 1px solid #E2E8F0;
            border-top: 4px solid #2563EB;
            border-radius: 12px;
            padding: 14px 10px;
            text-align: center;
            box-shadow: 0 4px 14px rgba(15, 23, 42, 0.06);
        }
        .kpi-label { font-size: 0.72rem; text-transform: uppercase; font-weight: 700; color: #64748B; margin-bottom: 6px; }
        .kpi-safe { font-size: 1.15rem; font-weight: 800; color: #059669; }
        .kpi-danger { font-size: 1.15rem; font-weight: 800; color: #DC2626; }
        /* 4-Stage Pipeline Cards */
        .pipe-box {
            background: #FFFFFF; border: 1.5px solid #CBD5E1;
            border-radius: 10px; padding: 12px; text-align: center; font-size: 0.84rem;
            box-shadow: 0 3px 10px rgba(15, 23, 42, 0.04);
        }
        .pipe-safe { border-color: #10B981; background: #ECFDF5; }
        .pipe-block { border-color: #EF4444; background: #FEF2F2; }
        /* Clean White Enterprise Sidebar */
        section[data-testid="stSidebar"] {
            background-color: #FFFFFF !important;
            border-right: 1px solid #E2E8F0;
        }
        /* Royal Blue Enterprise Action Button */
        div.stButton > button[kind="primary"] {
            background: linear-gradient(90deg, #1D4ED8 0%, #2563EB 50%, #0284C7 100%) !important;
            color: #FFFFFF !important; font-weight: 700; border: none;
            border-radius: 10px; padding: 0.7rem 1.2rem;
            box-shadow: 0 6px 16px rgba(37, 99, 235, 0.28);
        }
    </style>
    """, unsafe_allow_html=True)

def render_banner():
    st.markdown("""
    <div class="cyber-banner">
        <div class="cyber-title">🛡️ CRYPTASENTINEL AI <span class="badge-live">● ENTERPRISE ZERO-TRUST GATEWAY</span></div>
        <div class="cyber-sub">
            Autonomous Runtime Decryption & Multi-Agent Mesh Firewall •
            <b>AES-256 Memory Guard</b> | <b>Shannon Entropy H(X)</b> | <b>Stego Auto-Decoder</b> | <b>Swarm Polygraph</b>
        </div>
    </div>
    """, unsafe_allow_html=True)
