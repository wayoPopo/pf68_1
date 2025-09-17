@echo off
pip install -q numpy python-dotenv
echo compile cpp file!!
g++ ..\resources\W11\bin\gen.cpp -o ..\resources\W11\bin\gen.exe
echo generate testcase
cd ..\resources\W11\bin\
gen.exe
cd ..\..\..\W11
copy ..\resources\W11\testcases\*.txt .\
copy ..\resources\W11\testcases\*.csv .\
@echo on