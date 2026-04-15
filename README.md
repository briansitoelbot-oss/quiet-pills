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

1. Sube esta carpeta a GitHub
2. Ve a [render.com](https://render.com)
3. New → Blueprint
4. Conecta tu GitHub
5. Añade variable de entorno:
   - `DISCORD_WEBHOOK` = tu_webhook_real
6. Deploy!

## Seguridad

El webhook NUNCA se expone públicamente porque:
- Está en `.env` (ignorado por `.gitignore`)
- Se configura como variable de entorno en el hosting
- El servidor lo lee internamente
