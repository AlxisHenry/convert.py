from cx_Freeze import setup, Executable

base = None

executables = [
    Executable("main.py", base=base)
]

packages = [
    "idna",
    "tkinter",
]

options = {
    'build_exe': {    
        'packages':packages,
    },
}

setup(
    name = "convert.py",
    options = options,
    version = "1.0",
    description = 'Image converter',
    executables = executables
)