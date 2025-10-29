"""
Audio utilities for recording and processing.
"""
import sounddevice as sd
import numpy as np
from typing import Optional


def list_audio_devices() -> list:
    """
    List available audio devices.
    
    Returns:
        List of available audio devices
    """
    devices = sd.query_devices()
    print("Available audio devices:")
    for i, device in enumerate(devices):
        print(f"  [{i}] {device['name']}")
    return devices


def get_default_device() -> Optional[int]:
    """
    Get default audio device index.
    
    Returns:
        Device index or None
    """
    default = sd.default.device
    print(f"Default input device: {default[0]}")
    print(f"Default output device: {default[1]}")
    return default[0]


def record_audio(duration: float, sample_rate: int = 16000) -> np.ndarray:
    """
    Record audio from microphone.
    
    Args:
        duration: Recording duration in seconds
        sample_rate: Sample rate in Hz
        
    Returns:
        Audio data as numpy array
    """
    print(f"Recording {duration} seconds...")
    audio_data = sd.rec(
        int(sample_rate * duration),
        samplerate=sample_rate,
        channels=1,
        dtype='float32'
    )
    sd.wait()
    print("Recording complete")
    return audio_data


def play_audio(audio_data: np.ndarray, sample_rate: int = 16000):
    """
    Play audio data.
    
    Args:
        audio_data: Audio data to play
        sample_rate: Sample rate in Hz
    """
    print("Playing audio...")
    sd.play(audio_data, samplerate=sample_rate)
    sd.wait()


def check_microphone() -> bool:
    """
    Check if microphone is available.
    
    Returns:
        True if microphone is available
    """
    try:
        default_device = sd.default.device[0]
        if default_device is not None:
            info = sd.query_devices(default_device)
            if info['max_input_channels'] > 0:
                print(f"Microphone available: {info['name']}")
                return True
        print("No microphone input device found")
        return False
    except Exception as e:
        print(f"Error checking microphone: {e}")
        return False


def get_audio_info() -> dict:
    """
    Get information about audio devices.
    
    Returns:
        Dictionary with audio device information
    """
    info = {
        'default_input': sd.default.device[0],
        'default_output': sd.default.device[1],
        'devices': []
    }
    
    devices = sd.query_devices()
    for i, device in enumerate(devices):
        info['devices'].append({
            'index': i,
            'name': device['name'],
            'channels': device['channels'],
            'sample_rate': device['default_samplerate']
        })
    
    return info

