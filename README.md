# Music Melodic-Device
Apply traditional transformations to music notes

## DESCRIPTION

TODO

## SYNOPSIS
```python
from music_melodicdevice import Device

# default scale: chromatic
device = Device(notes=['C4', 'E4', 'D4', 'G4', 'C5'])
transposed = device.transpose(2) # ['D4', 'F#4', 'E4', 'A4', 'D5']
inverted = device.invert('C4') # ['C4', 'G#3', 'A#3', 'F3', 'C3']

# diatonic transposition:
device = Device(scale_name='major', verbose=True)
device.notes = ['C4', 'E4', 'D4', 'G4', 'C5']
transposed = device.transpose(2) # ['E4', 'G4', 'F4', 'B4', 'E5']
inverted = device.invert('C4') # ['C4', 'A3', 'B3', 'F3', 'C3']

# unknown note:
device = Device()
device.build_scale('major')
transposed = device.transpose(2, ['C4', 'E4', 'D#4', 'G4', 'C5'])
# ['E4', 'G4', None, 'B4', 'E5']
inverted = device.invert('C4', ['C4', 'E4', 'D#4', 'G4', 'C5'])
# ['C4', 'A3', None, 'F3', 'C3']
```

## MUSICAL EXAMPLES
```python
# TODO
```
