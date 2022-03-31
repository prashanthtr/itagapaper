
# Description

itagapaper is Python tool for interactively tagging conferences papers using user-specified keywords.

Running the program opens an interactive command-prompt appliation that displays each paper abstract and title.

The program works on keyword based search. The search results can be modified With a set of user-specified keywords (keywords folder)

Every paper, the user queries and tags, is written back to the database.

The selected files are separately stored in file (selected_papers.txt) for later viewing.

# Steps

Please execute the steps in following for effective use.

## Navigate to github folder using Cd.

	>> cd pathtofile/itagapaper/

## Install dependencies
	
	>> pip install -r requirements.txt

## Search command
	
	>> python i-prompt.py --kw keywords2.txt --db nime_abstracts.json

## View results

	>> python selected_papers.py

