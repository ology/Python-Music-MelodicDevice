import sys
sys.path.append('./src')
import music_melodicdevice.musical_scales as musical_scales

class Device:
    def __init__(self, scale_note='C', scale_name='chromatic', notes=[], verbose=0):
        self.scale_note = scale_note
        self.scale_name = scale_name
        self.notes = notes
        self.verbose = verbose
        self.build_scale()

    def _find_pitch(self, p):
        try:
            i = self.scale.index(p)
        except ValueError:
            i = -1
        return i

    def build_scale(self, name=None):
        if name:
            self.scale_name = name
        scale = []
        for i in range(-1,10):
            s = musical_scales.scale(self.scale_note, self.scale_name, starting_octave=i)
            scale.append(s[:-1])
        scale = [ f"{x}" for s in scale for x in s ]
        if self.verbose:
            print("Scale:", scale, len(scale))
        self.scale = scale

    def transpose(self, offset, notes=[]):
        if not notes:
            notes = self.notes
        if self.verbose:
            print("Notes:", notes)
        transposed = []
        for n in notes:
            i = self._find_pitch(n)
            if i == -1:
                transposed.append(None)
            else:
                val = self.scale[i + offset]
                transposed.append(val)
        if self.verbose:
            print('Transposed:', transposed)
        return transposed

    def intervals(self, notes=[]):
        if not notes:
            notes = self.notes
        pitches = []
        for note in notes:
            i = self._find_pitch(note)
            pitches.append(i)
        if self.verbose:
            print(f"Pitch indexes: {pitches}")
        intervals = []
        last = None
        for pitch in pitches:
            if last is not None:
                intervals.append(pitch - last)
            last = pitch
        if self.verbose:
            print(f"Intervals: {intervals}")
        return intervals

    def invert(self, axis_note, notes=[]):
        if not notes:
            notes = self.notes
        if self.verbose:
            print("Axis, Notes:", axis_note, notes)
        axis = self._find_pitch(axis_note)
        nums = [ self._find_pitch(n) for n in notes ]
        inverted = []
        for n in nums:
            if n == -1:
                inv = None
            else:
                inv = axis - (n - axis)
            inverted.append(inv)
        named = []
        for x in inverted:
            if not x:
                name = None
            else:
                name = self.scale[x]
            named.append(name)
        if self.verbose:
            print("Inverted:", named)
        return named
