# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'youtube.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import QObject, QEvent, QUrl, Qt
from PySide6.QtGui import QDesktopServices

from videotrans.configure import config


class LineEditClickFilter(QObject):
    def eventFilter(self, obj, event):
        if event.type() == QEvent.MouseButtonPress:
            print(obj.text())
            # 在这里处理点击事件
            print("LineEdit 被点击了！")
            if obj.text().strip():
                QDesktopServices.openUrl(QUrl.fromLocalFile(obj.text().strip()))
            # 可以在这里执行任何函数或方法
            return True  # 表示事件已处理，不再传递
        # 其他事件交给基类处理，保持默认行为
        return False
class Ui_youtubeform(object):
    def setupUi(self, youtubeform):
        youtubeform.setObjectName("youtubeform")
        youtubeform.setWindowModality(QtCore.Qt.NonModal)
        youtubeform.resize(500, 300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(youtubeform.sizePolicy().hasHeightForWidth())
        youtubeform.setSizePolicy(sizePolicy)
        youtubeform.setMaximumSize(QtCore.QSize(500, 300))
        self.set = QtWidgets.QPushButton(youtubeform)
        self.set.setGeometry(QtCore.QRect(170, 200, 141, 35))
        self.set.setMinimumSize(QtCore.QSize(0, 35))
        self.set.setObjectName("set")
        self.set.setCursor(Qt.PointingHandCursor)
        self.layoutWidget = QtWidgets.QWidget(youtubeform)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 16, 471, 123))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(100, 35))
        self.label.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(100, 35))
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.selectdir = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.selectdir.sizePolicy().hasHeightForWidth())
        self.selectdir.setSizePolicy(sizePolicy)
        self.selectdir.setMinimumSize(QtCore.QSize(100, 35))
        self.selectdir.setObjectName("selectdir")
        self.selectdir.setCursor(Qt.PointingHandCursor)
        self.verticalLayout.addWidget(self.selectdir)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.proxy = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.proxy.sizePolicy().hasHeightForWidth())
        self.proxy.setSizePolicy(sizePolicy)
        self.proxy.setMinimumSize(QtCore.QSize(0, 35))
        self.proxy.setObjectName("proxy")
        self.verticalLayout_2.addWidget(self.proxy)
        self.url = QtWidgets.QLineEdit(self.layoutWidget)
        self.url.setMinimumSize(QtCore.QSize(0, 35))
        self.url.setObjectName("url")
        self.verticalLayout_2.addWidget(self.url)
        self.outputdir = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.outputdir.sizePolicy().hasHeightForWidth())
        self.outputdir.setSizePolicy(sizePolicy)
        self.outputdir.setMinimumSize(QtCore.QSize(0, 35))
        self.outputdir.setReadOnly(True)
        self.outputdir.setObjectName("outputdir")
        self.outputdir.setToolTip(config.uilanglist['Open target dir'])

        self.click_filter = LineEditClickFilter()
        self.outputdir.installEventFilter(self.click_filter)




        self.verticalLayout_2.addWidget(self.outputdir)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.verticalLayout_2)
        self.logs = QtWidgets.QLabel(youtubeform)
        self.logs.setGeometry(QtCore.QRect(30, 250, 441, 16))
        self.logs.setText("")
        self.logs.setObjectName("logs")

        self.retranslateUi(youtubeform)
        QtCore.QMetaObject.connectSlotsByName(youtubeform)

    def retranslateUi(self, youtubeform):
        youtubeform.setWindowTitle( '下载Youtube视频' if config.defaulelang=='zh' else "Youtube Download")
        self.set.setText( '立即开始' if config.defaulelang=='zh' else "Start Download")
        self.label.setText( '代理地址' if config.defaulelang=='zh' else "Proxy")
        self.label_2.setText( '视频播放页url' if config.defaulelang=='zh' else "Video URL")
        self.selectdir.setText( '保存目录' if config.defaulelang=='zh' else "Select Out Dir")
        self.proxy.setPlaceholderText( '填写代理地址，格式 http://127.0.0.1:端口号' if config.defaulelang=='zh' else "eg http://127.0.0.1:7890")