
import streamlit as st
import os
import time
from sentinel_engine import init_enterprise_db, fetch_ledger_df, encrypt_payload, build_live_agent
from ui_styles import apply_cyber_theme, render_banner

st.set_page_config(page_title="CryptaSentinel AI | Zero-Trust SOC", layout="wide", page_icon="🛡️")
apply_cyber_theme()
render_banner()

init_enterprise_db()
live_agent = build_live_agent()

if not os.environ.get("GEMINI_API_KEY"):
    st.error("🚨 GEMINI_API_KEY missing! Set `$env:GEMINI_API_KEY='your_key'` in terminal before running.")
    st.stop()

with st.sidebar:
    st.markdown("### 🎛️ SOC Master Controls")
    firewall_on = st.toggle("Zero-Trust Runtime Shield", value=True)
    st.caption("🟢 Pre-Execution Memory Wipe ARMED" if firewall_on else "🔴 WARNING: Firewall Bypassed")
    origin_channel = st.selectbox("Agent Mesh Ingress Hop:", [
        "External_Vendor_Email (Untrusted Node)",
        "B2B_EDI_SupplyChain_Gateway (External)",
        "Internal_ERP_Accounting_Node (Trusted)"
    ])
    st.divider()
    st.markdown("### 🏦 Live SQLite Treasury Ledger")
    rows = fetch_ledger_df()
    if rows:
        for r in rows:
            st.markdown(f"""
            <div style="background:#F8FAFC; border:1px solid #E2E8F0; border-left:4px solid #10B981; padding:8px 12px; border-radius:8px; margin-bottom:8px; font-size:0.82rem; color:#0F172A;">
                <b>TX #{r[0]}</b> • <span style="color:#059669; font-weight:700;">{r[4]}</span><br>
                Vendor: <b>{r[2]}</b><br>
                Settled: <span style="color:#2563EB; font-weight:700;">${r[3]:,.2f} USD</span>
            </div>""", unsafe_allow_html=True)
    else:
        st.caption("No payouts settled yet.")

with st.expander("🔐 Sender Encryption Studio (Generate Real AES-256 Wire Packet Before Sending)"):
    c_s1, c_s2 = st.columns(2)
    with c_s1:
        draft = st.text_input("Draft B2B Invoice or Attack Payload to Encrypt:")
    with c_s2:
        if draft.strip():
            st.text_area("Copy Generated AES-256 Ciphertext:", value=encrypt_payload(draft.strip()), height=75)
        else:
            st.info("Type a message on the left to generate its AES-256 encrypted wire token.")

st.markdown("#### 📡 Step 1: Enterprise Wire Ingress")
tab_enc, tab_txt, tab_file = st.tabs([
    "🔐 Raw AES-256 Ciphertext (Black-Box Ingress)",
    "✍️ Plaintext Simulator (Auto-Encrypts on Wire)",
    "📂 Upload File (.enc / .txt / .json)"
])

wire_packet = ""
with tab_enc:
    c_in = st.text_area("Paste incoming AES-256 Ciphertext (`gAAAAAB...`):", height=100)
    if c_in.strip():
        wire_packet = c_in.strip()

with tab_txt:
    p_in = st.text_area("Enter Plaintext Invoice or Attack (Auto-encrypts into AES-256):", height=100)
    if p_in.strip():
        wire_packet = encrypt_payload(p_in.strip())

with tab_file:
    up = st.file_uploader("Upload encrypted `.enc` or plaintext ledger:", type=["enc", "txt", "csv", "json"])
    if up is not None:
        raw_f = up.read().decode("utf-8", errors="ignore").strip()
        wire_packet = raw_f if raw_f.startswith("gAAAAAB") else encrypt_payload(raw_f)
        st.success(f"Loaded `{up.name}` ({len(raw_f)} bytes)")

