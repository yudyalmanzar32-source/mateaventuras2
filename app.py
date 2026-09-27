import streamlit as st
import os
from dotenv import load_dotenv
from database.schema import init_db
from database.connection import get_db
from services.progress_service import log_attempt, get_student_stats
import json

load_dotenv()

st.set_page_config(page_title="MateAventuras 3D RA", page_icon="assets/ar_star_badge.jpg", layout="wide")

# Inicialización de DB
init_db()

# CSS Personalizado Infantil (Especial para niños de 5 años: Colores Dulces, Redondeados y Alegres)
st.markdown('''
<style>
    @import url('https://fonts.googleapis.com/css2?family=Fredoka:wght@400;600;700;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Fredoka', 'Comic Sans MS', sans-serif;
    }
    
    .stApp { 
        background: linear-gradient(135deg, #FEF9C3 0%, #E0F2FE 50%, #FCE7F3 100%); 
        color: #0F172A;
    }
    
    /* Animaciones CSS */
    @keyframes bounceQuestion {
        0% { transform: scale(0.96); opacity: 0; }
        60% { transform: scale(1.01); opacity: 1; }
        100% { transform: scale(1); opacity: 1; }
    }
    
    @keyframes floatImage {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-6px); }
        100% { transform: translateY(0px); }
    }

    h1 { 
        color: #FF4757 !important; 
        font-weight: 800;
        text-align: center;
        text-shadow: 2px 2px 0px #FFFFFF, 4px 4px 0px rgba(255, 71, 87, 0.15);
        font-size: 2.2rem !important;
        margin-bottom: 0.2rem !important;
    }
    
    h2 { 
        color: #0284C7 !important; 
        text-align: center;
        font-weight: 700;
        font-size: 1.5rem !important;
    }
    
    h3 {
        font-size: 1.25rem !important;
        color: #0F172A !important;
    }
    
    /* Banner de Pregunta estilo Caramelo */
    .question-card-container {
        background: #FFFFFF;
        border: 4px solid #38BDF8;
        border-radius: 24px;
        padding: 22px;
        box-shadow: 0 10px 25px rgba(56, 189, 248, 0.2);
        animation: bounceQuestion 0.4s ease-out;
    }

    .question-banner {
        background: linear-gradient(135deg, #FFFBEB 0%, #FEF08A 100%);
        border: 3px solid #F59E0B;
        border-radius: 20px;
        padding: 18px;
        margin-bottom: 18px;
        box-shadow: 0 6px 18px rgba(245, 158, 11, 0.18);
        text-align: center;
    }
    
    .question-banner h2 {
        color: #D97706 !important;
        font-size: 1.4rem !important;
        font-weight: 800;
        margin: 0 0 8px 0;
    }
    
    .question-banner p {
        color: #1E293B !important;
        font-size: 1.35rem !important;
        font-weight: 700 !important;
        line-height: 1.4 !important;
        margin: 0;
    }

    .kid-card {
        background: #FFFFFF;
        border: 4px solid #38BDF8;
        border-radius: 22px;
        padding: 16px;
        text-align: center;
        box-shadow: 0 8px 20px rgba(56, 189, 248, 0.2);
        transition: transform 0.2s ease, border-color 0.2s ease;
    }
    
    .kid-card:hover {
        transform: translateY(-5px);
        border-color: #FF4757;
    }

    .level-grid-container {
        background: #FFFFFF;
        border: 3px solid #F472B6;
        border-radius: 20px;
        padding: 14px 18px;
        margin-bottom: 16px;
        box-shadow: 0 8px 20px rgba(244, 114, 182, 0.15);
    }
    
    .ar-badge-kid {
        background: #FEF08A;
        border: 3px solid #EAB308;
        border-radius: 18px;
        padding: 8px 14px;
        color: #854D0E;
        font-weight: bold;
        font-size: 1.05rem;
        text-align: center;
        box-shadow: 0 4px 10px rgba(234, 179, 8, 0.2);
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 6px;
    }
    
    .camera-frame {
        background: #FFFFFF;
        border: 4px dashed #C084FC;
        border-radius: 24px;
        padding: 18px;
        height: 100%;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        align-items: center;
        box-shadow: 0 10px 25px rgba(192, 132, 252, 0.2);
    }
    
    .camera-frame img {
        animation: floatImage 4s infinite ease-in-out;
        border-radius: 18px;
        max-height: 380px;
        object-fit: contain;
    }
    
    /* Botones Divertidos Bubbly */
    div.stButton > button:first-child { 
        background: linear-gradient(135deg, #FF6B81 0%, #FF4757 100%);
        color: #FFFFFF; 
        border-radius: 20px; 
        font-weight: 800; 
        border: 3px solid #FFFFFF; 
        height: 3.2em; 
        font-size: 16px;
        box-shadow: 0 6px 16px rgba(255, 71, 87, 0.35);
        cursor: pointer;
    }
    
    div.stButton > button:first-child:hover { 
        background: linear-gradient(135deg, #FF4757 0%, #ED4C67 100%);
        transform: scale(1.03);
    }

    /* Opciones de Radio Súper Legibles */
    div[class*="stRadio"] label p {
        font-size: 1.35rem !important;
        font-weight: 800 !important;
        color: #0F172A !important;
        background: #F8FAFC;
        padding: 12px 24px;
        border-radius: 18px;
        border: 3px solid #CBD5E1;
        margin: 6px 0;
        display: inline-block;
        box-shadow: 0 4px 10px rgba(0,0,0,0.04);
        transition: all 0.2s ease;
    }
    
    div[class*="stRadio"] label:hover p {
        border-color: #FF4757;
        background: #FFF5F5;
        transform: translateX(4px);
    }
</style>
''', unsafe_allow_html=True)

