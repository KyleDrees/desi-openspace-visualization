# DESI OpenSpace Visualization Pipeline

This repository contains a data processing pipeline designed to convert Dark Energy Spectroscopic Instrument (DESI) catalogs into 3D Cartesian coordinates and color-indexed datasets optimized for the OpenSpace visualization engine. 

This work is part of an ongoing project at The Ohio State University's Planetarium to create highly realistic, immersive 3D flythroughs of the universe.

## 📁 Repository Structure

**Production Scripts (`scripts/`)**
* `fitstocsv_fullsurvey.ipynb`: Ingests raw DESI catalogs, applies quality filters, calculates Cartesian coordinates, and computes rest-frame optical colors.
* `generate.py`: Quantizes RGB values into 1000 distinct colors to optimize rendering, generates a `.cmap` file, and exports an indexed `.csv`.
* `slice_wedge.py`: An interactive tool to slice the master catalog into smaller data wedges based on user-defined coordinate and redshift ranges.

**OpenSpace Assets (`openspace_assets/`)**
* `desi_dr1.asset`: Main Lua configuration to load the full catalog (starts disabled for live planetarium reveals).
* `template_wedge.asset`: A reusable Lua template for loading individual data slices.
* `lupton_palette.cmap`: The color map linking quantized color IDs to specific RGB values.
* `galaxy_sprites.tmap`: Lua mapping for rendering galaxy textures.

**Other Directories**
* **`plots/`**: Generated analytical graphs and diagnostic plots.
* **`archive/`**: Previous iterations and primitive code versions.
* **`data/`**: Local directory for massive raw `.fits` catalogs and `.csv` outputs (ignored by git). 

## 🚀 Installation & Dependencies

This pipeline requires several scientific and astronomical Python libraries. Install them via pip:

`pip install numpy pandas matplotlib scipy astropy kcorrect`

## 🛠️ Usage Instructions

1. Run `scripts/fitstocsv_fullsurvey.ipynb` to clean the raw data and export the initial spatial `.csv`.
2. Run `scripts/generate.py` to produce the `.cmap` and indexed master `.csv` files.
3. (Optional) Run `scripts/slice_wedge.py` to create specific subsets of the master catalog.
4. Load `desi_dr1.asset` or your generated wedge assets in your OpenSpace environment.

## 🗺️ Project Roadmap

- [x] Map basic XYZ positions and k-corrected colors from DESI DR1.
- [x] **Dynamic Wedges:** Create a Python script to easily slice the universe into manageable data wedges.
- [x] **Planetarium Integration:** Set up individual wedge toggles in OpenSpace for live audience Q&A sessions.
- [ ] **Data Merging:** Combine pipeline with morphology and luminosity data by joining on `TARGETID`.
- [ ] **Realistic Rendering:** Map DESI morphology tags to specific OpenSpace textures and scale sizes logarithmically.
- [ ] **Automated Flythroughs:** Record seamless, looping flythroughs for the McPherson Lab display screens.
- [ ] **DR3 Integration:** Transition pipeline to support the upcoming DESI Data Release 3.