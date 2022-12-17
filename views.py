from flask import current_app, render_template
import services.customer_service as customerService
import sqlite3 as sql

def home_page():
    return render_template("home.html")


def customers_page():
    customers = customerService.get_customers()
    return render_template("customers.html", customers=customers)


def add_customers_page():
    
    return render_template("AddCustomer.html")



def delete_customer(id):
   
    customerService.delete_customer(id)
    customers = customerService.get_customers()

    return render_template("customers.html", customers=customers)

def people_page():
    
    return render_template("people.html")

def add_people_page():
    
    return render_template("AddPeople.html")


def customer_transactions_page():
    
    return render_template("CustomerTransactions.html")

def add_customer_transactions_page():
    
    return render_template("AddCustomerTransactions.html")


def invoice_lines_page():
    
    return render_template("InvoiceLines.html")

def add_invoice_lines_page():
    
    return render_template("AddInvoiceLines.html")


def invoices_page():
    
    return render_template("Invoices.html")

def add_invoices_page():
    
    return render_template("AddInvoices.html")

def order_lines_page():
    
    return render_template("OrderLines.html")

def add_order_lines_page():
    
    return render_template("AddOrderLines.html")


def orders_page():
    
    return render_template("Orders.html")

def add_orders_page():
    
    return render_template("AddOrders.html")

def stockitem_holdings_page():
    
    return render_template("StockItemHoldings.html")

def add_stockitem_holdings_page():
    
    return render_template("AddStockItemHoldings.html")

def stockitem_transactions_page():
    
    return render_template("StockItemTransactions.html")

def add_stockitem_transactions_page():
    
    return render_template("AddStockItemTransactions.html")


def stockitems_page():
    
    return render_template("StockItems.html")

def add_stockitems_page():
    
    return render_template("AddStockItems.html")

def customer_transactions():
    customer_transactions 
