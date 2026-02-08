import os
import subprocess
import configparser
import psutil


def is_valorant_running():
    """Checks if the Valorant process is currently active in Windows."""
    for proc in psutil.process_iter(['name']):
        try:
            # Valorant's actual game executable name
            if proc.info['name'] == "VALORANT-Win64-Shipping.exe":
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False


def get_valorant_config_path():
    """Locates the GameUserSettings.ini file in Local AppData."""
    local_appdata = os.getenv('LOCALAPPDATA')
    config_root = os.path.join(local_appdata, r'VALORANT\Saved\Config')

    if not os.path.exists(config_root):
        return None

    # Iterates through UUID folders to find the active Windows config
    for folder in os.listdir(config_root):
        path = os.path.join(config_root, folder, 'Windows',
                            'GameUserSettings.ini')
        if os.path.exists(path):
            return path
    return None


def apply_custom_settings():
    """Edits the .ini file to ensure optimal settings before launch."""
    ini_path = get_valorant_config_path()
    if not ini_path:
        return False

    config = configparser.ConfigParser()
    config.read(ini_path)

    section = '/Script/ShooterGame.ShooterGameUserSettings'
    if not config.has_section(section):
        config.add_section(section)

    # Example tweaks: Disable VSync and set Resolution Quality to 100%
    config.set(section, 'bUseVsync', 'False')
    config.set(section, 'sg.ResolutionQuality', '100.000000')

    with open(ini_path, 'w') as configfile:
        config.write(configfile, space_around_delimiters=False)
    return True


def launch_valorant():
    """Launches the game via the Riot Client."""
    apply_custom_settings()

    riot_client_path = r"C:\Riot Games\Riot Client\RiotClientServices.exe"
    launch_args = ["--launch-product=valorant", "--launch-patchline=live"]

    if os.path.exists(riot_client_path):
        subprocess.Popen([riot_client_path] + launch_args)
        return True
    return False
