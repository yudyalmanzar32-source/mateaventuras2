# MateAventuras 🚀🔢
¡Juega, descubre y conquista retos matemáticos!

MateAventuras es una aplicación web gamificada para estudiantes de primer grado de primaria. Permite a los niños aprender matemáticas mediante misiones en distintos mundos, y ofrece a los docentes un panel de control avanzado con estadísticas e interacción educativa.

## ✍️ Autora
- **Yudelka Almanzar Rivera**

## 🌐 Despliegue en GitHub Pages (Juego Web Standalone)
El proyecto está optimizado para funcionar directamente en **GitHub Pages** con todos los mundos, niveles, sonidos Web Audio, animaciones de confetti e insignias sin necesidad de un servidor Python.

### Pasos para Activar GitHub Pages en GitHub:
1. Sube este repositorio a tu cuenta de GitHub (`git push origin main`).
2. Ve a la pestaña **Settings** (Configuración) de tu repositorio en GitHub.
3. En el menú lateral izquierdo, haz clic en **Pages**.
4. En **Build and deployment** -> **Source**, selecciona **GitHub Actions** (o `Deploy from a branch` seleccionando la rama `main` y `/ (root)`).
5. Guarda los cambios. ¡En unos segundos tu sitio estará publicado y visible para todos tus estudiantes!

## 🛠️ Ejecución Local con Streamlit (Modo Servidor Python)
1. Clonar o descomprimir el repositorio.
2. Crear un entorno virtual e instalar dependencias:
   `pip install -r requirements.txt`
3. Renombrar `.env.example` a `.env` y colocar tu clave de OpenAI (opcional para IA).
4. Inicializar la base de datos y ejecutar la aplicación:
   `streamlit run app.py`

## 🧪 Pruebas
Ejecuta las pruebas automatizadas con: `pytest tests/`
