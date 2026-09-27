import json

def generate_questions(world_name, topic, difficulty, num_questions, api_key=None):
    if not api_key:
        raise ValueError("API Key no configurada. Usa el banco de preguntas manual.")
    
    # Aquí iría la llamada real a OpenAI (ej. client.chat.completions.create)
    # Retornamos un JSON simulado estructurado como lo haría la IA validada.
    # EN PRODUCCIÓN: Reemplazar con el prompt estricto hacia el LLM.
    raise NotImplementedError("Integración con LLM requiere clave API real. Configura el .env")

def validate_ai_output(generated_json):
    try:
        data = json.loads(generated_json)
        for q in data:
            if q['correct_answer'] not in q['options']:
                return False
        return True
    except:
        return False
