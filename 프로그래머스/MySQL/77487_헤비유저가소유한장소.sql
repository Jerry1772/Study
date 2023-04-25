-- https://school.programmers.co.kr/learn/courses/30/lessons/77487

select * from places
where host_id in (select host_id from places group by host_id having count(host_id)>1)