create table {{ tbl }} as
select  a.store
       ,a.apple_price
       ,a.banana_price
       {% for var in vars %}
       ,a.{{ var + "_price" }}
       {% endfor %}
from food as a
where a.solddate > {{ start_date }} and a.solddate < {{ end_date }}
