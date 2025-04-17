@echo off
chcp 1251 > nul

:menu
cls
echo.
echo  [ Selenium Control ]
echo  1. Start HUB
echo  2. Start NODE 1 (Chrome)
echo  3. Start NODE 2 (Firefox + Edge)
echo  0. Exit
echo.

set /p choice="Select: "
if "%choice%"=="1" goto hub
if "%choice%"=="2" goto node1
if "%choice%"=="3" goto node2
if "%choice%"=="0" exit
goto menu

:hub
start "Selenium HUB" cmd /k "java -jar %CD%\server\selenium-server-4.31.0.jar hub --config %CD%\server\hub-config.toml"
goto menu

:node1
start "Node 6666" cmd /k "java -jar %CD%\server\selenium-server-4.31.0.jar node --config %CD%\server\node1-config.toml"
goto menu

:node2
start "Node 7777" cmd /k "java -jar %CD%\server\selenium-server-4.31.0.jar node --config %CD%\server\node2-config.toml"
goto menu
