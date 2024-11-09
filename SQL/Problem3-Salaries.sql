with division as (select departmentid, name, salary, dense_rank() over (partition by departmentid order by salary desc) as rownum from employee order by departmentid) select d.name as Department, e.name as Employee, Salary from division e join department d on e.departmentid = d.id where rownum <= 3