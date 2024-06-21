-- https://school.programmers.co.kr/learn/courses/30/lessons/157340

select distinct car_id, 
    case 
        when car_id in (SELECT car_id from CAR_RENTAL_COMPANY_RENTAL_HISTORY
                        where '2022-10-16' BETWEEN start_date and end_date)
        then "대여중"
        else "대여 가능"
    end as availability
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
order by car_id desc