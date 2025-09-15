import sys
sys.path.append('./src')
from music_melodicdevice.music_melodicdevice import Device
import unittest

class TestMelodicDevice(unittest.TestCase):
    def setUp(self):
        self.device = Device(verbose=True)
        self.notes = ['C4', 'E4', 'D4', 'G4', 'C5']
        self.nums = [60, 64, 62, 67, 72]

    def test_transpose_chromatic(self):
        expect = ['D4', 'F#4', 'E4', 'A4', 'D5']
        got = self.device.transpose(2, self.notes)
        self.assertEqual(got, expect)
        expect = ['E4', 'G#4', 'F#4', 'B4', 'E5']
        got = self.device.transpose(4, self.notes)
        self.assertEqual(got, expect)
        expect = ['A#3', 'D4', 'C4', 'F4', 'A#4']
        got = self.device.transpose(-2, self.notes)
        self.assertEqual(got, expect)
        expect = ['G#3', 'C4', 'A#3', 'D#4', 'G#4']
        got = self.device.transpose(-4, self.notes)
        self.assertEqual(got, expect)

    def test_transpose_chromatic_nums(self):
        expect = [62, 66, 64, 69, 74]
        got = self.device.transpose(2, self.nums)
        self.assertEqual(got, expect)
        expect = [64, 68, 66, 71, 76]
        got = self.device.transpose(4, self.nums)
        self.assertEqual(got, expect)
        expect = [58, 62, 60, 65, 70]
        got = self.device.transpose(-2, self.nums)
        self.assertEqual(got, expect)
        expect = [56, 60, 58, 63, 68]
        got = self.device.transpose(-4, self.nums)
        self.assertEqual(got, expect)

    def test_transpose_major(self):
        self.device = Device(scale_name='major')
        expect = ['E4', 'G4', 'F4', 'B4', 'E5']
        got = self.device.transpose(2, self.notes)
        self.assertEqual(got, expect)
        expect = ['G4', 'B4', 'A4', 'D5', 'G5']
        got = self.device.transpose(4, self.notes)
        self.assertEqual(got, expect)
        expect = ['A3', 'C4', 'B3', 'E4', 'A4']
        got = self.device.transpose(-2, self.notes)
        self.assertEqual(got, expect)
        expect = ['F3', 'A3', 'G3', 'C4', 'F4']
        got = self.device.transpose(-4, self.notes)
        self.assertEqual(got, expect)

    def test_transpose_major_nums(self):
        self.device = Device(scale_name='major')
        expect = [64, 67, 65, 71, 76]
        got = self.device.transpose(2, self.nums)
        self.assertEqual(got, expect)
        expect = [67, 71, 69, 74, 79]
        got = self.device.transpose(4, self.nums)
        self.assertEqual(got, expect)
        expect = [57, 60, 59, 64, 69]
        got = self.device.transpose(-2, self.nums)
        self.assertEqual(got, expect)
        expect = [53, 57, 55, 60, 65]
        got = self.device.transpose(-4, self.nums)
        self.assertEqual(got, expect)

    def test_transpose_unknown_note(self):
        self.device = Device(scale_name='major')
        notes = ['C4', 'E4', 'D#4', 'G4', 'C5']
        expect = ['E4', 'G4', None, 'B4', 'E5']
        got = self.device.transpose(2, notes)
        self.assertEqual(got, expect)

    def test_transpose_unknown_num(self):
        self.device = Device(scale_name='major')
        nums = [60, 64, 63, 67, 72]
        expect = [64, 67, None, 71, 76]
        got = self.device.transpose(2, nums)
        self.assertEqual(got, expect)

    def test_transpose_notes_method(self):
        self.device = Device(scale_name='major')
        notes = ['C4', 'E4', 'G4']
        expect = ['G4', 'B4', 'D5']
        self.device.notes = notes
        got = self.device.transpose(4)
        self.assertEqual(got, expect)

if __name__ == '__main__':
    unittest.main()
