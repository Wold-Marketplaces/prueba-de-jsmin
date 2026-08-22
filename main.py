import eel

eel.init('.')  # Carpeta donde están los HTML

# Exponemos funciones para abrir las otras páginas sólo cuando se llamen desde JavaScript
@eel.expose
def abrir_ingresos():
    # Abrimos la página dentro de la misma ventana/instancia de Eel usando mode='chrome-app'
    eel.start('ingresos.html', mode='chrome-app', size=(1000, 800), block=False)

@eel.expose
def abrir_ingresos_mes():
    eel.start('ingresos_mes.html', mode='chrome-app', size=(1000, 800), block=False)

# Ventana principal
# Para la ventana principal también usamos el modo app de Chrome para que todo quede embebido
# y no en una pestaña del navegador.

eel.start('index.html', mode='chrome-app', size=(1000, 800), block=True)

