# MateAventuras 🚀🔢
¡Juega, descubre y conquista retos matemáticos!

MateAventuras es una aplicación web gamificada diseñada para estudiantes de primer grado de primaria. Permite a los niños aprender matemáticas mediante misiones en distintos mundos interactivos, ofreciendo además un panel de control avanzado para docentes.

---

## 🔗 Enlaces Oficiales del Proyecto

- 🌐 **Landing Page & Juego Web (GitHub Pages):** [https://yudyalmanzar32-source.github.io/mateaventuras2/](https://yudyalmanzar32-source.github.io/mateaventuras2/)
- 🚀 **Aplicación Streamlit:** [https://mateaventuras.streamlit.app/](https://mateaventuras.streamlit.app/)
- 📦 **Repositorio en GitHub:** [https://github.com/yudyalmanzar32-source/mateaventuras2.git](https://github.com/yudyalmanzar32-source/mateaventuras2.git)

---

## ✍️ Autora
- **Yudelka Almanzar Rivera**

---

## 💡 Sustento Pedagógico y Justificación Educativa

### ¿Por qué desarrollar un juego de matemáticas para 1er Grado de Primaria?

El primer grado de educación primaria (niños entre 5 y 7 años) representa una etapa crítica en el desarrollo cognoscitivo del ser humano:

1. **Transición del Pensamiento Concreto al Pensamiento Simbólico:**
   De acuerdo con la teoría del desarrollo cognitivo de Jean Piaget, los niños en esta etapa se encuentran saliendo del estadio preoperacional e ingresando a las operaciones concretas. Requieren apoyos visuales, manipulating objetos y experiencias multisensoriales para comprender conceptos matemáticos abstractos como la adición, la sustracción y el conteo posicional.

2. **Prevención Temprana de la Ansiedad Matemática:**
   El aprendizaje abstracto tradicional basado únicamente en fichas impresas y repetición mecánica puede generar frustración o fobia matemática a una edad muy temprana. **MateAventuras** transforma el aprendizaje en una aventura gráfica donde el error se percibe como una oportunidad natural de aprendizaje, motivando al niño mediante dinámicas de juego (estrellas, insignias y música festiva).

3. **Gamificación y Motivación Intrínseca:**
   Al dividir el plan de estudio de primer grado en 4 mundos temáticos (*Bosque Numérico*, *Jungla de Operaciones*, *Castillo Geométrico* e *Isla de los Problemas*) y 10 niveles progresivos por mundo, el niño experimenta una sensación constante de logro y progreso individual.

4. **Inclusión Tecnológica y Acompañamiento Docente:**
   La integración de elementos en 3D/Realidad Aumentada estimula la memoria espacial y la atención sostenida. Asimismo, el panel docente proporciona visibilidad inmediata sobre la tasa de aciertos y el avance de los estudiantes, facilitando la intervención pedagógica oportuna.

---

## 🌐 Despliegue en GitHub Pages (Juego Web Standalone)
El proyecto está optimizado para funcionar directamente en **GitHub Pages** con todos los mundos, niveles, sonidos Web Audio, animaciones de confetti e insignias sin necesidad de un servidor Python activo.

### Pasos para Activar GitHub Pages en GitHub:
1. Sube este repositorio a tu cuenta de GitHub (`git push origin main`).
2. Ve a la pestaña **Settings** (Configuración) de tu repositorio en GitHub.
3. En el menú lateral izquierdo, haz clic en **Pages**.
4. En **Build and deployment** -> **Source**, selecciona **GitHub Actions** (o `Deploy from a branch` seleccionando la rama `main` y `/ (root)`).
5. Guarda los cambios. ¡En unos segundos tu sitio estará publicado y accesible para toda la comunidad educativa!

---

## 🛠️ Ejecución Local con Streamlit (Modo Servidor Python)
1. Clonar o descomprimir el repositorio:
   `git clone https://github.com/yudyalmanzar32-source/mateaventuras2.git`
2. Crear un entorno virtual e instalar dependencias:
   `pip install -r requirements.txt`
3. Renombrar `.env.example` a `.env` y colocar tu clave de OpenAI (opcional para IA).
4. Inicializar la base de datos y ejecutar la aplicación:
   `streamlit run app.py`

---

## 🧪 Pruebas Automatizadas
Ejecuta la suite de pruebas unitarias con:
`python -m pytest tests/`
