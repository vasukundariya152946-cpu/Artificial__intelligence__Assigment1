# TOwer of hanoi
def tower_of_hanoi(n,source,helper,destination):
    if n==1:
        print("Nove disk 1 From",source,"to ",destination)
        return
    tower_of_hanoi(n-1,source,destination,helper)
    print("Nove disk ",n,"from",source,"to",destination)
    (tower_of_hanoi(n-1,helper,source,destination))
# Number Of disks
n= int(input("Enter Number of disk :"))
# solve tower_of_hanoi
tower_of_hanoi(n,"A","B","C")
# total number of moves
print("Total moves :",(2**n)-1)
