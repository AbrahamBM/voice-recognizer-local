"""
Main entry point for the voice recognizer system.
Connects all modules: audio → text → intent → action → speech
"""
import sys
import os
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent))

from asr.vosk_asr import VoskASR
from nlu.matcher import match_intent
from executor.actions import execute
from tts.tts_engine import TTSEngine
from utils.audio import check_microphone


class VoiceRecognizer:
    """Main voice recognition system."""
    
    def __init__(self, model_path: str = "../models"):
        """
        Initialize voice recognizer system.
        
        Args:
            model_path: Path to Vosk model
        """
        print("🎙️  Initializing Voice Recognizer...")
        
        # Initialize components
        self.asr = VoskASR(model_path=model_path)
        self.tts = TTSEngine(language='spanish')
        
        # Check microphone
        if not check_microphone():
            print("⚠️  Warning: Microphone not detected")
        
        print("✅ Voice Recognizer ready!")
    
    def process_command(self, duration: float = 3.0, log_file: str = None) -> bool:
        """
        Process a voice command.
        
        Args:
            duration: Recording duration in seconds
            log_file: Optional log file path
            
        Returns:
            True if successful, False otherwise
        """
        # 1. Recognize speech
        text = self.asr.recognize_from_mic(duration=duration)
        
        if not text:
            return False
        
        # Log transcription
        if log_file:
            self._log_transcription(text, log_file)
        
        # 2. Match intent
        intent_data = match_intent(text)
        print(f"📋 Intent: {intent_data['intent']} (confidence: {intent_data['confidence']})")
        
        # 3. Execute action
        response = execute(intent_data)
        print(f"💬 Response: {response}")
        
        # 4. Speak response
        self.tts.speak(response)
        
        return True
    
    def process_text(self, text: str) -> str:
        """
        Process text input directly (for testing).
        
        Args:
            text: Input text
            
        Returns:
            Response text
        """
        print(f"📝 Processing text: {text}")
        
        # Match intent
        intent_data = match_intent(text)
        print(f"📋 Intent: {intent_data['intent']}")
        
        # Execute action
        response = execute(intent_data)
        print(f"💬 Response: {response}")
        
        return response
    
    def _log_transcription(self, text: str, log_file: str):
        """
        Log transcription to file.
        
        Args:
            text: Transcription text
            log_file: Log file path
        """
        try:
            with open(log_file, 'a', encoding='utf-8') as f:
                from datetime import datetime
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                f.write(f"{timestamp} | {text}\n")
        except Exception as e:
            print(f"Warning: Could not write to log file: {e}")
    
    def run_interactive(self, log_file: str = None):
        """
        Run in interactive mode (process commands until user exits).
        
        Args:
            log_file: Optional log file path
        """
        print("\n🎙️  Voice Recognizer - Interactive Mode")
        print("=" * 50)
        print("Commands:")
        print("  - Say 'hola' or 'saludos' for greeting")
        print("  - Ask 'qué hora es' for current time")
        print("  - Say 'enciende la luz' to turn on light")
        print("  - Say 'apaga la luz' to turn off light")
        print("  - Type 'exit' or press Ctrl+C to quit")
        print("=" * 50)
        
        try:
            while True:
                user_input = input("\n🎤 Press Enter to start recording (or 'exit' to quit): ")
                
                if user_input.lower() in ['exit', 'quit', 'q']:
                    print("👋 Goodbye!")
                    break
                
                success = self.process_command(duration=3.0, log_file=log_file)
                
                if not success:
                    print("⚠️  No speech detected. Try again.")
        
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
        except Exception as e:
            print(f"\n❌ Error: {e}")


def main():
    """Main entry point."""
    print("Voice Recognizer Local - Offline Speech Recognition")
    print("=" * 60)
    
    # Create logs directory if it doesn't exist
    os.makedirs("logs", exist_ok=True)
    log_file = "logs/transcriptions.log"
    
    # Initialize and run
    recognizer = VoiceRecognizer(model_path="../models")
    recognizer.run_interactive(log_file=log_file)


if __name__ == "__main__":
    main()

