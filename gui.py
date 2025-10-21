# - Contains a class, e.g. CPUMonitorGUI, which handles all user interface logic.
# - This class is responsible for:
#     • Creating and laying out widgets (labels, frames, charts, etc.).
#     • Displaying static CPU info (model, architecture, cores, threads).
#     • Periodically updating dynamic info (frequency, usage per core, etc.).
#     • Handling the update loop using a scheduler (like root.after in Tkinter).
# - Class Structure:
#     class CPUMonitorGUI:
#         - __init__(self, root):
#             • Initialize the main window.
#             • Create labels or other widgets for static/dynamic info.
#             • Instantiate the SystemInfo class (from system_info.py).
#             • Call internal setup methods like display_static_info() and update_dynamic_info().
#
#         - display_static_info(self):
#             • Fetch static CPU data from SystemInfo.
#             • Format and display it in the GUI.
#             • Called once during initialization.
#
#         - update_dynamic_info(self):
#             • Fetch dynamic CPU data from SystemInfo.
#             • Update the relevant widgets.
#             • Schedule itself to run again after a time interval (e.g., 1000 ms).
#
# - Optional additions:
#     • Method to stop or pause updates.
#     • Method to display charts or visual indicators.
#     • Event handlers (like refresh button, theme switch, etc.).

import customtkinter
from system_info import SystemInfo

class CPUMonitorGUI(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("800x500")
        self.title("CPU monitor")
        static_sys_info = SystemInfo().get_static_info()
        dynamic_sys_info = SystemInfo().get_dynamic_info()

        self.cpu_brand_label = customtkinter.CTkLabel(self, text=f"CPU brand: {static_sys_info["brand"]}", fg_color="transparent")
        self.cpu_arch_label = customtkinter.CTkLabel(self, text=f"CPU arch: {static_sys_info["arch"]}", fg_color="transparent")
        self.cpu_bits_label = customtkinter.CTkLabel(self, text=f"CPU bits: {static_sys_info["bits"]}", fg_color="transparent")
        self.cpu_l1_cache_label = customtkinter.CTkLabel(self, text=f"CPU L1 cache size: {static_sys_info["l1_cache"]}", fg_color="transparent")
        self.cpu_l2_cache_label = customtkinter.CTkLabel(self, text=f"CPU L2 cache size: {static_sys_info["l2_cache"]}", fg_color="transparent")
        self.cpu_l3_cache_label = customtkinter.CTkLabel(self, text=f"CPU L3 cache size: {static_sys_info["l3_cache"]}", fg_color="transparent")
        self.cpu_physical_cores_label = customtkinter.CTkLabel(self, text=f"CPU physical cores: {static_sys_info["physical_cores"]}", fg_color="transparent")
        self.cpu_logical_cores_label = customtkinter.CTkLabel(self, text=f"CPU logical cores: {static_sys_info["logical_cores"]}", fg_color="transparent")

        self.cpu_freq_label = customtkinter.CTkLabel(self, text=f"CPU frequency: Loading...", fg_color="transparent")
        self.cpu_usage_label = customtkinter.CTkLabel(self, text=f"CPU usage: Loading...", fg_color="transparent")

        self.cpu_brand_label.pack(side="top")
        self.cpu_arch_label.pack(side="top")
        self.cpu_bits_label.pack(side="top")
        self.cpu_l1_cache_label.pack(side="top")
        self.cpu_l2_cache_label.pack(side="top")
        self.cpu_l3_cache_label.pack(side="top")
        self.cpu_physical_cores_label.pack(side="top")
        self.cpu_logical_cores_label.pack(side="top")
        self.cpu_freq_label.pack(side="top")
        self.cpu_usage_label.pack(side="top")

        self.update_dynamic_info()

    def update_dynamic_info(self):
        dynamic_sys_info = SystemInfo().get_dynamic_info()
        self.cpu_freq_label.configure(text=f"CPU frequency: {dynamic_sys_info["cpu_freq"]:.2f} MHz")
        self.cpu_usage_label.configure(text=f"CPU usage: {dynamic_sys_info["cpu_usage"]:.1f} %")

        # Schedule next update after 1000ms
        self.after(1000, self.update_dynamic_info)