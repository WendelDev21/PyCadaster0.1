# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pycadaster.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTabWidget, QTableWidget, QTableWidgetItem, QToolBox,
    QVBoxLayout, QWidget)
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(806, 575)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(0, 0))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        MainWindow.setStyleSheet(u"background-color: rgb(65, 65, 65);\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy1)
        self.centralwidget.setStyleSheet(u"*{\n"
"	border:none;\n"
"}\n"
"QLabel{\n"
"	color:rgb(255, 255, 255);\n"
"}\n"
"\n"
"")
        self.horizontalLayout_5 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, -1, 0)
        self.left_menu = QFrame(self.centralwidget)
        self.left_menu.setObjectName(u"left_menu")
        self.left_menu.setMaximumSize(QSize(200, 16777215))
        self.left_menu.setStyleSheet(u"background-color: rgb(65, 65, 65);")
        self.left_menu.setFrameShape(QFrame.StyledPanel)
        self.left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.left_menu)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, -1, 0, -1)
        self.frame = QFrame(self.left_menu)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_4.addWidget(self.label_3)


        self.verticalLayout_2.addWidget(self.frame)

        self.left_frame = QFrame(self.left_menu)
        self.left_frame.setObjectName(u"left_frame")
        self.left_frame.setStyleSheet(u"QFrame{\n"
"\n"
"	background-color: rgb(65, 65, 65);\n"
"\n"
"}\n"
"QToolBox{\n"
"\n"
"	text-algn:left;\n"
"	background-color: rgb(228, 254, 255);\n"
"\n"
"}\n"
"QToolBox::tab{\n"
"\n"
"	border-radius:5px;\n"
"	background-color: rgb(194, 232, 255);\n"
"	text-algn:left;\n"
"\n"
"}")
        self.left_frame.setFrameShape(QFrame.StyledPanel)
        self.left_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.left_frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, -1, 9, -1)
        self.menu_box = QToolBox(self.left_frame)
        self.menu_box.setObjectName(u"menu_box")
        self.menu_box.setStyleSheet(u"")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 182, 466))
        self.page.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(65, 65, 65);\n"
