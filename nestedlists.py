if __name__ == '__main__':
    records=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([score,name])
    records.sort()
    i=0
    while i< len(records) and records[i][0]==records[0][0]:
        i=i+1
    second_lowest=records[i][0]
    names=[]
    while i< len(records) and records[i][0]== second_lowest:
        names.append(records[i][1])
        i=i+1
    names.sort()
    for name in names:
        print(name) 
