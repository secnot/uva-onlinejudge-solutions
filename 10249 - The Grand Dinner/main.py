import sys
from heapq import heappop, heappush, heapify



def read_num():
    return list(map(int, sys.stdin.readline().split()))

def load_case():
    M, N = read_num()
    if not M:
        return None, None

    teams = read_num() # Team members
    tables = read_num() # Tables capacity

    return teams, tables


def find_seating(tables, teams):

    if not tables:
        return None

    # List of members of each group seated at each table
    team_tables = [list() for _ in teams]

    # 
    tables = sorted([(seats,table) for table, seats in enumerate(tables)], reverse=True)
    
    
    team_heap = [(-members, team) for team, members in enumerate(teams)]
    heapify(team_heap)

    for seats, table in tables:
        # Check all members are seated
        if not team_heap:
            break
        
        #
        teams_seated = [] # List of teams seated at current table
        while team_heap and len(teams_seated)<seats:
            t = heappop(team_heap)
            teams_seated.append(t)

        # Record seating for the table
        for t in teams_seated:
            team_tables[t[1]].append(table+1)

        # Re-enque into heap teams with non seated members
        for members, team in teams_seated:
            if members+1 < 0:
                heappush(team_heap, (members+1, team))


    if team_heap:
        return None # There are team members without seating
    else:
        return team_tables


def print_seating(s):
    if not s:
        print(0)
    else:
        print(1)
        for t in s:
            print(' '.join(map(str, sorted(t))))


if __name__ == '__main__':

    while True:
        teams, tables = load_case()
        if teams is None:
            break
        print_seating(find_seating(tables, teams))
