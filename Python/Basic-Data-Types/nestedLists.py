if __name__ == '__main__':
    grades, scores = [], []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        grades.append([name, score])
        scores.append(score)
    second_smallest = sorted(list(set(scores)))[1]
    grades.sort()
    for i in range(len(grades)):
        if grades[i][1] == second_smallest:
            print(grades[i][0])

