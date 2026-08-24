# DESI OpenSpace Visualization Pipeline

This repository contains a data processing pipeline designed to convert Dark Energy Spectroscopic Instrument (DESI) catalogs into 3D Cartesian coordinates and color-indexed datasets optimized for the OpenSpace visualization engine. 

This work is part of an ongoing project at The Ohio State University's Planetarium (building upon SURP research) to create highly realistic, immersive 3D flythroughs of the universe.

## Repository Structure

The repository is organized to separate production scripts, OpenSpace rendering assets, and data:

* **`scripts/`**: Core processing code.
  * `fitstocsv_fullsurvey.ipynb`: Ingests raw DESI `.fits` catalogs, applies strict quality assurance filters, calculates comoving distances (XYZ coordinates), and uses `kcorrect` to compute rest-frame optical colors.
  * `generate.py`: Quantizes the original galaxy RGB values into exactly 1000 distinct color buckets to optimize rendering performance, generates a `.cmap` file, and exports an indexed `.csv`.
* **`openspace_assets/`**: Files directly read by OpenSpace.
  * `desi_dr1.asset`: The main Lua configuration file to load the catalog into OpenSpace.
  * `lupton_palette.cmap`: The color map linking quantized color IDs to specific RGB values.
  * `galaxy_sprites.tmap`: Lua mapping for rendering galaxy textures (in progress).
  * `Textures/`: Directory containing placeholder PNGs for spiral galaxies, elliptical galaxies, and quasars.
* **`plots/`**: Generated analytical graphs and diagnostic plots (e.g., Redshift vs. Color Index).
* **`archive/`**: Previous iterations, tests, and primitive code versions.
* **`data/`**: *(Not tracked in version control)* Local directory for massive raw `.fits` catalogs and generated `.csv` outputs. 

## Installation & Dependencies

This pipeline requires several scientific and astronomical Python libraries. Install them via pip:

```bash
pip install numpy pandas matplotlib scipy astropy kcorrect
```

## Usage Instructions

1. **Process Raw Data:** Run `scripts/fitstocsv_fullsurvey.ipynb` to clean the raw `.fits` data and export the initial spatial `.csv`.
2. **Quantize Colors:** Update the file paths in `scripts/generate.py` to match your local setup, then run the script to produce the `.cmap` and indexed `.csv` files.
3. **Render:** Load `desi_dr1.asset` in your OpenSpace environment.

## Project Roadmap & Next Steps

This project is actively being developed with the following milestones:

- [x] Map basic XYZ positions and k-corrected colors from DESI DR1.
- [ ] **Data Merging:** Combine the current pipeline with morphology data (Kyle) and luminosity data (Torston) by joining on the unique `TARGETID`.
- [ ] **Realistic Rendering:** Map DESI morphology tags to specific OpenSpace textures and scale sizes logarithmically based on intrinsic brightness.
- [ ] **Dynamic Wedges:** Create a Python script to easily slice the universe into manageable data wedges parameterized by RA, DEC, and Z ranges.
- [ ] **Planetarium Integration:** Set up individual wedge toggles in OpenSpace for live audience Q&A sessions.
- [ ] **Automated Flythroughs:** Record seamless, looping flythroughs for the McPherson Lab display screens.
- [ ] **DR3 Integration:** Transition pipeline to support the upcoming DESI Data Release 3.