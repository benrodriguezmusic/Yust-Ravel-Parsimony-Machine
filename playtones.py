import numpy as np
import sounddevice as sd

SAMPLE_RATE = 44100
BASE_FREQ = 261.63  # C4
DEFAULT_DURATION = 0.2


def play_sawtooth(n, duration=DEFAULT_DURATION, volume=0.1):
    """Play pitch number n (C=0) as a sawtooth wave."""
    freq = BASE_FREQ * (2 ** (n / 12))
    t = np.linspace(0, duration, int(SAMPLE_RATE * duration), False)
    wave = 2 * (t * freq - np.floor(0.5 + t * freq))

    # Apply 20 ms fade-in/out to avoid clicks
    fade_len = int(0.02 * SAMPLE_RATE)
    envelope = np.ones_like(wave)
    envelope[:fade_len] = np.linspace(0, 1, fade_len)
    envelope[-fade_len:] = np.linspace(1, 0, fade_len)
    wave *= envelope * volume

    sd.play(wave, SAMPLE_RATE)
    sd.wait()
