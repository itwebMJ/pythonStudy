/*
서브쿼리: 문장 안에 있는 문장. 
조건, 일괄 insert, create, update, delete에서 사용됨
select 컬럼명....
from 테이블
where 조건 (서브쿼리)
*/
#where 조건에서 서브쿼리 사용
select last_name, salary
from employees
where salary > (select salary from employees where last_name='Abel');

#서브쿼리를 사용하여 테이블 생성
create table emp1
as
select employee_id as emp_id, last_name as name, salary as sal, 
department_id as dept_id
from employees
where 1=0;

desc emp1;

#서브쿼리 사용하여 여러줄 insert
insert into emp1
select employee_id, last_name, salary, department_id
from employees
where department_id=80;

select * from emp1;

#merge: 테이블 합병. A, B를 합친다=> A에 합치는데 B에는 있는데 A에는 없는줄은 A에 새로 추가하고
#A, B양쪽에 다 있는 줄은 A의 행을 B의 값으로 갱신
insert into emp
select * from employees as e
on duplicate key update emp.employee_id=e.employee_id,
emp.first_name=e.first_name,
emp.last_name=e.last_name,
emp.email=e.email,
emp.phone_number=e.phone_number,
emp.hire_date=e.hire_date,
emp.job_id=e.job_id,
emp.salary=e.salary,
emp.commission_pct=e.commission_pct,
emp.manager_id=e.manager_id,
emp.department_id=e.department_id;
