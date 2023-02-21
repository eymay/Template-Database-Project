from flask import Flask
import views
from subprocess import call
import db_updated_check
#url rules created for each table

def set_urls(app,table, view):
    app.add_url_rule("/", view_func=views.home_page)
    app.add_url_rule("/"+table+"/<int:page>", endpoint=table+"_data_page", view_func=view.get_table, methods=["GET","POST"])
    app.add_url_rule("/"+table+"/add", endpoint=table+"_data_add", view_func=view.add_row,  methods=["POST"])
    app.add_url_rule("/"+table+"/delete", endpoint=table+"_data_delete", view_func=view.delete_row, methods=["GET", "POST"])
    app.add_url_rule("/"+table+"/update", endpoint=table+"_data_update", view_func=view.update_row, methods=["GET", "POST"])
    app.add_url_rule("/"+table+"/search", endpoint=table+"_data_search", view_func=view.search, methods=["GET", "POST"])


def create_app():
    app = Flask(__name__)
    app.config.from_object("settings")

    set_urls(app, "fed", views.Fed_Table())
    set_urls(app, "price", views.Price_Table())
   

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