# Map Image Assets
AR_IMAGES = {
    1: "assets/bosque_numerico_ar.jpg",
    2: "assets/jungla_operaciones_ar.jpg",
    3: "assets/castillo_geometrico_ar.jpg",
    4: "assets/isla_problemas_ar.jpg"
}

# Fun Component to Play Automatic Procedural Web Audio Music for each Map World
def render_map_music(world_id):
    music_info = {
        1: ("Bosque Numérico (Campanas Mágicas)", "sine", 300),
        2: ("Jungla de las Operaciones (Marimba Tropical)", "triangle", 260),
        3: ("Castillo Geométrico (Arpa Cristalina)", "sine", 350),
        4: ("Isla de los Problemas (Acordeón Pirata)", "sawtooth", 280)
    }
    
    title, instrument, tempo = music_info.get(world_id, ("Música RA", "sine", 300))
    
    html_code = f"""
    <div style="background: #FFFFFF; border: 3px solid #38BDF8; border-radius: 16px; padding: 8px 16px; display: flex; align-items: center; justify-content: space-between; margin: 4px 0 12px 0; box-shadow: 0 4px 12px rgba(56,189,248,0.18);">
        <span style="font-family: 'Fredoka', sans-serif; font-weight: bold; font-size: 1.05rem; color: #0F172A;">
            🎶 Música de la Aventura: <strong>{title}</strong>
        </span>
        <button id="musicBtn" onclick="toggleMusic()" style="background: linear-gradient(135deg, #10B981, #06B6D4); color: white; border: none; border-radius: 12px; padding: 6px 14px; font-weight: bold; cursor: pointer; font-size: 0.95rem; box-shadow: 0 2px 8px rgba(16,185,129,0.3);">
            Pausar / Reproducir
        </button>
    </div>

    <script>
    let audioCtx = null;
    let isPlaying = false;
    let intervalId = null;

    const themes = {{
        1: [261.63, 329.63, 392.00, 523.25, 659.25, 523.25, 392.00, 329.63], // Forest Chimes
        2: [196.00, 246.94, 293.66, 349.23, 392.00, 440.00, 349.23, 293.66], // Jungle Marimba
        3: [293.66, 369.99, 440.00, 554.37, 659.25, 739.99, 659.25, 554.37], // Crystal Castle Harp
        4: [220.00, 277.18, 329.63, 440.00, 392.00, 329.63, 277.18, 220.00]  // Pirate Accordion
    }};

    const notes = themes[{world_id}] || themes[1];
    let noteIdx = 0;

    function playNote(freq) {{
        if (!audioCtx) return;
        const osc = audioCtx.createOscillator();
        const gain = audioCtx.createGain();
        
        osc.type = "{instrument}";
        osc.frequency.setValueAtTime(freq, audioCtx.currentTime);
        
        gain.gain.setValueAtTime(0.1, audioCtx.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + 0.45);
        
        osc.connect(gain);
        gain.connect(audioCtx.destination);
        
        osc.start();
        osc.stop(audioCtx.currentTime + 0.45);
    }}

    function startMusic() {{
        if (!isPlaying) {{
            if (!audioCtx) {{
                const AudioContext = window.AudioContext || window.webkitAudioContext;
                audioCtx = new AudioContext();
            }}
            if (audioCtx.state === 'suspended') {{
                audioCtx.resume();
            }}
            isPlaying = true;
            const btn = document.getElementById('musicBtn');
            if (btn) {{
                btn.innerHTML = "Pausar Música";
                btn.style.background = "linear-gradient(135deg, #EF4444, #F59E0B)";
            }}
            intervalId = setInterval(() => {{
                playNote(notes[noteIdx]);
                noteIdx = (noteIdx + 1) % notes.length;
            }}, {tempo});
        }}
    }}

    function toggleMusic() {{
        const btn = document.getElementById('musicBtn');
        if (!isPlaying) {{
            startMusic();
        }} else {{
            isPlaying = false;
            btn.innerHTML = "Reproducir Música";
            btn.style.background = "linear-gradient(135deg, #10B981, #06B6D4)";
            if (intervalId) clearInterval(intervalId);
        }}
    }}

    // Reproducción automática al ingresar al mapa
    setTimeout(startMusic, 200);
    document.addEventListener('click', startMusic, {{ once: true }});
    </script>
    """
    st.components.v1.html(html_code, height=55)

