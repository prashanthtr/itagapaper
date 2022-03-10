
#Interactive prompt and rewrite

import json
import argparse
import re
import textwrap

# from rake_nltk import Rake
# r = Rake()

def get_arguments():

    parser = argparse.ArgumentParser(description="myParser")
    parser.add_argument("--keywords")
    parser.add_argument("--abstracts")
    return parser.parse_args()

def main():

    #url, parser, extractor, thresohold: args 
    args = get_arguments()
    prompt = args.keywords
    abstracts = args.abstracts
    get_papers(prompt, abstracts)

def get_papers(keywords, abstracts):
    # from json dictionary

    # r.extract_keywords_from_text(prompt)
    # prompt_keywords = r.get_ranked_phrases()

    # Load dictionary (current json file)
    with open(abstracts) as json_file:
        data = json.load(json_file)

    kw_file = open(keywords, "r") 
    prompt_keywords = kw_file.read().split("\n")
    
    # Remove whitespaces
    for pk in prompt_keywords:
        pk = pk.strip();

    #prompt_keywords = ["embodied", "embodied experience", "embodiment", "music cognition", "evaluation", "experience", "ontology", "presence", "new music experiences", "accessibility", "inclusivity", "flow", "knowledge", "perception", "digital score", "notation", "musicainship", "emergence", "real-time score"]
    #prompt_keywords = ["liveness", "EEG", "instrument", "skills", "awareness", "context", "musicianship"]
    #print(prompt_keywords)

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
        relevant = int(input())

        while relevant > 1 :
            print("Press value between 0 and 1")
            relevant = int(input())

        paper["user_relevance"].append(relevant)#(1/0)
        paper["prompt_keywords"].append(prompt_keywords) # HERE also, create a unique list of common keywords

    # USER LABELS THE RELEVANCE OF PAPERS SELECTED FROM THE CLASSIFICATION ALGORITHM
    # SOLOMIYA: ROUGHLY HOW MANY WORDS MATCH
    # 

    for data_item in data:
        
        for paper in match_results:
            if data_item["title"] == paper["title"]:
                data_item = paper
                break

    # rewrite new file
    with open('nime_abstracts.json', 'w') as outfile:
        json.dump(data, outfile, indent=4, sort_keys=True)

if __name__ == '__main__':
    main()
