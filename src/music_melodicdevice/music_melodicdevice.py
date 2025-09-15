from music21 import scale, note, pitch
import musical_scales
import re

class Device:
    def __init__(self, scale_note='C', scale_name='chromatic', notes=[], verbose=0):
        self.scale_note = scale_note
        self.scale_name = scale_name
        self.notes = notes
        self.verbose = verbose
        self.build_scale()

    def build_scale(self, name=None):
        if name:
            self.scale_name = name
        scale = []
        for i in range(10):
            s = musical_scales.scale(self.scale_note, self.scale_name, starting_octave=i)
            scale.append(s[:-1])
        scale = [ f"{x}" for s in scale for x in s ]
        if self.verbose:
            print("Scale:", scale)
        self.scale = scale

    def transpose(self, offset, notes=[]):
        if not len(notes):
            notes = self.notes
        if self.verbose:
            print("Notes:", notes)
        transposed = []
        for n in notes:
            i, pitch_val = self._find_pitch(n)
            if i == -1:
                transposed.append(None)
            else:
                val = self.scale[i + offset]
                transposed.append(val)
        if self.verbose:
            print('Transposed:', transposed)
        return transposed

    def _find_pitch(self, p):
        if isinstance(p, str) and any(c in p for c in 'ABCDEFG'):
            pitch_val = p
        else:
            pitch_val = int(p)
        try:
            i = self.scale.index(pitch_val)
        except ValueError:
            i = -1
        return i, pitch_val
