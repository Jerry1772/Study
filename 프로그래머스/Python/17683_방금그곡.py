# https://school.programmers.co.kr/learn/courses/30/lessons/17683

import re
def length(a):
    return len(a)-a.count('#')
def solution(m, musicinfos):
    answer = []
    for i in range(len(musicinfos)):
        musicinfos[i] = musicinfos[i].split(',')
        stt, ent= list(map(int,musicinfos[i][0].split(':'))), list(map(int,musicinfos[i][1].split(':')))
        time = (ent[0]-stt[0])*60 + (ent[1]-stt[1])
        while length(musicinfos[i][3])<time:
            musicinfos[i][3]+=musicinfos[i][3]
        while length(musicinfos[i][3]) != time:
            musicinfos[i][3] = musicinfos[i][3][:-1]
        musicinfos[i][3]+="Z"
        temp = (list(re.findall(m+'.',musicinfos[i][3])))
        if temp.count(m+"#") != len(temp):
            answer.append([musicinfos[i][2],time])   
    if answer:
        answer.sort(key = lambda x:x[1],reverse=1)
        return(answer[0][0])
    else:
        return '(None)'

if __name__ == "__main__":
    param = {
        "m": "ABCDEFG",
		"musicinfos": ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]
    }
    result = "HELLO"
    print(solution(**param), result)