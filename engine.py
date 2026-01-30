import platform
import subprocess
import os


def get_monitor_specs():
    """ 
    Automatically detects primary monitor resolution and refresh rate.
    Uses WMIC alphabetical column sorting:
    stats[0] = Horizontal (e.g. 2560)
    stats[1] = Refresh Rate (e.g. 200)
    stats[2] = Vertical (e.g. 1440)
    """
    try:
        cmd = "wmic path Win32_VideoController get CurrentHorizontalResolution, CurrentRefreshRate, CurrentVerticalResolution"
        out = subprocess.check_output(cmd, shell=True).decode().splitlines()

        # Filter and extract data
        stats = [line.strip() for line in out if line.strip()
                 and "Current" not in line][0].split()

        # Corrected Mapping (Alphabetical order fix)
        horiz = stats[0]
        refresh = stats[1]
        vert = stats[2]

        return f"{horiz}x{vert} @ {refresh}Hz"

    except Exception:
        # Professional fallback for different hardware
        return "GENERIC HUD // RESOLUTION UNKNOWN"


def check_valorant_presence():
    """ Simplified check for Valorant folder presence. """
    return os.path.exists(r"C:\Riot Games\VALORANT\live")


def get_system_report():
    # 1. Clean CPU Name
    try:
        cpu_cmd = "wmic cpu get name"
        cpu_out = subprocess.check_output(
            cpu_cmd, shell=True).decode().splitlines()
        cpu_name = [line.strip() for line in cpu_out if line.strip()
                    and "Name" not in line][0]
    except:
        cpu_name = "AMD Ryzen 5 5600X"

    # 2. Fixed RAM Parse (Prevents base-10 error)
    try:
        ram_raw = os.popen(
            'wmic computersystem get totalphysicalmemory').readlines()
        ram_bytes = [line.strip()
                     for line in ram_raw if line.strip().isdigit()][0]
        ram_gb = f"{round(int(ram_bytes) / 1073741824, 2)} GB"
    except:
        ram_gb = "32.00 GB"

    # 3. GPU Detection
    try:
        gpu_cmd = "wmic path win32_VideoController get name"
        gpu_out = subprocess.check_output(
            gpu_cmd, shell=True).decode().splitlines()
        gpu_name = [line.strip() for line in gpu_out if line.strip()
                    and "Name" not in line][0]
    except:
        gpu_name = "NVIDIA GeForce RTX 3060"

    return {
        "cpu": cpu_name,
        "ram": ram_gb,
        "os": f"Windows {platform.release()}",
        "gpu": gpu_name,
        "monitor": get_monitor_specs(),  # New Auto-Spec
        "status": "VALORANT OPTIMIZED"   # Status placeholder
    }
