import ctypes, os, subprocess


class User_Activity:

    @classmethod
    def get_idle_duration(cls):
        if os.name == 'nt':  # Windows
            return cls.__get_windows_idle_duration()
        elif os.name == 'posix':  # Linux/Unix
            return cls.__get_linux_idle()
        else:
            raise NotImplementedError("Unsupported OS")

    @staticmethod
    def __get_windows_idle_duration():
        lii = ctypes.Structure.LASTINPUTINFO()
        lii.cbSize = ctypes.sizeof(lii)
        ctypes.windll.user32.GetLastInputInfo(ctypes.byref(lii))
        millis = ctypes.windll.kernel32.GetTickCount() - lii.dwTime
        return millis / 1000.0  # Returns idle time in seconds

    @staticmethod
    def __get_linux_idle():
        # Requires xprintidle to be installed via apt/pacman!!!!
        idle_ms = subprocess.check_output(["xprintidle"]).strip()
        return float(idle_ms) / 1000.0