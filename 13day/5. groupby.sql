use encore;
select avg(salary), max(salary), min(salary), sum(salary)
from employees
where job_id like '%REP%';

#단일행함수
select ucase(last_name), last_name
from employees;

select count(commission_pct)
from employees
where department_id=80;

#그룹함수는 널인값을 빼고 계산
#ifnull(p1, p2):p1 컬럼이 null이면 p2로 대체
select avg(ifnull(commission_pct, 0))
from employees;

select department_id, avg(salary)
from employees
group by department_id
order by avg(salary) desc;

select department_id, job_id, sum(salary)
from employees
group by department_id, job_id;

select department_id, count(last_name)
from employees
group by department_id;

select department_id, max(salary)
from employees
group by department_id
having max(salary)>10000;