if st.button("⚡ INTERCEPT, DECRYPT IN MEMORY & RUN AI POLYGRAPH", type="primary", use_container_width=True):
    if not wire_packet:
        st.warning("⚠️ Paste an AES-256 ciphertext, enter text, or upload a file first.")
        st.stop()

    start_t = time.perf_counter()
    with st.spinner("Decrypting AES-256 stream in isolated memory & running Semantic Polygraph..."):
        try:
            res = live_agent.invoke({
                "encrypted_wire_packet": wire_packet, "decrypted_raw_text": "",
                "deobfuscated_text": "", "source_origin": origin_channel,
                "firewall_active": firewall_on, "entropy_score": 0.0, "ai_risk_score": 0,
                "ai_threat_reason": "", "extracted_vendor": "", "extracted_amount": 0.0,
                "memory_buffer": "", "final_status": "PENDING", "agent_response": "",
                "model_used": "", "audit_trail": []
            })
        except Exception as err:
            st.error(f"❌ Decryption Failed: Invalid AES-256 Ciphertext ({err})")
            st.stop()

    lat = round((time.perf_counter() - start_t) * 1000, 1)
    is_lock = res["final_status"] == "HARD_LOCKED"
    is_byp = res["final_status"] == "UNPROTECTED_EXECUTION"

    st.markdown("---")
    k1, k2, k3, k4 = st.columns(4)
    k1.markdown(f'<div class="kpi-card"><div class="kpi-label">Shannon Entropy H(X)</div><div class="{"kpi-danger" if res["entropy_score"]>4.2 else "kpi-safe"}">{res["entropy_score"]}</div></div>', unsafe_allow_html=True)
    k2.markdown(f'<div class="kpi-card"><div class="kpi-label">AI Semantic Risk</div><div class="{"kpi-danger" if res["ai_risk_score"]>=65 else "kpi-safe"}">{res["ai_risk_score"]} / 100</div></div>', unsafe_allow_html=True)
    k3.markdown(f'<div class="kpi-card"><div class="kpi-label">Memory Buffer</div><div class="{"kpi-danger" if is_lock else "kpi-safe"}">{"WIPED_0x000000" if is_lock else "VERIFIED_ACTIVE"}</div></div>', unsafe_allow_html=True)
    k4.markdown(f'<div class="kpi-card"><div class="kpi-label">Verdict ({lat} ms)</div><div class="{"kpi-danger" if (is_lock or is_byp) else "kpi-safe"}">{res["final_status"]}</div></div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    p1, p2, p3, p4 = st.columns(4)
    p1.markdown(f'<div class="pipe-box pipe-safe"><b>1. RUNTIME DECRYPT</b><br>AES-256 Unlocked<br><code>H(X)={res["entropy_score"]}</code></div>', unsafe_allow_html=True)
    p2.markdown(f'<div class="pipe-box {"pipe-block" if is_lock else "pipe-safe"}"><b>2. AI POLYGRAPH</b><br>Mesh & Stego Scan<br><code>{"THREAT FLAGGED" if is_lock else "INTENT CLEAN"}</code></div>', unsafe_allow_html=True)
    p3.markdown(f'<div class="pipe-box {"pipe-block" if (is_lock or is_byp) else "pipe-safe"}"><b>3. CONTEXT SHIELD</b><br>Memory Isolation<br><code>{"WIPED_0x000000" if is_lock else ("BYPASSED" if is_byp else "SHIELD ACTIVE")}</code></div>', unsafe_allow_html=True)
    p4.markdown(f'<div class="pipe-box {"pipe-block" if is_byp else "pipe-safe"}"><b>4. TREASURY / DB API</b><br>Downstream Action<br><code>{"HARD_LOCKED" if is_lock else ("DB BREACHED!" if is_byp else "SQLITE COMMITTED")}</code></div>', unsafe_allow_html=True)

    st.markdown("---")
    col_l, col_r = st.columns(2)
    with col_l:
        st.markdown("#### 🔍 Cryptographic & AI Security Audit Trail")
        for log in res["audit_trail"]:
            st.markdown(f"- {log}")
        with st.expander("Inspect Memory Buffer Content"):
            st.code(res["memory_buffer"], language="text")

    with col_r:
        st.markdown(f"#### 🤖 Autonomous Agent Output (`{res['model_used']}`)")
        if is_lock:
            st.error("🛡️ ATTACK NEUTRALIZED AT RUNTIME — $0 LOST")
        elif is_byp:
            st.error("💥 FIREWALL DISABLED — AGENT HIJACKED!")
        else:
            st.success("✅ VERIFIED INVOICE SETTLED IN LIVE SQLITE DB")
        st.code(res["agent_response"], language="text")
