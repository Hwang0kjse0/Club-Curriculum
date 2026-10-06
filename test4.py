n, k = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

# A는 작은 순서대로 정렬
A.sort()

# B는 큰 순서대로 정렬
B.sort(reverse=True)

for i in range(k):

    # B의 값이 더 클 때만 교환
    if A[i] < B[i]:
        A[i], B[i] = B[i], A[i]

    # 더 이상 교환해도 이득이 없다면 종료
    else:
        break

print(sum(A))