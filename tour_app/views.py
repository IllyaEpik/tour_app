import flask
from .models import Voucher
import main.settings as settings

def render_tour():
    # voucher = Voucher(
    #     title = "boeing_777", 
    #     date = "09.11.2024",
    #     country = "USA",
    #     price = "30000₴",
    #     description = "flight on birthday"
    # )
    # voucher_2 = Voucher(
    #     title = "boeing_452", 
    #     date = "09.11.2025",
    #     country = "Ukraine",
    #     price = "3000$",
    #     description = "flight on birthday"
    # )
    # voucher_3 = Voucher(      
    #     title = "boeing_067", 
    #     date = "09.11.2026",
    #     country = "Germany",
    #     price = "20000₴",
    #     description = "flight on birthday")
    # try:
    #     settings.data_base.session.add(voucher)
    #     settings.data_base.session.add(voucher_2)
    #     settings.data_base.session.add(voucher_3)
    #     settings.data_base.session.commit()
    # except Exception as error: print (error)
    list_tour = []
    for tour in Voucher.query.all():
        list_tour.append(tour)
    print("1")
    if flask.request.method == "POST":
        value = flask.request.form["button"]
        print(value, tour.id)
        # list_tour = []
        # for tour in Voucher.query.filter_by()
        return flask.render_template("tour.html", list_tour = list_tour, id = int(value))
    return flask.render_template("all_tours.html", list_tour = list_tour)

    