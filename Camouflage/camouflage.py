
def solution(clothes):
    answer = 1

    # 해시로 저장
    hash = {}
    for c in clothes:
        if c[1] in hash:
            hash[c[1]] += 1
        else:
            hash[c[1]] = 1

    # 각 종류 별 의상 수를 입는 경우의 수를 곱해준다.
    # 안 입는 경우의 수도 있기 때문에 +1
    for k in hash:
        answer *= (hash[k] + 1)

    # 모든 종류를 안 입는 경우는 없기 때문에 -1
    return answer -1