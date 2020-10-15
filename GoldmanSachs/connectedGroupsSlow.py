def countGroups(related):
    # Write your code here
    groupCount = len(related)
    groups = [[i] for i in range(groupCount)]
    for i in range(len(related)):
        bestGroup = groups[i]
        for j in range(len(related[i])):
            if related[i][j] == '1':
                groups[i].append(j)
                bestGroup.append(j)
        for k in range(len(groups)):
            if any(x in groups[k] for x in bestGroup) and len(bestGroup) > len(groups[k]):
                groups[k] = bestGroup
    groups = [sorted(list(set(i))) for i in groups]
    uniqueGroups = []

    for i in groups:
        if i not in uniqueGroups:
            uniqueGroups.append(i)
            
    return len(uniqueGroups)

related = ['1100', '1110', '0110', '0001']
print(countGroups(related))