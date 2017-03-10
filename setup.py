from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages = [], excludes = [])
buildOptions = dict(include_files = ['data', 'data/hiscore', 'data/intro.txt', 'data/Credits', 'data/images/', 'data/sounds', 'data/fonts', 'code',]) 
import sys
base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable('lunarpatrol.py', base=base)
]

setup(name='Lunar Patrol',
      version = '0.2',
      description = 'Space Shooter',
      options = dict(build_exe = buildOptions),
      executables = executables)
