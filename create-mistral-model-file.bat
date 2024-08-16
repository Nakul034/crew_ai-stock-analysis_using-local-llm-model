@echo off

:: Variables
set model_name=mistral
set custom_model_name=crewai-mistral

:: Get the base model
ollama pull %model_name%

:: Create the model file
ollama create %custom_model_name% -f .\MistralModelfile
