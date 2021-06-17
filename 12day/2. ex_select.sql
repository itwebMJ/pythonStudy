select last_name, salary from  employees where salary >12000;

select last_name, department_id from  employees where employee_id = 176;

select last_name, salary from  employees where salary<5000 or salary >12000;

select last_name, job_id, hire_date from  employees 

where '1998-02-02' < hire_date and  hire_date < '2005-05-01' order by hire_date asc;

select last_name, department_id from  employees where department_id in (20,50) order by last_name asc;

select last_name as Employee, salary as 'Monthly Salary' from  employees where salary<5000 or salary >12000 and department_id in (20,50) ;

select last_name, hire_date from  employees where  '2007-01-01' < hire_date and  hire_date < '2007-12-31';

select last_name, job_id from  employees where  manager_id is null;

select last_name, salary, commission_pct from  employees 
where commission_pct is not null order by commission_pct desc;

select last_name from  employees where last_name like '__a%';

select last_name from  employees where last_name like '%a%' or last_name like '%e%';

select last_name, job_id, salary from  employees where job_id = 'ST_CLERK' or job_id = 'SA_REP' and salary not in(2500 , 3500, 7000);

select last_name as Employee, salary as 'Monthly Salary', commission_pct from  employees 
where commission_pct = 0.2;
