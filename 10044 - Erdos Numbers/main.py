from sys import stdin
from collections import deque

INFINITE = 999999999


def read_scenario():
    npapers, nauthors = tuple(map(int, stdin.readline().split()))
    papers = [stdin.readline() for _ in range(npapers)]
    authors = [stdin.readline().rstrip() for _ in range(nauthors)]
    
    return papers, authors

def extract_paper_authors(paper):
   
    tokens = paper.replace(':', ',').split(', ')
    nauthors = (len(tokens)-1)//2

    authors = []
    for i in range(nauthors):
        last_name = tokens[i*2]
        initials = tokens[i*2+1]
        authors.append(last_name+', '+initials.rstrip())

    return authors

def build_author_ref(papers):
    # Build table containing all the authors found in the papers
    # and assign an unique id to each.
    author_ref = {'Erdos, P.': 0} # Assume HE is in some papaer
    next_id = 1

    for paper in papers:
        for author in paper:
            if author not in author_ref:
                author_ref[author] = next_id
                next_id += 1

    return author_ref


def find_erdos_bfs(papers, authors):

    paper_authors = [extract_paper_authors(paper) for paper in papers]
    author_ref = build_author_ref(paper_authors)
    
    # Create paper_authors/author_paper tables using author references 
    paper_authors = [[author_ref[author] for author in paper] for paper in paper_authors]
    author_papers = [[] for _ in author_ref.keys()]
    for num, paper in enumerate(paper_authors):
        for author in paper:
            author_papers[author].append(num) 


    # Initial erdos for each author and paper
    author_erdos = {ref: INFINITE for author, ref in author_ref.items()}
    paper_erdos = [INFINITE for paper_id in range(len(papers))]
    author_erdos[0]=0 # HE was the beginning
   
    # Use BFS to find erdos numbers starting by ERDOS HIMSELF
    queue = deque([0])
    while queue:
        author = queue.popleft()
        
        for paper in author_papers[author]:
            if author_erdos[author] >= paper_erdos[paper]:
                continue

            paper_erdos[paper] = author_erdos[author]
            for co_author in paper_authors[paper]:
                if author_erdos[co_author] == INFINITE:
                    author_erdos[co_author] = author_erdos[author]+1
                    queue.append(co_author)

    # Obtain requested authors erdos number
    erdos = []
    for author in authors:
        if author not in author_ref:
            erdos.append(INFINITE)
        else:
            erdos.append(author_erdos[author_ref[author]])

    return erdos


if __name__ == '__main__':

    nscenarios = int(stdin.readline())

    for s in range(nscenarios):
        papers, authors = read_scenario()
        erdos = find_erdos_bfs(papers, authors)

        print("Scenario {}".format(s+1))
        for author, erd in zip(authors, erdos):
            if erd == INFINITE:
                print(author, 'infinity')
            else:
                print(author, erd)
            

