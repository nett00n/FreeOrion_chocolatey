#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
#NoTrayIcon
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.
SetTitleMatchMode, 2 ; A window's title can contain WinTitle anywhere inside it to be a match.

Loop, 1000

{
sleep 1000
IfWinExist, FreeOrion
  {
    WinActivate
    Send {tab}
    Send {enter}
    sleep 1000
  }
  IfWinExist, FreeOrion
  {
    WinActivate
    Send {enter}
    sleep 1000
    ExitApp
  }
}
