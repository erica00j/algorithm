def solution(name, yearning, photo):
    return [sum(yearning[name.index(j)] for j in i if j in name) for i in photo]

print(solution(["may", "kein", "kain", "radi"],[5, 10, 1, 3],[["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]))