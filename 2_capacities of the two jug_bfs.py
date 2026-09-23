# capacities of =the two jumgt
CAP_A=4
cap_B=3
# goal amount
goal =2
# fiunctin to print the state
def print_state(state):
    print("jug A:",state[0],"liters")
    print("jug B:",state[1],"liters")
    print()

# Generae all possible moves
def get_neighbors(state):
    neighbors =[]
    a,b=state
    # 1.fill jug a
    if a<CAP_A:
        neighbors.append(((CAP_A,b),"fill jug A"))
    # 2.fill jug b
    if b<cap_B:
        neighbors.append(((a,cap_B),"fill jug b"))
    # 3 empyty jug a
    if a>0:
        neighbors.append(((0,b),"Empty jug A"))
         # 3 empyty jug B
    if b>0:
        neighbors.append(((a,0),"Empty jug B"))
    amount=min(a,cap_B-b)
    if amount>0:
        neighbors.append(((a-amount,b+amount),"pour jug A ->jug B"))
    amount=min(b,CAP_A-a)
    if amount>0:
        neighbors.append(((a+amount,b-amount),"pour jug B->jug A"))
    return neighbors
# bfs Algoritham
def bfs(start):
    queue = [(start,[])]
    visited=set()
    while queue:
        state,path=queue.pop(0)
        if state in visited:
            continue
        visited.add(state)
        if state[0]==goal or state[1]==goal:
            return path+[(state,"goal reached")]
        for neighboer,action in get_neighbors(state):
            
            if neighboer not in visited:
                queue.append((neighboer,path+[(neighboer,action)]))
    return None
start =(0,0) 
solution = bfs(start)

if solution:
    print("solution found in",len(solution)-1,"moves:\n")
    print("initial state:")
    print_state(start)
    for state,action in solution:
        print(action)
        print_state(state)
        
else:
    print("no soultion found")      
    