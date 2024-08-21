
# LemonFox API Wrapper

This Python class provides a simple interface to interact with the LemonFox API, which offers competitive pricing compared to OpenAI for audio transcription, large language models (LLM), and image generation. Currently, the class supports audio transcription, but more functionalities will be added soon.

## Features

- **Audio Transcription:** Convert speech to text by providing an audio file or a URL to an audio file.

## Installation

To use this class, you need to have Python installed on your machine. You can clone the repository and use the class in your projects.

```bash
git clone https://github.com/ionutsoftware/lemonfox-api-wrapper.git
cd lemonfox-api-wrapper
```

## Usage

### Audio Transcription

You can transcribe audio either by providing a local audio file or a URL to an audio file.

#### Transcribing Audio from a URL

```python
from lemonfox import LemonFox

# Initialize the class with your API key
api_key = "your_api_key_here"
lemonfox = LemonFox(api_key)

# URL of the audio file to transcribe
audio_url = "https://example.com/audio.mp3"

# Transcribe the audio
try:
    transcription = lemonfox.transcribe(language="en", is_url=True, url=audio_url)
    print("Transcription from URL:")
    print(transcription)
except ValueError as e:
    print(f"Error: {e}")
```

#### Transcribing Audio from a Local File

```python
from lemonfox import LemonFox

# Initialize the class with your API key
api_key = "your_api_key_here"
lemonfox = LemonFox(api_key)

# Path to the local audio file
audio_path = "path/to/your/audio.mp3"

# Transcribe the audio
try:
    transcription = lemonfox.transcribe(language="es", audio=audio_path)
    print("Transcription from Local File:")
    print(transcription)
except ValueError as e:
    print(f"Error: {e}")
```

## Upcoming Features

- **Large Language Models (LLM):** Access to powerful language models for natural language processing.
- **Image Generation:** Create images from text prompts using state-of-the-art AI models.

## API Documentation

For detailed API documentation, visit [LemonFox API Documentation](https://www.lemonfox.ai/apis).

## Contributing

Contributions are welcome! If you find a bug or have a feature request, feel free to open an issue or a pull request.

