"""
Vosk ASR (Automatic Speech Recognition) module.
Provides offline speech-to-text using Vosk.
"""
import json
import queue
import sounddevice as sd
from vosk import Model, KaldiRecognizer
from typing import Optional


class VoskASR:
    """Vosk-based ASR for offline speech recognition."""
    
    def __init__(self, model_path: str = "models", sample_rate: int = 16000):
        """
        Initialize Vosk ASR.
        
        Args:
            model_path: Path to Vosk model directory
            sample_rate: Audio sample rate (Hz)
        """
        self.sample_rate = sample_rate
        self.model_path = model_path
        
        # Load Vosk model
        try:
            self.model = Model(model_path)
            self.recognizer = KaldiRecognizer(self.model, sample_rate)
            self.recognizer.SetWords(True)
        except Exception as e:
            print(f"Warning: Could not load Vosk model from {model_path}")
            print(f"Error: {e}")
            print("Please download a Vosk model from https://alphacephei.com/vosk/models")
            print("Extract it to the 'models' directory")
            self.model = None
            self.recognizer = None
        
        self.audio_queue = queue.Queue()
    
    def recognize_from_mic(self, duration: float = 3.0) -> Optional[str]:
        """
        Record audio from microphone and recognize speech.
        
        Args:
            duration: Recording duration in seconds
            
        Returns:
            Recognized text or None if recognition failed
        """
        if self.recognizer is None:
            print("Error: Vosk model not loaded. Cannot recognize speech.")
            return None
        
        try:
            print(f"\n🔊 Listening for {duration} seconds...")
            
            # Record audio
            audio_data = sd.rec(
                int(self.sample_rate * duration),
                samplerate=self.sample_rate,
                channels=1,
                dtype='int16'
            )
            sd.wait()
            
            print("✅ Recording complete. Processing...")
            
            # Process audio
            chunks = []
            for i in range(0, len(audio_data), 4000):
                chunk = audio_data[i:i+4000].tobytes()
                if self.recognizer.AcceptWaveform(chunk):
                    result = json.loads(self.recognizer.Result())
                    if result.get('text'):
                        chunks.append(result['text'])
            
            # Get final result
            final_result = json.loads(self.recognizer.FinalResult())
            if final_result.get('text'):
                chunks.append(final_result['text'])
            
            recognized_text = ' '.join(chunks).strip()
            
            if recognized_text:
                print(f"🎤 Recognized: {recognized_text}")
                return recognized_text
            else:
                print("❌ No speech detected")
                return None
                
        except Exception as e:
            print(f"❌ Error during recognition: {e}")
            return None
    
    def recognize_from_file(self, file_path: str) -> Optional[str]:
        """
        Recognize speech from audio file.
        
        Args:
            file_path: Path to audio file
            
        Returns:
            Recognized text or None if recognition failed
        """
        if self.recognizer is None:
            print("Error: Vosk model not loaded.")
            return None
        
        try:
            import wave
            import sys
            
            wf = wave.open(file_path, "rb")
            
            if wf.getnchannels() != 1 or wf.getcomptype() != "NONE":
                print("Audio file must be WAV format mono PCM.")
                return None
            
            chunks = []
            while True:
                data = wf.readframes(4000)
                if len(data) == 0:
                    break
                
                if self.recognizer.AcceptWaveform(data):
                    result = json.loads(self.recognizer.Result())
                    if result.get('text'):
                        chunks.append(result['text'])
            
            final_result = json.loads(self.recognizer.FinalResult())
            if final_result.get('text'):
                chunks.append(final_result['text'])
            
            recognized_text = ' '.join(chunks).strip()
            wf.close()
            
            return recognized_text if recognized_text else None
            
        except Exception as e:
            print(f"Error processing audio file: {e}")
            return None