"")
        self.verticalLayout_4 = QVBoxLayout(self.page)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.btn_home = QPushButton(self.page)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setMinimumSize(QSize(100, 30))
        font = QFont()
        font.setPointSize(10)
        self.btn_home.setFont(font)
        self.btn_home.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_home.setStyleSheet(u"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(0, 170, 255);\n"
"	border-radius:15px;\n"
"	color:#fff;\n"
"}\n"
"QPushButton{\n"
"background-color: rgb(131, 131, 131);\n"
"border-radius:15px;\n"
"}")

        self.verticalLayout_4.addWidget(self.btn_home)

        self.btn_cadastrar = QPushButton(self.page)
        self.btn_cadastrar.setObjectName(u"btn_cadastrar")
        self.btn_cadastrar.setMinimumSize(QSize(100, 30))
        self.btn_cadastrar.setFont(font)
        self.btn_cadastrar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_cadastrar.setStyleSheet(u"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(0, 170, 255);\n"
"	border-radius:15px;\n"
"	color:#fff;\n"
"}\n"
"QPushButton{\n"
"background-color: rgb(131, 131, 131);\n"
"border-radius:15px;\n"
"}")

        self.verticalLayout_4.addWidget(self.btn_cadastrar)

        self.btn_contatos = QPushButton(self.page)
        self.btn_contatos.setObjectName(u"btn_contatos")
        self.btn_contatos.setMinimumSize(QSize(100, 30))
        self.btn_contatos.setFont(font)
        self.btn_contatos.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_contatos.setStyleSheet(u"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(0, 170, 255);\n"
"	border-radius:15px;\n"
"	color:#fff;\n"
"}\n"
"QPushButton{\n"
"background-color: rgb(131, 131, 131);\n"
"border-radius:15px;\n"
"}")

        self.verticalLayout_4.addWidget(self.btn_contatos)

        self.btn_sobre = QPushButton(self.page)
        self.btn_sobre.setObjectName(u"btn_sobre")
        self.btn_sobre.setMinimumSize(QSize(100, 30))
        self.btn_sobre.setFont(font)
        self.btn_sobre.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_sobre.setStyleSheet(u"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(0, 170, 255);\n"
"	border-radius:15px;\n"
"	color:#fff;\n"
"}\n"
"QPushButton{\n"
"background-color: rgb(131, 131, 131);\n"
"border-radius:15px;\n"
"}")

        self.verticalLayout_4.addWidget(self.btn_sobre)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.menu_box.addItem(self.page, u"Menu")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 182, 466))
        self.label_4 = QLabel(self.page_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(-10, 0, 191, 241))
        font1 = QFont()
        font1.setPointSize(8)
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"background-color: rgb(131, 131, 131);")
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_4.setIndent(-1)
        self.menu_box.addItem(self.page_2, u"Informa\u00e7\u00f5es")

        self.verticalLayout_3.addWidget(self.menu_box)


        self.verticalLayout_2.addWidget(self.left_frame)


        self.horizontalLayout_5.addWidget(self.left_menu)

        self.main_container = QFrame(self.centralwidget)
        self.main_container.setObjectName(u"main_container")
        self.main_container.setStyleSheet(u"background-color: rgb(65, 65, 65);")
        self.main_container.setFrameShape(QFrame.StyledPanel)
        self.main_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.main_container)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.top_frame = QFrame(self.main_container)
        self.top_frame.setObjectName(u"top_frame")
        sizePolicy.setHeightForWidth(self.top_frame.sizePolicy().hasHeightForWidth())
        self.top_frame.setSizePolicy(sizePolicy)
        self.top_frame.setLayoutDirection(Qt.LeftToRight)
        self.top_frame.setFrameShape(QFrame.StyledPanel)
        self.top_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.top_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_toggle = QPushButton(self.top_frame)
        self.btn_toggle.setObjectName(u"btn_toggle")
        icon = QIcon()
        icon.addFile(u":/icons/icons/menu2.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_toggle.setIcon(icon)
        self.btn_toggle.setIconSize(QSize(32, 32))

        self.horizontalLayout.addWidget(self.btn_toggle, 0, Qt.AlignLeft)


        self.verticalLayout.addWidget(self.top_frame)

        self.Pages = QStackedWidget(self.main_container)
        self.Pages.setObjectName(u"Pages")
        sizePolicy1.setHeightForWidth(self.Pages.sizePolicy().hasHeightForWidth())
        self.Pages.setSizePolicy(sizePolicy1)
        self.Pages.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(131, 131, 131);")
        self.pg_home = QWidget()
        self.pg_home.setObjectName(u"pg_home")
        self.verticalLayout_12 = QVBoxLayout(self.pg_home)
        self.verticalLayout_12.setSpacing(6)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.main_frame = QFrame(self.pg_home)
        self.main_frame.setObjectName(u"main_frame")
        sizePolicy1.setHeightForWidth(self.main_frame.sizePolicy().hasHeightForWidth())
        self.main_frame.setSizePolicy(sizePolicy1)
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.main_frame)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.logo = QLabel(self.main_frame)
        self.logo.setObjectName(u"logo")
        sizePolicy1.setHeightForWidth(self.logo.sizePolicy().hasHeightForWidth())
        self.logo.setSizePolicy(sizePolicy1)
        self.logo.setStyleSheet(u"background-color: rgb(131, 131, 131);")

        self.verticalLayout_5.addWidget(self.logo)


        self.verticalLayout_12.addWidget(self.main_frame)

        self.Pages.addWidget(self.pg_home)
        self.pg_cadastrar = QWidget()
        self.pg_cadastrar.setObjectName(u"pg_cadastrar")
        self.verticalLayout_6 = QVBoxLayout(self.pg_cadastrar)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.tabWidget = QTabWidget(self.pg_cadastrar)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(238, 238, 238);")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_9 = QVBoxLayout(self.tab)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.lbs_empresas = QLabel(self.tab)
        self.lbs_empresas.setObjectName(u"lbs_empresas")
        self.lbs_empresas.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(238, 238, 238);")
        self.lbs_empresas.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.lbs_empresas)

        self.frame_4 = QFrame(self.tab)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"QLineEdit{\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"	font:10pt \"MS Shell Dig 2\";\n"
