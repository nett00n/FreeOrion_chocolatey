$packageArgs = @{
packageName = 'FreeOrion'
fileType = 'exe'
url = 'https://github.com//freeorion/freeorion/releases/download/v0.4.10.2/FreeOrion_v0.4.10.2_2021-08-01.f663dad_Win32_Setup.exe'
checksum = 'f35041ee56a83c19ae3adeda8552c55d3580b1ba07fe8b87a8853279ae8c4f07'
checksumType   = 'sha256'
silentArgs = '/S'
}

Install-ChocolateyPackage @packageArgs