# Sound Component: Royal Trumpets Fanfare & Soft Crowd Applause Synthesizer (Zero Fireworks Noise)
def render_trumpet_applause_sound():
    html_code = """
    <script>
    function playTrumpetsAndApplause() {
        try {
            const AudioContext = window.AudioContext || window.webkitAudioContext;
            const ctx = new AudioContext();
            if (ctx.state === 'suspended') {
                ctx.resume();
            }

            // 1. Triumphant Royal Trumpet Fanfare (Warm Sawtooth Brass Timbre)
            const notes = [261.63, 329.63, 392.00, 523.25]; // C4, E4, G4, C5
            const times = [0, 0.14, 0.28, 0.42];
            const durations = [0.14, 0.14, 0.14, 0.75];

            notes.forEach((freq, idx) => {
                const osc = ctx.createOscillator();
                const gain = ctx.createGain();
                
                osc.type = 'sawtooth';
                osc.frequency.setValueAtTime(freq, ctx.currentTime + times[idx]);

                gain.gain.setValueAtTime(0.2, ctx.currentTime + times[idx]);
                gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + times[idx] + durations[idx]);

                osc.connect(gain);
                gain.connect(ctx.destination);

                osc.start(ctx.currentTime + times[idx]);
                osc.stop(ctx.currentTime + times[idx] + durations[idx]);
            });

            // 2. Crowd Clapping & Applause (Soft bandpass clapping tones, zero popping/fireworks noise)
            setTimeout(() => {
                for (let i = 0; i < 28; i++) {
                    const delay = Math.random() * 1.3;
                    const osc = ctx.createOscillator();
                    const gain = ctx.createGain();
                    const filter = ctx.createBiquadFilter();

                    filter.type = 'bandpass';
                    filter.frequency.value = 850 + Math.random() * 500;

                    osc.type = 'triangle';
                    osc.frequency.setValueAtTime(160 + Math.random() * 100, ctx.currentTime + delay);

                    gain.gain.setValueAtTime(0.1, ctx.currentTime + delay);
                    gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + delay + 0.05);

                    osc.connect(filter);
                    filter.connect(gain);
                    gain.connect(ctx.destination);

                    osc.start(ctx.currentTime + delay);
                    osc.stop(ctx.currentTime + delay + 0.05);
                }
            }, 380);

        } catch(e) {
            console.log("Audio error:", e);
        }
    }
    setTimeout(playTrumpetsAndApplause, 80);
    </script>
    """
    st.components.v1.html(html_code, height=0)

# Session State Initializations
if 'current_world' not in st.session_state: st.session_state.current_world = None
if 'current_level_num' not in st.session_state: st.session_state.current_level_num = 1

# Header Principal con Insignia RA
header_col1, header_col2, header_col3 = st.columns([1, 4, 1])
with header_col2:
    st.markdown("<h1>MATEAVENTURAS - REALIDAD AUMENTADA</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; font-size: 1.15rem; margin-bottom: 8px;'>Explora mundos 3D y supera 10 niveles por aventura</h3>", unsafe_allow_html=True)

conn = get_db()
stats = get_student_stats()

col_m1, col_m2, col_m3 = st.columns(3)

with col_m1:
    if os.path.exists("assets/ar_star_badge.jpg"):
        st.image("assets/ar_star_badge.jpg", width=55)
    st.metric("Estrellas RA Conquistadas", stats['correct'])

