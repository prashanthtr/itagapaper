
import json
# display paper

with open("nime_abstracts.json") as json_file:
    data = json.load(json_file)

with open('selected_papers.txt', 'w') as f:
    for paper in data:
        if len(paper["user_relevance"]) > 0 and sum(paper["user_relevance"]) >= 1:
            f.write(str(paper["yearno"]) + " \n" + paper["authornames"] + " : " + paper["title"] + " : \n " + paper["abstract"] + " \n")


