import copy
# object representations of table columns are used as reference
class fed_data(object):
    def __init__(self, row):
        self.Date = row[0]
        self.Interest = row[1]
        self.Vacancy = row[2]
        self.Inflation = row[3]

    def setID(self, id=None):
        self.Date = id
        return self.Date

    def toDict(self):
        fed_data = {
            'Date': self.Date,
            'Interest': self.Interest,
            'Vacancy': self.Vacancy,
            'Inflation': self.Inflation,
        }
        return fed_data

    def get(self):
        return self.toDict()

    def getCopy(self):
        return copy.deepcopy(self)

    def getNonKeyColumns():
        return ["Interest", "Vacancy", "Inflation"]

    def getColumns():
        return ["Date", "Interest", "Vacancy", "Inflation"]

class price_data(object):
    def __init__(self, row):
        self.Date = row[0]
        self.Interest = row[1]
        self.Vacancy = row[2]
        self.Inflation = row[3]
        self.Price= row[4]
        self.Value= row[5]
        self.Adjusted_Price= row[6]
        self.Adjusted_Value= row[7]
        self.Next_Quarter= row[8]

    def setID(self, id=None):
        self.Date = id
        return self.Date

    def toDict(self):
        price_data = {
            'Date': self.Date,
            'Interest': self.Interest,
            'Vacancy': self.Vacancy,
            'Inflation': self.Inflation,
            'Price': self.Price,
            'Value': self.Value,
            'Adjusted_Price': self.Adjusted_Price,
            'Adjusted_Value': self.Adjusted_Value,
            'Next_Quarter': self.Next_Quarter,
        }
        return price_data

    def get(self):
        return self.toDict()

    def getCopy(self):
        return copy.deepcopy(self)

    def getNonKeyColumns():
        return ["Interest", "Vacancy", "Inflation", "Price", "Value","Adjusted_Price", "Adjusted_Value", "Next_Quarter" ]

    def getColumns():
        return ["Date", "Interest", "Vacancy", "Inflation","Price", "Value","Adjusted_Price", "Adjusted_Value", "Next_Quarter" ]


    
class CustomerTransactions(object):
    def __init__(self,row):
        self.CustomerTransactionID = row[0]
        self.CustomerID =row[1]
        self.InvoiceID =row[2]
        self.TransactionDate =row[3]
        self.AmountExcludingTax =row[4]
        self.TaxAmount =row[5]
        self.TransactionAmount =row[6]
        self.OutstandingBalance =row[7]
        self.FinalizationDate =row[8]
        self.IsFinalized =row[9]

    def toDict(self):
        customertransactions = {
            'CustomerTransactionID': self.CustomerTransactionID,
            'CustomerID': self.CustomerID,
            'InvoiceID': self.InvoiceID,
            'TransactionDate': self.TransactionDate,
            'AmountExcludingTax': self.AmountExcludingTax,
            'TaxAmount': self.TaxAmount,
            'TransactionAmount': self.TransactionAmount,
            'OutstandingBalance': self.OutstandingBalance,
            'FinalizationDate': self.FinalizationDate,
            'IsFinalized': self.IsFinalized,
        }
        return customertransactions

    def get(self):
        return self.toDict()

    def getCopy(self):
        return copy.deepcopy(self)

    def getNonKeyColumns():
        return ["CustomerID", "InvoiceID", "TransactionDate", "AmountExcludingTax", "TaxAmount", "TransactionAmount","OutstandingBalance","FinalizationDate","IsFinalized"]

    def getColumns():
        return ["CustomerTransactionID","CustomerID", "InvoiceID", "TransactionDate", "AmountExcludingTax", "TaxAmount", "TransactionAmount","OutstandingBalance","FinalizationDate","IsFinalized"]


class InvoiceLines(object):
    def __init__(self, row):
        self.InvoiceLineID = row[0]
        self.InvoiceID = row[1]
        self.StockItemID = row[2]
        self.Description = row[3]
        self.Quantity = row[4]
        self.UnitPrice = row[5]
        self.LineProfit = row[6]
        self.ExtendedPrice = row[7]

    def toDict(self):
        invoicelines = {
            'InvoiceLineID': self.InvoiceLineID,
            'InvoiceID': self.InvoiceID,
            'StockItemID': self.StockItemID,
            'Description': self.Description,
            'Quantity': self.Quantity,
            'UnitPrice': self.UnitPrice,
            'LineProfit': self.LineProfit,
            'ExtendedPrice': self.ExtendedPrice,
        }
        return invoicelines

    def get(self):
        return self.toDict()

    def getCopy(self):
        return copy.deepcopy(self)

    def getNonKeyColumns():
        return ["InvoiceID", "StockItemID", "Description", "Quantity", "UnitPrice","LineProfit","ExtendedPrice"]

    def getColumns():
        return ["InvoiceLineID","InvoiceID", "StockItemID", "Description", "Quantity", "UnitPrice", "LineProfit","ExtendedPrice"]


