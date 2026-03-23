import os
import shutil

# Diccionario de extensiones → carpeta
extensiones_dict = {
    ".txt":  "documentos",
    ".docx": "documentos",
    ".pdf":  "libros",
    ".jpg":  "imagenes",
    ".png":  "imagenes",
    ".exe":  "ejecutables",
    ".zip":  "archivos_comprimidos",
    ".rar":  "archivos_comprimidos",
    ".mp4":  "videos",
    ".avi":  "videos",
    ".py":   "codigos",
    ".epub":  "libros epub",
    ".torrent": "torrents",
    ".jar": "mods",
    ".srt": "subtitulos",
    ".json": "modelos",
    ".bbmodel": "modelos 3D",
    ".webp": "imagenes"

}

carpeta_por_defecto = "otros"
carpeta_organizar_ruta = r"C:\carpeta alternativa\ordenarss"

# Lista todos los archivos y carpetas
archivos = os.listdir(carpeta_organizar_ruta)

for archivo in archivos:
    ruta_origen = os.path.join(carpeta_organizar_ruta, archivo)

    # Solo procesamos archivos (ignoramos carpetas)
    if os.path.isfile(ruta_origen):
        # Obtenemos la extensión (incluye el punto .)
        extension = os.path.splitext(archivo)[1].lower()  # .jpg → minúsculas

        # Buscamos la carpeta destino (con valor por defecto)
        nombre_carpeta = extensiones_dict.get(extension, carpeta_por_defecto)

        # Ruta completa de la carpeta destino
        ruta_destino_carpeta = os.path.join(carpeta_organizar_ruta, nombre_carpeta)

        # Creamos la carpeta si no existe
        if not os.path.exists(ruta_destino_carpeta):
            os.makedirs(ruta_destino_carpeta)

        # Ruta final del archivo
        ruta_destino = os.path.join(ruta_destino_carpeta, archivo)

        # Movemos el archivo
        try:
            shutil.move(ruta_origen, ruta_destino)
            print(f"Movido: {archivo} → {nombre_carpeta}")
        except Exception as e:
            print(f"Error al mover {archivo}: {e}")