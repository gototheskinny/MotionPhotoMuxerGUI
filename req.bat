@echo off
echo Installing dependencies...
echo.

:: Install tkinter
python -m pip install tkinter

:: Install any other dependencies needed for the script
python -m pip install pyexiv2
python -m pip install package1
python -m pip install package2
python -m pip install package3

echo.
echo Dependencies installed successfully!