class Invoices(object):
    def __init__(self, row):
        self.InvoiceID = row[0]
        self.CustomerID = row[1]
        self.OrderID = row[2]
        self.ContactPersonID = row[3]
        self.AccountsPersonID = row[4]
        self.InvoiceDate = row[5]
        self.CustomerPurchaseOrderNumber = row[6]
        self.DeliveryInstructions = row[7]
        self.InternalComments = row[8]
        self.DeliveryRun =row[9]
        self.RunPosition=row[10]
        self.ReturnedDeliveryData=row[11]
        self.ConfirmedDeliveryTime=row[12]
        self.ConfirmedReceivedBy=row[13]

    def toDict(self):
        invoices = {
            'InvoiceID': self.InvoiceID,
            'CustomerID': self.CustomerID,
            'OrderID': self.OrderID,
            'ContactPersonID': self.ContactPersonID,
            'AccountsPersonID': self.AccountsPersonID,
            'InvoiceDate': self.InvoiceDate,
            'CustomerPurchaseOrderNumber': self.CustomerPurchaseOrderNumber,
            'DeliveryInstructions': self.DeliveryInstructions,
            'InternalComments': self.InternalComments,
            'DeliveryRun': self.DeliveryRun,
            'RunPosition': self.RunPosition,
            'ReturnedDeliveryData': self.ReturnedDeliveryData,
            'ConfirmedDeliveryTime': self.ConfirmedDeliveryTime,
            'ConfirmedReceivedBy': self.ConfirmedReceivedBy,
        }
        return invoices

    def get(self):
        return self.toDict()

    def getCopy(self):
        return copy.deepcopy(self)
        
    def getNonKeyColumns():
        return ["CustomerID", "OrderID", "ContactPersonID", "AccountsPersonID", "InvoiceDate", "CustomerPurchaseOrderNumber","DeliveryInstructions","InternalComments", "DeliveryRun","RunPosition","ReturnedDeliveryData","ConfirmedDeliveryTime","ConfirmedReceivedBy"]

    def getColumns():
        return ["InvoiceID","CustomerID", "OrderID", "ContactPersonID", "AccountsPersonID", "InvoiceDate", "CustomerPurchaseOrderNumber","DeliveryInstructions","InternalComments", "DeliveryRun","RunPosition","ReturnedDeliveryData","ConfirmedDeliveryTime","ConfirmedReceivedBy"]



class OrderLines(object):
    def __init__(self, row):
        self.OrderLineID = row[0]
        self.OrderID = row[1]
        self.StockItemID = row[2]
        self.Description = row[3]
        self.Quantity = row[4]
        self.UnitPrice = row[5]
        self.PickedQuantity = row[6]
        self.PickingCompletedWhen = row[7]

    def toDict(self):
        orderlines = {
            'OrderLineID': self.OrderLineID,
            'OrderID': self.OrderID,
            'StockItemID': self.StockItemID,
            'Description': self.Description,
            'UnitPrice': self.UnitPrice,
            'Quantity': self.Quantity,
            'PickedQuantity': self.PickedQuantity,
            'PickingCompletedWhen': self.PickingCompletedWhen,
        }
        return orderlines

    def get(self):
        return self.toDict()

    def getCopy(self):
        return copy.deepcopy(self)

    def getNonKeyColumns():
        return ["OrderID", "StockItemID", "Description", "UnitPrice", "Quantity", "PickedQuantity", "PickingCompletedWhen"]

    def getColumns():
        return ["OrderLineID", "OrderID", "StockItemID", "Description", "UnitPrice", "Quantity", "PickedQuantity", "PickingCompletedWhen"]



