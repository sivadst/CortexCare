# CortexCare

Streamlit app for quick student stress analysis and lightweight recommendations.

## Run locally

```bash
pip install -r requirements.txt
streamlit run main.py
```

## Deploy on Streamlit Community Cloud

1. Push this repository to GitHub.
2. Open `https://share.streamlit.io/`.
3. Click **Create app**.
4. Select this repository and set the entrypoint file to `main.py`.
5. In Advanced settings, keep Python `3.12` unless you need a different supported version.
6. Deploy.

The repo already includes:

- `requirements.txt` for Python dependencies
- `.streamlit/config.toml` for Streamlit configuration
