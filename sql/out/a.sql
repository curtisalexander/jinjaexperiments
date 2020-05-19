create table sold as
select  a.store
       ,a.apple_price
       ,a.banana_price
       ,a.carrot_price
       ,a.date_price
from food as a
where a.solddate > 2020-01-02 and a.solddate < 2020-02-01