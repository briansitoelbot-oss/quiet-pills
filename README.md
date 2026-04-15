# Quiet Pills Game Copier

Servidor Flask para Quiet Pills Game Copier.

## Archivos

- `app.py` - Servidor principal
- `requirements.txt` - Dependencias de Python
- `Procfile` - Para deploy en Render
- `.gitignore` - Archivos ignorados (webhook seguro)
- `.env.example` - Plantilla para variables de entorno
- `public/index.html` - Página web

## Setup Local

```bash
# 1. Entra en la carpeta
cd quiet-pills

# 2. Crea archivo .env con tu webhook
echo DISCORD_WEBHOOK=tu_webhook_aqui > .env

# 3. Instala dependencias
pip install -r requirements.txt

# 4. Ejecuta
python app.py
```

## Deploy en Render (GRATIS)

cd C:\Users\OLd9\Desktop\quiet-pills
git add .
git commit -m "Fix route"
git push

## Seguridad

El webhook NUNCA se expone públicamente porque:
- Está en `.env` (ignorado por `.gitignore`)
- Se configura como variable de entorno en el hosting
- El servidor lo lee internamente
