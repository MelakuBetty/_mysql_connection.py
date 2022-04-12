from db.DB import DB


class Select(DB):
    cxnx = DB()
    print(cxnx.connect("select * from actor",'select'))
    print(cxnx.connect("select last_name from actor ORDER BY first_name asc",'select'))
    print(cxnx.connect("select first_name from actor ORDER BY first_name asc",'select'))
    print(cxnx.connect("select title from film ORDER BY title desc",'select'))
    print(cxnx.connect("select country from country ORDER BY country asc",'select'))
