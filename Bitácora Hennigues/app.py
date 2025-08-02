from flask import Flask, render_template
from livereload import Server

app = Flask(__name__, static_folder="static", template_folder="templates")

# Recarga de plantillas y estáticos en desarrollo
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0   # desactiva caché de estáticos en dev

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.debug = True  # activa el reloader del servidor
    server = Server(app.wsgi_app)

    # Archivos a vigilar (ajusta rutas si añades más)
    server.watch("app.py")
    server.watch("templates/*.html")
    server.watch("static/*.css")
    server.watch("static/*.js")

    # Arranca con inyección del script de livereload en las páginas
    server.serve(host="127.0.0.1", port=5000, debug=True, restart_delay=0.2)
