import datetime
from jinja2 import Environment, FileSystemLoader

env = Environment(
    loader=FileSystemLoader("sql/in"), trim_blocks=True, lstrip_blocks=True
)

template = env.get_template("a.sql")

start_date = "2020-01-02"
end_date = (
    datetime.date.fromisoformat(start_date) + datetime.timedelta(days=30)
).isoformat()

with open("sql/out/a.sql", "w") as f:
    f.write(
        template.render(
            tbl="sold",
            vars=["carrot", "date"],
            start_date=start_date,
            end_date=end_date,
        )
    )
