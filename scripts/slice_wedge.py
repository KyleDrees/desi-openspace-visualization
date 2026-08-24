import pandas as pd

# Update this path if your data folder is located elsewhere
MASTER_CSV_PATH = "/users/PCON0003/ulricclaar/desi-openspace-visualization/data/desi_catalog_indexed.csv"

print("--- DESI OpenSpace Wedge Slicer ---")
print("Please enter your wedge boundaries:\n")

# Prompt the user for input and convert it to numbers
ra_min = float(input("Minimum RA (0 to 360): "))
ra_max = float(input("Maximum RA (0 to 360): "))
dec_min = float(input("Minimum DEC (-90 to 90): "))
dec_max = float(input("Maximum DEC (-90 to 90): "))
z_min = float(input("Minimum Redshift Z (e.g., 0.01): "))
z_max = float(input("Maximum Redshift Z (e.g., 3.0): "))

print("\nLoading master catalog...")
df = pd.read_csv(MASTER_CSV_PATH)

print("Slicing the universe...")
# Filter the data based on the user's inputs
wedge = df[
    (df['TARGET_RA'] >= ra_min) & (df['TARGET_RA'] <= ra_max) &
    (df['TARGET_DEC'] >= dec_min) & (df['TARGET_DEC'] <= dec_max) &
    (df['Z'] >= z_min) & (df['Z'] <= z_max)
]

# Generate a smart filename based on the inputs
filename = f"../data/wedge_RA{int(ra_min)}-{int(ra_max)}_DEC{int(dec_min)}-{int(dec_max)}_Z{z_min}-{z_max}.csv"

# Export the new wedge
wedge.to_csv(filename, index=False)
print(f"Success! Saved {len(wedge)} objects to {filename}")