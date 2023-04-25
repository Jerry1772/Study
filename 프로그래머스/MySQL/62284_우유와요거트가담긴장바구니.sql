-- https://school.programmers.co.kr/learn/courses/30/lessons/62284

SELECT cart_id from cart_products 
where cart_id in (select cart_id from cart_products where name='Yogurt') and name = 'Milk'