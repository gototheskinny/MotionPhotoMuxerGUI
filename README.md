MotionPhotoMuxerGUI
================

> **Note**
> I've switched back to Android for the time being. I do have access to an iPhone for testing, but
> likely won't be focusing on developing this much further.

Convert Apple Live Photos into Google Motion Photos commonly found on Android phones.

# Installation

As of right now, this script only has one dependency, `py3exiv2`. Unfortunately
this requires building a C++ library to install, so you need to install a C++ toolchain.

*****For GUI you also need: a Windows PC that supports python 3.
And you need to run this "requirement installer" .bat to use it properly.

You need the MotionPhotoMuxerGUI.pyw and ***MotionPhotoMuxer.py*** in the same directory or folder.

You need to use .JPG images and .MOV(h.264) videos to use this!!!! It's not gonna work with ".heic" images and (H.265)".MOV" video files!! To transfer the correct formatted files make sure that you use on your iPhone go to:

-Settings.

-Photos.

At the bottom of the page you'll see ***"Transfer to Mac or PC"*** section select ***AUTOMATIC*** *not the OTHER option*

Than you transfer the Live Photos that you wanna convert.(i ***dont*** recommend transferring REGULAR VIDEOS like this. Only "Live Photos")

**HOW TO USE THE GUI:**

First you need to install C++ toolchain [https://visualstudio.microsoft.com/vs/features/cplusplus/](https://visualstudio.microsoft.com/vs/features/cplusplus/) **WITHOUT IT it's not gonna work**

Than you need to install python [https://www.python.org/downloads/](https://www.python.org/downloads/)

Than you need to download both of the ORG AND GUI [ORG](https://github.com/gototheskinny/MotionPhotoMuxerGUI/blob/main/MotionPhotoMuxer.py) [GUI](https://github.com/gototheskinny/MotionPhotoMuxerGUI/blob/main/MotionPhotoMuxerGUI.pyw)

**than double click** to run the [GUI](https://github.com/gototheskinny/MotionPhotoMuxerGUI/blob/main/MotionPhotoMuxerGUI.pyw)

Than you need to Select the folder that your Live Photos are in

Than you need to Select the folder that you want the GENERETED GOOGLE MOTION PHOTOS to be in.

Than you click the **RUN** button. This is it you've MUXED them!!







Using Ubuntu as an example:

~~~bash
sudo apt-get install build-essential python-all-dev libexiv2-dev libboost-python-dev python3 python3-pip python3-venv
python3 -m pip install -r requirements.txt
~~~

## Installing on a Pixel/Android Phone

* Install [Termux from the F-Droid App store](https://f-droid.org/en/packages/com.termux/)
* Install the following packages within Termux in order to satisfy the dependencies for `pyexiv2`:

~~~bash
'pkg install python3'
'pkg install git'
'pkg install build-essential'
'pkg install exiv2'
'pkg install boost-headers'
git clone https://github.com/mihir-io/MotionPhotoMuxer.git
python3 -m pip install -r MotionPhotoMuxer/requirements.txt
~~~

This should leave you with a working copy of MotionPhotoMuxer directly on your Pixel/other Android phone.
You may want to make sure Termux has the "Storage" permission granted from within the system settings, if
you plan on writing the output files to the `/sdcard/` partition.


# Usage

~~~
usage: MotionPhotoMuxer.py [-h] [--verbose] [--dir DIR] [--recurse] [--photo PHOTO] [--video VIDEO] [--output OUTPUT]

Merges a photo and video into a Microvideo-formatted Google Motion Photo

optional arguments:
  -h, --help       show this help message and exit
  --verbose        Show logging messages.
  --dir DIR        Process a directory for photos/videos. Takes precedence over --photo/--video
  --recurse        Recursively process a directory. Only applies if --dir is also provided
  --photo PHOTO    Path to the JPEG photo to add.
  --video VIDEO    Path to the MOV video to add.
  --output OUTPUT  Path to where files should be written out to.
~~~

A JPEG photo and MOV or MP4 video must be provided. The code only does simple
error checking to see if the file extensions are `.jpg|.jpeg` and `.mov|.mp4`
respectively, so if the actual photo/video encoding is something funky, things
may not work right.

> **Note**
> The output motion photo tends to work more reliably in my experience if the input video is H.264 rather than HEVC.

This has been tested successfully on a couple photos taken on an iPhone 12 and
uploaded to Google Photos through a Pixel XL, but there hasn't been any
extensive testing done yet, so use at your own risk!

# Credit

This wouldn't have been possible without the excellent writeup on the process
of working with Motion Photos [here](https://medium.com/android-news/working-with-motion-photos-da0aa49b50c).
