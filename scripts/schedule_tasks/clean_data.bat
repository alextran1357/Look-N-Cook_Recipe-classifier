@echo off
echo 

:: 
cd ./../..

:: Pull the changes from the master branch
echo Pulling latest updates from Git...
git pull origin master

:: Check for errors in git pull
if %errorlevel% neq 0 (
    echo Error pulling from Git. Exiting.
    exit /b %errorlevel%
)

:: Navigate to the directory where python script is
cd ./script/

:: Run python script
echo Running the data generator
python data_generator.py

:: Check for errors in python scipt exe
if %errorlevel% neq 0(
    echo Error in Python script. Exiting
    exit /b %errorlevel%
)

echo Data generation process completed successfully.
pause