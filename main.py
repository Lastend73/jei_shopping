# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'shoppingmallHlDBnO.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHeaderView, QMainWindow, QPushButton,
    QSizePolicy, QStatusBar, QTabWidget, QTableWidget,
    QTableWidgetItem, QWidget)
import sys
import product_button_function as product_button_function
class Ui_MainWindow(object):
    
    def setupUi(self, MainWindow):
        try :
            if not MainWindow.objectName():
                MainWindow.setObjectName(u"MainWindow")
            MainWindow.resize(900, 300) # 창 크기 조절
            MainWindow.setMouseTracking(False)
            #
            self.centralwidget = QWidget(MainWindow)
            self.centralwidget.setObjectName(u"centralwidget")

            # 탭 위젯 생성 (거래처 태그)
            self.tabWidget = QTabWidget(self.centralwidget)
            self.tabWidget.setObjectName(u"tabWidget")
            self.tabWidget.setGeometry(QRect(5, 5, 890, 290))

            self.tab = QWidget()
            self.tab.setObjectName(u"tab")

            self.pushButton_2 = QPushButton(self.tab)
            self.pushButton_2.setObjectName(u"pushButton_2")
            # self.pushButton_2.clicked.connect(self.on_pushButton_2_clicked)
            self.pushButton_2.clicked.connect(self.on_pushButton_2_clicked)
            self.pushButton_2.setGeometry(QRect(10, 10, 75, 24))

            self.pushButton_3 = QPushButton(self.tab)
            self.pushButton_3.setObjectName(u"pushButton_3")
            self.pushButton_3.clicked.connect(self.on_pushButton_3_clicked)
            self.pushButton_3.setGeometry(QRect(90, 10, 75, 24))
            self.tableWidget = QTableWidget(self.tab)
            if (self.tableWidget.columnCount() < 4):
                self.tableWidget.setColumnCount(4)
            __qtablewidgetitem = QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
            __qtablewidgetitem1 = QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
            __qtablewidgetitem2 = QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
            __qtablewidgetitem3 = QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
            self.tableWidget.setObjectName(u"tableWidget")
            self.tableWidget.setGeometry(QRect(10, 40, 860, 190))

            self.tableWidget.horizontalHeader().setDefaultSectionSize(220)
            self.tableWidget.verticalHeader().setVisible(False)
            
            self.tabWidget.addTab(self.tab, "")

            # 품목 탭
            self.tab1 = QWidget()
            self.tab1.setObjectName(u"tab1")

            self.pushButton = QPushButton(self.tab1)
            self.pushButton.setObjectName(u"pushButton")
            self.pushButton.clicked.connect(self.on_pushButton_clicked)
            self.pushButton.setGeometry(QRect(10, 10, 75, 24))

            # 품목 수정 버튼
            self.pushButton_6 = QPushButton(self.tab1)
            self.pushButton_6.setObjectName(u"pushButton5")
            self.pushButton_6.clicked.connect(self.on_pushButton_6_clicked)
            self.pushButton_6.setGeometry(QRect(90, 10, 75, 24))
            
            self.tableWidget_2 = QTableWidget(self.tab1)
            if (self.tableWidget_2.columnCount() < 4):
                self.tableWidget_2.setColumnCount(4)
            __qtablewidgetitem4 = QTableWidgetItem()
            self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem4)
            __qtablewidgetitem5 = QTableWidgetItem()
            self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem5)
            __qtablewidgetitem6 = QTableWidgetItem()
            self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem6)
            __qtablewidgetitem7 = QTableWidgetItem()
            self.tableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem7)
            self.tableWidget_2.setObjectName(u"tableWidget_2")
            self.tableWidget_2.setGeometry(QRect(10, 40, 860, 190))

            self.tableWidget_2.horizontalHeader().setDefaultSectionSize(220)
            self.tableWidget_2.verticalHeader().setVisible(False)
            self.tabWidget.addTab(self.tab1, "")

            self.tab2 = QWidget()
            self.tab2.setObjectName(u"tab2")

            self.pushButton_5 = QPushButton(self.tab2)
            self.pushButton_5.setObjectName(u"pushButton_5")
            self.pushButton_5.clicked.connect(self.on_pushButton_5_clicked)
            self.pushButton_5.setGeometry(QRect(35, 25, 800, 200))

            self.tabWidget.addTab(self.tab2, "")
            MainWindow.setCentralWidget(self.centralwidget)
            self.statusbar = QStatusBar(MainWindow)
            self.statusbar.setObjectName(u"statusbar")
            MainWindow.setStatusBar(self.statusbar)

            self.retranslateUi(MainWindow)

            self.tabWidget.setCurrentIndex(0)


            QMetaObject.connectSlotsByName(MainWindow)
        except Exception as e:
            print(e)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"쇼핑몰 데이터 가져오기", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"품목 조회", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"병원 조회", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"수정", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"데이터 출력하기", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"수정", None))

        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"병원코드(쇼핑몰)", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"병원명", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"주소", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"병원코드(SAP)", None));

        ___qtablewidgetitem4 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", "제품코드(쇼핑몰)", None));
        ___qtablewidgetitem5 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", "제품명", None));
        ___qtablewidgetitem6 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", "제품코드(SAP)", None));
        ___qtablewidgetitem7 = self.tableWidget_2.horizontalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", "수량", None));

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"병원코드 맵핑", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), QCoreApplication.translate("MainWindow", u"품목코드 맵핑", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2), QCoreApplication.translate("MainWindow", u"결과", None))
    # retranslateUi

    def on_pushButton_2_clicked(self): #조회 버튼
        print('조회 버튼 클릭')
        product_button_function.on_pushButton_2_clicked(self.tableWidget)

    def on_pushButton_3_clicked(self): #수정 버튼
        print('수정 버튼 클릭')
        product_button_function.on_pushButton_3_clicked(self.tableWidget)

    def on_pushButton_5_clicked(self): # 데이터 출려갛기 버튼
        print('출력 버튼 클릭')
        product_button_function.on_pushButton_5_clicked()

    # 품목 탭
    def on_pushButton_clicked(self): #조회 버튼
        print('품목 조회 버튼 클릭')
        product_button_function.on_pushButton_clicked(self.tableWidget_2)

    def on_pushButton_6_clicked(self): #조회 버튼
        print('품목 수정 버튼 클릭')
        product_button_function.on_pushButton_6_clicked(self.tableWidget_2)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())


