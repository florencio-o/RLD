from cx_Freeze import setup, Executable

from config import version

setup(name = "RLD",
      version = version,
      description = "RLD",
      executables = [Executable("main.py", target_name="RLD.exe", base=None, icon=None)]
)