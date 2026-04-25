# 🎵 Music Generation API (FastAPI)

## 📌 Overview

This project is a lightweight music generation API built using FastAPI.
It takes a text prompt as input and generates a simple melody using rule-based logic, returning a downloadable MIDI file.

The goal is to demonstrate end-to-end system design:

* API development
* Prompt-based logic handling
* Programmatic music generation

---

## 🚀 Features

* 🎯 FastAPI-based REST API
* 🎼 Prompt → Melody generation (rule-based)
* 🎹 MIDI file creation using Python
* 📁 Downloadable music output
* 🌐 Simple frontend UI (HTML + JS)
* ⚡ Lightweight (no heavy ML models used)

---

## 🏗️ Project Structure

```
music-api/
│
├── app/
│   ├── main.py
│   ├── melody_generator.py
│   ├── midi_utils.py
│
├── static/
│   ├── index.html
│   └── outputs/
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation & Setup

```bash
git clone <your-repo-link>
cd music-api

pip install -r requirements.txt
uvicorn app.main:app --reload
```

---

## 🔌 API Endpoint

### POST `/generate-music`

#### Request

```json
{
  "prompt": "happy melody"
}
```

#### Response

```json
{
  "result": "static/outputs/abc123.mid",
  "melody": [[60, 0.5], [62, 1], ...]
}
```

---

## 🌐 UI Usage

Open in browser:

```
http://127.0.0.1:8000/
```

* Enter a prompt (e.g., "happy birthday tune")
* Click **Generate**
* Download the generated MIDI file

---

## 🎵 Sample Output

A sample MIDI file is included in:

```
static/outputs/sample.mid
```

You can open it using:

* VLC Media Player
* Windows Media Player
* Online MIDI players

---

## 🧠 How It Works

1. Prompt is analyzed for keywords (e.g., "happy", "sad")
2. A musical scale is selected
3. A melody is generated using random note selection within the scale
4. Notes are converted into MIDI format using `mido`
5. File is saved and returned via API


---

## ⚠️ Limitations

* Uses rule-based logic (not a trained AI model)
* Output is simple MIDI (not real audio like WAV/MP3)
* Melody is not musically complex

---

## 💡 Future Improvements

* Convert MIDI → WAV audio output
* Add tempo and rhythm control
* Improve melody structure (chords, patterns)
* Use ML-based music generation

---

## 👨‍💻 Author

Khanakh Prajapati
