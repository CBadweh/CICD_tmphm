rem @echo off
set "usage=usage: flashi [{Debug|Release}]"

setlocal

set "build_type=Debug"
if not [%1]==[] set "build_type=%1"

set "ws_root=C:\Users\Sheen\Desktop\Embedded_System\I2C_tmphm\tmphm_CICD"

@REM To find the sn number, runt he command
@REM C:\Program Files\STMicroelectronics\STM32Cube\STM32CubeProgrammer\bin>STM32_Programmer_CLI.exe -l
set "sn=0670FF3632524B3043205426"
set "image_file=%ws_root%\%build_type%\tmphm_CICD.bin"

"%ws_root%\ci-cd-tools\flash.bat" %sn% "%image_file%"

