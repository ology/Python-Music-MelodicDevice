import sys
sys.path.append('./src')
import music_melodicdevice.musical_scales as musical_scales
from typing import List, Tuple, Optional, Union

# TICKS = 96
# OCTAVES = 10

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

    def grace_note(self, duration, pitch, offset=0):
        i = self._find_pitch(pitch)
        grace_note = self.scale[i + offset]
        x = duration
        y = 1/16 # 64th note
        z = x - y
        if self.verbose:
            print(f"Durations: {x} + {y} = {z}")
        return [[y, grace_note], [z, pitch]]

    def turn(self, duration, pitch, offset=1):
        factor = 4
        i = self._find_pitch(pitch)
        above = self.scale[i + offset]
        below = self.scale[i - offset]
        x = duration
        z = x / factor
        if self.verbose:
            print(f"Durations: {x}, {z}")
        return [[z, above], [z, pitch], [z, below], [z, pitch]]

    def trill(self, duration: str, pitch: Union[str, int], number: int = 2, offset: int = 1):
        named = isinstance(pitch, str) and pitch[0] in 'ABCDEFG'
        i, pitch_num = self._find_pitch(pitch)
        alt_num = self._scale[i + offset]
        if named:
            pitch = self.pitchname(pitch_num)
            alt = self.pitchname(alt_num)
        else:
            pitch = pitch_num
            alt = alt_num
        x = self._duration_ticks(duration)
        z = round(x / number / 2)
        if self.verbose:
            print(f"Durations: {x}, {z}")
        trill = []
        for _ in range(number):
            trill.append([z, pitch])
            trill.append([z, alt])
        return trill

    def mordent(self, duration: str, pitch: Union[str, int], offset: int = 1):
        number = 4
        named = isinstance(pitch, str) and pitch[0] in 'ABCDEFG'
        i, pitch_num = self._find_pitch(pitch)
        alt_num = self._scale[i + offset]
        if named:
            pitch = self.pitchname(pitch_num)
            alt = self.pitchname(alt_num)
        else:
            pitch = pitch_num
            alt = alt_num
        x = self._duration_ticks(duration)
        y = round(x / number)
        z = round(x - (2 * y))
        if self.verbose:
            print(f"Durations: {x}, {y}, {z}")
        return [[y, pitch], [y, alt], [z, pitch]]

    def slide(self, duration: str, from_pitch: Union[str, int], to_pitch: Union[str, int]):
        # Always use chromatic scale for slide
        chromatic_scale = []
        for octave in range(-1, OCTAVES - 1):
            chromatic_scale += get_scale(self.scale_note, 'chromatic', octave)
        named = isinstance(from_pitch, str) and from_pitch[0] in 'ABCDEFG'
        i, from_num = self._find_pitch(from_pitch, chromatic_scale)
        j, to_num = self._find_pitch(to_pitch, chromatic_scale)
        start, end = (i, j) if i <= j else (j, i)
        x = self._duration_ticks(duration)
        y = end - start + 1
        z = round(x / y)
        if self.verbose:
            print(f"Durations: {x}, {y}, {z}")
        notes = []
        for idx in range(start, end + 1):
            midi_num = chromatic_scale[idx]
            if named:
                notes.append([z, self.pitchname(midi_num)])
            else:
                notes.append([z, midi_num])
        if j < i:
            notes = list(reversed(notes))
        return notes
