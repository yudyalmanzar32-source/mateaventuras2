# 🗺️ Índice General y Navegación del Repositorio - MateAventuras 🚀🔢

¡Bienvenido al mapa de navegación de **MateAventuras**! Este documento sirve como guía de arquitectura, directorio de módulos y referencia técnica para explorar el código fuente del proyecto.

---

## 👩‍💻 Autora y Créditos
- **Autora:** Yudelka Almanzar Rivera
- **Proyecto:** Aplicación Web Gamificada con Realidad Aumentada e Inteligencia Artificial para el Aprendizaje de Matemáticas en Educación Primaria (1er Grado).

---

## 📂 Mapa de Estructura del Proyecto

```
MateAventuras/
├── 📄 app.py                      # Punto de entrada principal (Interfaz Streamlit, Mundos 3D y Panel Docente)
├── 📄 README.md                   # Descripción general, requisitos e instalación rápida
├── 📄 INDEX.md                    # (Este archivo) Índice de navegación y arquitectura detallada
├── 📄 requirements.txt            # Dependencias del proyecto (Streamlit, Pandas, Plotly, etc.)
├── 📄 .env.example                # Plantilla de variables de entorno (OpenAI API Key)
├── 📄 mateaventuras.db            # Base de datos SQLite (almacenamiento local)
│
├── 📁 services/                   # Lógica de negocio y servicios
│   ├── 📄 ai_generator.py         # Generación de preguntas matemáticas asistida por IA
│   ├── 📄 auth_service.py         # Control de autenticación de usuarios y roles
│   ├── 📄 math_engine.py          # Motor matemático de validación y dificultad
│   └── 📄 progress_service.py     # Registro de progreso, racha de medallas y estadísticas
│
├── 📁 database/                   # Gestión y persistencia de datos
│   ├── 📄 connection.py           # Conexión centralizada a SQLite
│   └── 📄 schema.py               # Esquema de tablas de la base de datos e inicialización
│
├── 📁 assets/                     # Recursos visuales (Badges y Mundos de Realidad Aumentada 3D)
│   ├── 🖼️ ar_star_badge.jpg       # Insignia de Estrella Dorada
│   ├── 🖼️ ar_victory_badge.jpg    # Insignia de Victoria
│   ├── 🖼️ bosque_numerico_ar.jpg  # Escenario: Bosque Numérico
│   ├── 🖼️ castillo_geometrico_ar.jpg # Escenario: Castillo Geométrico
│   ├── 🖼️ isla_problemas_ar.jpg   # Escenario: Isla de los Problemas
│   └── 🖼️ jungla_operaciones_ar.jpg # Escenario: Jungla de Operaciones
│
└── 📁 tests/                      # Suite de pruebas automatizadas con Pytest
    ├── 📄 test_ai_validation.py   # Pruebas de integración para la generación por IA
    ├── 📄 test_auth.py            # Pruebas de autenticación y sesiones
    └── 📄 test_math.py            # Pruebas unitarias para el motor matemático
```

---

## 🔍 Guía Detallada de Componentes

### 1. Interfaz Principal ([app.py](file:///c:/Users/morel%20technology/Downloads/MateAventuras/app.py))
- **Estilos Adaptados:** CSS personalizado con tipografía alegre (`Fredoka`), gradientes pastel, animaciones de rebote y tarjetas interactivas diseñadas especialmente para niños pequeños.
- **Modos de Juego:**
  - 🌲 **Bosque Numérico:** Conteo y reconocimiento de cantidades.
  - 🦁 **Jungla de Operaciones:** Sumas y restas con elementos gráficos.
  - 🏰 **Castillo Geométrico:** Identificación de formas 2D y 3D.
  - 🏝️ **Isla de Problemas:** Desafíos lógicos y razonamiento matemático.
- **Panel del Docente:** Dashboard interactivo con gráficos Plotly para evaluar el rendimiento grupal, historial de intentos y generador de preguntas con IA.

---

### 2. Servicios Lógicos (`services/`)
- [ai_generator.py](file:///c:/Users/morel%20technology/Downloads/MateAventuras/services/ai_generator.py): Integración con API de Inteligencia Artificial para la creación contextualizada de ejercicios matemáticos según el nivel.
- [auth_service.py](file:///c:/Users/morel%20technology/Downloads/MateAventuras/services/auth_service.py): Manejo seguro de inicio de sesión, diferenciación de perfiles (Estudiante vs. Profesor).
- [math_engine.py](file:///c:/Users/morel%20technology/Downloads/MateAventuras/services/math_engine.py): Evaluación en tiempo real de respuestas y asignación de puntajes.
- [progress_service.py](file:///c:/Users/morel%20technology/Downloads/MateAventuras/services/progress_service.py): Auditoría de desempeño, cálculo de rachas de victorias y asignación de insignias.

---

### 3. Base de Datos (`database/`)
- [connection.py](file:///c:/Users/morel%20technology/Downloads/MateAventuras/database/connection.py): Provee la conexión SQLite idempotente.
- [schema.py](file:///c:/Users/morel%20technology/Downloads/MateAventuras/database/schema.py): Define las tablas principales:
  - `usuarios`: Datos y roles de usuarios.
  - `preguntas`: Banco de ejercicios por mundo.
  - `intentos`: Historial de respuestas y tiempos de resolución.
  - `insignias`: Logros desbloqueados por los estudiantes.

---

### 4. Recursos Visuales (`assets/`)
Contiene las imágenes utilizadas para simular experiencias de Realidad Aumentada (RA) y la entrega de medallas de reconocimiento a los estudiantes.

---

### 5. Pruebas Automáticas (`tests/`)
Para ejecutar la suite de calidad:
```bash
pytest tests/
```
- Cobertura de autenticación, respuestas matemáticas y respuestas del servicio IA.

---

## 🚀 Cómo Ejecutar la Aplicación

1. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```
2. **Iniciar servidor Streamlit:**
   ```bash
   streamlit run app.py
   ```
3. Abrir en el navegador: `http://localhost:8501`

---

*Última actualización de índice: Septiembre 2026*
