use encore;
select * from employees;
select * from departments;
select department_id, department_name
from departments
where department_id<50;

select last_name, 12*salary*commission_pct
from employees;

select last_name, 'aaa', salary, salary+300 'sal 2' 
from employees;

select employee_id, last_name, hire_date
from employees
order by hire_date desc;
select distinct department_id from employees;

desc employees;

select employee_id, last_name, job_id, department_id
from employees
where department_id=90;

select last_name, job_id, department_id
from employees
where last_name='Whalen';

select last_name
from employees
where last_name like '_o%';

select sysdate()
from dual;

select * from locations;
