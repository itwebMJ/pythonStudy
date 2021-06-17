use encore;
select e.last_name from employees e
join employees d
on e.employee_id = d.employee_id
where e.employee_id = '176';

create table job_grades(
gra char(1) primary key,
lowest_sal int ,
highest_sal int
);

insert into job_grades values('A', 1000, 2999);
insert into job_grades values('B', 3000, 5999);
insert into job_grades values('C', 6000, 9999);
insert into job_grades values('D', 10000, 14999);
insert into job_grades values('E', 15000, 24999);
insert into job_grades values('F', 25000, 40000);
desc job_grades;
select * from job_grades;
select employee_id, last_name, salary, gra
from employees e join job_grades j
on e.salary between j.lowest_sal and j.highest_sal
