"""
Tests for actions module.
"""
import pytest
import sys
from pathlib import Path
from datetime import datetime

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from executor.actions import execute, get_system_status, list_available_intents


class TestActions:
    """Test cases for action executor."""
    
    def test_execute_saludo(self):
        """Test execute greeting."""
        intent_data = {'intent': 'saludo', 'raw_text': 'hola'}
        response = execute(intent_data)
        assert isinstance(response, str)
        assert len(response) > 0
    
    def test_execute_hora(self):
        """Test execute time query."""
        intent_data = {'intent': 'hora', 'raw_text': 'qué hora es'}
        response = execute(intent_data)
        assert isinstance(response, str)
        assert len(response) > 0
        # Should contain hour
        assert any(char.isdigit() for char in response)
    
    def test_execute_encender_luz(self):
        """Test execute turn on light."""
        intent_data = {'intent': 'encender_luz', 'raw_text': 'enciende la luz'}
        response = execute(intent_data)
        assert isinstance(response, str)
        assert 'luz' in response.lower()
    
    def test_execute_apagar_luz(self):
        """Test execute turn off light."""
        intent_data = {'intent': 'apagar_luz', 'raw_text': 'apaga la luz'}
        response = execute(intent_data)
        assert isinstance(response, str)
        assert 'luz' in response.lower()
    
    def test_execute_unknown(self):
        """Test execute unknown intent."""
        intent_data = {'intent': 'unknown', 'raw_text': 'xyz'}
        response = execute(intent_data)
        assert isinstance(response, str)
        assert len(response) > 0
    
    def test_get_system_status(self):
        """Test get system status."""
        status = get_system_status()
        assert isinstance(status, str)
        assert len(status) > 0
    
    def test_list_available_intents(self):
        """Test list available intents."""
        intents = list_available_intents()
        assert isinstance(intents, list)
        assert len(intents) > 0
        assert 'saludo' in intents
        assert 'hora' in intents
        assert 'encender_luz' in intents
        assert 'apagar_luz' in intents
    
    def test_execute_with_invalid_intent(self):
        """Test execute with invalid intent."""
        intent_data = {'intent': 'invalid_intent', 'raw_text': 'test'}
        response = execute(intent_data)
        assert isinstance(response, str)
        assert len(response) > 0
    
    def test_intent_data_missing_intent(self):
        """Test with missing intent in data."""
        intent_data = {'raw_text': 'test'}
        response = execute(intent_data)
        assert isinstance(response, str)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

