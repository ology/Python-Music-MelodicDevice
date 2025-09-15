from music21 import scale, note, pitch
import musical_scales
import re

class Device:
    OCTAVES = 10

    def __init__(self, scale_note='C', scale_name='chromatic', notes=[], verbose=0):
        self.scale_note = scale_note
        self.scale_name = scale_name
        self.notes = notes
        self.verbose = verbose
        self._scale = self._build_scale()

    def _build_scale(self):
        s = musical_scales.scale(self.scale_note, self.scale_name)
        # remove the octave number from the stringified Note:
        s2 = []
        for n in s:
            s2.append(re.sub(r"\d+", "", f"{n}"))
        if self.flat:
            s2 = [ self._equiv(note) for note in s2 ]
        if self.verbose:
            print('Scale:', s2)
        return s2

    def transpose(self, offset, notes=None):
        notes = notes if notes is not None else self.notes
        named = isinstance(notes[0], str) and any(n in notes[0] for n in 'ABCDEFG')
        transposed = []
        for n in notes:
            i, pitch_val = self._find_pitch(n)
            if i == -1:
                transposed.append(None)
            else:
                midi_val = self._scale[i + offset]
                if named:
                    transposed.append(pitch.Pitch(midi_val).nameWithOctave)
                else:
                    transposed.append(midi_val)
        if self.verbose:
            print('Transposed:', transposed)
        return transposed

    def _find_pitch(self, p):
        if isinstance(p, str) and any(c in p for c in 'ABCDEFG'):
            pitch_val = pitch.Pitch(p).midi
        else:
            pitch_val = int(p)
        try:
            i = self._scale.index(pitch_val)
        except ValueError:
            i = -1
        return i, pitch_val
