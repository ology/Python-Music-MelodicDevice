import sys
sys.path.append('./src')
from music_melodicdevice.music_melodicdevice import Device
import unittest

class TestMelodicDevice(unittest.TestCase):
    def test_transpose_chromatic(self):
        device = Device(notes=['C4', 'E4', 'D4', 'G4', 'C5'], verbose=False)
        self.assertEqual(device.transpose(2), ['D4', 'F#4', 'E4', 'A4', 'D5'])
        self.assertEqual(device.transpose(4), ['E4', 'G#4', 'F#4', 'B4', 'E5'])
        self.assertEqual(device.transpose(-2), ['A#3', 'D4', 'C4', 'F4', 'A#4'])
        self.assertEqual(device.transpose(-4), ['G#3', 'C4', 'A#3', 'D#4', 'G#4'])

    def test_transpose_major(self):
        device = Device(scale_name='major', verbose=False)
        device.notes = ['C4', 'E4', 'D4', 'G4', 'C5']
        self.assertEqual(device.transpose(2), ['E4', 'G4', 'F4', 'B4', 'E5'])
        self.assertEqual(device.transpose(4), ['G4', 'B4', 'A4', 'D5', 'G5'])
        self.assertEqual(device.transpose(-2), ['A3', 'C4', 'B3', 'E4', 'A4'])
        self.assertEqual(device.transpose(-4), ['F3', 'A3', 'G3', 'C4', 'F4'])

    def test_transpose_unknown_note(self):
        device = Device(notes=['C4', 'E4', 'D#4', 'G4', 'C5'], verbose=False)
        device.build_scale('major')
        self.assertEqual(device.transpose(2), ['E4', 'G4', None, 'B4', 'E5'])

    def test_inversion_note_names(self):
        device = Device(notes=['A4', 'C5', 'B4', 'A4', 'E5'], verbose=False)
        self.assertEqual(device.intervals(), [3, -1, -2, 7])
        device = Device(notes=['C4', 'A#3', 'G#3', 'A#3', 'G3'], verbose=False)
        self.assertEqual(device.invert('C4'), ['C4','D4','E4','D4','F4'])
        device = Device(notes=['C4', 'D4', 'E4', 'D4', 'F4'], verbose=False)
        self.assertEqual(device.invert('C4'), ['C4', 'A#3', 'G#3', 'A#3', 'G3'])
        device = Device(notes=['C4', 'D4', 'E4', 'D4', 'F4'], verbose=False)
        self.assertEqual(device.invert('C#4'), ['D4', 'C4', 'A#3', 'C4', 'A3'])
        # https://en.wikipedia.org/wiki/Inversion_(music)#Melodies
        device = Device(verbose=True)
        notes = ['A#4','E4','F#4','D#4','F4','A4','D5','C#5','G4','G#4','B4','C5']
        self.assertEqual(device.intervals(notes), [-6, 2, -3, 2, 4, 5, -1, -6, 1, 3, 1])
        expect = ['A#4','E5','D5','F5','D#5','B4','F#4','G4','C#5','C5','A4','G#4']
        got = device.invert('A#4', notes)
        self.assertEqual(got, expect)
        notes = ['C4', 'E4', 'D4', 'G4', 'C5']
        self.assertEqual(device.intervals(notes), [4, -2, 5, 5])
        expect = ['C4','G#3','A#3','F3','C3']
        got = device.invert('C4', notes)
        self.assertEqual(got, expect)

    # def test_inversion_diatonic(self):
    #     obj = Inversion(scale_name='major')
    #     notes = ['C4', 'E4', 'D4', 'G4', 'C5']
    #     expect = [2, -1, 3, 3]
    #     got = obj.intervals(notes)
    #     self.assertEqual(got, expect)
    #     expect = ['C4', 'A3', 'B3', 'F3', 'C3']
    #     got = obj.invert('C4', notes)
    #     self.assertEqual(got, expect)
    #     # https://en.wikipedia.org/wiki/Inversion_(music)#Melodies
    #     notes = ['G4', 'A4', 'G4', 'F4', 'G4', 'A4', 'B4', 'A4', 'G4', 'A4']
    #     expect = [1, -1, -1, 1, 1, 1, -1, -1, 1]
    #     got = obj.intervals(notes)
    #     self.assertEqual(got, expect)
    #     expect = ['D3', 'C3', 'D3', 'E3', 'D3', 'C3', 'B2', 'C3', 'D3', 'C3']
    #     got = obj.invert('D3', notes)
    #     self.assertEqual(got, expect)

if __name__ == '__main__':
    unittest.main()