with col_m2:
    if os.path.exists("assets/ar_victory_badge.jpg"):
        st.image("assets/ar_victory_badge.jpg", width=55)
    st.metric("Misiones Completadas", stats['total'])

with col_m3:
    st.markdown("""
        <div class='ar-badge-kid'>
            <strong>VISOR CÁMARA 3D: ACTIVO</strong>
        </div>
    """, unsafe_allow_html=True)

st.markdown("---")

if st.session_state.current_world is None:
    st.subheader("MAPAS DE AVENTURA 3D")
    worlds = conn.execute("SELECT * FROM worlds WHERE active = 1 ORDER BY order_index").fetchall()
    
    cols = st.columns(4)
    for i, w in enumerate(worlds):
        w_id = w['id']
        img_path = AR_IMAGES.get(w_id, "assets/bosque_numerico_ar.jpg")
        with cols[i % 4]:
            st.markdown(f"<div class='kid-card'>", unsafe_allow_html=True)
            if os.path.exists(img_path):
                st.image(img_path, use_container_width=True)
            st.markdown(f"### {w['name']}")
            st.caption(f"{w['description']} • **10 Niveles**")
            if st.button(f"JUGAR MAPA (10 NIVELES)", key=f"w_{w_id}"):
                st.session_state.current_world = w_id
                st.session_state.current_level_num = 1
                st.rerun()
            st.markdown("</div>", unsafe_allow_html=True)
