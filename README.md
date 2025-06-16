# JARVIS: Voice-Activated Virtual Assistant

## Overview

JARVIS is a voice-activated virtual assistant designed to make daily tasks more convenient and efficient. Powered by OpenAI's GPT-3.5-turbo, JARVIS can perform web browsing, play music, fetch news, and respond to complex queries. Its functionality and simplicity make it a powerful tool for both personal and professional use.

---

## Features

### Voice Recognition

* **Speech Recognition:** Listens for and recognizes voice commands using the `speech_recognition` library.
* **Wake Word Activation:** Activates upon detecting the wake word "Jarvis."

### Text-to-Speech

* Converts text to speech using:

  * **`pyttsx3`** for local TTS conversion.
  * **Google Text-to-Speech (gTTS)** for playback using `pygame`.

### Web Browsing

* Opens websites like Google, Facebook, YouTube, and LinkedIn based on voice commands.

### Music Playback

* Interfaces with a `musicLibrary` module to play songs through web links.

### News Fetching

* Retrieves and reads the latest news headlines using NewsAPI.

### OpenAI Integration

* Processes complex queries and generates responses using OpenAI's GPT-3.5-turbo.
* Functions as a general virtual assistant, similar to Alexa or Google Assistant.

---

## Workflow

### 1. Initialization

* JARVIS starts with a greeting: "Initializing Jarvis..."

### 2. Wake Word Detection

* Listens for the wake word "Jarvis."
* Acknowledges activation by saying "Ya."

### 3. Command Processing

* Determines actions based on voice commands:

  * **Open websites**
  * **Play music**
  * **Fetch news**
  * **Generate responses via OpenAI**

### 4. Speech Output

* Provides responses using the `speak` function, leveraging either `pyttsx3` or `gTTS`.

---

## Technologies Used

* **Programming Language:** Python
* **Speech Recognition:** `speech_recognition` library
* **Text-to-Speech:** `pyttsx3`, `gTTS`, `pygame`
* **Web Interaction:** Web browser module
* **News Fetching:** NewsAPI
* **AI Integration:** OpenAI GPT-3.5-turbo

---

## How to Use

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-username/jarvis.git
   cd jarvis
   ```

2. **Install Dependencies**
   Install the required Python libraries:

   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up API Keys**

   * **OpenAI API Key**: Obtain your key from OpenAI and set it in the environment variable or configuration file.
   * **NewsAPI Key**: Obtain your key from [NewsAPI](https://newsapi.org/).

4. **Run the Application**

   ```bash
   python jarvis.py
   ```

5. **Interact with JARVIS**

   * Use the wake word "Jarvis" to activate the assistant.
   * Provide commands such as "Open YouTube," "Play music," or "What's the latest news?"

---

## Future Enhancements

* Integrate smart home device control.
* Add calendar and reminder functionalities.
* Expand multi-language support.
* Enhance the wake word detection for better accuracy.

---

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, feel free to create a pull request or open an issue in the repository.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

* OpenAI for the GPT-3.5-turbo API.
* NewsAPI for news fetching capabilities.
* The developers of `speech_recognition`, `pyttsx3`, `gTTS`, and other libraries used in this project.
