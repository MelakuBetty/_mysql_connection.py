from db.DB import DB


class Update(DB):
    cxnx = DB()
    cxnx.connect("UPDATE actor SET first_name = 'Lilah' WHERE first_name = 'ADAM'",'select')
    cxnx.connect("UPDATE actor SET first_name = 'Aviva' WHERE first_name = 'Aviva'",'select')
    cxnx.connect("UPDATE country SET country = 'Israel' WHERE country = 'Afghanistan'",'select')
    cxnx.connect("UPDATE city SET city = 'Ashdod' WHERE city = 'Abu Dhabi'",'select')
    cxnx.connect("UPDATE address SET address = 'Ad Halom' WHERE address = '47 MySakila Drive'",'select')