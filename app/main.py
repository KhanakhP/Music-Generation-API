from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel

from app.melody_generator import generate_melody
from app.midi_utils import create_midi

app = FastAPI()

# ✅ Static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# ✅ UI route (place here, not "on top randomly")
@app.get("/")
def serve_ui():
    return FileResponse("static/index.html")


class PromptRequest(BaseModel):
    prompt: str


@app.post("/generate-music")
def generate_music(req: PromptRequest):
    melody = generate_melody(req.prompt)
    file_path = create_midi(melody)

    return {
        "result": file_path,
        "melody": melody
    }