# Promptly

Promptly is an early prototype for a word-recall assistant. The current version is a Streamlit app that uses DistilGPT2 to suggest likely next words from the sentence context typed by the user.

## Current Version

This repository currently contains a text-based prototype:

- `app.py` - Streamlit user interface
- `predictor.py` - DistilGPT2 next-word prediction logic
- `requirements.txt` - Python dependencies

The app is intentionally general-purpose. It does not force medical or patient-specific words. It predicts based on the context provided by the user.

## Long-Term Product Direction

The intended product direction is an assistive word-recall system that can eventually:

1. Connect to a phone or wearable microphone.
2. Listen during an active user-controlled session.
3. Detect a pause of around two seconds.
4. Decide whether the sentence seems incomplete.
5. Predict a helpful next word or short phrase.
6. Speak the suggestion through a wearable or earbud.
7. Learn the user's frequently used words, phrases, and communication patterns locally.

## Privacy Notice

This is a prototype. Do not enter private medical records, names, IDs, addresses, or sensitive personal information while testing.

## Requirements

- Python 3.9 or newer recommended
- Internet connection for the first model download
- Laptop or desktop for the current prototype

## Setup Instructions

Clone the repository:

```bash
git clone https://github.com/DevarshPathak/promptly.git
cd promptly
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the environment.

Windows:

```bash
venv\Scripts\activate
```

Mac/Linux:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the app:

```bash
streamlit run app.py
```

Open the local URL shown in your terminal. It is usually:

```txt
http://localhost:8501
```

## Example Inputs

Try these examples in the app:

```txt
This product will help customers
```

```txt
Our marketing strategy should focus on
```

```txt
The main benefit of this service is
```

```txt
I want to explain the value of
```

```txt
The client is interested in
```

```txt
The campaign performance improved because
```

## How It Works

The app uses a causal language model, DistilGPT2, through the Hugging Face Transformers pipeline. It generates a few tokens after the user's text and extracts the first new word as the suggested next word.

## Next Planned Version

The next development milestone should move toward the actual app concept:

- Add microphone input.
- Add live speech-to-text.
- Detect around two seconds of pause.
- Predict the next word or phrase after the pause.
- Add text-to-speech output.
- Add local personalization memory for frequently used words and phrases.

## Run Notes

The first run may take longer because the model files are downloaded. Later runs should be faster because the model is cached locally.
