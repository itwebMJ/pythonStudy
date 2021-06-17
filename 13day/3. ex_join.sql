#4-1
select last_name, e.department_id, department_name
from employees e join departments d
on e.department_id = d.department_id;

#4-2
select job_id, location_id
from employees join departments
using(department_id)
where department_id=80;

#4-3
select last_name, department_name, d.location_id, city
from employees e join departments d
on e.department_id = d.department_id 
join locations l
on d.location_id = l.location_id
where commission_pct is not null;

#4-4
select last_name, department_name
from employees join departments
using(department_id)
where last_name like '%a%'
and not last_name like 'a%';

#4-5
select last_name, job_id, department_id, department_name
from employees join departments
using(department_id)
join locations
using(location_id)
where city='toronto';

#4-6
select e.employee_id as 'EMP#', e.last_name as Employee, 
m.employee_id as 'Mgr#', m.last_name as Manager
from employees e join employees m
on e.manager_id = m.employee_id;

#4-7
select e.employee_id as 'EMP#', e.last_name as Employee, 
m.employee_id as 'Mgr#', m.last_name as Manager
from employees e left outer join employees m
on e.manager_id = m.employee_id;

#4-8. 각 사원을 동료 이름을 같이 출력. 
select e.last_name, e.department_id, c.last_name as colleague
from employees e join employees c
on e.department_id = c.department_id
where e.last_name <> c.last_name;

#4-9
desc job_grades;
select last_name, job_id, department_name, salary, gra
from employees join departments
using(department_id)
join job_grades 
on salary between lowest_sal and highest_sal; 

#4-10
select e2.last_name, e2.hire_date
from employees e1 join employees e2
on e1.hire_date < e2.hire_date
where e1.last_name='Davies';

select hire_date from employees where last_name='Davies';

#4-11
select e.last_name as Employee, e.hire_date as 'Emp Hired', 
m.last_name as Manager, m.hire_date as 'Mgr Hired'
from employees e join employees m
on e.hire_date < m.hire_date;
