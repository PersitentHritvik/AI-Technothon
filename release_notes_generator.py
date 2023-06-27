import pandas as pd
import os
#read a text file
with open('commits.txt', 'r') as f:
    commits = f.readlines()



import openai

# Set up your OpenAI API credentials
#Here I have used my API key which is saves as an environment variable
openai.api_key = os.environ["OPENAI_API_KEY"]


# Prepare input prompt for OpenAI
input_prompt = "### Git Commits:\n\n" + "\n\n".join(commits) + "\n\n### Release Notes:"

# Generate release notes using OpenAI model
response = openai.Completion.create(
    
    engine="text-davinci-003",
    prompt=input_prompt,
    max_tokens=100,  # Adjust the length of the generated response as needed
    n=1  # Set the number of responses to generate
)

# Extract and process the generated release notes
generated_notes = response.choices[0].text.strip()

# write generated notes to a file
with open('generated_notes.txt', 'w') as f:
    f.write(generated_notes)


from tabulate import tabulate
import openpyxl
lines=generated_notes.splitlines()

df=pd.DataFrame({'Release Notes':lines})

#write df to excel file
df.to_excel('ReleaseNotes.xlsx',index=False)






