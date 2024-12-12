from itertools import product



def maximize_expression(K, M, lists):
    # twoj kod tutaj
    pow_lists = [[x**2 for x in l] for l in lists]
    return max(sum(x) % M for x in product(*pow_lists))



if __name__ == "__main__":
    K, M = map(int, input().rstrip().split())

    lists = [list(map(int, input().rstrip().split()[1:])) for _ in range(K)]

    result = maximize_expression(K, M, lists)
    print(result)
