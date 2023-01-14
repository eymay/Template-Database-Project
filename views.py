from flask import current_app, render_template, request, redirect, url_for

from services.service import *
# Context Class holds the context of the application
class Context():
    def __init__(self):
        self.isEdit = False
        self.selectedID = 0
        self.selectedIDColumn = 0
        self.page = 1

#Table class is the parent class for all the tables
class Table():
    def __init__(self, type, service, data_class):
        self.type = type
        self.service = service
        self.data_class = data_class
        self.page = 1
        self.sort_by = None

    def get_table(self, page):
        service = self.service()

        if page <= 0:
            return redirect(url_for(self.type+"_page", page=1))

        self.sort_by = request.args.get("sortby")

        data = service.get_data(page, self.sort_by)

        self.page = page
        context = Context()
        context.page = self.page

        return render_template("generic_list.html", title=self.type, table=data, context=context)

    def add_row(self):
        row = []
        columns = self.data_class.getColumns()
        for column in columns:
            if column in self.data_class.getNonKeyColumns():
                row.append(request.form[column])
            else:
                row.append(None)

        obj = self.data_class(row)

        service = self.service()
        service.add_row(obj)

        return redirect(url_for(self.type + "_page", page=self.page))

    def update_row(self):
        idString = request.args.get("update_id")
        idString = idString.replace("'", "")
        id = idString.split("[")[1].split(",")[0]
        idColumn = self.data_class.getColumns()[0]
        
        if request.method == "GET":
            service = self.service()
            data = service.get_data(self.page, self.sort_by)
            
            context = Context()
            try:
                context.isEdit = True
                context.selectedID = int(id)
                context.selectedIDColumn = idColumn
            except:
                pass
            return render_template("generic_list.html", title=self.type, table=data, context=context)
        else:
            row = []
            columns = self.data_class.getColumns()
            for column in columns:
                if column in self.data_class.getNonKeyColumns():
                    row.append(request.form[column])
                else:
                    row.append(None)

            obj = self.data_class(row)

            service = self.service()
            service.update_row(obj, id, idColumn)
            return redirect(url_for(self.type + "_page", page=self.page))

    def delete_row(self):
        idString = request.args.get("delete_id")
        idString.replace("'", "")
        id = idString.split("[")[1].split(",")[0]

        idColumn = self.data_class.getColumns()[0]

        service = self.service()
        service.delete_row(id, idColumn)

        return redirect(url_for(self.type + "_page", page=self.page))

    def search(self):
        if request.method == "POST":
            form = {}

            for column in self.data_class.getColumns():
                if request.form[column] != "":
                    form[column] = request.form[column]

            service = self.service()
            search_data = service.search_and_list(form)

            if len(search_data) == 0:
                row = []
                for column in self.data_class.getColumns():
                    row.append("")
                data = self.data_class(row)
                search_data.append(data)

            return render_template("generic_list.html", title=self.type, table=search_data, context=Context())

    def get_table_goto_row(self, id):
        return render_template("generic_list.html", title=self.type, table=self.service().get_data(), context=context)
def home_page():
    return render_template("home.html") 

class Fed_Table(Table):
    def __init__(self):
        super().__init__("fed_data", Fed_Service, fed_data)
class Price_Table(Table):
    def __init__(self):
        super().__init__("price_data", Price_Service, price_data)
