import numpy as np
import matplotlib.pyplot as plt


years = np.array(list(range(1947, 2026)))
MussabRuns = np.array(list(np.random.rand(len(years))*50), dtype=int)
JhonRuns = np.array(list(np.random.rand(len(years))*70), dtype=int)
MRRuns = np.array(list(np.random.rand(len(years))*80), dtype=int)


plt.plot(years, MussabRuns, color='blue', linestyle='-', label="Mussab's Runs")
plt.plot(years, JhonRuns, color='orange', linestyle='--', label="Jhon's Runs")
plt.plot(years, MRRuns, color='red', linestyle='-.', label="MR's Runs")
with plt.xkcd():
    plt.title("Cricket Runs Over Years")
    plt.xlabel("Years")
    plt.ylabel("Runs Scored")
    plt.legend()
    plt.tight_layout()
    plt.show()
