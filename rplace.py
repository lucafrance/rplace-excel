import pandas as pd

raw_df = pd.read_csv("tile_placements_sorted.csv")

# Calculate the most recent timestamp for each pair of coordinates
last_changes = raw_df.pivot_table(index=["x_coordinate", "y_coordinate"], values="ts", aggfunc=max)

# Use consistent indexes to allow joining
raw_df.set_index(["ts", "x_coordinate", "y_coordinate"], inplace=True)
last_changes.set_index("ts", append=True, inplace=True)

# Join the color for the most recent change
last_changes = last_changes.join(raw_df, on=["ts", "x_coordinate", "y_coordinate"], how="left")

# Export to csv
last_changes.reset_index(inplace=True)
last_changes.sort_values(["x_coordinate", "y_coordinate", "color"], inplace=True)
last_changes.drop_duplicates(inplace=True)
last_changes.to_csv("tile_placements_last.csv", columns=["x_coordinate", "y_coordinate", "color"], index=False)
