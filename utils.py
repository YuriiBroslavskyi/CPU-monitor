# - A helper module for small, reusable functions.
# - Examples:
#     • format_frequency(value) → "3.40 GHz"
#     • format_usage_list(list_of_percentages) → "Core0: 20% | Core1: 15% ..."
#     • safe_round(value, digits) → rounded float or default value
#     • time formatting, unit conversions, etc.
# - Keeps your main code clean and readable.

import numpy as np
from system_info import SystemInfo
import matplotlib.pyplot as plt

class Utils:
    def createDiagram(self):
        dynamic_sys_info = SystemInfo().get_dynamic_info()

        x = np.array([
            f"Core-{i + 1}" for i in range(len(dynamic_sys_info["cpu_usage"]))
        ])
        y = np.array(dynamic_sys_info["cpu_usage"])

        fig, ax = plt.subplots(figsize=(8, 4))

        colors = ["red" if usage > 50 else "skyblue" for usage in y]
        ax.bar(x, y, color=colors)

        ax.set_title("CPU Usage per Core")
        ax.set_xlabel("Core")
        ax.set_ylabel("Usage (%)")
        ax.set_ylim(0, 100)
        plt.tight_layout()

        # Return the figure instead of showing it
        return fig