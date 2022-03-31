
#Interactive prompt and rewrite

import json
import argparse
import re
import textwrap
import os

# from rake_nltk import Rake
# r = Rake()

def get_arguments():

    parser = argparse.ArgumentParser(description="myParser")
    parser.add_argument("--kw")
    parser.add_argument("--db")
    return parser.parse_args()

def main():

    #url, parser, extractor, thresohold: args 
    args = get_arguments()
    prompt = args.kw
    abstracts = args.db
    get_papers(prompt, abstracts)

def get_papers(keywords, abstracts):
    
    # from json dictionary

    # r.extract_keywords_from_text(prompt)
    # prompt_keywords = r.get_ranked_phrases()

    # Load dictionary (current json file)
    with open("db/"+abstracts) as json_file:
        data = json.load(json_file)

    kw_file = open("keywords/" + keywords, "r") 
    prompt_keywords = kw_file.read().split("\n")
    
    # Remove whitespaces
    for pk in prompt_keywords:
        pk = pk.strip();

    # prompt_keywords = ["embodied", "embodied experience", "embodiment", "music cognition", "evaluation", "experience", "ontology", "presence", "new music experiences", "accessibility", "inclusivity", "flow", "knowledge", "perception", "digital score", "notation", "musicainship", "emergence", "real-time score"]
    # prompt_keywords = ["liveness", "EEG", "instrument", "skills", "awareness", "context", "musicianship"]
    # print(prompt_keywords)

    match_results = []

    for papers in data:

        count = 0

        for words in prompt_keywords:

            # counts number of unique keyword matches
            if any(words in kw for kw in papers["keywords"]):
                #match_results.append(words)
                count= count+1

        # Classification
        # Atleast 3 keys match
        if count >= 3:
            match_results.append(papers)

    print(" \n ")
    print(len(match_results), " matching papers " )

    for paper in match_results:

        print(" \n ")

        print(textwrap.fill("Title : " + paper["title"], 100))

        print(" \n ")
        print(textwrap.fill("Authornames : " + paper["authornames"], 100))

        print(" \n ")
        print("Abstract : " )
        print(textwrap.fill(paper["abstract"], 100))
        print(" \n ")
        print("Please label if this is relevant, 1 for yes, 0 for no")
        relevant = input()

        while not relevant.isnumeric() or int(relevant) > 1 :
            print("Press value between 0 or 1")
            relevant = input()

        if int(relevant) == 0 or int(relevant) == 1:
           relevant = int(relevant) 

        paper["user_relevance"].append(relevant)#(1/0)
        paper["prompt_keywords"].append(prompt_keywords) # HERE also, create a unique list of common keywords

        # Writes a paper to database everytime solomiya selects it as relevant
        for data_item in data:
            if data_item["title"] == paper["title"]:
                data_item = paper
                break

        with open("db/"+abstracts, 'w') as outfile:
            json.dump(data, outfile, indent=4, sort_keys=True)

        with open("selected_papers/" + os.path.splitext(abstracts)[0] + "-" + os.path.splitext(keywords)[0] + ".txt", 'w') as f:
            for paper in data:
                if len(paper["user_relevance"]) > 0 and sum(paper["user_relevance"]) >= 1:
                    f.write(paper["yearno"].encode('ascii', 'ignore').decode('ascii') + " \n" + paper["authornames"] + " : " + paper["title"] + " : \n " + paper["abstract"] + " \n")

        print("\n")
        print("Please open the selected_papers.txt file available in the folder")
        print("\n")

    # USER LABELS THE RELEVANCE OF PAPERS SELECTED FROM THE CLASSIFICATION ALGORITHM
    # SOLOMIYA: ROUGHLY HOW MANY WORDS MATCH
    # 

if __name__ == '__main__':
    main()
