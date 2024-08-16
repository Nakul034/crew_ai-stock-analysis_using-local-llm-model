# CrewAI Local LLM

Run CrewAI locally for free!

# Steps

- Install Ollama
- Create custom local LLM made for CrewAI, (say :llama2 or mistral)
  - Run the ./setup/create-llama-model-file.bat file 
    - Make this script executable by running `create-llama-model-file.bat`
  - This will create a model file in the models directory
  - To change models, edit the create-llama-model-file.bat script
- Verify you are using local llm
  - `type \.ollama\logs\server.log'
- Install the requirements by 'poetry install --no-root'
  - it will install all the requirements from the 'pyproject.tomal' file

- Run main.py for running in terminal for the output
- Run app.py for front-end UI and wait for output


# Tips

- If using multiple models,

# Warnings & Recommendations

- Ollama doesn't work with Async tasks and a bunch of newer CrewAI features yet.
- Lose context. Be very explicit in tasks. Not generic.

# Resources

- Want to find out which LLMs support which features in CrewAI? Here's the link for you:
  - https://python.langchain.com/docs/integrations/llms/
- Learn more about Modelfiles:
  - https://github.com/ollama/ollama/blob/main/docs/modelfile.md
- Check out CrewAI's instructions for working with Ollama and running LLMs locally:
  - https://docs.crewai.com/how-to/LLM-Connections/#connect-crewai-to-llms
