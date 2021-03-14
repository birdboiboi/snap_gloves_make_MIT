@echo off

echo uploading on %1 

for %%f in (*.py) do (ampy --port %1 put %%f & echo %%f uploaded)

echo done