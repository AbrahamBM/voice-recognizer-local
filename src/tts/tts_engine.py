"""
Text-to-Speech module using pyttsx3 for offline TTS.
"""
import pyttsx3
from typing import Optional


class TTSEngine:
    """Offline TTS engine using pyttsx3."""
    
    def __init__(self, language: str = 'spanish'):
        """
        Initialize TTS engine.
        
        Args:
            language: Language code ('spanish' or 'english')
        """
        self.language = language
        self.engine = None
        
        try:
            self.engine = pyttsx3.init()
            
            # Configure voice
            voices = self.engine.getProperty('voices')
            
            # Set language
            if language == 'spanish':
                # Try to find Spanish voice
                for voice in voices:
                    if 'spanish' in voice.name.lower() or 'es' in voice.id.lower():
                        self.engine.setProperty('voice', voice.id)
                        break
            elif language == 'english':
                # Use default English voice
                if voices:
                    self.engine.setProperty('voice', voices[0].id)
            
            # Set properties
            self.engine.setProperty('rate', 150)  # Speed
            self.engine.setProperty('volume', 0.9)  # Volume
            
        except Exception as e:
            print(f"Warning: Could not initialize TTS engine: {e}")
            self.engine = None
    
    def speak(self, text: str) -> bool:
        """
        Convert text to speech and speak it.
        
        Args:
            text: Text to speak
            
        Returns:
            True if successful, False otherwise
        """
        if self.engine is None:
            print(f"[TTS]: {text}")
            return False
        
        try:
            print(f"🔊 Speaking: {text}")
            self.engine.say(text)
            self.engine.runAndWait()
            return True
        except Exception as e:
            print(f"Error during TTS: {e}")
            return False
    
    def save_to_file(self, text: str, filename: str) -> bool:
        """
        Save speech to audio file.
        
        Args:
            text: Text to speak
            filename: Output filename
            
        Returns:
            True if successful, False otherwise
        """
        if self.engine is None:
            return False
        
        try:
            self.engine.save_to_file(text, filename)
            self.engine.runAndWait()
            print(f"Audio saved to {filename}")
            return True
        except Exception as e:
            print(f"Error saving audio: {e}")
            return False


def speak(text: str, language: str = 'spanish') -> bool:
    """
    Convenience function to speak text.
    
    Args:
        text: Text to speak
        language: Language code
        
    Returns:
        True if successful, False otherwise
    """
    tts = TTSEngine(language=language)
    return tts.speak(text)

