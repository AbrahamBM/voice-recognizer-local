# Voice Recognizer Local

Sistema de reconocimiento de voz offline completo que funciona sin conexión a internet. Este proyecto simula un asistente de voz con reconocimiento de voz, comprensión de lenguaje natural, ejecución de acciones y síntesis de voz.

## Descripción

Voice Recognizer Local es un sistema de asistente de voz que integra:
- **ASR (Automatic Speech Recognition)**: Reconocimiento de voz usando Vosk
- **NLU (Natural Language Understanding)**: Comprensión de intenciones basada en reglas
- **Executor**: Ejecución de acciones simuladas
- **TTS (Text-to-Speech)**: Síntesis de voz usando pyttsx3

## Estructura del Proyecto

```
voice-recognizer-local/
├── README.md                         # Contexto del proyecto y guía de uso
├── requirements.txt                  # Dependencias de Python necesarias
├── examples/                         # Ejemplos y audios de prueba
├── logs/                             # Carpeta de logs generados por la app
│   └── transcriptions.log            # Historial de transcripciones
├── models/                           # Modelos Vosk descargados localmente
│   └── vosk-model-small-es-0.42/     # Modelo español ejemplo
│       ├── am/                       # Parámetros acústicos
│       ├── conf/                     # Configuración del modelo
│       ├── graph/                    # Grafos FST para decodificación
│       ├── ivector/                  # Configs y matrices de i-vectors
│       └── README                    # Notas del modelo
├── src/                              # Código fuente del asistente
│   ├── __init__.py                   # Marca el paquete Python
│   ├── main.py                       # Punto de entrada de la app
│   ├── asr/                          # Módulo de reconocimiento de voz (ASR)
│   │   ├── __init__.py
│   │   └── vosk_asr.py               # Integración con Vosk para ASR
│   ├── executor/                     # Ejecutor de acciones según intención
│   │   ├── __init__.py
│   │   └── actions.py                # Acciones simuladas (encender/apagar, etc.)
│   ├── logs/                         # Utilidades o datos de logging internos
│   ├── nlu/                          # Comprensión de lenguaje natural (NLU)
│   │   ├── __init__.py
│   │   └── matcher.py                # Reglas/patrones para detectar intenciones
│   ├── tts/                          # Síntesis de voz (TTS)
│   │   ├── __init__.py
│   │   └── tts_engine.py             # Engine de TTS con pyttsx3
│   └── utils/                        # Utilidades compartidas
│       ├── __init__.py
│       └── audio.py                  # Grabación/procesamiento básico de audio
└── tests/                            # Suite de pruebas
    ├── test_actions.py               # Tests de acciones del ejecutor
    └── test_matcher.py               # Tests del NLU (matcher)
```

## 🔧 Simulación en TinkerCad

Este proyecto incluye una representación física simulada que permite visualizar el funcionamiento del sistema mediante componentes Arduino. Cada módulo del software está representado por un LED que se ilumina durante su ejecución, permitiendo observar el flujo completo del procesamiento de voz.

