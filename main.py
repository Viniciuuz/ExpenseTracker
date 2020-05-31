# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'finalV2.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime
import pandas as pd

today = datetime.today()


class Ui_ExpenseTracker(object):
    def setupUi(self, ExpenseTracker):
        ExpenseTracker.setObjectName("ExpenseTracker")
        ExpenseTracker.resize(587, 486)

        self.gridLayout_2 = QtWidgets.QGridLayout(ExpenseTracker)
        self.gridLayout_2.setObjectName("gridLayout_2")

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        self.tabWidget = QtWidgets.QTabWidget(ExpenseTracker)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setObjectName("tabWidget")

        self.summary_tab = QtWidgets.QWidget()
        self.summary_tab.setObjectName("summary_tab")

        self.gridLayout_4 = QtWidgets.QGridLayout(self.summary_tab)
        self.gridLayout_4.setObjectName("gridLayout_4")

        self.main_table = QtWidgets.QTableView(self.summary_tab)
        self.main_table.setObjectName("main_table")
        self.main_table.setModel(PandasModel(pd.read_csv('expenses.log')))
        self.main_table.horizontalHeader().setStretchLastSection(True)

        self.gridLayout_4.addWidget(self.main_table, 2, 0, 1, 1)

        self.summary_groupBox = QtWidgets.QGroupBox(self.summary_tab)
        self.summary_groupBox.setObjectName("summary_groupBox")

        self.gridLayout_3 = QtWidgets.QGridLayout(self.summary_groupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")

        self.select_category = QtWidgets.QComboBox(self.summary_groupBox)
        self.select_category.setMaximumSize(QtCore.QSize(200, 16777215))
        self.select_category.setObjectName("select_category")
        self.select_category.addItem("")
        self.select_category.addItem("")
        self.select_category.addItem("")
        self.select_category.addItem("")
        self.select_category.addItem("")

        self.gridLayout_3.addWidget(self.select_category, 0, 5, 1, 1)

        self.month_label = QtWidgets.QLabel(self.summary_groupBox)
        self.month_label.setMaximumSize(QtCore.QSize(35, 16777215))
        self.month_label.setObjectName("month_label")

        self.gridLayout_3.addWidget(self.month_label, 0, 0, 1, 1)

        self.select_month = QtWidgets.QComboBox(self.summary_groupBox)
        self.select_month.setMaximumSize(QtCore.QSize(100, 16777215))
        self.select_month.setObjectName("select_month")
        self.select_month.addItem("")
        self.select_month.addItem("")
        self.select_month.addItem("")
        self.select_month.addItem("")
        self.select_month.addItem("")
        self.select_month.addItem("")
        self.select_month.addItem("")
        self.select_month.addItem("")
        self.select_month.addItem("")
        self.select_month.addItem("")
        self.select_month.addItem("")
        self.select_month.addItem("")
        self.select_month.addItem("")

        self.gridLayout_3.addWidget(self.select_month, 0, 1, 1, 1)

        self.category_label = QtWidgets.QLabel(self.summary_groupBox)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.category_label.sizePolicy().hasHeightForWidth())

        self.category_label.setSizePolicy(sizePolicy)
        self.category_label.setMaximumSize(QtCore.QSize(50, 16777215))
        self.category_label.setObjectName("category_label")
        self.gridLayout_3.addWidget(self.category_label, 0, 4, 1, 1)
        self.year_input = QtWidgets.QLineEdit(self.summary_groupBox)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.year_input.sizePolicy().hasHeightForWidth())

        self.year_input.setSizePolicy(sizePolicy)
        self.year_input.setMaximumSize(QtCore.QSize(40, 16777215))
        self.year_input.setText("2020")
        self.year_input.setMaxLength(4)
        self.year_input.setObjectName("year_input")
        self.gridLayout_3.addWidget(self.year_input, 0, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.summary_groupBox)
        self.label.setMaximumSize(QtCore.QSize(25, 16777215))
        self.label.setObjectName("label")

        self.gridLayout_3.addWidget(self.label, 0, 2, 1, 1)

        self.bt_updateTable = QtWidgets.QPushButton(self.summary_groupBox)
        self.bt_updateTable.clicked.connect(self.filter_table)

        font = QtGui.QFont()
        font.setPointSize(10)

        self.bt_updateTable.setFont(font)
        self.bt_updateTable.setObjectName("bt_updateTable")

        self.gridLayout_3.addWidget(self.bt_updateTable, 1, 0, 1, 10)
        self.gridLayout_4.addWidget(self.summary_groupBox, 0, 0, 1, 1)

        self.tabWidget.addTab(self.summary_tab, "")

        self.register_tab = QtWidgets.QWidget()
        self.register_tab.setObjectName("register_tab")

        self.gridLayout = QtWidgets.QGridLayout(self.register_tab)
        self.gridLayout.setObjectName("gridLayout")

        self.select_category_register = QtWidgets.QComboBox(self.register_tab)
        self.select_category_register.setMaximumSize(QtCore.QSize(150, 16777215))
        self.select_category_register.setObjectName("select_category_register")
        self.select_category_register.addItem("")
        self.select_category_register.addItem("")
        self.select_category_register.addItem("")
        self.select_category_register.addItem("")
        self.select_category_register.addItem("")

        self.gridLayout.addWidget(self.select_category_register, 1, 3, 1, 1)

        self.calendarWidget = QtWidgets.QCalendarWidget(self.register_tab)

        font = QtGui.QFont()
        font.setPointSize(12)

        self.calendarWidget.setFont(font)
        self.calendarWidget.setObjectName("calendarWidget")

        self.gridLayout.addWidget(self.calendarWidget, 4, 0, 1, 6)

        self.description_label_2 = QtWidgets.QLabel(self.register_tab)
        self.description_label_2.setMaximumSize(QtCore.QSize(60, 16777215))
        self.description_label_2.setObjectName("description_label_2")

        self.gridLayout.addWidget(self.description_label_2, 1, 0, 1, 1)

        self.description_input_2 = QtWidgets.QLineEdit(self.register_tab)
        self.description_input_2.setMaximumSize(QtCore.QSize(150, 16777215))
        self.description_input_2.setText("")
        self.description_input_2.setObjectName("description_input_2")

        self.gridLayout.addWidget(self.description_input_2, 2, 1, 1, 1)

        self.category_label_tab2 = QtWidgets.QLabel(self.register_tab)
        self.category_label_tab2.setMaximumSize(QtCore.QSize(60, 16777215))
        self.category_label_tab2.setObjectName("category_label_tab2")

        self.gridLayout.addWidget(self.category_label_tab2, 1, 2, 1, 1)

        self.category_label_tab2_2 = QtWidgets.QLabel(self.register_tab)
        self.category_label_tab2_2.setMaximumSize(QtCore.QSize(60, 16777215))
        self.category_label_tab2_2.setObjectName("category_label_tab2_2")

        self.gridLayout.addWidget(self.category_label_tab2_2, 2, 0, 1, 1)

        self.bt_register = QtWidgets.QPushButton(self.register_tab)
        self.bt_register.clicked.connect(self.register_entry)

        font = QtGui.QFont()
        font.setPointSize(12)

        self.bt_register.setFont(font)
        self.bt_register.setObjectName("bt_register")

        self.gridLayout.addWidget(self.bt_register, 5, 0, 1, 6)

        self.date_label = QtWidgets.QLabel(self.register_tab)

        font = QtGui.QFont()
        font.setPointSize(15)

        self.date_label.setFont(font)
        self.date_label.setAlignment(QtCore.Qt.AlignCenter)
        self.date_label.setObjectName("date_label")

        self.gridLayout.addWidget(self.date_label, 3, 0, 1, 6)

        self.select_category_register_2 = QtWidgets.QComboBox(self.register_tab)
        self.select_category_register_2.setMaximumSize(QtCore.QSize(150, 16777215))
        self.select_category_register_2.setObjectName("select_category_register_2")
        self.select_category_register_2.addItem("")
        self.select_category_register_2.addItem("")

        self.gridLayout.addWidget(self.select_category_register_2, 1, 1, 1, 1)

        self.description_label = QtWidgets.QLabel(self.register_tab)
        self.description_label.setMaximumSize(QtCore.QSize(60, 16777215))
        self.description_label.setObjectName("description_label")

        self.gridLayout.addWidget(self.description_label, 2, 2, 1, 1)

        self.description_input = QtWidgets.QLineEdit(self.register_tab)
        self.description_input.setMaximumSize(QtCore.QSize(150, 16777215))
        self.description_input.setText("")
        self.description_input.setObjectName("description_input")

        self.gridLayout.addWidget(self.description_input, 2, 3, 1, 1)

        self.tabWidget.addTab(self.register_tab, "")

        self.horizontalLayout_3.addWidget(self.tabWidget)

        self.gridLayout_2.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)

        self.label_3 = QtWidgets.QLabel(ExpenseTracker)

        font = QtGui.QFont()
        font.setPointSize(9)

        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)

        self.retranslateUi(ExpenseTracker)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(ExpenseTracker)

    def retranslateUi(self, ExpenseTracker):
        _translate = QtCore.QCoreApplication.translate
        ExpenseTracker.setWindowTitle(_translate("ExpenseTracker", "ExpenseTracker"))
        self.summary_groupBox.setTitle(_translate("ExpenseTracker", "Filter"))
        self.select_category.setItemText(0, _translate("ExpenseTracker", "Select"))
        self.select_category.setItemText(1, _translate("ExpenseTracker", "Bill"))
        self.select_category.setItemText(2, _translate("ExpenseTracker", "Food"))
        self.select_category.setItemText(3, _translate("ExpenseTracker", "Groceries"))
        self.select_category.setItemText(4, _translate("ExpenseTracker", "Payment"))
        self.month_label.setText(_translate("ExpenseTracker", "Month:"))
        self.select_month.setItemText(0, _translate("ExpenseTracker", "Select"))
        self.select_month.setItemText(1, _translate("ExpenseTracker", "Jan"))
        self.select_month.setItemText(2, _translate("ExpenseTracker", "Feb"))
        self.select_month.setItemText(3, _translate("ExpenseTracker", "Mar"))
        self.select_month.setItemText(4, _translate("ExpenseTracker", "Apr"))
        self.select_month.setItemText(5, _translate("ExpenseTracker", "May"))
        self.select_month.setItemText(6, _translate("ExpenseTracker", "Jun"))
        self.select_month.setItemText(7, _translate("ExpenseTracker", "Jul"))
        self.select_month.setItemText(8, _translate("ExpenseTracker", "Aug"))
        self.select_month.setItemText(9, _translate("ExpenseTracker", "Sep"))
        self.select_month.setItemText(10, _translate("ExpenseTracker", "Oct"))
        self.select_month.setItemText(11, _translate("ExpenseTracker", "Nov"))
        self.select_month.setItemText(12, _translate("ExpenseTracker", "Dec"))
        self.category_label.setText(_translate("ExpenseTracker", "Category:"))
        self.label.setText(_translate("ExpenseTracker", "Year:"))
        self.bt_updateTable.setText(_translate("ExpenseTracker", "Filter/Update"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.summary_tab), _translate("ExpenseTracker", "Summary"))
        self.select_category_register.setItemText(0, _translate("ExpenseTracker", "Select"))
        self.select_category_register.setItemText(1, _translate("ExpenseTracker", "Bill"))
        self.select_category_register.setItemText(2, _translate("ExpenseTracker", "Food"))
        self.select_category_register.setItemText(3, _translate("ExpenseTracker", "Groceries"))
        self.select_category_register.setItemText(4, _translate("ExpenseTracker", "Payment"))
        self.description_label_2.setText(_translate("ExpenseTracker", "Transaction:"))
        self.category_label_tab2.setText(_translate("ExpenseTracker", "Category:"))
        self.category_label_tab2_2.setText(_translate("ExpenseTracker", "value:"))
        self.bt_register.setText(_translate("ExpenseTracker", "Register"))
        self.date_label.setText(_translate("ExpenseTracker", "Date:"))
        self.select_category_register_2.setItemText(0, _translate("ExpenseTracker", "Spent"))
        self.select_category_register_2.setItemText(1, _translate("ExpenseTracker", "Received"))
        self.description_label.setText(_translate("ExpenseTracker", "Description:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.register_tab), _translate("ExpenseTracker", "Register"))
        self.label_3.setText(_translate("ExpenseTracker", "<html><head/><body><p>Created by: <a href=\"https://github.com/Viniciuuz\"><span style=\" text-decoration: underline; color:#0000ff;\">https://github.com/Viniciuuz</span></a></p></body></html>"))

    def register_entry(self):
        trans    = self.select_category_register_2.currentText()
        date     = self.calendarWidget.selectedDate().toString("yyyy-MM-dd")
        value    = self.description_input_2.text()
        category = self.select_category_register.currentText()
        desc     = self.description_input.text()
    
        data     = {'Transaction': trans, 'Date': date, 'Value': value, 'Category': category, 'Description': desc}

        pd.read_csv('expenses.log').append(data, ignore_index=True).to_csv('expenses.log', index=False)

        self.main_table.setModel(PandasModel(pd.read_csv('expenses.log')))

        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Success")
        msg.setText('Succesfully registred')
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.exec_()

    def filter_table(self):
        filter_month    = self.select_month.currentText()
        filter_year     = self.year_input.text()
        filter_category = self.select_category.currentText()
        
        df = pd.read_csv('expenses.log', parse_dates=['Date'], date_parser=lambda x: pd.to_datetime(x, format='%Y/%m/%d'))

        #update table without any filter
        if filter_month == 'Select' and filter_category == 'Select':
            self.main_table.setModel(PandasModel(df))

        #filter only by month
        elif filter_month != 'Select' and filter_category == 'Select':
            self.main_table.setModel(PandasModel(df[(df['Date'].dt.month == monthToNum(filter_month))]))

        #filter only by category
        elif filter_category != 'Select' and filter_month == 'Select':
            self.main_table.setModel(PandasModel(df[(df['Category'] == filter_category)]))

        #filter by month and category
        elif filter_category != 'Select' and filter_month != 'Select':
            self.main_table.setModel(PandasModel(df[(df['Date'].dt.month == monthToNum(filter_month)) & df['Category'] == filter_category]))

        #-----------year filtering-----------

        #filter only by year
        elif filter_month == 'Select' and filter_year != today.year and filter_category == 'Select':
            self.main_table.setModel(PandasModel(df[df['Date'].df.year == filter_year]))

        #filter by month, year and category
        elif filter_month != 'Select' and filter_year != today.year and filter_category != Select:
            self.main_table.setModel(PandasModel(df[(df['Date'].dt.month == monthToNum(filter_month)) & df['Date'].df.year == filter_year]))

        #filter by month and year
        elif filter_month != 'Select' and filter_year != today.year and filter_category == 'Select':
            self.main_table.setModel(PandasModel(df[(df['Date'].dt.month == monthToNum(filter_month)) & df['Date'].df.year == filter_year & df['Category'] == filter_category]))

        #filter ny category and year
        elif filter_month == 'Select' and filter_year != today.year and filter_category != 'Select':
             self.main_table.setModel(PandasModel(df[df['Date'].df.year == filter_year & df['Category'] == filter_category]))

def monthToNum(shortMonth):
    return{
        'Jan' : 1,
        'Feb' : 2,
        'Mar' : 3,
        'Apr' : 4,
        'May' : 5,
        'Jun' : 6,
        'Jul' : 7,
        'Aug' : 8,
        'Sep' : 9, 
        'Oct' : 10,
        'Nov' : 11,
        'Dec' : 12
    }[shortMonth]



class PandasModel(QtCore.QAbstractTableModel):
    def __init__(self, data, parent=None):
        QtCore.QAbstractTableModel.__init__(self, parent)
        self._data = data

    def rowCount(self, parent=None):
        return len(self._data.values)

    def columnCount(self, parent=None):
        return self._data.columns.size

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if index.isValid():
            if role == QtCore.Qt.DisplayRole:
                return str(self._data.values[index.row()][index.column()])
        return None

    def headerData(self, col, orientation, role):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return self._data.columns[col]
        return None

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ExpenseTracker = QtWidgets.QWidget()
    ui = Ui_ExpenseTracker()
    ui.setupUi(ExpenseTracker)
    ExpenseTracker.show()
    sys.exit(app.exec_())
