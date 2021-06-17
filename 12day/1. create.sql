#스키마 데이터베이스 => 저장소 한 단위. 한 스미마에 테이블 여러개 만들어서 사용 가능

#use 스미마 : 사용할 db 선택
use test;

#테이블 생성
create table tba(
num integer primary key,
name char(10) not null
);

#insert : 테이블에 한줄 추가

insert into tba values(1, 'aaaa');
insert into tba values(2, 'bbb');
insert into tba values(3, 'ccc');
insert into tba values(4, 'ddd');

commit;

#검색

select * from tba;
