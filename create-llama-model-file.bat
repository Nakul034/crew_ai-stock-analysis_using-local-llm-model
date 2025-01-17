@echo off

:: Variables
set model_name=llama2
set custom_model_name=crewai-llama2

:: Get the base model
ollama pull %model_name%

:: Create the model file
ollama create %custom_model_name% -f .\Llama2Modelfile
