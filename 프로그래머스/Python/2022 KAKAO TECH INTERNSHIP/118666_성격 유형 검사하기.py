# https://school.programmers.co.kr/learn/courses/30/lessons/118666

def solution(survey, choice):
    characters = (("R","T"),("C","F"),("J","M"),("A","N"))
    
    scores = {c1:0 for c2 in characters for c1 in c2}
        
    for s, c in zip(survey, choice):
        scores[s[0]] -= c-4
        scores[s[1]] += c-4
    
    answer = [c1 if scores[c1]>=scores[c2]else c2 for c1,c2 in characters]

    return ''.join(answer)       

if __name__ == "__main__":
    param = {
        "survey": ["AN", "CF", "MJ", "RT", "NA"],
		"choice": [5, 3, 2, 7, 5]
    }
    result = "TCMA"
    print(solution(**param), result)