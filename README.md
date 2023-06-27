ReadMe File 
----------------------------------------------------------------------------------------------------------------------------------------------------------



1) Problem Statement :

Develop an Auto Release Notes solution that leverages Git commits and AI generation to automatically generate tabular release notes. 
The current process of creating release notes involves manual extraction from Jira or other sources, leading to inefficiencies. 
The solution aims to automate this process by analyzing Git commits and utilizing AI technology to generate comprehensive release notes in a tabular format.
By automating the release notes generation, the solution aims to save time and effort, ensuring accurate and consistent documentation of software releases.

2) Short Description of the approch used :

-> Collecting Git Commits: Git commits are collected from the repository, through the GitHub API using get_commits.py python script. 

-> Preprocessing Git Commits: The collected Git commits are preprocessed to extract relevant information such as the commit message, 
commit hash, and other details.These commit messages will be stored in a commits.txt file.

-> Generating Release Notes: The extracted commit information is processed using natural language processing (NLP) techniques 
and AI models to generate comprehensive release notes.The OpenAI "text-davinci-003" model is utilized to generate human-like text based on the provided 
commit messages.

-> Formatting Release Notes: The generated release notes are formatted and added into the generated_notes.txt file, including relevant details such as 
the commit hash, commit message, and other relevant information.

-> Writing to an Excel File: The formatted release notes are written to a ReleaseNotes.xlsx file for tabular format representation and further use.
The excel file can be easily shared or incorporated into other systems or processes.

->Automating the process : We have setup a CI pipeline using GitHub actions which contains a python_scripts.yml file which will trigger our python scripts
 to trigger everytime a new commit is being made to the main branch of vsCode repository.

 By automating the release notes generation process using Git commits and AI-based text generation,this approach enables the efficient and consistent
 creation of release notes for software projects. It saves time and effort by eliminating the manual extraction process and ensures accurate and 
standardized documentation of software releases.The suggestions like writing to a file and reading from the file in release_notes_generator.py are 
provided by copilot.

3) Tech Stack involved :

-> Version Control System: Git is used as the version control system to manage the code repository and track commits.

-> Git API: We have used the Git API to get the commits from vsCode open repository of GitHub.

-> Python: Python is a popular programming language used for scripting and automation. It is utilized in this case to write the code that collects commits,
 processes the data, generates release notes, and writes them to a file.

-> OpenAI GPT Model: The OpenAI GPT model (text-davinci-003) is utilized for text generation based on the provided commit messages. OpenAI provides an API that allows
 integration with their powerful language models.

-> File I/O: Python's built-in file I/O functionality is used to read and write release notes to a text file.

-> Github CoPilot : GitHub CoPilot is used to give code suggestions like what to import and how to write to a text file.

Overall, the combination of Git,GitHub CoPilot, Python, NLP techniques, OpenAI GPT models, and text formatting libraries forms the tech stack for automating the 
release notes generation process. 


4)Instructions to run the code :

-> Extract the zip file : File will contain a release_notes_generator.py, get_commits.py and readme.md file.

-> Clone or download the repository : Clone or download the repository containing the code for release notes generation from a Git repository. If you're using an open-source
   repository, clone it to your local machine (https://github.com/PersitentHritvik/AI-Technothon.git). 

-> Install Dependencies : The dependencies will automatically be installed from the requirements.txt file using the yamel file(python_scripts.yml file) which is stored in the 
  .github/workflows/ directory. 

-> Configure Git Repository: If you want to generate release notes from a specific Git repository, update the code with the appropriate repository information 
   (e.g., repository URL, credentials) in the get_commits.py file, currently we are using vsCode repository.

->  Verify the Generated Release Notes: Once the script finishes executing, check the generated ReleaseNotes.xlsx file. It should contain the formatted release notes based
    on the Git commits.  


