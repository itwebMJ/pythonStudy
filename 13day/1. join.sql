join: 2개 이상의 테이블을 연결해서 검색

natural join: 조인할 테이블의 동일한 이름 컬럼을 기준으로 값이 같은 줄들을 연결

using: 조인 기준으로 사용할 컬럼 명시
on: 조인 조건 작성

<등가조인. 조인기준 컬럼의 값이 같을 조건으로 조인)
select 이름, 부서이름
from 사원테이블 natural join 부서테이블 

select 이름, 부서이름
from 사원테이블 join 부서테이블 
using(부서번호)   => 조인할 컬럼을 지정

select 이름, 부서이름
from 사원테이블 e join 부서테이블 d
on e.부서번호 = d.부서번호
where 부서번호=10

outer join(포괄조인): 조인 조건을 만족하지 않는 행을 같이 보여줌
left outer join: 왼쪽 테이블의 만족하지 않는 행을 같이 보여줘라
right outer join: 오른쪽 테이블의 만족하지 않는 행을 같이 보여줘라

<left outer join>
select 이름, 부서이름
from 사원테이블 e left outer join 부서테이블 d
on e.부서번호 = d.부서번호

<right outer join>
select 이름, 부서이름
from 사원테이블 e right outer join 부서테이블 d
on e.부서번호 = d.부서번호

<full outer join>
select 이름, 부서이름
from 사원테이블 e left outer join 부서테이블 d
on e.부서번호 = d.부서번호
union
select 이름, 부서이름
from 사원테이블 e right outer join 부서테이블 d
on e.부서번호 = d.부서번호

<self join: 자기 자신을 조인>=> 테이블 별칭 꼭 사용해야 함
사번이 175번인 사람의 매니저 이름이 무엇인가?
select e.이름, m.이름
from 사원테이블 e join 사원테이블 m
on e.manager_id = m.사번
where e.사번=175

<비등가조인: 등가(=)가 아닌 조건으로 조인>
select employee_id, last_name, salary, gra
from employees e join job_grades j
on e.salary between j.lowest_sal and j.highest_sal;
