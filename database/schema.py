import sqlite3
import os

DB_PATH = "mateaventuras.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    
    # Students
    c.execute('''CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL,
        course TEXT NOT NULL, active INTEGER DEFAULT 1, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )''')
    
    # Teachers
    c.execute('''CREATE TABLE IF NOT EXISTS teachers (
        id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT UNIQUE NOT NULL,
        password_hash TEXT, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )''')
    
    # Worlds
    c.execute('''CREATE TABLE IF NOT EXISTS worlds (
        id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL,
        description TEXT, order_index INTEGER, active INTEGER DEFAULT 1
    )''')
    
    # Questions
    c.execute('''CREATE TABLE IF NOT EXISTS questions (
        id INTEGER PRIMARY KEY AUTOINCREMENT, world_id INTEGER, topic TEXT,
        difficulty TEXT, question_text TEXT, options_json TEXT, correct_answer TEXT,
        explanation TEXT, source TEXT, approved INTEGER DEFAULT 0, active INTEGER DEFAULT 1,
        FOREIGN KEY(world_id) REFERENCES worlds(id)
    )''')
    
    # Attempts
    c.execute('''CREATE TABLE IF NOT EXISTS attempts (
        id INTEGER PRIMARY KEY AUTOINCREMENT, student_id INTEGER, question_id INTEGER,
        selected_answer TEXT, is_correct INTEGER, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(student_id) REFERENCES students(id), FOREIGN KEY(question_id) REFERENCES questions(id)
    )''')
    
    # Seed Initial Teacher if empty
    c.execute("SELECT COUNT(*) FROM teachers")
    if c.fetchone()[0] == 0:
        c.execute("INSERT INTO teachers (username, password_hash) VALUES (?, ?)", ('maestra', ''))
                  
    # Seed Initial Worlds if empty
    c.execute("SELECT COUNT(*) FROM worlds")
    if c.fetchone()[0] == 0:
        worlds = [('Bosque Numérico', 'Aprende los números y cuenta objetos mágicos', 1),
                  ('Jungla de las Operaciones', 'Sumas y restas divertidas en la jungla', 2),
                  ('Castillo Geométrico', 'Figuras y patrones en el castillo', 3),
                  ('Isla de los Problemas', 'Resuelve divertidos problemas piratas', 4)]
        c.executemany("INSERT INTO worlds (name, description, order_index) VALUES (?, ?, ?)", worlds)

    # Seed Questions if empty or re-seeding 10 levels per world
    c.execute("DELETE FROM questions")
    
    questions = [
        # ==========================================
        # BOSQUE NUMÉRICO (world_id=1, Niveles 1-10)
        # ==========================================
        (1, "Conteo Básico", "Nivel 1", "En el bosque ves 2 mariposas azules y 1 amarilla. ¿Cuántas mariposas ves en total?", '["2", "3", "4", "5"]', "3", "¡Excelente! 2 + 1 = 3 mariposas.", "Sistema", 1, 1),
        (1, "Secuencia Numérica", "Nivel 2", "Encuentra el número que falta en la cuenta: 1, 2, 3, __, 5", '["3", "4", "5", "6"]', "4", "¡Súper bien! El número 4 va después del 3.", "Sistema", 1, 1),
        (1, "Suma de Objetos", "Nivel 3", "El duende del bosque tiene 6 hortalizas mágicas y encuentra 3 más. ¿Cuántas tiene ahora?", '["8", "9", "10", "11"]', "9", "¡Genial! 6 + 3 = 9 hortalizas.", "Sistema", 1, 1),
        (1, "Conteo de 2 en 2", "Nivel 4", "Cuenta de 2 en 2 en el bosque: 2, 4, 6, 8, __", '["9", "10", "11", "12"]', "10", "¡Correcto! Contando de 2 en 2 sigue el 10.", "Sistema", 1, 1),
        (1, "Comparar Números", "Nivel 5", "¿Qué número es MAYOR entre 8 y 5 en las flores brillantes?", '["5", "8", "Iguales", "Ninguno"]', "8", "¡Exacto! El 8 es más grande que el 5.", "Sistema", 1, 1),
        (1, "Conteo de 5 en 5", "Nivel 6", "Cuenta de 5 en 5: 5, 10, 15, __", '["16", "18", "20", "25"]', "20", "¡Increíble! 15 más 5 nos da 20.", "Sistema", 1, 1),
        (1, "Resta de Manzanas", "Nivel 7", "Un árbol del bosque tiene 10 manzanas. Se caen 4. ¿Cuántas quedan en el árbol?", '["5", "6", "7", "8"]', "6", "¡Muy bien! 10 - 4 = 6 manzanas.", "Sistema", 1, 1),
        (1, "Número Menor", "Nivel 8", "¿Cuál número es MENOR entre 12 y 9?", '["9", "12", "Iguales", "10"]', "9", "¡Fantástico! El 9 es menor que el 12.", "Sistema", 1, 1),
        (1, "Cuenta Regresiva", "Nivel 9", "Encuentra el número que falta hacia atrás: 10, 9, 8, 7, __, 5", '["4", "5", "6", "7"]', "6", "¡Bien hecho! 7 menos 1 es 6.", "Sistema", 1, 1),
        (1, "Gran Desafío del Bosque", "Nivel 10", "¡Desafío Final! En el bosque hay 7 conejitos, 3 ardillas y 2 pajaritos. ¿Cuántos animales hay en total?", '["10", "11", "12", "13"]', "12", "¡ERES UN MAESTRO DEL BOSQUE! 7 + 3 + 2 = 12 animales.", "Sistema", 1, 1),

        # ===============================================
        # JUNGLA DE LAS OPERACIONES (world_id=2, Niveles 1-10)
        # ===============================================
        (2, "Sumas Fáciles", "Nivel 1", "¿Cuánto es 3 + 2 en las frutas mágicas de la jungla?", '["4", "5", "6", "7"]', "5", "¡Muy bien! 3 + 2 = 5.", "Sistema", 1, 1),
        (2, "Restas Fáciles", "Nivel 2", "¿Cuánto es 7 - 3 en las piedras del río de la jungla?", '["3", "4", "5", "6"]', "4", "¡Exacto! 7 - 3 = 4.", "Sistema", 1, 1),
        (2, "Plátanos del Mono", "Nivel 3", "Un mono comió 4 plátanos por la mañana y 4 por la tarde. ¿Cuántos plátanos comió en total?", '["6", "7", "8", "9"]', "8", "¡Genial! 4 + 4 = 8 plátanos.", "Sistema", 1, 1),
        (2, "Suma con Tótem", "Nivel 4", "¿Cuánto es 6 + 5 en el tótem brillante de la jungla?", '["10", "11", "12", "13"]', "11", "¡Excelente! 6 + 5 = 11.", "Sistema", 1, 1),
        (2, "Lianas Cortadas", "Nivel 5", "Había 10 lianas en un árbol y se cortaron 4. ¿Cuántas lianas sanas quedan?", '["4", "5", "6", "7"]', "6", "¡Bien calculado! 10 - 4 = 6 lianas.", "Sistema", 1, 1),
        (2, "Flores Jungla", "Nivel 6", "¿Cuánto es 9 + 4 en las flores de la jungla?", '["11", "12", "13", "14"]', "13", "¡Fantástico! 9 + 4 = 13.", "Sistema", 1, 1),
        (2, "Portal Mágico", "Nivel 7", "¿Cuánto es 15 - 7 en el portal mágico?", '["7", "8", "9", "10"]', "8", "¡Muy bien! 15 - 7 = 8.", "Sistema", 1, 1),
        (2, "Cueva de Murciélagos", "Nivel 8", "En la cueva hay 8 murciélagos y entran 6 más. ¿Cuántos murciélagos hay ahora?", '["12", "13", "14", "15"]', "14", "¡Súper! 8 + 6 = 14 murciélagos.", "Sistema", 1, 1),
        (2, "Saltos del Jaguar", "Nivel 9", "Un jaguar da 18 saltos en total. Si ya dio 9 saltos, ¿cuántos le faltan?", '["8", "9", "10", "11"]', "9", "¡Correcto! 18 - 9 = 9 saltos.", "Sistema", 1, 1),
        (2, "Gran Desafío Jungla", "Nivel 10", "¡Desafío Final! Tienes 20 cocos. Regalas 5 a un tucán y 3 a un perezoso. ¿Cuántos cocos te quedan?", '["10", "11", "12", "13"]', "12", "¡ERES UN MAESTRO DE LA JUNGLA! 20 - 5 - 3 = 12 cocos.", "Sistema", 1, 1),

        # ==========================================
        # CASTILLO GEOMÉTRICO (world_id=3, Niveles 1-10)
        # ==========================================
        (3, "Lados del Cuadrado", "Nivel 1", "¿Cuántos lados tiene un cuadrado en las puertas del castillo?", '["3", "4", "5", "6"]', "4", "¡Correcto! El cuadrado tiene 4 lados iguales.", "Sistema", 1, 1),
        (3, "Forma Sin Esquinas", "Nivel 2", "¿Qué figura redonda no tiene ninguna esquina ni lado recto?", '["Cuadrado", "Triángulo", "Círculo", "Rectángulo"]', "Círculo", "¡Muy bien! El círculo es redondo y sin esquinas.", "Sistema", 1, 1),
        (3, "Esquinas del Triángulo", "Nivel 3", "¿Cuántas esquinas (vértices) tiene un triángulo brillante?", '["2", "3", "4", "5"]', "3", "¡Excelente! El triángulo tiene 3 esquinas.", "Sistema", 1, 1),
        (3, "Pelota 3D", "Nivel 4", "¿Qué cuerpo 3D parece una pelota de fútbol de cristal?", '["Cubo", "Esfera", "Cilindro", "Cono"]', "Esfera", "¡Genial! La esfera es redonda por todos lados.", "Sistema", 1, 1),
        (3, "Dado de Cristal", "Nivel 5", "¿Qué cuerpo 3D parece un dado de jugar?", '["Cubo", "Esfera", "Pirámide", "Cilindro"]', "Cubo", "¡Súper! El cubo tiene 6 caras cuadradas.", "Sistema", 1, 1),
        (3, "Lados del Rectángulo", "Nivel 6", "Un rectángulo tiene 4 lados. ¿Cuántos lados tienen 2 rectángulos en total?", '["6", "8", "10", "12"]', "8", "¡Bien hecho! 4 + 4 = 8 lados.", "Sistema", 1, 1),
        (3, "Tubo Mágico", "Nivel 7", "¿Qué cuerpo 3D parece una lata o tubo flotante?", '["Cono", "Esfera", "Cilindro", "Cubo"]', "Cilindro", "¡Correcto! El cilindro tiene dos bases circulares.", "Sistema", 1, 1),
        (3, "Patrón de Figuras", "Nivel 8", "Completa la serie: Triángulo, Círculo, Triángulo, Círculo, __", '["Triángulo", "Círculo", "Cuadrado", "Estrella"]', "Triángulo", "¡Perfecto! Sigue el triángulo en el patrón.", "Sistema", 1, 1),
        (3, "Tres Lados", "Nivel 9", "¿Qué figura tiene 3 lados y 3 esquinas?", '["Cuadrado", "Triángulo", "Círculo", "Rectángulo"]', "Triángulo", "¡Excelente! Es el triángulo.", "Sistema", 1, 1),
        (3, "Gran Desafío del Castillo", "Nivel 10", "¡Desafío Final! Un cubo tiene 6 caras. ¿Cuántas caras tienen 3 cubos juntos sin tocarse?", '["12", "16", "18", "24"]', "18", "¡ERES UN MAESTRO DEL CASTILLO! 6 x 3 = 18 caras en total.", "Sistema", 1, 1),

        # ==========================================
        # ISLA DE LOS PROBLEMAS (world_id=4, Niveles 1-10)
        # ==========================================
        (4, "Monedas del Pirata", "Nivel 1", "El pirata tenía 3 monedas y encontró 2 en la playa. ¿Cuántas monedas tiene?", '["4", "5", "6", "7"]', "5", "¡Tesoro encontrado! 3 + 2 = 5 monedas.", "Sistema", 1, 1),
        (4, "Loros del Barco", "Nivel 2", "En el barco había 6 loros y volaron 2. ¿Cuántos loros quedan en el barco?", '["3", "4", "5", "6"]', "4", "¡Bien calculado! 6 - 2 = 4 loros.", "Sistema", 1, 1),
        (4, "Caracoles Marinos", "Nivel 3", "Sofía junta 5 caracoles y Mateo junta 4 caracoles. ¿Cuántos juntaron en total?", '["7", "8", "9", "10"]', "9", "¡Genial! 5 + 4 = 9 caracoles.", "Sistema", 1, 1),
        (4, "Llaves del Cofre", "Nivel 4", "El cofre de la isla necesita 10 llaves. Ya tienes 6. ¿Cuántas llaves te faltan?", '["3", "4", "5", "6"]', "4", "¡Exacto! 10 - 6 = 4 llaves.", "Sistema", 1, 1),
        (4, "Navegación Pirata", "Nivel 5", "El barco navega 8 millas el lunes y 7 el martes. ¿Cuántas millas navegó en total?", '["13", "14", "15", "16"]', "15", "¡Súper! 8 + 7 = 15 millas.", "Sistema", 1, 1),
        (4, "Palmeras y Viento", "Nivel 6", "Hay 12 palmeras en la playa y el viento tira 3. ¿Cuántas palmeras quedan de pie?", '["8", "9", "10", "11"]', "9", "¡Muy bien! 12 - 3 = 9 palmeras.", "Sistema", 1, 1),
        (4, "Filas de Oro", "Nivel 7", "Un cofre tiene 2 filas de monedas de oro con 5 monedas en cada fila. ¿Cuántas hay?", '["8", "9", "10", "12"]', "10", "¡Fantástico! 5 + 5 = 10 monedas.", "Sistema", 1, 1),
        (4, "Peces Conchas", "Nivel 8", "Compraste 15 conchas en el mercado pirata y regalaste 6. ¿Cuántas te quedan?", '["8", "9", "10", "11"]', "9", "¡Excelente! 15 - 6 = 9 conchas.", "Sistema", 1, 1),
        (4, "Pasos del Mapa", "Nivel 9", "El mapa marca 14 pasos hacia el tesoro. Llevas 8 pasos. ¿Cuántos te faltan?", '["5", "6", "7", "8"]', "6", "¡Bien hecho! 14 - 8 = 6 pasos.", "Sistema", 1, 1),
        (4, "Gran Desafío de la Isla", "Nivel 10", "¡Desafío Final! Barbanegra tiene 15 rubíes. Regala 4 a su tripulación y halla 5 más. ¿Cuántos tiene?", '["14", "15", "16", "17"]', "16", "¡ERES EL REY PIRATA DE LAS MATES! (15 - 4) + 5 = 16 rubíes.", "Sistema", 1, 1)
    ]
    
    c.executemany("""INSERT INTO questions 
                     (world_id, topic, difficulty, question_text, options_json, correct_answer, explanation, source, approved, active) 
                     VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", questions)
    
    conn.commit()
    conn.close()
