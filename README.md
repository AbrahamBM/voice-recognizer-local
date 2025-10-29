# Voice Recognizer Local

Sistema de reconocimiento de voz offline completo que funciona sin conexión a internet. Este proyecto simula un asistente de voz con reconocimiento de voz, comprensión de lenguaje natural, ejecución de acciones y síntesis de voz.

## 📋 Descripción

Voice Recognizer Local es un sistema de asistente de voz que integra:
- **ASR (Automatic Speech Recognition)**: Reconocimiento de voz usando Vosk
- **NLU (Natural Language Understanding)**: Comprensión de intenciones basada en reglas
- **Executor**: Ejecución de acciones simuladas
- **TTS (Text-to-Speech)**: Síntesis de voz usando pyttsx3

## 🏗️ Estructura del Proyecto

```
voice-recognizer-local/
├── README.md
├── requirements.txt
├── src/
│   ├── main.py                 # Punto de entrada principal
│   ├── asr/
│   │   └── vosk_asr.py        # Módulo de reconocimiento de voz
│   ├── nlu/
│   │   └── matcher.py          # Módulo de comprensión de lenguaje
│   ├── executor/
│   │   └── actions.py           # Módulo de ejecución de acciones
│   ├── tts/
│   │   └── tts_engine.py       # Módulo de síntesis de voz
│   └── utils/
│       └── audio.py            # Utilidades de audio
├── tests/
│   ├── test_matcher.py         # Tests para NLU
│   └── test_actions.py         # Tests para acciones
├── models/                     # Modelos de Vosk (descargar manualmente)
└── examples/
    └── sample.wav              # Archivo de ejemplo
```

## 🚀 Instalación

### 1. Prerrequisitos

- Python 3.8 o superior
- Microphone (opcional, para reconocimiento de voz en vivo)
- Sistema operativo: Windows, macOS, o Linux

### 2. Clonar o descargar el proyecto

```bash
cd voice-recognizer-local
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Descargar modelo de Vosk (Opcional pero recomendado)

Para reconocimiento de voz, necesitas descargar un modelo de Vosk:

1. Visita [https://alphacephei.com/vosk/models](https://alphacephei.com/vosk/models)
2. Descarga un modelo (recomendado: `vosk-model-small-es-0.42` para español o `vosk-model-small-en-us-0.15` para inglés)
3. Extrae el modelo en la carpeta `models/`

**Ejemplo:**
```bash
# Para español
cd models
# Descargar y extraer modelo español
# Estructura esperada: models/vosk-model-small-es-0.42/
```

### 5. Verificar instalación

```bash
# Ejecutar tests
pytest tests/ -v
```

## 💻 Uso

### Modo Interactivo

Ejecuta el asistente en modo interactivo:

```bash
python src/main.py
```

El programa te pedirá que presiones Enter para empezar a grabar. Di uno de estos comandos:
- "hola" o "saludos" - Saludo
- "qué hora es" - Consultar hora
- "enciende la luz" - Encender luz
- "apaga la luz" - Apagar luz

### Uso Programático

```python
from src.main import VoiceRecognizer

# Inicializar
recognizer = VoiceRecognizer(model_path="models")

# Procesar comando de voz
recognizer.process_command(duration=3.0)

# O procesar texto directamente
response = recognizer.process_text("qué hora es")
print(response)
```

### Reconocimiento desde Archivo

```python
from src.asr.vosk_asr import VoskASR

asr = VoskASR(model_path="models")
text = asr.recognize_from_file("examples/sample.wav")
print(text)
```

## 🧪 Tests

Ejecutar todos los tests:

```bash
pytest tests/ -v
```

Ejecutar tests específicos:

```bash
pytest tests/test_matcher.py -v
pytest tests/test_actions.py -v
```

## 📝 Intenciones Soportadas

El sistema reconoce las siguientes intenciones:

| Intent | Ejemplos | Acción |
|--------|----------|--------|
| `saludo` | "hola", "saludos", "hi" | Responder con saludo |
| `hora` | "qué hora es", "dime la hora" | Mostrar hora actual |
| `encender_luz` | "enciende la luz", "prende la luz" | Simular encender luz |
| `apagar_luz` | "apaga la luz", "apagar luz" | Simular apagar luz |

## 🛠️ Personalización

### Agregar Nueva Intención

1. Edita `src/nlu/matcher.py` y agrega el patrón:

```python
nueva_intencion_patterns = [
    r'\b(palabra|clave)\s*patrón\b'
]

for pattern in nueva_intencion_patterns:
    if re.search(pattern, text_lower):
        return {
            'intent': 'nueva_intencion',
            'confidence': 0.9,
            'raw_text': text
        }
```

2. Edita `src/executor/actions.py` y agrega la acción:

```python
elif intent == 'nueva_intencion':
    return "Respuesta para nueva intención"
```

### Cambiar Idioma TTS

Edita `src/main.py`:

```python
self.tts = TTSEngine(language='english')  # o 'spanish'
```

## 📊 Logging de Transcripciones

El sistema registra automáticamente las transcripciones en:
- `logs/transcriptions.log`

Formato del log:
```
2025-10-28 22:30:45 | hola cómo estás
2025-10-28 22:31:12 | qué hora es
```

## ⚙️ Configuración

### Parámetros de Grabación

Edita la duración de grabación en `main.py`:

```python
recognizer.process_command(duration=5.0)  # 5 segundos
```

### Voz TTS

Configurar velocidad y volumen en `src/tts/tts_engine.py`:

```python
self.engine.setProperty('rate', 150)    # Velocidad (palabras/min)
self.engine.setProperty('volume', 0.9)  # Volumen (0.0-1.0)
```

## 🐛 Solución de Problemas

### Error: "Vosk model not loaded"
- **Solución**: Descarga e instala un modelo de Vosk en `models/`

### Error: "No microphone input device found"
- **Solución**: Conecta un micrófono o configura el dispositivo de entrada por defecto

### Error: TTS no funciona
- **Solución**: El texto se imprimirá en consola en su lugar

### Tests fallan
- **Solución**: Asegúrate de haber instalado todas las dependencias: `pip install -r requirements.txt`

## 📦 Dependencias Principales

- **vosk**: Reconocimiento de voz offline
- **sounddevice**: Grabación y reproducción de audio
- **pyttsx3**: Síntesis de voz offline
- **pytest**: Framework de testing

## 📄 Licencia

Este proyecto es de código abierto. Siéntete libre de usarlo y modificarlo.

## 👤 Autor

Creado como proyecto educativo de reconocimiento de voz offline.

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Para mejorar el proyecto:
1. Agrega nuevas intenciones
2. Mejora la precisión del NLU
3. Agrega más tests
4. Mejora la documentación

---

**Nota**: Este proyecto es una simulación educativa. Para uso en producción, considera sistemas más robustos y seguros.

