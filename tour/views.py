import flask
import pandas as pd
import os
from main.models import Voucher
from main.settings import main
from main.settings import db

def render_tour():
    xl_path = os.path.abspath(os.path.join(__file__, '../../main/tours.xlsx'))
    xl_read = pd.read_excel(
        io=xl_path,
        header=None,
        names=["id", "title", "date", "country", "price", "description"]
    )
    for index, row in xl_read.iterrows():
        
        vouchers = Voucher(
            id=row["id"],
            title=row["title"],
            date=row["date"],
            country=row["country"],
            price=row["price"],
            description=row["description"]
        )


    db.session.add(vouchers)
    db.session.commit()
    return flask.render_template("tour.html", db = db, voucher = vouchers)




def render_tour_page():
    
    # vouchers = Voucher.query.all()
    return flask.render_template("tour1.html", db = db, voucher = Voucher)