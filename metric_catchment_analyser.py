# -*- coding: utf-8 -*-
"""
/***************************************************************************
 MetricCatchmentAnalyser
                                 A QGIS plugin
 Network based metric catchment analysis
                              -------------------
        begin                : 2016-02-13
        git sha              : $Format:%H$
        copyright            : (C) 2016 by Laurens Versluis
        email                : l.versluis@spacesyntax.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *

# Initialize Qt resources from file resources.py
import resources
# Import the code for the dialog
from metric_catchment_analyser_dialog import MetricCatchmentAnalyserDialog
import os.path
# Import the mca class
import mca_tools

class MetricCatchmentAnalyser:
    """QGIS Plugin Implementation."""

    def __init__(self, iface):
        """Constructor.

        :param iface: An interface instance that will be passed to this class
            which provides the hook by which you can manipulate the QGIS
            application at run time.
        :type iface: QgsInterface
        """
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value('locale/userLocale')[0:2]
        locale_path = os.path.join(
            self.plugin_dir,
            'i18n',
            'MetricCatchmentAnalyser_{}.qm'.format(locale))

        if os.path.exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)

        # Create the dialog (after translation) and keep reference
        self.dlg = MetricCatchmentAnalyserDialog()

        self.mca_tools = mca_tools
        # Declare instance attributes
        self.actions = []
        self.menu = self.tr(u'&Metric Catchment Analyser')

        # TODO: We are going to let the user set this up in a future iteration
        self.toolbar = self.iface.addToolBar(u'MetricCatchmentAnalyser')
        self.toolbar.setObjectName(u'MetricCatchmentAnalyser')

        # setup lineEdit boxes
        self.dlg.path_input_network.clear()
        self.dlg.path_input_origins.clear()
        self.dlg.path_output_network.setText("Save as temporary layer...")
        self.dlg.path_output_polygon.setText("Save as temporary layer...")
        # connect input browse buttons
        self.dlg.browse_input_network.clicked.connect(self.browse_input_network)
        self.dlg.browse_input_origins.clicked.connect(self.browse_input_origins)
        # connect drop-down menus
        self.dlg.choose_network.activated.connect(self.choose_network)
        self.dlg.choose_origins.activated.connect(self.choose_origins)
        # connect output browse buttons
        self.dlg.browse_output_network.clicked.connect(self.browse_output_network)
        self.dlg.browse_output_polygon.clicked.connect(self.browse_output_polygon)
        # connect the run button
        self.dlg.run_mca.clicked.connect(self.analysis)
        # setup the progress bar
        self.dlg.progress_mca.setMinimum(1)
        self.dlg.progress_mca.setMaximum(4)


    # noinspection PyMethodMayBeStatic
    def tr(self, message):
        """Get the translation for a string using Qt translation API.

        We implement this ourselves since we do not inherit QObject.

        :param message: String for translation.
        :type message: str, QString

        :returns: Translated version of message.
        :rtype: QString
        """
        # noinspection PyTypeChecker,PyArgumentList,PyCallByClass
        return QCoreApplication.translate('MetricCatchmentAnalyser', message)


    def add_action(
        self,
        icon_path,
        text,
        callback,
        enabled_flag=True,
        add_to_menu=True,
        add_to_toolbar=True,
        status_tip=None,
        whats_this=None,
        parent=None):
        """Add a toolbar icon to the toolbar.

        :param icon_path: Path to the icon for this action. Can be a resource
            path (e.g. ':/plugins/foo/bar.png') or a normal file system path.
        :type icon_path: str

        :param text: Text that should be shown in menu items for this action.
        :type text: str

        :param callback: Function to be called when the action is triggered.
        :type callback: function

        :param enabled_flag: A flag indicating if the action should be enabled
            by default. Defaults to True.
        :type enabled_flag: bool

        :param add_to_menu: Flag indicating whether the action should also
            be added to the menu. Defaults to True.
        :type add_to_menu: bool

        :param add_to_toolbar: Flag indicating whether the action should also
            be added to the toolbar. Defaults to True.
        :type add_to_toolbar: bool

        :param status_tip: Optional text to show in a popup when mouse pointer
            hovers over the action.
        :type status_tip: str

        :param parent: Parent widget for the new action. Defaults None.
        :type parent: QWidget

        :param whats_this: Optional text to show in the status bar when the
            mouse pointer hovers over the action.

        :returns: The action that was created. Note that the action is also
            added to self.actions list.
        :rtype: QAction
        """

        icon = QIcon(icon_path)
        action = QAction(icon, text, parent)
        action.triggered.connect(callback)
        action.setEnabled(enabled_flag)

        if status_tip is not None:
            action.setStatusTip(status_tip)

        if whats_this is not None:
            action.setWhatsThis(whats_this)

        if add_to_toolbar:
            self.toolbar.addAction(action)

        if add_to_menu:
            self.iface.addPluginToMenu(
                self.menu,
                action)

        self.actions.append(action)

        return action

    def initGui(self):
        """Create the menu entries and toolbar icons inside the QGIS GUI."""

        icon_path = ':/plugins/MetricCatchmentAnalyser/icon.png'
        self.add_action(
            icon_path,
            text=self.tr(u'Metric Catchment Analyser'),
            callback=self.run,
            parent=self.iface.mainWindow())

    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""
        for action in self.actions:
            self.iface.removePluginMenu(
                self.tr(u'&Metric Catchment Analyser'),
                action)
            self.iface.removeToolBarIcon(action)
        # remove the toolbar
        del self.toolbar

    def choose_network(self):
        layers = self.iface.legendInterface().layers()
        layer_name = self.dlg.choose_network.currentText()
        layer_index = self.dlg.choose_network.currentIndex()
        network = layers[layer_index]
        if not network.isValid():
            self.iface.messageBar().pushMessage(
                "Metric Catchment Analyser: ",
                "Invalid network file!",
                level=QgsMessageBar.WARNING,
                duration=5)
        elif not network.wkbType() == QGis.WKBLineString:
            self.iface.messageBar().pushMessage(
                "Metric Catchment Analyser: ",
                "This file does not contain lines!",
                level=QgsMessageBar.WARNING,
                duration=5)
        else:
            self.dlg.path_input_network.setText(layer_name)

    def browse_input_network(self):
        filename = QFileDialog.getOpenFileName(self.dlg, "Select input file ","", '*.shp')
        network = QgsVectorLayer(filename, 'input', 'ogr')
        if not network.isValid():
            self.iface.messageBar().pushMessage(
                "Metric Catchment Analyser: ",
                "Invalid network file!",
                level=QgsMessageBar.WARNING,
                duration=5)
        elif not network.wkbType() == QGis.WKBLineString:
            self.iface.messageBar().pushMessage(
                "Metric Catchment Analyser: ",
                "This file does not contain lines!",
                level=QgsMessageBar.WARNING,
                duration=5)
        else:
            self.dlg.path_input_network.setText(filename)
            return network

    def choose_origins(self):
        layers = self.iface.legendInterface().layers()
        layer_name = self.dlg.choose_origins.currentText()
        layer_index = self.dlg.choose_origins.currentIndex()
        origins = layers[layer_index]
        if not origins.isValid():
            self.iface.messageBar().pushMessage(
                "Metric Catchment Analyser: ",
                "Invalid network file!",
                level=QgsMessageBar.WARNING,
                duration=5)
        elif not origins.wkbType() == QGis.WKBPoint:
            self.iface.messageBar().pushMessage(
                "Metric Catchment Analyser: ",
                "This file does not contain points!",
                level=QgsMessageBar.WARNING,
                duration=5)
        else:
            self.dlg.path_input_origins.setText(layer_name)

    def browse_input_origins(self):
        filename = QFileDialog.getOpenFileName(self.dlg, "Select input file ","", '*.shp')
        origins = QgsVectorLayer(filename, 'input', 'ogr')
        if not origins.isValid():
            self.iface.messageBar().pushMessage(
                "Metric Catchment Analyser: ",
                "Invalid origin file!",
                level=QgsMessageBar.WARNING,
                duration=5)
        elif not origins.wkbType() == QGis.WKBPoint:
            self.iface.messageBar().pushMessage(
                "Metric Catchment Analyser: ",
                "This file does not contain points!",
                level=QgsMessageBar.WARNING,
                duration=5)
        else:
            self.dlg.path_input_origins.setText(filename)
            return origins

    def browse_output_network(self):
        file_name = QFileDialog.getSaveFileName(self.dlg, "Save output file ","mca_network", '*.shp')
        self.dlg.path_output_network.setText(file_name)

    def browse_output_polygon(self):
        file_name = QFileDialog.getSaveFileName(self.dlg, "Save output file ","mca_catchment", '*.shp')
        self.dlg.path_output_polygon.setText(file_name)

    def analysis(self,mca):
        self.dlg.progress_mca.reset()
        # loading the network
        network_index = self.dlg.choose_network.currentIndex()
        layers = self.iface.legendInterface().layers()
        network = layers[network_index]

        # loading the origins
        origin_index = self.dlg.choose_origins.currentIndex()
        layers = self.iface.legendInterface().layers()
        origins = layers[origin_index]
        crs = network.crs()

        # loading settings
        radius = self.dlg.radius.value()
        network_tolerance = self.dlg.network_tolerance.value()
        polygon_tolerance = self.dlg.polygon_tolerance.value()
        self.dlg.progress_mca.setValue(1)

        # setting up the output network
        output_network = QgsVectorLayer("linestring?crs="+ crs.toWkt(), "mca_network", "memory")

        # setup of output polygon
        output_catchment = QgsVectorLayer("polygon?crs="+ crs.toWkt(), "mca_catchment", "memory")
        output_catchment.dataProvider().addAttributes([QgsField("origin", QVariant.String)])
        output_catchment.updateFields()
        self.dlg.progress_mca.setValue(2)

        # build graph
        graph, tied_points, origins = self.mca_tools.graph_builder(network,origins,network_tolerance)
        # run analysis
        self.mca_tools.mca(
            graph,
            tied_points,
            output_network,
            output_catchment,
            polygon_tolerance,
            radius)
        self.dlg.progress_mca.setValue(3)
        # render network
        if self.dlg.check_network.isChecked() == True:
            self.mca_tools.mca_network_renderer(output_network, radius)
        # render catchments
        if self.dlg.check_polygon.isChecked() == True:
            self.mca_tools.mca_catchment_renderer(output_catchment)
        self.dlg.progress_mca.setValue(4)

    def run(self):
        # list of active layers for the comboxes
        layers = self.iface.legendInterface().layers()
        layer_list = []
        for layer in layers:
            layer_list.append(layer.name())

        self.dlg.choose_network.addItems(layer_list)
        self.dlg.choose_origins.addItems(layer_list)
        # show the dialog
        self.dlg.show()



