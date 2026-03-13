# Enterprise Portfolio Pursuit Framework (Fixed Build)

This is a repaired, working version of the original repository.

## What was fixed

- Rebuilt `app.py` into valid Python
- Rebuilt `requirements.txt` into valid package lines
- Rebuilt `Dockerfile` into valid Docker syntax
- Rebuilt `docker-compose.yml` into a working Compose file
- Cleaned the README and startup steps

## Run with Docker

### 1) Open Terminal in this folder

### 2) Build and start

```bash
docker compose up --build
```

### 3) Open in browser

```text
http://localhost:8501
```

## Run without Docker

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

Then open `http://localhost:8501`.

## Stop the app

If using Docker:

```bash
docker compose down
```

If using local Streamlit, press `Ctrl + C` in Terminal.
