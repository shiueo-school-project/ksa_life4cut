import subprocess

command = "pyside6-rcc resources.qrc -o ./modules/resources_rc.py"
subprocess.run(command.split(' '), shell=True, check=True)

import os.path
import platform
import subprocess
import time

from Utils import jsonreader
from Utils import requirements_txt


def build(withconsole):
    try:
        system = platform.system()
        config = jsonreader.get("Config/config.json")
        print(system)

        if system == 'Windows':
            requirements_txt.run()

            buildfile_name = "ksa_life4cut.py"
            Output_dir_name = "ksa-life4cut-build"
            icon = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Icon/ksa_life4cut.ico")
            IconFolder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Icon")
            ConfigFolder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Config")
            FontFolder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Font")
            ThemesFolder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "themes")
            ImagesFolder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "images")

            if withconsole:
                command = f"python -m nuitka --mingw64 --show-modules --follow-imports " \
                          f"--windows-company-name=SHI3DO --windows-product-version={config.version} " \
                          f"--output-dir={Output_dir_name} --verbose --assume-yes-for-downloads " \
                          f"--windows-icon-from-ico={icon} --onefile " \
                          f"--include-data-dir={IconFolder}=Icon " \
                          f"--include-data-dir={ConfigFolder}=Config " \
                          f"--include-data-dir={FontFolder}=Font " \
                          f"--include-data-dir={ThemesFolder}=themes " \
                          f"--include-data-dir={ImagesFolder}=images " \
                          f"--enable-plugin=pyside6 " \
                          f"--include-package=PIL " \
                          f"{buildfile_name}"
            else:
                command = f"python -m nuitka --mingw64 --show-modules --follow-imports " \
                          f"--windows-company-name=SHI3DO --windows-product-version={config.version} " \
                          f"--output-dir={Output_dir_name} --verbose --assume-yes-for-downloads " \
                          f"--windows-icon-from-ico={icon} --onefile " \
                          f"--include-data-dir={IconFolder}=Icon " \
                          f"--include-data-dir={ConfigFolder}=Config " \
                          f"--include-data-dir={FontFolder}=Font " \
                          f"--include-data-dir={ThemesFolder}=themes " \
                          f"--include-data-dir={ImagesFolder}=images " \
                          f"--enable-plugin=pyside6 " \
                          f"--include-package=PIL " \
                          f"--windows-disable-console " \
                          f"{buildfile_name}"

            start = time.time()
            subprocess.run(command.split(' '), shell=True, check=True)
            end = time.time()

            print(f"{end - start}s 사용됨")
            print(command)

        elif system == 'Linux':
            print(system)
        elif system == 'Darwin':
            print(system)
        else:
            print("OS를 알 수 없음")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    build(withconsole=False)
