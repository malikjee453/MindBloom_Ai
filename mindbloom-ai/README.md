# MindBloom AI 🌱

**Built by: Engr. Mubashir Malik**

Streamlit emotional-wellbeing companion using Groq `openai/gpt-oss-120b`, multi-agent routing, optional RAG over uploaded documents, and a local mood journal.

## Local setup

```bash
python -m venv .venv
```
Windows:
```powershell
.venv\Scripts\activate
```
macOS/Linux:
```bash
source .venv/bin/activate
```

```bash
pip install -r requirements.txt
```

Set `GROQ_API_KEY`, then:

```bash
streamlit run app.py
```

## Streamlit Cloud

1. Upload the contents of this folder to a GitHub repository.
2. Create a Streamlit app from that repository.
3. Set the main file to `app.py`.
4. Add this secret under **Settings → Secrets**:

```toml
GROQ_API_KEY = "YOUR_GROQ_API_KEY"
```

5. Deploy.

`app.py`, `core/`, `agents/`, `rag/`, and `pages/` must all be at the repository root.

## RAG

Knowledge Center supports PDF, DOCX, TXT and Markdown. It uses `sentence-transformers/all-MiniLM-L6-v2` and FAISS. Streamlit Cloud storage is ephemeral, so uploaded knowledge may need to be re-indexed after a restart/redeploy.

## Safety

This is a supportive self-help application, not a clinician or emergency service. It does not diagnose or prescribe medication and avoids unsafe withdrawal instructions. In an emergency, contact local emergency services or an appropriate crisis resource.
