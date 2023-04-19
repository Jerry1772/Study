# https://school.programmers.co.kr/learn/courses/30/lessons/72414

import re
h2s = 3600
m2s = 60
def solution(playtime, advtime, logs):
    pa,pb,pc,aa,ab,ac = list(map(int, playtime.split(":")))+(list(map(int, advtime.split(":"))))
    playtime,advtime = (h2s*pa+m2s*pb+pc,h2s*aa+m2s*ab+ac)
    viewers = [0]*playtime
    Log = []
    for l in logs:
        q,w,e,z,x,c = list(map(int,re.split('[:-]',l)))
        Log.append([q*h2s+w*m2s+e,1])
        Log.append([z*h2s+x*m2s+c,0])
    Log.sort()
    v,p = 0,0
    for m,n in Log:
        viewers[p:m] = [v]*(m-p)
        v+=(1 if n else -1)
        p = m
    v = sum(viewers[:advtime])
    answer = v
    time = 0
    for i in range(1,playtime-advtime):
        v = v-viewers[i]+viewers[i+advtime]
        if answer<v:
            answer = v
            time = i+1
        answer = max(answer,v)
    return("{}:{}:{}".format(str(time//h2s).zfill(2),str((time%h2s)//m2s).zfill(2),str((time%h2s%m2s)).zfill(2)))

if __name__ == "__main__":
    playtime = "99:59:59"
    adv_time = "25:00:00"
    logs = ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]
    result = "01:00:00"
    print(solution(playtime, adv_time, logs), result)