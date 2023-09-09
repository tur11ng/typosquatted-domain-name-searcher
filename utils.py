from enum import Enum, auto
from pathlib import Path


class OperatingSystem(Enum):
    Android = auto()
    iOS = auto()
    Windows = auto()
    Linux = auto()


class Utils:
    @staticmethod
    def get_font_path(operating_system: OperatingSystem) -> Path:
        current_directory = Path.cwd()

        match operating_system:
            case OperatingSystem.iOS:
                return current_directory / 'assets' / 'fonts' / 'sf-pro' / 'SF-Pro-Text-Regular.ttf'
            case OperatingSystem.Android:
                return current_directory / 'assets' / 'fonts' / 'roboto' / 'Roboto-Regular.ttf'
            case OperatingSystem.Windows:
                return current_directory / 'assets' / 'fonts' / 'segoe-ui' / 'Segoe-UI.ttf'
            case OperatingSystem.Linux:
                return current_directory / 'assets' / 'fonts' / 'ubuntu' / 'Ubuntu-Regular.ttf'
            case _:
                raise ValueError(f"Unsupported OS type: {operating_system}")