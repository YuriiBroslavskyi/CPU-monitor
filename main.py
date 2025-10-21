# Entry point
# Initialise main window with customtkinter
# Create an instance of the gui class
# Start the GUI main loop

from gui import CPUMonitorGUI

if __name__ == '__main__':
    app = CPUMonitorGUI()
    app.mainloop()