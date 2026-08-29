-- Write your query below

with base as (
select *,
dense_rank() over (partition by student_id order by score desc, exam_id) as rnk
from exam_results
)

select student_id, exam_id, score from base
where rnk = 1
order by student_id

