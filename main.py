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
            self.pushButton_5.setEnabled(False)  # 초기에 비활성화 상태로 설정

            self.tabWidget.addTab(self.tab2, "")
            MainWindow.setCentralWidget(self.centralwidget)
            self.statusbar = QStatusBar(MainWindow)
            self.statusbar.setObjectName(u"statusba ")
            MainWindow.setStatusBar(self.statusbar)

            self.retranslateUi(MainWindow)

            self.tabWidget.setCurrentIndex(0)

            # 프로그램 시작 시 자동으로 품목코드 조회
            self.on_pushButton_clicked()

            QMetaObject.connectSlotsByName(MainWindow)
        except Exception as e:
            print(e)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"쇼핑몰 데이터 가져오기", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"품목 조회", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"데이터 출력하기", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"수정", None))

        ___qtablewidgetitem4 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", "제품코드(쇼핑몰)", None));
        ___qtablewidgetitem5 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", "제품명", None));
        ___qtablewidgetitem6 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", "제품코드(SAP)", None));
        ___qtablewidgetitem7 = self.tableWidget_2.horizontalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", "수량", None));

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), QCoreApplication.translate("MainWindow", u"품목코드 맵핑", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2), QCoreApplication.translate("MainWindow", u"결과", None))
    # retranslateUi

    def on_pushButton_clicked(self): #조회 버튼
        print('품목 조회 버튼 클릭')
        product_button_function.on_pushButton_clicked(self.tableWidget_2, self.pushButton_5)

    def on_pushButton_6_clicked(self): #조회 버튼
        print('품목 수정 버튼 클릭')
        product_button_function.on_pushButton_6_clicked(self.tableWidget_2, self.pushButton_5)

    def on_pushButton_5_clicked(self): # 데이터 출려갛기 버튼
        print('출력 버튼 클릭')
        product_button_function.on_pushButton_5_clicked()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())


