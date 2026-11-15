---
baslik: BIL437 Computer Vision: Remote Sensing and Digital Image Processing (University of South Carolina, John R. Jensen)
ozet: Dr. John R. Jensen's (University of South Carolina, Geography) Remote Sensing and Digital Image Processing lecture presentations: in situ data and remote sensing, the process, advantages and limitations, and sensor systems such as Landsat, SPOT, AVHRR, MODIS, IKONOS, and AVIRIS.
---

The five presentations distributed in the final part of the BIL437 Computer Vision course (lecture6_1 and lecture6_2_1 – 6_2_4) are "Remote Sensing and Digital Image Processing" lecture slides prepared by **Dr. John R. Jensen** (Department of Geography, University of South Carolina, Columbia); the source note on the slides reads "Jensen, 2000/2003/2004". The text of the presentations is summarized below; since the presentations are mostly filled with satellite and aerial images, the images have not been transcribed. The originals of the five presentations can be downloaded as a ZIP at the end of the post.

*Note: This content belongs to a third-party source; it is shared for archival and nostalgic purposes with the source credited. It will be removed upon request by the rights holder.*

## 1. What is remote sensing? (lecture6_1)

**The purpose of science** is to discover universal truths. Scientists observe and measure the physical world, living organisms, and processes (erosion, deforestation, urban sprawl).

### In situ data

The data needed to accept or reject a hypothesis can be collected directly in the field; this is called *in situ* data. This is time-consuming, expensive, and error-prone. Errors arising from the method may stem from the following: the sampling design failing to capture the spatial variability of the phenomenon (some places are sampled heavily, others sparsely), measurement instruments being used incorrectly, and instruments not being calibrated. It is wrong to call in situ measurements "ground truth"; we should call them "ground reference data," because they also contain error. Example in situ measurements: spectroradiometer measurements and leaf area index (LAI) measurements on soybeans.

### Definition of remote sensing

The combined ASPRS definition (Colwell, 1997): photogrammetry and remote sensing is "the art, science, and technology of obtaining reliable information about physical objects and the environment, through the process of recording, measuring, and interpreting imagery and digital representations of energy patterns derived from noncontact sensor systems." A remote sensing instrument collects information about an object or phenomenon within the sensor's instantaneous field of view (IFOV) without direct physical contact with it; the sensor is on an airborne (suborbital) or satellite platform.

### Observations

- Is remote sensing a science? According to the presentation, remote sensing is a tool/technique, similar to mathematics: remotely measuring the electromagnetic radiation (EMR) leaving an object and converting it into information with mathematical and statistical algorithms is a scientific activity, and it works in harmony with the other tools of the mapping sciences (cartography, GIS).
- With sensors, information can be obtained about an object (for example, poplar crown diameter) or the geographic extent of a phenomenon; the reflected, emitted, or backscattered EMR is a surrogate for the actual property and must be calibrated and converted into information through visual and/or digital image processing.

### Advantages

- If the sensor records only reflected or emitted EMR (passive), it does not disturb the object of interest.
- Data can be collected systematically (for example, a 9×9 inch vertical aerial photograph frame); this can eliminate the sampling bias present in some in situ studies.
- Under controlled conditions, it can provide basic biophysical information such as x, y location, z elevation or depth, biomass, temperature, and moisture content.
- It has become critical for modeling processes such as water supply estimation, eutrophication, and nonpoint-source pollution; and land-use change, water demand, and population forecasting on the urban fringe.

### Limitations

- The biggest limitation is that it is often oversold; it is not a cure-all that provides every kind of information, but an effort to provide spatial, spectral, and temporal information efficiently and economically.
- Humans choose the sensing system, its resolutions, calibration, platform, timing, and processing method; these choices can introduce error.
- Powerful active systems that emit their own radiation, such as LIDAR, RADAR, and SONAR, can affect the phenomenon being studied.
- Sensors can lose their calibration; collecting and processing data can be expensive.

### The remote sensing process

1. The hypothesis is defined (inductive/deductive; deterministic or probabilistic model).
2. In situ and ancillary data are collected to calibrate the sensor data and to evaluate its geometric, radiometric, and thematic characteristics.
3. Remote sensor data are collected with passive or active, analog or digital instruments (preferably at the same time as the in situ data).
4. The data are processed through analog/digital image processing, modeling, and n-dimensional visualization.
5. Metadata, processing history, and accuracy information are provided; results are communicated in forms such as images, graphics, statistical tables, GIS databases, and spatial decision support systems.

The radiance recorded within the IFOV of an optical sensor is a function of variables such as L (W m⁻² sr⁻¹), wavelength λ, the spectral response of the location s(x, y, z), time t, polarization, and so on.

## 2. Remote sensing data collection (lecture6_2_1 – 6_2_4)

A digital image is obtained in two ways: (1) digitizing an analog (printed) image; (2) sensors such as Landsat 7 ETM+ that already provide data in digital form. Types of analog aerial photographs: black-and-white panchromatic, infrared, natural color, and false-color infrared. Digitization uses scanners with linear-array or area-array CCDs; the relationship between the digitizer's instantaneous field of view (dpi or micrometers) and the pixel ground resolution given the photograph scale is shown.

The presentations then introduce the following systems in turn (with sensor characteristics, bands, resolutions, and sample images):

- **Landsat MSS** (Landsat 1–5): Multispectral Scanner, sun-synchronous orbit, 79×79 m IFOV; **Landsat 4–5 Thematic Mapper (TM)**: seven bands, 30×30 m; leaf reflectance and moisture content; **Landsat 7 ETM+** (30×30 m, first image 18 April 1999, Sioux Falls).
- **GOES** (East/West coverage areas, infrared imagery), **AVHRR** (data acquisition characteristics, bandwidths, global NDVI vegetation index image).
- Airborne systems: **Daedalus AMS**, **ATLAS** (near-infrared band 6), scaled 2.5×2.5 m scan images, ground temperature map of Four Mile Creek (infrared, temperature density slicing).
- **SPOT** (HRV, CCD linear array, 10×10 m panchromatic; comparison of detail and coverage with Landsat TM; SPOT Vegetation, 10-day global synthesis), **IRS-1D** (5×5 m), **ASTER** (15×15 m), **MODIS** (2,330 km swath width, Nile Delta image), **MISR**.
- High-resolution commercial satellites: **EROS A1** (1.8 m), **IKONOS** (1×1 m panchromatic, 4×4 m multispectral, stereo pair, "pan-sharpened" merged image).
- **Imaging spectrometry**: **AVIRIS** data cube and hyperspectral product classification; digital frame cameras (Positive Systems, Emerge Spatial); digital array panoramic camera with 32,000×8,000 detectors; SPIN-2.
