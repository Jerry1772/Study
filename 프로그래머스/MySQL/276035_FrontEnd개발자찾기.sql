-- https://school.programmers.co.kr/learn/courses/30/lessons/276035

select d.ID, d.EMAIL, d.FIRST_NAME, d.LAST_NAME 
from DEVELOPERS as d
where d.SKILL_CODE&(
    select sum(s.CODE) from SKILLCODES as s
    where s.CATEGORY="Front End"
) > 0
order by d.ID asc;