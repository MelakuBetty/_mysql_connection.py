from db.DB import DB


class Join(DB):
    cxnx = DB()
    print(cxnx.connect("select f.title from film f right join film_category fc on f.film_id = fc.film_id", 'select'))
