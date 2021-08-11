In this folder i present code that you, the user, can use to do exposure time calculations for the Nancy Grace Roman Space Telescope. 
You can apply this code to two kinds of objects: point sources, and extended sources with half-light radii of 0.20 arcsec or 0.3 arcsec.
When running the gui or the notebook you will be asked to select your filter, the Zodical light contribution, the S/N, and the nature of your source.
The options for each are discussed below:

- Filters: F062, F087, F106, F129, F158, F184, F146, F213
- Zodiacal light contributions (multiples of the minimum): 1.4, 2.0, 3.0
- Source: point sources, half-light radius = 0.2", half-light radius = 0.3"
- S/N: 5, 10, 15, 20, 50

Exposure times are quantized in multiples of 3 readout frames, with the number of visits/dithers: 1
You can calculate either the magnitude for an object at a for a given exposure time and a S/N, or the exposure time needed for a given magnitude.