**🔗 [Ver Simulación en TinkerCad](https://www.tinkercad.com/things/aPTMwrCgVry-pia-micro-lab?sharecode=rPbKNDZp1P1STcpVJYrVdIy9z66ohUe5sYGmHNuM6B8)**

### Características de la Simulación

- **Visualización en tiempo real**: LEDs de colores representan cada etapa del proceso
- **Interfaz LCD**: Muestra el estado actual y respuestas del sistema  
- **Entrada interactiva**: Botones y potenciómetro simulan comandos de voz
- **Audio simulado**: Buzzer representa la síntesis de voz

### Componentes Representados

| LED | Módulo del Sistema |
|-----|-------------------|
| 🔴 Rojo | Captura de Audio |
| 🟡 Amarillo | Reconocimiento ASR (Vosk) |
| 🟢 Verde | Análisis NLU |
| 🔵 Azul | Ejecución de Acciones |
| ⚪ Blanco | Síntesis de Voz (TTS) |

Para más detalles sobre la implementación en hardware, consulta la carpeta `/tinkercad` en el repositorio.

## Instalación

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

## Uso

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

## Tests

Ejecutar todos los tests:

```bash
pytest tests/ -v
```

Ejecutar tests específicos:

```bash
pytest tests/test_matcher.py -v
pytest tests/test_actions.py -v
```

## Intenciones Soportadas

El sistema reconoce las siguientes intenciones:

| Intent | Ejemplos | Acción |
|--------|----------|--------|
| `saludo` | "hola", "saludos", "hi" | Responder con saludo |
| `hora` | "qué hora es", "dime la hora" | Mostrar hora actual |
| `encender_luz` | "enciende la luz", "prende la luz" | Simular encender luz |
| `apagar_luz` | "apaga la luz", "apagar luz" | Simular apagar luz |

## Personalización

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

## Logging de Transcripciones

El sistema registra automáticamente las transcripciones en:
- `logs/transcriptions.log`

Formato del log:
```
2025-10-28 22:30:45 | hola cómo estás
2025-10-28 22:31:12 | qué hora es
```

## Configuración

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

## Recomendaciones y Mejores Prácticas

### Instalación y Configuración
1. **Entorno Virtual**: Se recomienda crear un entorno virtual antes de instalar dependencias:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   pip install -r requirements.txt
   ```

2. **Path del Modelo**: Asegúrate de que el modelo de Vosk esté en la estructura correcta:
   ```
   models/
   └── vosk-model-small-es-0.42/
       ├── am/
       ├── conf/
       ├── graph/
       └── ivector/
   ```

3. **Dependencias en Windows**: Si encuentras problemas instalando dependencias en Windows:
   - Usa `python -m pip install` en lugar de solo `pip install`
   - Verifica que estés usando la versión correcta de Python con `python --version`

### Uso del Sistema
1. **Calidad de Audio**: Para mejores resultados:
   - Habla claramente y a una distancia de 30-50 cm del micrófono
   - Reduce el ruido de fondo
   - Usa frases completas

2. **Duración de Grabación**: Ajusta la duración según tus necesidades:
   - 3 segundos: Para comandos cortos (recomendado)
   - 5 segundos: Para frases más largas

3. **Tests**: Ejecuta los tests antes de usar el sistema:
   ```bash
   pytest tests/ -v
   ```

### Posibles Mejoras
- Agregar más intenciones y comandos
- Implementar reconocimiento de voz en tiempo real
- Mejorar el NLU con machine learning
- Agregar soporte multiidioma
- Implementar memoria de contexto para conversaciones

## Solución de Problemas

### Error: "Vosk model not loaded"
- **Solución**: Descarga e instala un modelo de Vosk en `models/`
- **IMPORTANTE**: Asegúrate de que el modelo esté en la carpeta correcta: `models/vosk-model-small-es-0.42/` (con toda la estructura interna: am/, conf/, graph/, ivector/)
- **Ruta correcta**: El path debe apuntar a la carpeta específica del modelo, no solo a `models/`

### Error: "No microphone input device found"
- **Solución**: Conecta un micrófono o configura el dispositivo de entrada por defecto

### Error: TTS no funciona
- **Solución**: El texto se imprimirá en consola en su lugar

### Tests fallan
- **Solución**: Asegúrate de haber instalado todas las dependencias: `pip install -r requirements.txt`

### Error: "ModuleNotFoundError: No module named 'sounddevice'"
- **Solución**: Instala las dependencias manualmente: `python -m pip install vosk sounddevice numpy pyttsx3 cffi requests`

### Error al cargar modelo en Windows
- **Solución**: Asegúrate de usar el path completo del modelo. En Windows, el path debe ser absoluto o usar `os.path.join()` para garantizar compatibilidad
- **Ejemplo**: El código en `src/main.py` ya incluye la construcción correcta del path

## Dependencias Principales

- **vosk**: Reconocimiento de voz offline
- **sounddevice**: Grabación y reproducción de audio
- **pyttsx3**: Síntesis de voz offline
- **pytest**: Framework de testing

## Licencia

Este proyecto es de código abierto. Siéntete libre de usarlo y modificarlo.

## Autores

- **2109430** Abraham Bernacho Mares ITS
- **2127772** José Ricardo Cruz Tapia ITS
- **2127967** Guillermo Vladimir Flores Báez ITS

Proyecto educativo de reconocimiento de voz offline desarrollado como parte del curso de LAB 	CONTROLADORES Y MICROCONTRL. PROGRAMABLES.

## Contribuciones

Las contribuciones son bienvenidas. Para mejorar el proyecto:
1. Agrega nuevas intenciones
2. Mejora la precisión del NLU
3. Agrega más tests
4. Mejora la documentación

---

**Nota**: Este proyecto es una simulación educativa. Para uso en producción, considera sistemas más robustos y seguros.