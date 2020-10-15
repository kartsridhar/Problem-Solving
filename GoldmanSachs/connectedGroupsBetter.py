def countGroups(related):
    # Write your code here
    from collections import defaultdict
    
    groups = defaultdict(set)

    for i in range(len(related)):
        for j in range(len(related[i])):
            if related[i][j] == '1':
                groups[i].add(j)

    uniqueGroups = []
    count = 0

    for g1 in groups.values():
        updatedGroup = g1
        for g2 in groups.values():
            length = len(g1.intersection(g2))
            if length > 0 and len(g2) > len(g1):
                updatedGroup = g1.union(g2)
                g1 = updatedGroup
        if updatedGroup not in uniqueGroups:
            uniqueGroups.append(updatedGroup)
            count += 1
    
    return count
     
related = ['1100', '1110', '0110', '0001']
print(countGroups(related))