else:
    # Modo de Juego por Mundo y 10 Niveles
    w_id = st.session_state.current_world
    world = conn.execute("SELECT * FROM worlds WHERE id = ?", (w_id,)).fetchone()
    img_path = AR_IMAGES.get(w_id, "assets/bosque_numerico_ar.jpg")
    
    # Reproductor de Música del Mapa (Auto-activado)
    render_map_music(w_id)
    
    top_nav_c1, top_nav_c2 = st.columns([2, 5])
    with top_nav_c1:
        if st.button("⬅️ VOLVER A LOS MAPAS"):
            st.session_state.current_world = None
            st.rerun()
    with top_nav_c2:
        st.markdown(f"<h2 style='text-align: left; margin: 0; padding-top: 4px;'>{world['name']}</h2>", unsafe_allow_html=True)

    # MAPA DE BOTONES DE 10 NIVELES (5x2)
    st.markdown("<div class='level-grid-container'>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; margin-bottom: 10px; color: #D97706 !important;'>MAPA DE NIVELES (SELECCIONA TU NIVEL):</h3>", unsafe_allow_html=True)
    
    # Fila 1: Niveles 1 al 5
    grid_cols_1 = st.columns(5)
    for lvl in range(1, 6):
        is_active = (lvl == st.session_state.current_level_num)
        lbl = f"⭐ NIVEL {lvl}" if is_active else f"NIVEL {lvl}"
        with grid_cols_1[lvl - 1]:
            if st.button(lbl, key=f"btn_lvl_{lvl}"):
                st.session_state.current_level_num = lvl
                st.rerun()
                
    # Fila 2: Niveles 6 al 10
    grid_cols_2 = st.columns(5)
    for lvl in range(6, 11):
        is_active = (lvl == st.session_state.current_level_num)
        lbl = f"⭐ NIVEL {lvl}" if is_active else f"NIVEL {lvl}"
        with grid_cols_2[lvl - 6]:
            if st.button(lbl, key=f"btn_lvl_{lvl}"):
                st.session_state.current_level_num = lvl
                st.rerun()

    lvl_num = st.session_state.current_level_num
    st.progress(lvl_num / 10.0, text=f"Progreso en {world['name']}: Nivel {lvl_num} de 10")
    
    if lvl_num <= 3:
        st.info(f"**NIVEL {lvl_num}: PRINCIPIANTE** - ¡Ideal para aprender!")
    elif lvl_num <= 7:
        st.warning(f"**NIVEL {lvl_num}: AVANZADO** - ¡Retos interesantes!")
    elif lvl_num <= 9:
        st.error(f"**NIVEL {lvl_num}: EXPERTO** - ¡Mentes brillantes!")
    else:
        st.success(f"**NIVEL 10: ¡DESAFÍO FINAL!** - ¡Conquista el mundo!")
        
    st.markdown("</div>", unsafe_allow_html=True)

    # Distribución Equilibrada en Pantalla (Cámara 3D + Preguntas perfectamente balanceadas)
    col_left, col_right = st.columns([1, 1], gap="medium")
    
    with col_left:
        st.markdown("<div class='camera-frame'>", unsafe_allow_html=True)
        st.markdown("<div style='text-align: center; font-weight: bold; color: #A855F7; margin-bottom: 8px; font-size: 1.1rem;'>📸 VISOR MÁGICO 3D - ESCANEO RA</div>", unsafe_allow_html=True)
        if os.path.exists(img_path):
            st.image(img_path, caption=f"Imagen 3D de {world['name']}", use_container_width=True)
        st.markdown("<div style='text-align: center; font-weight: bold; color: #0284C7; margin-top: 8px; background: #E0F2FE; border-radius: 12px; padding: 6px;'>🔍 Observa los detalles para responder el reto</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with col_right:
        target_diff = f"Nivel {lvl_num}"
        q = conn.execute("""
            SELECT * FROM questions 
            WHERE world_id = ? AND difficulty = ? AND approved = 1 AND active = 1 
            LIMIT 1
        """, (w_id, target_diff)).fetchone()
        
        # Fallback si no hay nivel exacto
        if not q:
            q = conn.execute("SELECT * FROM questions WHERE world_id = ? AND approved = 1 AND active = 1 ORDER BY RANDOM() LIMIT 1", (w_id,)).fetchone()
            
        if q:
            st.markdown("<div class='question-card-container'>", unsafe_allow_html=True)
            st.markdown(f"""
                <div class='question-banner'>
                    <h2>🎯 RETO MÁGICO - {target_diff}</h2>
                    <p>{q['question_text']}</p>
                </div>
            """, unsafe_allow_html=True)
            
            options = json.loads(q['options_json'])
            
            with st.form("ar_answer_form"):
                st.markdown("<h3 style='font-size: 1.15rem; color: #0284C7;'>SELECCIONA TU RESPUESTA:</h3>", unsafe_allow_html=True)
                ans = st.radio("Opciones de respuesta", options, label_visibility="collapsed")
                submit = st.form_submit_button("✨ COMPROBAR MI RESPUESTA ✨")
                
                if submit:
                    is_correct = 1 if ans == q['correct_answer'] else 0
                    log_attempt(None, q['id'], ans, is_correct)
                    
                    if is_correct:
                        # Reproducir Sonido de Trompetas y Aplausos (Sin ruido de fuegos artificiales)
                        render_trumpet_applause_sound()
                        # Animación visual de Globos Flotantes Mantenida
                        st.balloons()
                        
                        st.markdown("""
                            <div style='background: #DCFCE7; border: 3px solid #22C55E; border-radius: 20px; padding: 16px; text-align: center; margin: 12px 0; box-shadow: 0 8px 20px rgba(34, 197, 94, 0.3);'>
                                <h2 style='color: #15803D !important; font-size: 1.7rem !important;'>🎺 ¡VICTORIA! ¡APLAUSOS Y TROMPETAS! 👏</h2>
                                <p style='font-size: 1.25rem; font-weight: bold; color: #166534;'>¡Superaste el reto y ganaste 1 estrella brillante!</p>
                            </div>
                        """, unsafe_allow_html=True)
                        
                        if os.path.exists("assets/ar_star_badge.jpg"):
                            st.image("assets/ar_star_badge.jpg", width=160)
                            
                        st.success(f"Explicación: {q['explanation']}")
                        
                        if lvl_num < 10:
                            if st.form_submit_button("⏩ AVANZAR AL SIGUIENTE NIVEL"):
                                st.session_state.current_level_num = lvl_num + 1
                                st.rerun()
                        else:
                            st.balloons()
                            if os.path.exists("assets/ar_victory_badge.jpg"):
                                st.image("assets/ar_victory_badge.jpg", width=250, caption="¡INSIGNIA DE CAMPEÓN ABSOLUTO!")
                    else:
                        st.markdown(f"""
                            <div style='background: #FEF2F2; border: 3px solid #EF4444; border-radius: 20px; padding: 14px; text-align: center; margin: 12px 0;'>
                                <h2 style='color: #B91C1C !important; font-size: 1.5rem !important;'>🎈 ¡Casi lo logras! 💪</h2>
                                <p style='font-size: 1.2rem; font-weight: bold; color: #991B1B;'>La respuesta correcta era: <strong>{q['correct_answer']}</strong></p>
                            </div>
                        """, unsafe_allow_html=True)
                        st.info(f"Explicación: {q['explanation']}. ¡Inténtalo de nuevo!")
            st.markdown("</div>", unsafe_allow_html=True)
        else:
            st.info("¡Pronto habrá más misiones en este nivel!")
        
conn.close()
