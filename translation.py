class Translation(object):

    ERROR = "<b>ERROR :</b> {}"

    START_TEXT = """**👋🏻Hola {}**[,](https://i.imgur.com/lnD3SuK.jpg)\n
**Descarga videos de cualquier citio:**\n
➜__Google Drive__
➜__YouTube__
➜__Twitter__
➜__Instagram__
➜__Etc...__

**Para ayuda use /help**"""
    FORMAT_SELECTION = "Seleccione el formato deseado: <a href='{}'>el tamaño del archivo puede ser aproximado</a> \nSi desea configurar una miniatura personalizada, envíe una foto antes o rápidamente después de tocar cualquiera de los botones a continuación. Puede usar /deletethumbnail miniatura para eliminar la miniatura generada automáticamente."
    SET_CUSTOM_USERNAME_PASSWORD = """Si quieres descargar videos premium, proporcionar en el siguiente formato:
URL | filename | username | password"""
    DOWNLOAD_START = "📥Downloading..."
    UPLOAD_START = "📤Uploading..."
    RCHD_TG_API_LIMIT = "Descargado en {} segundos.\nTamaño de archivo detectado: {}\nLo siento. Pero no puedo cargar archivos de más de 2 GB debido a las limitaciones de la API de Telegram."
    AFTER_SUCCESSFUL_UPLOAD_MSG = "Gracias por usar X Upload\n\n<b>Join : @KeimaSenpai_oficial</b>"
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "Descargado en {} segundos.\nSubido en {} segundos."
    SAVED_CUSTOM_THUMB_NAIL = "Vídeo personalizado / file thumbnail salvado. Esta imagen se usará en el video. / file."
    DEL_ETED_CUSTOM_THUMB_NAIL = "✅ Miniatura personalizada borrada con éxito."
    CUSTOM_CAPTION_UL_FILE = "{}"
    NO_VOID_FORMAT_FOUND = "ERROR...\n<b>YouTubeDL</b> said: {}"
    HELP_USER = """<b>¿Cómo usarme? ¡Sigue estos pasos!</b>
    
➜ Enviar url (ejemplo.dominio/Archivo.mp4 | Nuevo nombre de archivo.mp4).\n
➜ Enviar imagen como miniatura personalizada (opcional).\n
➜ Select the button.3. Seleccione el botón.
   SVideo - Dar archivo como video con capturas de pantalla.
   DFile  - Dar archivo (video) como archivo con capturas de pantalla.
   Video  - Dar archivo como video sin capturas de pantalla.
   File   - Dar archivo sin capturas de pantalla.

<b>❑ Si el bot no respondió, comuníquese con <a href="tg://user?id=1618347551">Keima Senpai</a></b>"""
    REPLY_TO_MEDIA_ALBUM_TO_GEN_THUMB = "Responder /generatecustomthumbnail a un álbum multimedia, para generar una miniatura personalizada"
    ERR_ONLY_TWO_MEDIA_IN_ALBUM = """El álbum de medios debe contener solo dos fotos. Vuelva a enviar el álbum multimedia y vuelva a intentarlo o envíe solo dos fotos en un álbum."
Puedes usar el comando /rename después de recibir el archivo para cambiarle el nombre con compatibilidad con miniaturas personalizadas.
"""
    CANCEL_STR = "Process Cancelled"
    ZIP_UPLOADED_STR = "Subido {} archivos en {} segundos"
    SLOW_URL_DECED = "Vaya, esa parece ser una URL muy lenta. Ya que estabas jodiendo mi casa, no estoy de humor para descargar este archivo. Mientras tanto, ¿por qué no pruebas esto: ==> https://shrtz.me/PtsVnf6 y me consigues una URL rápida para que pueda subir a Telegram, sin que me ralentice para otros usuarios?"

    ERROR_YTDLP = "Informe este problema en https://yt-dl.org/bug. Asegúrese de estar utilizando la última versión; consulte https://yt-dl.org/update sobre cómo actualizar. Asegúrese de llamar a youtube-dl con la marca --verbose e incluir su salida completa."
