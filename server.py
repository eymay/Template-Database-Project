from flask import Flask
import views
from subprocess import call
import db_updated_check
#url rules created for each table
def create_app():
    app = Flask(__name__)
    app.config.from_object("settings")
    
    fedView = views.Fed_Table()
    app.add_url_rule("/", view_func=views.home_page)
    app.add_url_rule("/fed/<int:page>", endpoint="fed_data_page", view_func=fedView.get_table, methods=["GET","POST"])
    app.add_url_rule("/fed/add", endpoint="fed_data_add", view_func=fedView.add_row,  methods=["POST"])
    app.add_url_rule("/fed/delete", endpoint="fed_data_delete", view_func=fedView.delete_row, methods=["GET", "POST"])
    app.add_url_rule("/fed/update", endpoint="fed_data_update", view_func=fedView.update_row, methods=["GET", "POST"])
    app.add_url_rule("/fed/search", endpoint="fed_data_search", view_func=fedView.search, methods=["GET", "POST"])
   
    priceView = views.Price_Table()
    app.add_url_rule("/", view_func=views.home_page)
    app.add_url_rule("/price/<int:page>", endpoint="price_data_page", view_func=priceView.get_table, methods=["GET","POST"])
    app.add_url_rule("/price/add", endpoint="price_data_add", view_func=priceView.add_row,  methods=["POST"])
    app.add_url_rule("/price/delete", endpoint="price_data_delete", view_func=priceView.delete_row, methods=["GET", "POST"])
    app.add_url_rule("/price/update", endpoint="price_data_update", view_func=priceView.update_row, methods=["GET", "POST"])
    app.add_url_rule("/price/search", endpoint="price_data_search", view_func=priceView.search, methods=["GET", "POST"])
   

    app.config["dbname"] = "import_test.db"
 

    return app

def create_db():
    if not (db_updated_check.database_date_check()):
        rc = call("./import_tables.sh")

if __name__ == "__main__":
    # create_db() ################COMMENT to disable DB creation at every run
    app = create_app()
    port = app.config.get("PORT", 5000)
    app.run(port=port)
