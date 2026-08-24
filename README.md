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
* `Textures/`: Directory containing placeholder PNGs for spiral galaxies, elliptical galaxies, and quasars.

**Other Directories**
* **`plots/`**: Generated analytical graphs and diagnostic plots.
* **`archive/`**: Previous iterations and primitive code versions.
* **`data/`**: Local directory for massive raw `.fits` catalogs and `.csv` outputs (ignored by git). 

## 🚀 Installation & Dependencies

This pipeline requires several scientific and astronomical Python libraries. Install them via pip:

```bash
pip install numpy pandas matplotlib scipy astropy kcorrect
```

## 🛠️ Pipeline Usage Instructions

1. Run `scripts/fitstocsv_fullsurvey.ipynb` to clean the raw data and export the initial spatial `.csv`.
2. Run `scripts/generate.py` to produce the `.cmap` and indexed master `.csv` files.
3. (Optional) Run `scripts/slice_wedge.py` to create specific subsets of the master catalog.
4. Load `desi_dr1.asset` or your generated wedge assets in your OpenSpace environment.

## 🌌 OpenSpace Setup & Integration

### File Placement
* Copy the contents of your `openspace_assets/` folder and your exported `.csv` data files into the `data/assets/` directory of your local OpenSpace installation.

### Enabling Assets in OpenSpace
1. Open your planetarium's main OpenSpace `.profile` file (located in the `data/profiles/` folder) using a basic text editor.
2. Scroll to the `asset.require` section and add the path to your asset file:
   ```lua
   asset.require("openspace_assets/desi_dr1")
   ```
3. Save the profile and launch OpenSpace. You can toggle the dataset on or off in the GUI menu under `/Universe/Galaxies/DESI`.

### Creating New Wedge Asset Files
To load individual data slices as separate toggles in the OpenSpace menu without restarting the software:

1. **Duplicate the Template:** Copy `openspace_assets/template_wedge.asset` and rename it (e.g., `wedge_RA0-30.asset`).
2. **Configure the Header Variables:** Open the duplicated file and set the three configuration variables at the very top:
   * **`wedge_identifier`**: A unique internal system name for OpenSpace (no spaces, e.g., `"DESI_Wedge_RA0_30"`). Every wedge must have a completely distinct identifier so OpenSpace does not crash when loading multiple files.
   * **`wedge_csv_file`**: The exact filename of your sliced CSV file exported by `slice_wedge.py` (e.g., `"wedge_RA0-30_DEC-10-10_Z0.01-0.5.csv"`).
   * **`wedge_gui_name`**: The display label that will actually appear next to the checkbox in the OpenSpace menu (e.g., `"Wedge 1 (RA 0-30)"`).
3. **Register in Profile:** Add the new wedge asset to your `.profile` file just like you did with the main survey:
   ```lua
   asset.require("openspace_assets/wedge_RA0-30")
   ```

## 🗺️ Project Roadmap

- [x] Map basic XYZ positions and k-corrected colors from DESI DR1.
- [x] **Dynamic Wedges:** Create a Python script to easily slice the universe into manageable data wedges.
- [x] **Planetarium Integration:** Set up individual wedge toggles in OpenSpace for live audience Q&A sessions.
- [ ] **Data Merging:** Combine pipeline with morphology and luminosity data by joining on `TARGETID`.
- [ ] **Realistic Rendering:** Map DESI morphology tags to specific OpenSpace textures and scale sizes logarithmically.
- [ ] **Automated Flythroughs:** Record seamless, looping flythroughs for the McPherson Lab display screens.
- [ ] **DR3 Integration:** Transition pipeline to support the upcoming DESI Data Release 3.