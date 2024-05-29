# https://school.programmers.co.kr/learn/courses/30/lessons/42890

def solution(relation):
    answer_list = list()
    for i in range(1, 1 << len(relation[0])):
        tmp_set = set()
        for j in range(len(relation)):
            tmp = ''
            for k in range(len(relation[0])):
                if i & (1 << k):
                    tmp += str(relation[j][k])
            tmp_set.add(tmp)

        if len(tmp_set) == len(relation):
            not_duplicate = True
            for num in answer_list:
                if (num & i) == num:
                    not_duplicate = False
                    break
            if not_duplicate:
                answer_list.append(i)
    return len(answer_list)

if __name__ == "__main__":
    param = {
        "relation": [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
    }
    result = 2
    print(solution(**param), result)