
import json
# display paper

with open("nime_abstracts.json") as json_file:
    data = json.load(json_file)

with open('selected_papers.txt', 'w') as f:
    for paper in data:
        if len(paper["user_relevance"]) > 0 and sum(paper["user_relevance"]) >= 1:
            f.write(paper["yearno"].encode('ascii', 'ignore').decode('ascii') + " \n" + paper["authornames"] + " : " + paper["title"] + " : \n " + paper["abstract"] + " \n")

print("\n")
print("Please open the selected_papers.txt file available in the folder")
print("\n")