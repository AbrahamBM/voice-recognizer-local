"""
NLU (Natural Language Understanding) module.
Implements intent matching using rule-based approach.
"""
from typing import Dict, Any
import re


def match_intent(text: str) -> Dict[str, Any]:
    """
    Match intent from user text using rule-based NLU.
    
    Args:
        text: User input text
        
    Returns:
        Dictionary with 'intent', 'confidence', and 'raw_text'
    """
    if not text:
        return {
            'intent': 'unknown',
            'confidence': 0.0,
            'raw_text': text
        }
    
    text_lower = text.lower().strip()
    
    # Intent patterns
    saludo_patterns = [
        r'\b(hola|saludos|buenos días|buenas tardes|buenas noches|hi|hello|hey)\b',
        r'\b(cómo estás|qué tal|qué pasa)\b'
    ]
    
    hora_patterns = [
        r'\b(qué hora es|dime la hora|hora actual|time)\b',
        r'\b(dime la fecha|qué día es|fecha actual)\b'
    ]
    
    encender_luz_patterns = [
        r'\b(enciende|activa|prende|on)\s*(la\s*)?luz',
        r'\bturn\s*(on|up)\s*the\s*light',
        r'\bprender\s*(la\s*)?luz'
    ]
    
    apagar_luz_patterns = [
        r'\b(apaga|desactiva|apaga|off)\s*(la\s*)?luz',
        r'\bturn\s*off\s*the\s*light',
        r'\bapagar\s*(la\s*)?luz'
    ]
    
    # Check for matches
    for pattern in saludo_patterns:
        if re.search(pattern, text_lower):
            return {
                'intent': 'saludo',
                'confidence': 0.9,
                'raw_text': text
            }
    
    for pattern in hora_patterns:
        if re.search(pattern, text_lower):
            return {
                'intent': 'hora',
                'confidence': 0.9,
                'raw_text': text
            }
    
    for pattern in encender_luz_patterns:
        if re.search(pattern, text_lower):
            return {
                'intent': 'encender_luz',
                'confidence': 0.9,
                'raw_text': text
            }
    
    for pattern in apagar_luz_patterns:
        if re.search(pattern, text_lower):
            return {
                'intent': 'apagar_luz',
                'confidence': 0.9,
                'raw_text': text
            }
    
    # No match found
    return {
        'intent': 'unknown',
        'confidence': 0.0,
        'raw_text': text
    }


def extract_entities(text: str) -> Dict[str, Any]:
    """
    Extract entities from text (optional, for future enhancement).
    
    Args:
        text: User input text
        
    Returns:
        Dictionary with extracted entities
    """
    entities = {}
    
    # Could extract numbers, dates, locations, etc.
    # For now, just return empty dict
    
    return entities


def get_intent_description(intent: str) -> str:
    """
    Get description of intent.
    
    Args:
        intent: Intent name
        
    Returns:
        Description string
    """
    descriptions = {
        'saludo': 'Greeting/Hola',
        'hora': 'Time query/Qué hora es',
        'encender_luz': 'Turn on light/Encender luz',
        'apagar_luz': 'Turn off light/Apagar luz',
        'unknown': 'Unknown/Desconocido'
    }
    
    return descriptions.get(intent, 'Unknown')