"}\n"
"QFrame{\n"
"	\n"
"	background-color: rgb(231, 231, 231);\n"
"}")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_4)
        self.gridLayout.setObjectName(u"gridLayout")
        self.txt_email = QLineEdit(self.frame_4)
        self.txt_email.setObjectName(u"txt_email")

        self.gridLayout.addWidget(self.txt_email, 4, 1, 1, 2)

        self.txt_telefone = QLineEdit(self.frame_4)
        self.txt_telefone.setObjectName(u"txt_telefone")

        self.gridLayout.addWidget(self.txt_telefone, 4, 0, 1, 1)

        self.txt_bairro = QLineEdit(self.frame_4)
        self.txt_bairro.setObjectName(u"txt_bairro")

        self.gridLayout.addWidget(self.txt_bairro, 2, 2, 1, 1)

        self.txt_uf = QLineEdit(self.frame_4)
        self.txt_uf.setObjectName(u"txt_uf")

        self.gridLayout.addWidget(self.txt_uf, 3, 1, 1, 1)

        self.txt_cep = QLineEdit(self.frame_4)
        self.txt_cep.setObjectName(u"txt_cep")

        self.gridLayout.addWidget(self.txt_cep, 3, 2, 1, 1)

        self.txt_nome = QLineEdit(self.frame_4)
        self.txt_nome.setObjectName(u"txt_nome")
        self.txt_nome.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_nome, 0, 1, 1, 2)

        self.txt_numero = QLineEdit(self.frame_4)
        self.txt_numero.setObjectName(u"txt_numero")

        self.gridLayout.addWidget(self.txt_numero, 2, 0, 1, 1)

        self.txt_complemento = QLineEdit(self.frame_4)
        self.txt_complemento.setObjectName(u"txt_complemento")

        self.gridLayout.addWidget(self.txt_complemento, 2, 1, 1, 1)

        self.txt_logadouro = QLineEdit(self.frame_4)
        self.txt_logadouro.setObjectName(u"txt_logadouro")
        self.txt_logadouro.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_logadouro, 1, 0, 1, 3)

        self.txt_cnpj = QLineEdit(self.frame_4)
        self.txt_cnpj.setObjectName(u"txt_cnpj")

        self.gridLayout.addWidget(self.txt_cnpj, 0, 0, 1, 1)

        self.txt_municipio = QLineEdit(self.frame_4)
        self.txt_municipio.setObjectName(u"txt_municipio")

        self.gridLayout.addWidget(self.txt_municipio, 3, 0, 1, 1)


        self.verticalLayout_9.addWidget(self.frame_4)

        self.btn_cadastro_usuarios = QPushButton(self.tab)
        self.btn_cadastro_usuarios.setObjectName(u"btn_cadastro_usuarios")
        self.btn_cadastro_usuarios.setMinimumSize(QSize(100, 30))
        font2 = QFont()
        font2.setPointSize(12)
        self.btn_cadastro_usuarios.setFont(font2)
        self.btn_cadastro_usuarios.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_cadastro_usuarios.setStyleSheet(u"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(0, 170, 255);\n"
"	border-radius:15px;\n"
"	color:#fff;\n"
"}\n"
"QPushButton{\n"
"	border-radius:15px;\n"
"	background-color: rgb(131, 131, 131);\n"
"	color: rgb(255, 255, 255);\n"
"}")

        self.verticalLayout_9.addWidget(self.btn_cadastro_usuarios, 0, Qt.AlignHCenter)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_8 = QVBoxLayout(self.tab_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.lbs_usuarios_cadastrados = QLabel(self.tab_2)
        self.lbs_usuarios_cadastrados.setObjectName(u"lbs_usuarios_cadastrados")
        self.lbs_usuarios_cadastrados.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(238, 238, 238);")
        self.lbs_usuarios_cadastrados.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.lbs_usuarios_cadastrados)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.tableWidget = QTableWidget(self.tab_2)
        if (self.tableWidget.columnCount() < 11):
            self.tableWidget.setColumnCount(11)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setStyleSheet(u"QHeaderView::section{\n"
"	\n"
"	background-color: rgb(148, 148, 148);\n"
"	color: rgb(255, 255, 255);\n"
"	font:10pt \"MS Shell Dig 2\";\n"
"}")

        self.horizontalLayout_6.addWidget(self.tableWidget)

        self.frame_3 = QFrame(self.tab_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setLayoutDirection(Qt.LeftToRight)
        self.frame_3.setStyleSheet(u"background-color: rgb(189, 189, 189);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_3)
        self.verticalLayout_7.setSpacing(6)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(9, 9, 7, -1)
        self.btn_exel = QPushButton(self.frame_3)
        self.btn_exel.setObjectName(u"btn_exel")
        self.btn_exel.setMinimumSize(QSize(100, 30))
        self.btn_exel.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_exel.setStyleSheet(u"QPushButton:hover{\n"
"	\n"
"	\n"
"	\n"
"	\n"
"	background-color: rgb(0, 203, 98);\n"
"	border-radius:15px;\n"
"	color:#fff;\n"
"}\n"
"QPushButton{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:15px;\n"
"}")

        self.verticalLayout_7.addWidget(self.btn_exel)

        self.btn_alterar = QPushButton(self.frame_3)
        self.btn_alterar.setObjectName(u"btn_alterar")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_alterar.sizePolicy().hasHeightForWidth())
        self.btn_alterar.setSizePolicy(sizePolicy2)
        self.btn_alterar.setMinimumSize(QSize(100, 30))
        self.btn_alterar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_alterar.setStyleSheet(u"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(0, 170, 255);\n"
"	border-radius:15px;\n"
"	color:#fff;\n"
"}\n"
"QPushButton{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:15px;\n"
"}")

        self.verticalLayout_7.addWidget(self.btn_alterar)

        self.btn_excluir = QPushButton(self.frame_3)
        self.btn_excluir.setObjectName(u"btn_excluir")
        sizePolicy2.setHeightForWidth(self.btn_excluir.sizePolicy().hasHeightForWidth())
        self.btn_excluir.setSizePolicy(sizePolicy2)
        self.btn_excluir.setMinimumSize(QSize(100, 30))
        self.btn_excluir.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_excluir.setStyleSheet(u"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(255, 0, 0);\n"
"	border-radius:15px;\n"
"	color:#fff;\n"
"}\n"
"QPushButton{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:15px;\n"
"}")

        self.verticalLayout_7.addWidget(self.btn_excluir)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_2)


        self.horizontalLayout_6.addWidget(self.frame_3)


        self.verticalLayout_8.addLayout(self.horizontalLayout_6)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_6.addWidget(self.tabWidget)

        self.Pages.addWidget(self.pg_cadastrar)
        self.pg_contatos = QWidget()
        self.pg_contatos.setObjectName(u"pg_contatos")
        self.verticalLayout_10 = QVBoxLayout(self.pg_contatos)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_7 = QLabel(self.pg_contatos)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_7)

        self.label_8 = QLabel(self.pg_contatos)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_10.addWidget(self.label_8)

        self.label_9 = QLabel(self.pg_contatos)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_10.addWidget(self.label_9)

        self.label = QLabel(self.pg_contatos)
        self.label.setObjectName(u"label")

        self.verticalLayout_10.addWidget(self.label)

        self.Pages.addWidget(self.pg_contatos)
        self.pg_sobre = QWidget()
        self.pg_sobre.setObjectName(u"pg_sobre")
        sizePolicy1.setHeightForWidth(self.pg_sobre.sizePolicy().hasHeightForWidth())
        self.pg_sobre.setSizePolicy(sizePolicy1)
        self.verticalLayout_11 = QVBoxLayout(self.pg_sobre)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_10 = QLabel(self.pg_sobre)
        self.label_10.setObjectName(u"label_10")
        sizePolicy1.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy1)
        self.label_10.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_11.addWidget(self.label_10)

        self.label_11 = QLabel(self.pg_sobre)
        self.label_11.setObjectName(u"label_11")
        sizePolicy1.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy1)
        self.label_11.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_11.setWordWrap(True)

        self.verticalLayout_11.addWidget(self.label_11)

        self.Pages.addWidget(self.pg_sobre)

        self.verticalLayout.addWidget(self.Pages)

        self.footer_frame = QFrame(self.main_container)
        self.footer_frame.setObjectName(u"footer_frame")
        self.footer_frame.setStyleSheet(u"")
        self.footer_frame.setFrameShape(QFrame.StyledPanel)
        self.footer_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.footer_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.footer_frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_3.addWidget(self.label_2)


        self.verticalLayout.addWidget(self.footer_frame)


        self.horizontalLayout_5.addWidget(self.main_container)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.menu_box.setCurrentIndex(0)
        self.Pages.setCurrentIndex(1)
        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"PyCadaster", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_cadastrar.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.btn_contatos.setText(QCoreApplication.translate("MainWindow", u"Contatos", None))
        self.btn_sobre.setText(QCoreApplication.translate("MainWindow", u"Sobre", None))
        self.menu_box.setItemText(self.menu_box.indexOf(self.page), QCoreApplication.translate("MainWindow", u"Menu", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/></p><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\">PyCadaster 0.1</span></p><p align=\"center\">Este sistema est\u00e1 em fase de</p><p align=\"center\">desenvolvimento e testes.</p><p align=\"center\">Caso encontre algum</p><p align=\"center\">Bug ou problema, contate</p><p align=\"center\">O desenvolvedor na aba</p><p align=\"center\">Contatos.</p><p align=\"center\"><br/></p></body></html>", None))
        self.menu_box.setItemText(self.menu_box.indexOf(self.page_2), QCoreApplication.translate("MainWindow", u"Informa\u00e7\u00f5es", None))
        self.btn_toggle.setText("")
        self.logo.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">SISTEMA DE CADASTRO DE EMPRESAS</span></p><p align=\"center\"><img width=\"200\" height=\"200\" src=\":/icons/icons/logo.png\"/></p><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">PYCADASTER 0.1</span></p></body></html>", None))
        self.lbs_empresas.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; color:#0087ca;\">REALIZAR CADASTROS</span></p></body></html>", None))
        self.txt_email.setPlaceholderText(QCoreApplication.translate("MainWindow", u"EMAIL", None))
        self.txt_telefone.setPlaceholderText(QCoreApplication.translate("MainWindow", u"TELEFONE", None))
        self.txt_bairro.setPlaceholderText(QCoreApplication.translate("MainWindow", u"BAIRRO", None))
        self.txt_uf.setPlaceholderText(QCoreApplication.translate("MainWindow", u"UF", None))
        self.txt_cep.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CEP", None))
        self.txt_nome.setPlaceholderText(QCoreApplication.translate("MainWindow", u"NOME EMPRESARIAL", None))
        self.txt_numero.setPlaceholderText(QCoreApplication.translate("MainWindow", u"NUMERO", None))
        self.txt_complemento.setPlaceholderText(QCoreApplication.translate("MainWindow", u"COMPLEMENTO", None))
        self.txt_logadouro.setPlaceholderText(QCoreApplication.translate("MainWindow", u"LOGADOURO", None))
        self.txt_cnpj.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CNPJ", None))
        self.txt_municipio.setPlaceholderText(QCoreApplication.translate("MainWindow", u"MUNICIPIO", None))
        self.btn_cadastro_usuarios.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Cadastro", None))
        self.lbs_usuarios_cadastrados.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; color:#0087ca;\">USU\u00c1RIOS CADASTRADOS</span></p></body></html>", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"CNPJ", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"NOME", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"LOGADOURO", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"NUMERO", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"COMPLEMENTO", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"BAIRRO", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"MUNICIPIO", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"UF", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"CEP", None));
        ___qtablewidgetitem9 = self.tableWidget.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"TELEFONE", None));
        ___qtablewidgetitem10 = self.tableWidget.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"EMAIL", None));
        self.btn_exel.setText(QCoreApplication.translate("MainWindow", u"Gerar tabela", None))
        self.btn_alterar.setText(QCoreApplication.translate("MainWindow", u"Atualizar", None))
        self.btn_excluir.setText(QCoreApplication.translate("MainWindow", u"Deletar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Usu\u00e1rios", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">CONTATOS</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/icons/icons/whatsApp.png\" /> <span style=\" font-size:18pt; font-weight:600; vertical-align:super;\">(79) 9 9980-1810</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/icons/icons/email.png\"/><span style=\" font-size:18pt; font-weight:600; vertical-align:super;\">lwendel003@gmail.com</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/icons/icons/linkedin.png\" width=\"32\" height=\"32\"/><a href=\"www.linkedin.com/in/wendev69\"><span style=\" font-size:18pt; text-decoration: underline; color:#0000ff; vertical-align:super;\">Wendel Lucas</span></a></p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">SOBRE</span></p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Este sistema faz consulta do CNPJ utilizando API da receita federal e faz o cadastro em um banco de dados SQLITE3.</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">\u00a9 PyCadaster 2024</p></body></html>", None))
    # retranslateUi

