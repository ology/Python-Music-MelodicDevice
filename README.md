# Python-Music-MelodicDevice
Apply traditional transformations to music notes

## DESCRIPTION

TODO

## SYNOPSIS
```python
from music_melodicdevice import Device

# default scale: chromatic
device = Device(notes=['C4', 'E4', 'D4', 'G4', 'C5'])
transposed = device.transpose(2) # ['D4', 'F#4', 'E4', 'A4', 'D5']

# diatonic transposition:
device = Device(scale_name='major', verbose=True)
device.notes = ['C4', 'E4', 'D4', 'G4', 'C5']
transposed = device.transpose(2) # ['E4', 'G4', 'F4', 'B4', 'E5']

# unknown note:
device = Device()
device.build_scale('major')
transposed = device.transpose(2, ['C4', 'E4', 'D#4', 'G4', 'C5'])
# ['E4', 'G4', None, 'B4', 'E5'])
```

## MUSICAL EXAMPLES
```python
# TODO
```
