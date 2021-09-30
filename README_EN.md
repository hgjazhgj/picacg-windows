# PicACG

## [简体中文](README.md) | English

[![GitHub](https://img.shields.io/github/license/tonquer/picacg-windows)](https://raw.githubusercontent.com/tonquer/picacg-windows/master/LICENSE.txt) 
[![GitHub](https://img.shields.io/github/workflow/status/tonquer/picacg-windows/CI?label=CI)](https://github.com/tonquer/picacg-windows/actions)
![Relese](https://img.shields.io/badge/Python-3.7.9%2B-brightgreen)
[![Relese](https://img.shields.io/github/v/release/tonquer/picacg-windows)](https://github.com/tonquer/picacg-windows/releases)
![Relese](https://img.shields.io/github/downloads/tonquer/picacg-windows/latest/total)
![Relese](https://img.shields.io/github/downloads/tonquer/picacg-windows/total)

- PicACG PC Client (Support Windows, Linux and macOS), using QT as interface.
- Only for technical references, please do not use it for other purposes.
- If you think this project is helpful, please give it a STAR, thanks!
- If you encounter any problems, please post them to ISSUE.
## Functions
- Most of the features of PicACG PC Client have been implemented.
- Support for viewing and downloading.

## My other projects
 [![Readme Card](https://github-readme-stats.vercel.app/api/pin/?username=tonquer&repo=ehentai-windows)](https://github.com/tonquer/ehentai-windows)  
 [![Readme Card](https://github-readme-stats.vercel.app/api/pin/?username=tonquer&repo=waifu2x-ncnn-vulkan-python)](https://github.com/tonquer/waifu2x-ncnn-vulkan-python)
## How to use
  ### Windows (tested on Win10)
  1. Download the latest version at https://github.com/tonquer/picacg-windows/releases
  2. Unzip
  3. Run start.exe
  4. Updates can be installed by downloading the latest version and overwrite the original directory.
  5. If waifu2x cannot be initialized, please update the graphics driver and install [VS Library](https://download.visualstudio.microsoft.com/download/pr/366c0fb9-fe05-4b58-949a-5bc36e50e370/015EDD4E5D36E053B23A01ADB77A2B12444D3FB6ECCEFE23E3A8CD6388616A16/VC_redist.x64.exe). If it still cannot be enabled, your computer does not support Vulkan.
  ### macOS (tested on macOS 10.15.7)
  1. Download the latest version at https://github.com/tonquer/picacg-windows/releases
  2. Unzip
  3. Drag PicACG into the Applications folder on the left sidebar of the Finder.
  4. Find and run PicACG from the Launchpad.
  ### Linux (tested on deepin 20.2)
  1. Download qt dependencies at http://ftp.br.debian.org/debian/pool/main/x/xcb-util/libxcb-util1_0.4.0-1+b1_amd64.deb
  2. Install the dependencies (sudo dpkg -i ./libxcb-util1_0.4.0-1+b1_amd64.deb)
  3. Download the latest version at https://github.com/tonquer/picacg-windows/releases
  4. tar -zxvf bika.tar.gz
  5. cd bika && chmod +x start
  6. ./start
  7. If you want to use waifu2x, please make sure your device supports vulkan, and then install the vulkan driver package (sudo apt install mesa-vulkan-drivers)

## How to build
  ### Use Git Actions
  1. Check the result in [Git Actions](https://github.com/tonquer/picacg-windows/actions)

## Proxy issues
  Please see https://github.com/tonquer/picacg-windows/discussions/48

## Interface demos

* Login
![Login](example/登录.gif)

* Search
![Search](example/搜索.gif)

* Comic details
![Comic details](example/漫画详情.gif)

* Download
![Download](example/下载.gif)

* Browsing pictures
![Browsing pictures](example/看图.gif)

* waifu2x
![waifu2x](example/waifu2x.gif)

## Thanks for the following projects
  ### waifu2x
   [![Readme Card](https://github-readme-stats.vercel.app/api/pin/?username=nagadomi&repo=waifu2x)](https://github.com/nagadomi/waifu2x)  
   [![Readme Card](https://github-readme-stats.vercel.app/api/pin/?username=nihui&repo=waifu2x-ncnn-vulkan)](https://github.com/nagadomi/waifu2x-ncnn-vulkan)  
   [![Readme Card](https://github-readme-stats.vercel.app/api/pin/?username=tonquer&repo=waifu2x-ncnn-vulkan-python)](https://github.com/tonquer/waifu2x-ncnn-vulkan-python)  
  ### Qt
   [![Readme Card](https://github-readme-stats.vercel.app/api/pin/?username=PyQt5&repo=PyQt)](https://github.com/PyQt5/PyQt)  
   [![Readme Card](https://github-readme-stats.vercel.app/api/pin/?username=PyQt5&repo=PyQtClient)](https://github.com/PyQt5/PyQtClient)  
  ### Qt Skin
   [![Readme Card](https://github-readme-stats.vercel.app/api/pin/?username=satchelwu&repo=QSS-Skin-Builder)](https://github.com/satchelwu/QSS-Skin-Builder)  
  ### Qt scroll
   [![Readme Card](https://github-readme-stats.vercel.app/api/pin/?username=zhiyiYo&repo=Groove)](https://github.com/zhiyiYo/Groove)  
