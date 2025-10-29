"""
Actions module for executing intents.
Simulates actions like turning lights on/off, getting time, etc.
"""
from typing import Dict, Any
from datetime import datetime


def execute(intent_data: Dict[str, Any]) -> str:
    """
    Execute action based on intent.
    
    Args:
        intent_data: Dictionary with 'intent' and 'raw_text'
        
    Returns:
        Response text to be spoken
    """
    intent = intent_data.get('intent', 'unknown')
    
    if intent == 'saludo':
        return "¡Hola! ¿En qué puedo ayudarte?"
    
    elif intent == 'hora':
        now = datetime.now()
        hour = now.hour
        minute = now.minute
        return f"Son las {hour} con {minute} minutos"
    
    elif intent == 'encender_luz':
        # Simulate turning on light
        print("Light turned ON")
        return "Luz encendida"
    
    elif intent == 'apagar_luz':
        # Simulate turning off light
        print("Light turned OFF")
        return "Luz apagada"
    
    elif intent == 'unknown':
        raw_text = intent_data.get('raw_text', '')
        return f"No entiendo el comando: '{raw_text}'. Por favor, intenta de nuevo."
    
    else:
        return "Lo siento, no pude procesar tu solicitud."


def get_system_status() -> str:
    """
    Get system status information.
    
    Returns:
        Status message
    """
    return "Sistema funcionando correctamente"


def list_available_intents() -> list:
    """
    List all available intents.
    
    Returns:
        List of intent names
    """
    return ['saludo', 'hora', 'encender_luz', 'apagar_luz', 'unknown']
