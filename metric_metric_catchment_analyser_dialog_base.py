# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'metric_catchment_analyser_dialog_base.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MetricCatchmentAnalyserDialogBase(object):
    def setupUi(self, MetricCatchmentAnalyserDialogBase):
        MetricCatchmentAnalyserDialogBase.setObjectName(_fromUtf8("MetricCatchmentAnalyserDialogBase"))
        MetricCatchmentAnalyserDialogBase.resize(509, 425)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MetricCatchmentAnalyserDialogBase.sizePolicy().hasHeightForWidth())
        MetricCatchmentAnalyserDialogBase.setSizePolicy(sizePolicy)
        MetricCatchmentAnalyserDialogBase.setMinimumSize(QtCore.QSize(509, 425))
        self.gridLayout_2 = QtGui.QGridLayout(MetricCatchmentAnalyserDialogBase)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_5 = QtGui.QLabel(MetricCatchmentAnalyserDialogBase)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 11, 1, 1, 1)
        self.network_tolerance = QtGui.QDoubleSpinBox(MetricCatchmentAnalyserDialogBase)
        self.network_tolerance.setObjectName(_fromUtf8("network_tolerance"))
        self.gridLayout.addWidget(self.network_tolerance, 9, 0, 1, 1)
        self.radius = QtGui.QLineEdit(MetricCatchmentAnalyserDialogBase)
        self.radius.setObjectName(_fromUtf8("radius"))
        self.gridLayout.addWidget(self.radius, 8, 0, 1, 1)
        self.browse_input_network = QtGui.QPushButton(MetricCatchmentAnalyserDialogBase)
        self.browse_input_network.setObjectName(_fromUtf8("browse_input_network"))
        self.gridLayout.addWidget(self.browse_input_network, 3, 1, 1, 1)
        self.label_4 = QtGui.QLabel(MetricCatchmentAnalyserDialogBase)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 8, 1, 1, 1)
        self.path_network = QtGui.QLineEdit(MetricCatchmentAnalyserDialogBase)
        self.path_network.setObjectName(_fromUtf8("path_network"))
        self.gridLayout.addWidget(self.path_network, 14, 0, 1, 1)
        self.network_layer = QtGui.QLabel(MetricCatchmentAnalyserDialogBase)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.network_layer.sizePolicy().hasHeightForWidth())
        self.network_layer.setSizePolicy(sizePolicy)
        self.network_layer.setObjectName(_fromUtf8("network_layer"))
        self.gridLayout.addWidget(self.network_layer, 2, 0, 1, 1)
        self.check_polygon = QtGui.QCheckBox(MetricCatchmentAnalyserDialogBase)
        self.check_polygon.setObjectName(_fromUtf8("check_polygon"))
        self.gridLayout.addWidget(self.check_polygon, 15, 0, 1, 1)
        self.polygon_tolerance = QtGui.QLineEdit(MetricCatchmentAnalyserDialogBase)
        self.polygon_tolerance.setObjectName(_fromUtf8("polygon_tolerance"))
        self.gridLayout.addWidget(self.polygon_tolerance, 11, 0, 1, 1)
        self.label = QtGui.QLabel(MetricCatchmentAnalyserDialogBase)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 9, 1, 1, 1)
        self.origin_layer = QtGui.QLabel(MetricCatchmentAnalyserDialogBase)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.origin_layer.sizePolicy().hasHeightForWidth())
        self.origin_layer.setSizePolicy(sizePolicy)
        self.origin_layer.setObjectName(_fromUtf8("origin_layer"))
        self.gridLayout.addWidget(self.origin_layer, 5, 0, 1, 1)
        self.choose_origin = QtGui.QComboBox(MetricCatchmentAnalyserDialogBase)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.choose_origin.sizePolicy().hasHeightForWidth())
        self.choose_origin.setSizePolicy(sizePolicy)
        self.choose_origin.setObjectName(_fromUtf8("choose_origin"))
        self.gridLayout.addWidget(self.choose_origin, 6, 0, 1, 1)
        self.browse_input_origin = QtGui.QPushButton(MetricCatchmentAnalyserDialogBase)
        self.browse_input_origin.setObjectName(_fromUtf8("browse_input_origin"))
        self.gridLayout.addWidget(self.browse_input_origin, 6, 1, 1, 1)
        self.browse_output_polygon = QtGui.QPushButton(MetricCatchmentAnalyserDialogBase)
        self.browse_output_polygon.setObjectName(_fromUtf8("browse_output_polygon"))
        self.gridLayout.addWidget(self.browse_output_polygon, 17, 1, 1, 1)
        self.browse_output_network = QtGui.QPushButton(MetricCatchmentAnalyserDialogBase)
        self.browse_output_network.setObjectName(_fromUtf8("browse_output_network"))
        self.gridLayout.addWidget(self.browse_output_network, 14, 1, 1, 1)
        self.choose_network = QtGui.QComboBox(MetricCatchmentAnalyserDialogBase)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.choose_network.sizePolicy().hasHeightForWidth())
        self.choose_network.setSizePolicy(sizePolicy)
        self.choose_network.setObjectName(_fromUtf8("choose_network"))
        self.gridLayout.addWidget(self.choose_network, 3, 0, 1, 1)
        self.line_3 = QtGui.QFrame(MetricCatchmentAnalyserDialogBase)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.gridLayout.addWidget(self.line_3, 16, 0, 1, 2)
        self.check_network = QtGui.QCheckBox(MetricCatchmentAnalyserDialogBase)
        self.check_network.setObjectName(_fromUtf8("check_network"))
        self.gridLayout.addWidget(self.check_network, 13, 0, 1, 1)
        self.path_polygon = QtGui.QLineEdit(MetricCatchmentAnalyserDialogBase)
        self.path_polygon.setObjectName(_fromUtf8("path_polygon"))
        self.gridLayout.addWidget(self.path_polygon, 17, 0, 1, 1)
        self.line = QtGui.QFrame(MetricCatchmentAnalyserDialogBase)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 7, 0, 1, 2)
        self.line_2 = QtGui.QFrame(MetricCatchmentAnalyserDialogBase)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.gridLayout.addWidget(self.line_2, 12, 0, 1, 2)
        self.progress_mca = QtGui.QProgressBar(MetricCatchmentAnalyserDialogBase)
        self.progress_mca.setProperty("value", 24)
        self.progress_mca.setObjectName(_fromUtf8("progress_mca"))
        self.gridLayout.addWidget(self.progress_mca, 18, 0, 2, 1)
        self.run_mca = QtGui.QPushButton(MetricCatchmentAnalyserDialogBase)
        self.run_mca.setObjectName(_fromUtf8("run_mca"))
        self.gridLayout.addWidget(self.run_mca, 19, 1, 1, 1)
        self.close_mca = QtGui.QPushButton(MetricCatchmentAnalyserDialogBase)
        self.close_mca.setObjectName(_fromUtf8("close_mca"))
        self.gridLayout.addWidget(self.close_mca, 18, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(MetricCatchmentAnalyserDialogBase)
        QtCore.QObject.connect(self.close_mca, QtCore.SIGNAL(_fromUtf8("pressed()")), MetricCatchmentAnalyserDialogBase.reject)
        QtCore.QMetaObject.connectSlotsByName(MetricCatchmentAnalyserDialogBase)

    def retranslateUi(self, MetricCatchmentAnalyserDialogBase):
        MetricCatchmentAnalyserDialogBase.setWindowTitle(_translate("MetricCatchmentAnalyserDialogBase", "Metric Catchment Analyser", None))
        self.label_5.setText(_translate("MetricCatchmentAnalyserDialogBase", "Polygon tolerance", None))
        self.browse_input_network.setText(_translate("MetricCatchmentAnalyserDialogBase", "Browse", None))
        self.label_4.setText(_translate("MetricCatchmentAnalyserDialogBase", "Radius", None))
        self.network_layer.setText(_translate("MetricCatchmentAnalyserDialogBase", "Network layer", None))
        self.check_polygon.setText(_translate("MetricCatchmentAnalyserDialogBase", "Catchment polygon", None))
        self.label.setText(_translate("MetricCatchmentAnalyserDialogBase", "Network tolerance", None))
        self.origin_layer.setText(_translate("MetricCatchmentAnalyserDialogBase", "Origin layer", None))
        self.browse_input_origin.setText(_translate("MetricCatchmentAnalyserDialogBase", "Browse", None))
        self.browse_output_polygon.setText(_translate("MetricCatchmentAnalyserDialogBase", "Browse", None))
        self.browse_output_network.setText(_translate("MetricCatchmentAnalyserDialogBase", "Browse", None))
        self.check_network.setText(_translate("MetricCatchmentAnalyserDialogBase", "Catchment network", None))
        self.run_mca.setText(_translate("MetricCatchmentAnalyserDialogBase", "Run", None))
        self.close_mca.setText(_translate("MetricCatchmentAnalyserDialogBase", "Close", None))
