import pandas as pd
#takes csv made from fitstocsv_fullsurvey.ipynb and generates a .cmap file for OpenSpace
#Make sure to change the INPUT_CSV_PATH, OUTPUT_CSV_PATH, and CMAP_OUTPUT_PATH variables below to your desired paths before running this script.
# --- Configuration ---
INPUT_CSV_PATH = "/users/PCON0003/ulricclaar/desi-openspace-visualization/openspace_assets/desi_catalog_fullsurvey_0-1-3.csv" 
OUTPUT_CSV_PATH = "/users/PCON0003/ulricclaar/desi-openspace-visualization/openspace_assets/desi_catalog_indexed_0-1-3.csv"
CMAP_OUTPUT_PATH = "/users/PCON0003/ulricclaar/desi-openspace-visualization/openspace_assets/lupton_palette_0-1-3.cmap"

print("1/4: Loading data into pandas...")
df = pd.read_csv(INPUT_CSV_PATH)

print("2/4: Mathematically quantizing into 1000 colors...")
# Multiply by 9.999 and truncate to an integer to get 10 distinct buckets (0 through 9)
r_bin = (df['color_r'] * 9.999).astype(int)
g_bin = (df['color_g'] * 9.999).astype(int)
b_bin = (df['color_b'] * 9.999).astype(int)

# Combine into a single ID from 0 to 999
# Example: R=9, G=5, B=1 becomes ID 951
df['color_id'] = r_bin * 100 + g_bin * 10 + b_bin

print("3/4: Generating .cmap file with 1000 colors...")
with open(CMAP_OUTPUT_PATH, 'w') as f:
    f.write("1000\n") # Tell OpenSpace to expect 1000 colors
    
    # Generate the exact RGB values for IDs 0 through 999
    for i in range(1000):
        # Reverse the math to get the float values back
        r = (i // 100) / 9.0
        g = ((i // 10) % 10) / 9.0
        b = (i % 10) / 9.0
        f.write(f"{r:.6f} {g:.6f} {b:.6f} 1.0\n")

print("4/4: Saving final .csv...")
df = df.drop(columns=['color_r', 'color_g', 'color_b'])
df.to_csv(OUTPUT_CSV_PATH, index=False) 

print("SUCCESS! Process complete.") 