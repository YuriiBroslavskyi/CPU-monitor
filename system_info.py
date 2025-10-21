# - Contains all logic for collecting system information.
# - Uses psutil for dynamic system data.
# - Uses cpuinfo for static hardware data.
# - This module has no GUI code — it only provides data.
#
# - Class Structure:
#     class SystemInfo:
#         - __init__(self):
#             • Load CPU static data once using cpuinfo.
#             • Store it for quick access later.
#
#         - get_static_info(self):
#             • Return static CPU information as a dictionary:
#                 - CPU brand/model name
#                 - Architecture
#                 - Physical cores
#                 - Logical threads
#                 - Any other constant data
#
#         - get_dynamic_info(self):
#             • Return dynamic CPU information as a dictionary:
#                 - Current frequency (MHz)
#                 - CPU usage percentage per core
#                 - Optional: temperature, load average, etc.
#
#         - (optional) get_memory_info(), get_disk_info(), etc.:
#             • Extend later if you want to show more system stats.
import cpuinfo
import psutil

class SystemInfo:
    def __init__(self):
        self.cpuinfo_static = cpuinfo.get_cpu_info()

    def get_static_info(self):
        self.cpu_brand = self.cpuinfo_static.get("brand_raw", "Unknown")
        self.cpu_arch = self.cpuinfo_static.get("arch", "Unknown")
        self.cpu_bits = self.cpuinfo_static.get("bits", "Unknown")
        self.python_version = self.cpuinfo_static.get("python_version", "Unknown")
        self.cpu_l1_cache_size = self.cpuinfo_static.get("l1_cache_size", "Unknown")
        self.cpu_l2_cache_size = self.cpuinfo_static.get("l2_cache_size", "Unknown")
        self.cpu_l3_cache_size = self.cpuinfo_static.get("l3_cache_size", "Unknown")
        self.cpu_physical_cores = psutil.cpu_count(logical=False)
        self.cpu_logical_cores = psutil.cpu_count(logical=True)

        return {
            "brand": self.cpu_brand,
            "arch": self.cpu_arch,
            "bits": self.cpu_bits,
            "python_version": self.python_version,
            "l1_cache": self.cpu_l1_cache_size,
            "l2_cache": self.cpu_l2_cache_size,
            "l3_cache": self.cpu_l3_cache_size,
            "physical_cores": self.cpu_physical_cores,
            "logical_cores": self.cpu_logical_cores,
        }

    def get_dynamic_info(self):
        self.cpu_freq = psutil.cpu_freq().current
        self.cpu_usage = psutil.cpu_percent()

        return {
            "cpu_freq": self.cpu_freq,
            "cpu_usage": self.cpu_usage
        }