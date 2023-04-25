-- https://school.programmers.co.kr/learn/courses/30/lessons/59045

select ins.animal_id, ins.animal_type, ins.name from animal_ins as ins
inner join animal_outs as outs on ins.animal_id = outs.animal_id
where ins.SEX_UPON_INTAKE != outs.sex_upon_outcome
order by ins.animal_id