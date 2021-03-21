@echo off
echo using cmd - ampy --port COM# put file
echo make sure ampy is installed and python's Scripts are in the PATH
echo uploading on %1 

for %%f in (*.py) do ( ampy --port %1 put %%f & echo %%f uploaded)

echo done