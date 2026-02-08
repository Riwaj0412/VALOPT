import subprocess
import os


def get_system_report():
    report = {
        "cpu": "Unknown Processor",
        "gpu": "Unknown Graphics",
        "ram": "0 GB"
    }

    # CPU Detection
    try:
        cpu_out = subprocess.check_output(
            "wmic cpu get name", shell=True).decode().splitlines()
        # Filter out empty lines and the header "Name"
        cpu_name = [line.strip() for line in cpu_out if line.strip()
                    and "Name" not in line][0]
        report["cpu"] = cpu_name
    except Exception:
        report["cpu"] = "Generic Processor"

    # RAM Detection
    try:
        ram_raw = subprocess.check_output(
            "wmic computersystem get totalphysicalmemory", shell=True).decode().splitlines()
        ram_bytes = [line.strip() for line in ram_raw if line.strip()
                     and "TotalPhysicalMemory" not in line][0]
        # Convert bytes to GB and round
        gb = round(int(ram_bytes) / (1024**3))
        report["ram"] = f"{gb} GB DDR4/DDR5"
    except Exception:
        report["ram"] = "8 GB RAM"

    # GPU Detection
    try:
        gpu_out = subprocess.check_output(
            "wmic path win32_VideoController get name", shell=True).decode().splitlines()
        # Pick the first actual GPU found (often the dedicated one)
        gpus = [line.strip()
                for line in gpu_out if line.strip() and "Name" not in line]
        if gpus:
            report["gpu"] = gpus[0]
    except Exception:
        report["gpu"] = "Integrated Graphics"

    return report


def get_monitor_specs():
    try:
        cmd = "wmic path Win32_VideoController get CurrentHorizontalResolution, CurrentRefreshRate, CurrentVerticalResolution"
        out = subprocess.check_output(cmd, shell=True).decode().splitlines()
        stats = [line.strip() for line in out if line.strip()
                 and "Current" not in line][0].split()
        return f"{stats[0]}x{stats[2]} @ {stats[1]}Hz"
    except Exception:
        return "1920x1080 @ 60Hz"


def check_valorant_presence():
    # Common Riot installation path
    return os.path.exists(r"C:\Riot Games\VALORANT\live")
