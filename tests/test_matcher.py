"""
Tests for NLU matcher module.
"""
import pytest
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from nlu.matcher import match_intent, get_intent_description


class TestMatcher:
    """Test cases for intent matcher."""
    
    def test_saludo_spanish(self):
        """Test greeting intent in Spanish."""
        result = match_intent("hola")
        assert result['intent'] == 'saludo'
        assert result['confidence'] > 0.8
    
    def test_saludo_english(self):
        """Test greeting intent in English."""
        result = match_intent("hello")
        assert result['intent'] == 'saludo'
    
    def test_hora_query(self):
        """Test time query intent."""
        result = match_intent("qué hora es")
        assert result['intent'] == 'hora'
        assert result['confidence'] > 0.8
    
    def test_encender_luz(self):
        """Test turn on light intent."""
        result = match_intent("enciende la luz")
        assert result['intent'] == 'encender_luz'
    
    def test_apagar_luz(self):
        """Test turn off light intent."""
        result = match_intent("apaga la luz")
        assert result['intent'] == 'apagar_luz'
    
    def test_unknown_intent(self):
        """Test unknown intent."""
        result = match_intent("xyz abc 123")
        assert result['intent'] == 'unknown'
        assert result['confidence'] == 0.0
    
    def test_empty_text(self):
        """Test empty text."""
        result = match_intent("")
        assert result['intent'] == 'unknown'
    
    def test_case_insensitive(self):
        """Test case insensitive matching."""
        result1 = match_intent("HOLA")
        result2 = match_intent("hola")
        assert result1['intent'] == result2['intent']
        assert result1['intent'] == 'saludo'
    
    def test_partial_match(self):
        """Test partial text matching."""
        result = match_intent("hola cómo estás")
        assert result['intent'] == 'saludo'
    
    def test_get_intent_description(self):
        """Test intent description."""
        desc = get_intent_description('saludo')
        assert 'hola' in desc.lower() or 'greeting' in desc.lower()
        
        desc_unknown = get_intent_description('unknown_intent')
        assert 'unknown' in desc_unknown.lower()


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

