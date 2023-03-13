# jds6600_python

Python class to remote-control a Junce-Instrument JDS6600 signal generator, using the USB-connection (serial-line emulation)

- version 0.0.1 (2018/01/19): initial release, reading basic parameters
- version 0.0.2 (2018/01/28): added "measure" menu + support functions, documtation
- version 0.0.3 (2018/02/07): added "counter" and "sweep" menu
- version 0.0.4 (2018/02/14): added "pulse" and "burst" menu + codecleanup
- version 0.0.5 (2018/02/16): added system menu
- version 0.1.0 (2018/02/17): added arbitrary waveform 
- version 0.1.1:(2023/03/04): line_end is now chr(0x0d)+chr(0x0a) for the api of the newer machines instead of chr(0x0a) for the older ones. Should work also with the single ending (0x0a). Also backward compatibility with the old serial library for Python implemented.


## API
For the API-calls, see api.txt

## Examples
See examples/readjds.py


## License
MIT license. See "LICENSE" for more info


ENJOY!!!


TO DO:
- add docstrings


Andreas
