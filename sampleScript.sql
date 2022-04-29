select *
from TableA ta
    join TableB tb on tb.Id=tb.tAId
    left join TableC tc on tc.Id=tb.tCId
    right join TableD td 
        on td.Id=tc.tBId
where b.name='something'
order by ta.Name

    select count(1) as myCount
    from TableE te
    group by te.someColumn
    having count(myId) > 5