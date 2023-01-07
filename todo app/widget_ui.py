# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QProgressBar, QPushButton,
    QSizePolicy, QSpinBox, QVBoxLayout, QWidget)
import resource_rc

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(402, 381)
        self.widget = QWidget(Widget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 10, 381, 361))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.task_list_widget = QListWidget(self.widget)
        self.task_list_widget.setObjectName(u"task_list_widget")

        self.verticalLayout.addWidget(self.task_list_widget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.task_line_edit = QLineEdit(self.widget)
        self.task_line_edit.setObjectName(u"task_line_edit")

        self.horizontalLayout.addWidget(self.task_line_edit)

        self.add_button = QPushButton(self.widget)
        self.add_button.setObjectName(u"add_button")

        self.horizontalLayout.addWidget(self.add_button)

        self.remove_button = QPushButton(self.widget)
        self.remove_button.setObjectName(u"remove_button")

        self.horizontalLayout.addWidget(self.remove_button)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.current_task_label = QLabel(self.widget)
        self.current_task_label.setObjectName(u"current_task_label")
        self.current_task_label.setAutoFillBackground(True)

        self.verticalLayout.addWidget(self.current_task_label)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.minute_spinbox = QSpinBox(self.widget)
        self.minute_spinbox.setObjectName(u"minute_spinbox")

        self.horizontalLayout_2.addWidget(self.minute_spinbox)

        self.play_button = QPushButton(self.widget)
        self.play_button.setObjectName(u"play_button")
        icon = QIcon()
        icon.addFile(u":/images/start.png", QSize(), QIcon.Normal, QIcon.Off)
        self.play_button.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.play_button)

        self.pause_button = QPushButton(self.widget)
        self.pause_button.setObjectName(u"pause_button")
        icon1 = QIcon()
        icon1.addFile(u":/images/pause.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pause_button.setIcon(icon1)

        self.horizontalLayout_2.addWidget(self.pause_button)

        self.stop_button = QPushButton(self.widget)
        self.stop_button.setObjectName(u"stop_button")
        icon2 = QIcon()
        icon2.addFile(u":/images/stop-button.png", QSize(), QIcon.Normal, QIcon.Off)
        self.stop_button.setIcon(icon2)

        self.horizontalLayout_2.addWidget(self.stop_button)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.progressBar = QProgressBar(self.widget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)

        self.horizontalLayout_3.addWidget(self.progressBar)

        self.elapsed_time_label = QLabel(self.widget)
        self.elapsed_time_label.setObjectName(u"elapsed_time_label")

        self.horizontalLayout_3.addWidget(self.elapsed_time_label)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.retranslateUi(Widget)

        self.play_button.setDefault(False)


        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Form", None))
        self.task_line_edit.setPlaceholderText(QCoreApplication.translate("Widget", u"Add task here", None))
        self.add_button.setText(QCoreApplication.translate("Widget", u"Add", None))
        self.remove_button.setText(QCoreApplication.translate("Widget", u"Remove", None))
        self.current_task_label.setText("")
        self.play_button.setText("")
        self.pause_button.setText("")
        self.stop_button.setText("")
        self.elapsed_time_label.setText(QCoreApplication.translate("Widget", u"00:00:00", None))
    # retranslateUi

