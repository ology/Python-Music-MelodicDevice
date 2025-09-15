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
        device = Device(notes=['C4', 'E4', 'D4', 'G4', 'C5'], scale_name='major', verbose=False)
        device.notes = ['C4', 'E4', 'D4', 'G4', 'C5']
        self.assertEqual(device.transpose(2), ['E4', 'G4', 'F4', 'B4', 'E5'])
        self.assertEqual(device.transpose(4), ['G4', 'B4', 'A4', 'D5', 'G5'])
        self.assertEqual(device.transpose(-2), ['A3', 'C4', 'B3', 'E4', 'A4'])
        self.assertEqual(device.transpose(-4), ['F3', 'A3', 'G3', 'C4', 'F4'])

    def test_transpose_unknown_note(self):
        device = Device(notes=['C4', 'E4', 'D#4', 'G4', 'C5'], scale_name='major')
        self.assertEqual(device.transpose(2), ['E4', 'G4', None, 'B4', 'E5'])

    # def test_transpose_notes_method(self):
    #     self.device = Device(scale_name='major')
    #     notes = ['C4', 'E4', 'G4']
    #     expect = ['G4', 'B4', 'D5']
    #     self.device.notes = notes
    #     got = self.device.transpose(4)
    #     self.assertEqual(got, expect)

if __name__ == '__main__':
    unittest.main()
