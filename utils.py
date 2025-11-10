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

import requests
from bs4 import BeautifulSoup
import urllib.parse
import cpuinfo


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

    # def convMHzToGHz(self):
    #     dynamic_sys_info = SystemInfo().get_dynamic_info()
    #
    #     return dynamic_sys_info["cpu_freq"] * 1e-9

    def get_cpu_multithread_rating(self):
        cpu_name = cpuinfo.get_cpu_info().get('brand_raw', 'CPU name not available')
        encoded_cpu_name = urllib.parse.quote(cpu_name)
        base_url = "https://www.cpubenchmark.net/cpu.php?cpu="
        url = f"{base_url}{encoded_cpu_name}"

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                          '(KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
        }

        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            rating_element = soup.find(string="Multithread Rating")
            if rating_element:
                rating_value = rating_element.find_next().text.strip()
                print(rating_value)
                return rating_value
            else:
                return f"Unable to find the multi-thread rating for {cpu_name} on the page."
        else:
            return f"Failed to retrieve the page. Status code: {response.status_code}"