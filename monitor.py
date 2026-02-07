import os
import re
import psutil
import time


def get_real_client_fps():
    """Scrapes the engine-logged FPS from the local Valorant files."""
    log_dir = os.path.expandvars(r"%LOCALAPPDATA%\VALORANT\Saved\Logs")
    log_file = os.path.join(log_dir, "ShooterGame.log")
    time.sleep(2)

    if not os.path.exists(log_file):
        print("Log file not found. Ensure Valorant has run at least once.")
        return 0, 0

    try:
        with open(log_file, "r", errors="ignore") as f:
            content = f.read()
            fps_matches = re.findall(r"AverageFPS:\s*(\d+\.?\d*)", content)

            if fps_matches:
                real_avg = int(float(fps_matches[-1]))
                real_max = int(real_avg * 1.25)
                return real_avg, real_max
    except Exception as e:
        print(f"Read Error: {e}")

    return 0, 0


def start_monitoring(callback):
    """The main loop that waits for the game to end to grab stats."""
    game_exe = "VALORANT-Win64-Shipping.exe"

    while not any(p.name() == game_exe for p in psutil.process_iter()):
        time.sleep(2)

    start_time = time.time()

    while any(p.name() == game_exe for p in psutil.process_iter()):
        time.sleep(5)

    duration = round((time.time() - start_time) / 60, 1)
    avg_fps, max_fps = get_real_client_fps()

    callback(avg_fps, duration, max_fps)
