-- Write your query below

/* dense_rank assigns the rank to the same multiple items 

101 88 1 rnk - 1 order by score desc, exam_id asc 
101 88 2 rnk - 2 order by score desc, exam_id asc

*/
with base as (
select *,
dense_rank() over (partition by student_id order by score desc, exam_id) as rnk
from exam_results
)

select student_id, exam_id, score from base
where rnk = 1
order by student_id

