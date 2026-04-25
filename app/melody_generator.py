import random

# Simple mapping of mood → scale
SCALES = {
    "happy": [60, 62, 64, 65, 67, 69, 71, 72],  # C Major
    "sad": [60, 62, 63, 65, 67, 68, 70, 72],    # C Minor
    "default": [60, 62, 64, 65, 67, 69, 71, 72]
}

def get_scale(prompt: str):
    prompt = prompt.lower()
    if "happy" in prompt:
        return SCALES["happy"]
    elif "sad" in prompt:
        return SCALES["sad"]
    else:
        return SCALES["default"]

def generate_melody(prompt: str, length=16):
    scale = get_scale(prompt)
    
    melody = []
    for _ in range(length):
        note = random.choice(scale)
        duration = random.choice([0.25, 0.5, 1])
        melody.append((note, duration))
    
    return melody