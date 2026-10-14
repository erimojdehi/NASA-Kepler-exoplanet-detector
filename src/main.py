
import lightkurve as lk
import matplotlib.pyplot as plt

target = "Kepler-10"


# Search available datasets
results = lk.search_lightcurve(
    target,
    author="Kepler"
)

print(f"Found {len(results)} datasets")
print(results)


# Download the first dataset
lc = results[0].download()

if lc is None:
    raise RuntimeError("Download failed")

# Inspect its contents
print("\nDownloaded dataset:")
print(lc)

# Clean and normalize brightness values
lc = lc.remove_nans().normalize()

# Plot brightness over time
lc.plot()
plt.title(f"{target} - Kepler Observations")

# Save the graph
plt.savefig("kepler10_lightcurve.png", dpi=150)
print("\nGraph saved: kepler10_lightcurve.png")