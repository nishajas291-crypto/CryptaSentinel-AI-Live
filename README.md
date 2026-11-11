# 🛡️ CryptaSentinel AI: Autonomous Runtime Decryption & Multi-Agent Mesh Firewall

**Enterprise Zero-Trust Security Gateway for Agentic AI Workflows**  
*Powered by Runtime AES-256 Decryption • Shannon Entropy Screening • Auto Steganography Decoding • SwarmIntercept Multi-Agent Polygraph • Google Gemini*

---

## 🚨 The Enterprise Security Blind Spot

Modern enterprises encrypt sensitive B2B workflows—such as supplier invoices, treasury ledgers, and EDI payloads—using AES-256. Traditional perimeter firewalls and Data Loss Prevention (DLP) scanners inspect these files only in their encrypted state, passing them as harmless random noise.

However, when an autonomous AI agent decrypts the payload in memory, **two critical attacks** occur simultaneously:
1. **Decryption-Triggered Prompt Injection:** Hidden adversarial instructions (often obfuscated via Base64 or zero-width steganography) unlock inside the LLM's active context window.
2. **Lateral Multi-Hop Agent Collusion:** A compromised ingress agent delegates unauthorized actions (such as wiring treasury funds or dumping payroll databases) to privileged downstream agents.

---

## 🏗️ Unified 4-Stage Zero-Trust Architecture

**CryptaSentinel AI** merges runtime cryptographic memory protection with **SwarmIntercept's** multi-agent intent polygraph into a single stateful **LangGraph** proxy gateway:

```text
[ Encrypted AES-256 Wire Packet ]  (Bypasses Traditional Perimeter DLP)
               │
               ▼
┌─────────────────────────────────────────────────────────┐
│ STAGE 1: Runtime Memory Decryption & Entropy Screen     │
│  • Unlocks AES-256 payload in isolated memory           │
│  • Computes Shannon Entropy H(X) to flag anomalies      │
│  • Auto-decodes Base64 & zero-width steganography       │
└──────────────┬──────────────────────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────────────────────┐
│ STAGE 2: Live AI Semantic Polygraph (SwarmIntercept)     │
│  • Evaluates semantic intent & risk score (0–100)       │
│  • Traces multi-hop agent provenance & collusion paths  │
└──────────────┬──────────────────────────────────────────┘
               │
       ┌───────┴───────┐
       │               │
 [ VERIFIED ]    [ THREAT >= 65 ]
       │               │
       ▼               ▼
┌─────────────┐ ┌─────────────────────────────────────────┐
│ STAGE 4:    │ │ STAGE 3: Atomic Context Flush & Lock    │
│ Safe DB &   │ │  • Overwrites memory -> WIPED_0x000000  │
│ Treasury    │ │  • Hard-locks downstream Treasury/DB    │
│ Execution   │ │  • Returns CRITICAL_POLICY_VIOLATION    │
└─────────────┘ └─────────────────────────────────────────┘
```

---

## ✨ Key Capabilities

* **🔐 Black-Box AES-256 Runtime Guard:** Intercepts and inspects payloads at the exact microsecond of in-memory decryption before tokens reach the target LLM.
* **📐 Mathematical Shannon Entropy Screening:** Measures character-level randomness \(H(X) = -\sum P(x_i)\log_2 P(x_i)\) to detect padded and obfuscated payloads.
* **🕵️ Real-Time Steganography De-Obfuscation:** Automatically strips zero-width characters and decodes embedded Base64 command strings prior to semantic evaluation.
* **🕸️ Multi-Agent Intent Polygraph:** Prevents compromised public-facing agents (e.g., email/vendor parsers) from triggering high-privilege internal agents (Treasury/SQLite DB).
* **🧹 Deterministic Atomic Memory Wipe (`WIPED_0x000000`):** Purges poisoned context buffers and isolates downstream APIs (`HARD_LOCKED`) with zero false-positive leakage.
* **🔄 High-Availability Model Failover:** Seamlessly routes live security evaluation across `gemini-3.8-flash` and `gemini-3.5-flash` nodes.

---

## 🗂️ Project Structure

```text
CryptaSentinel-Live/
├── sentinel_engine.py   # LangGraph pipeline, AES-256, Entropy, Stego decoder, SQLite DB & Gemini Polygraph
├── ui_styles.py         # Enterprise Cloud SaaS SOC theme & glassmorphic telemetry components
├── app.py               # Streamlit Zero-Trust SOC console & Sender Encryption Studio
└── README.md            # Project documentation
```

---

## 🚀 Quickstart & Local Deployment

### 1. Clone & Create Virtual Environment
```powershell
git clone https://github.com/nishajas291-crypto/CryptaSentinel-AI-Live.git
cd CryptaSentinel-AI
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 2. Install Dependencies
```powershell
pip install streamlit langgraph cryptography google-genai
```

### 3. Configure Google Gemini API Key & Launch SOC Console
```powershell
\$env:GEMINI_API_KEY="your_actual_gemini_api_key"
streamlit run app.py
```

---

## 🔬 Live Verification Scenarios

| Scenario | Payload Characteristics | Shannon Entropy $H(X)$ | AI Risk Score | Gateway Action |
| :--- | :--- | :---: | :---: | :--- |
| **1. Verified B2B Invoice** | Standard Dubai supplier logistics invoice (`$14,500 USD`) | `~3.95` (Normal) | `5 / 100` | `VERIFIED_SAFE` (Committed to SQLite Treasury DB) |
| **2. Trojan Encrypted Heist** | AES-256 ciphertext hiding `SYSTEM OVERRIDE` wire transfer | `> 4.50` (Elevated) | `98 / 100` | `HARD_LOCKED` (`WIPED_0x000000`, `$0` Lost) |
| **3. Base64 Stego Smuggling** | JSON invoice hiding Base64-encoded payroll dump command | `5.57` (Anomalous) | `98 / 100` | `HARD_LOCKED` (Auto-decoded & neutralized) |

---

## 📄 License

Distributed under the MIT License. Built for Enterprise Agentic AI Security.