class Orders(object):
    def __init__(self, row):
        self.OrderID = row[0]
        self.CustomerID = row[1]
        self.OrderDate = row[2]
        self.ExpectedDeliveryDate = row[3]
        self.CustomerPurchaseOrderNumber = row[4]
        self.IsUndersupplyBackordered = row[5]
        self.PickingCompletedWhen = row[6]
    
    def setID(self, id=None):
        self.id = id
        return self.id

    def toDict(self):
        orders = {
            'OrderID': self.OrderID,
            'CustomerID': self.CustomerID,
            'OrderDate': self.OrderDate,
            'ExpectedDeliveryDate': self.ExpectedDeliveryDate,
            'CustomerPurchaseOrderNumber': self.CustomerPurchaseOrderNumber,
            'IsUndersupplyBackordered': self.IsUndersupplyBackordered,
            'PickingCompletedWhen': self.PickingCompletedWhen,
        }
        return orders

    def get(self):
        return self.toDict()

    def getCopy(self):
        return copy.deepcopy(self)

    def getNonKeyColumns():
        return ["CustomerID", "OrderDate", "ExpectedDeliveryDate", "CustomerPurchaseOrderNumber", "IsUndersupplyBackordered", "PickingCompletedWhen"]

    def getColumns():
        return ["OrderID", "CustomerID", "OrderDate", "ExpectedDeliveryDate", "CustomerPurchaseOrderNumber", "IsUndersupplyBackordered", "PickingCompletedWhen"]


class People(object):
    def __init__(self, row):
        self.PersonID = row[0]
        self.FullName = row[1]
        self.LogonName = row[2]
        self.HashedPassword = row[3]
        self.IsSystemUser = row[4]
        self.IsEmployee = row[5]
        self.IsSalesperson = row[6]
        self.PhoneNumber = row[7]
        self.EmailAddress = row[8]

    def toDict(self):
        people = {
            'PersonID': self.PersonID,
            'FullName': self.FullName,
            'LogonName': self.LogonName,
            'HashedPassword': self.HashedPassword,
            'IsSystemUser': self.IsSystemUser,
            'IsEmployee': self.IsEmployee,
            'IsSalesPerson': self.IsSalesperson,
            'PhoneNumber': self.PhoneNumber,
            'EmailAddress': self.EmailAddress,
        }
        return people

    def get(self):
        return self.toDict()

    def getCopy(self):
        return copy.deepcopy(self)

    def getNonKeyColumns():
        return ["FullName", "LogonName", "HashedPassword", "IsSystemUser", "IsEmployee", "IsSalesperson", "PhoneNumber", "EmailAddress"] 

    def getColumns():
        return ["PersonID", "FullName", "LogonName", "HashedPassword", "IsSystemUser", "IsEmployee", "IsSalesperson", "PhoneNumber", "EmailAddress"] 




class StockItems(object):
    def __init(self, row):
        self.StockItemID = row[0]
        self.StockItemName = row[1]
        self.LeadTimeDays = row[2]
        self.UnitPrice = row[3]
        self.RecommendedRetailPrice = row[4]

    def toDict(self):
        stockitems = {
            'StockItemID': self.StockItemID,
            'StockItemName': self.StockItemName,
            'LeadTimeDays': self.LeadTimeDays,
            'UnitPrice': self.UnitPrice,
            'RecommendedRetailPrice': self.RecommendedRetailPrice,
        }
        return stockitems

    def get(self):
        return self.toDict()

    def getCopy(self):
        return copy.deepcopy(self)

    def getNonKeyColumns():
        return ["StockItemName", "LeadTimeDays", "UnitPrice", "RecommendedRetailPrice"] 

    def getColumns():
        return ["StockItemID", "StockItemName", "LeadTimeDays", "UnitPrice", "RecommendedRetailPrice"] 

class StockItemTransactions(object):
    def __init__(self, row):
        self.StockItemTransactionID = row[0]
        self.StockItemID = row[1]
        self.CustomerID = row[2]
        self.InvoiceID = row[3]
        self.TransactionOccurredWhen = row[4]
        self.Quantity = row[5]

    def toDict(self):
        stockitemtransactions = {
            'StockItemTransactionID': self.StockItemTransactionID,
            'StockID': self.StockItemID,
            'CustomerID': self.CustomerID,
            'InvoiceID': self.InvoiceID,
            'TransactionOccerredWhen': self.TransactionOccurredWhen,
            'Quantity': self.Quantity,
        }
        return stockitemtransactions

    def get(self):
        return self.toDict()

    def getCopy(self):
        return copy.deepcopy(self)

    def getNonKeyColumns():
        return ["StockID", "CustomerID", "InvoiceID", "TransactionOccerredWhen", "Quantity"] 

    def getColumns():
        return ["StockItemTransactionID", "StockID", "CustomerID", "InvoiceID", "TransactionOccerredWhen", "Quantity"] 
