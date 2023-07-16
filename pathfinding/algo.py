# this is our main entry point exported in __init__.py
def search(graph, start, end):
    # initial values
    visited = []
    seen = {}
    done = {}
    
    # initial path to our stat point (distance: zero)
    seen[start] = {"len": 0, "path": [start]}
    # loop as long as we did not visit (e.g. "finish") our destination node
    while end not in visited:
        # search for the next unfinished node having the shortest overall distance
        found = None
        for node in seen:   
            if found == None or seen[node]["len"] < seen[found]["len"]:
                found = node
        if found == None:
            # TODO: this should be an exception
            print("Could not find any path, found so far: %s" % str(done))
            return None;
        
        # visit the found node
        #print("visiting %s" % found)
        visited.append(found)
        visible = {k:v for k,v in graph[found].items() if k not in visited}       # all nodes not yet visited
        walked_distance = seen[found]["len"]
        walked_path = seen[found]["path"]
        for visible_node, distance in visible.items():
            if visible_node not in seen or walked_distance + distance < seen[visible_node]["len"]:
                seen[visible_node] = {"len": walked_distance + distance, "path": walked_path + [visible_node]}
        done[found] = seen[found]
        del seen[found]
    
    # return our shortest path from `start` to `end`
    return done[end]