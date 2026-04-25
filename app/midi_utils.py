from mido import Message, MidiFile, MidiTrack
import uuid
import os

OUTPUT_DIR = "static/outputs"

def create_midi(melody):
    mid = MidiFile()
    track = MidiTrack()
    mid.tracks.append(track)

    tempo = 500000  # default tempo

    for note, duration in melody:
        track.append(Message('note_on', note=note, velocity=64, time=0))
        track.append(Message('note_off', note=note, velocity=64, time=int(duration * 480)))

    filename = f"{uuid.uuid4()}.mid"
    filepath = os.path.join(OUTPUT_DIR, filename)

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    mid.save(filepath)

    return filepath