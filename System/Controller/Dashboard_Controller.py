from UI_Screen.Dashboard_Screen import Ui_MainWindow
from Controller.Main_Window import MainWindow
from PyQt5.QtWidgets import QMessageBox, QFileDialog, QMainWindow
from PyQt5.QtChart import QPieSeries, QChart, QChartView, QPieSlice, QBarSet, QBarSeries, QBarCategoryAxis,QValueAxis
from PyQt5.QtGui import QPainter, QPdfWriter
from PyQt5.QtCore import Qt, QMargins, QDate
from Utility.datetime_manager import DatetimeManager
from Utility.message_manager import MessageManager
from Utility.canvas import MplCanvas
from UI_Screen import Report_Screen


class DashboardController(MainWindow):
    def __init__(self, router, db_connection, login_controller,upload_video_controller):
        self.ui = Ui_MainWindow()
        super(DashboardController, self).__init__(self.ui, router)
        self.db_connection = db_connection
        self.login_controller = login_controller
        self.ui.to_date_edit.setDate(QDate.currentDate())
        self.ui.to_date_edit.setDisplayFormat("yyyy-MM-dd")
        self.ui.from_date_edit.setDisplayFormat("yyyy-MM-dd")
        self.upload_video_controller = upload_video_controller
        self.logged_user = None
        self.card_data = []
        self.bar_data = []
        self.pie_data = []

        # Receive logged user from login_controller
        self.login_controller.user_passed.connect(self.receive_user)

        # Receive signal from upload video controller to update the dashboard
        self.upload_video_controller.detection_complete_signal.connect(self.refresh)
        
        # Connect button
        self.ui.search_button.clicked.connect(self.get_card_data)
        self.ui.trend_source.currentTextChanged.connect(self.create_barchart)
        self.ui.trend_year.currentTextChanged.connect(self.create_barchart)
        self.ui.generate_button.clicked.connect(self.create_report)

        # Create the matplotlib FigureCanvas object for bar chart and piechart
        self.bar_canvas = MplCanvas(self, width=5, height=4, dpi=100)
        self.pie_canvas = MplCanvas(self, width=5, height=4, dpi=100)

        # Add canvas to layout
        self.ui.bar_chart_layout.addWidget(self.bar_canvas)
        self.ui.pie_chart_layout.addWidget(self.pie_canvas)

    # Get logged user information
    def receive_user(self, logged_user):
        self.logged_user = logged_user
        self.refresh()

    def refresh(self):
        self.get_video_source()
        self.get_detection_year()
        self.get_card_data()
        self.create_barchart()
        self.create_piechart()

    def get_card_data(self):
        # filter condition
        from_date = self.ui.from_date_edit.text()
        to_date = self.ui.to_date_edit.text()
        source_filter = self.ui.source_combo.currentText()

        # Avoid from_date is later than to_date
        if (DatetimeManager.compare_dates(from_date,  to_date)) > 0:
            MessageManager.show_message(QMessageBox.Critical, "Invalid Date", "The 'from date' cannot be later than 'to date'")
            return
        
        # To retrieve data
        query = f"""SELECT d.upload_date, v.result, d.source AS total_fake from video v 
                    INNER JOIN detection d ON v.detection_id = d.detection_id 
                    WHERE d.user_id = '{self.logged_user.email}'"""
        
        # Execute and retrieve data
        data_list = self.db_connection.execute_query(query)[1].fetchall()
        
        total_video = 0
        total_fake = 0

        for data_row in data_list:
            # video source filter
            if data_row[2] != source_filter and source_filter != "All" and source_filter != "":
                continue

            # Filter by date
            if not (DatetimeManager.compare_dates(data_row[0], self.ui.from_date_edit.text()) >= 0 and DatetimeManager.compare_dates(data_row[0], self.ui.to_date_edit.text()) <= 0):
                continue
                
            total_video = total_video + 1
            if (data_row[1] == "Fake"):
                total_fake = total_fake + 1

        real_percentage = 0
        fake_percentage = 0

        if (total_video != 0):
            fake_percentage = round((total_fake/total_video)*100,2)
            real_percentage = round((100 - fake_percentage),2)

        # save card data
        self.card_data = [str(total_video), str(total_fake), str(real_percentage) + "%", str(fake_percentage) + "%"]
        self.ui.total_upload_label.setText(self.card_data[0])
        self.ui.total_deepfake_label.setText(self.card_data[1])
        self.ui.real_pcent_label.setText(self.card_data[2])
        self.ui.fake_pcent_label.setText(self.card_data[3])

        
    def get_video_source(self):
        # Remove all item first to avoid duplication
        self.ui.source_combo.clear()
        self.ui.trend_source.clear()
        # get existing source from database
        query = f"SELECT DISTINCT source from detection WHERE user_id = '{self.logged_user.email}'"

        result = self.db_connection.execute_query(query)[1].fetchall()
        
        self.ui.source_combo.addItem("All")
        self.ui.trend_source.addItem("All")

        for source in result:
            self.ui.source_combo.addItem(str(source[0]))
            self.ui.trend_source.addItem(str(source[0]))

    def get_detection_year(self):
        self.ui.trend_year.clear()
        query = f"SELECT DISTINCT strftime('%Y',upload_date) AS YEAR from DETECTION WHERE user_id = '{self.logged_user.email}' ORDER BY YEAR DESC"
        
        # Execute and retrieve data
        result = self.db_connection.execute_query(query)[1].fetchall()

        # Add year as item into the combobox
        for year in result:
            self.ui.trend_year.addItem(str(year[0]))

    def get_barchart_data(self):
        selected_year = self.ui.trend_year.currentText()
        selected_source = self.ui.trend_source.currentText()
        
        if (selected_source == "All"):
            query = f"""SELECT month, ROUND((SUM(CASE WHEN result = 'Fake' THEN 1 ELSE 0 END)/CAST(COUNT(month) as FLOAT))*100,2) FROM
                        (SELECT CASE strftime('%m', d.upload_date)
                                WHEN '01' THEN 'Jan'
                                WHEN '02' THEN 'Feb'
                                WHEN '03' THEN 'Mar'
                                WHEN '04' THEN 'Apr'
                                WHEN '05' THEN 'May'
                                WHEN '06' THEN 'Jun'
                                WHEN '07' THEN 'Jul'
                                WHEN '08' THEN 'Aug'
                                WHEN '09' THEN 'Sep'
                                WHEN '10' THEN 'Oct'
                                WHEN '11' THEN 'Nov'
                                WHEN '12' THEN 'Dec'
                            END AS month, v.result
                            FROM detection d INNER JOIN video v ON d.detection_id = v.detection_id 
                            WHERE strftime('%Y',d.upload_date) = '{selected_year}' and 
                            d.user_id = '{self.logged_user.email}') t
                            GROUP BY month"""
        else:
            query = f"""SELECT month, ROUND((SUM(CASE WHEN result = 'Fake' THEN 1 ELSE 0 END)/CAST(COUNT(month) as FLOAT))*100,2) FROM
                        (SELECT CASE strftime('%m', d.upload_date)
                                WHEN '01' THEN 'Jan'
                                WHEN '02' THEN 'Feb'
                                WHEN '03' THEN 'Mar'
                                WHEN '04' THEN 'Apr'
                                WHEN '05' THEN 'May'
                                WHEN '06' THEN 'Jun'
                                WHEN '07' THEN 'Jul'
                                WHEN '08' THEN 'Aug'
                                WHEN '09' THEN 'Sep'
                                WHEN '10' THEN 'Oct'
                                WHEN '11' THEN 'Nov'
                                WHEN '12' THEN 'Dec'
                            END AS month, v.result
                            FROM detection d INNER JOIN video v ON d.detection_id = v.detection_id 
                            WHERE strftime('%Y',d.upload_date) = '{selected_year}' and 
                            d.source = '{selected_source}' and 
                            d.user_id = '{self.logged_user.email}') t
                            GROUP BY month"""
                  
        # Execute and retrieve data
        return self.db_connection.execute_query(query)[1].fetchall()

    # Remove all widget in layout
    def clear_layout(self, layout):
        # Iterate over all items in the layout
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                # Remove the widget from the layout
                widget.setParent(None)
                widget.deleteLater()

    # Plot the bar chart
    def create_barchart(self):
        # Clear plot element to refresh it
        self.bar_canvas.axes.clear()

        # Get chart data
        data_list = self.get_barchart_data()
        
        month_count = {"Jan":[0,0],"Feb":[0,0],"Mar":[0,0],"Apr":[0,0],"May":[0,0],"Jun":[0,0],"Jul":[0,0],"Aug":[0,0],"Sep":[0,0],"Oct":[0,0],"Nov":[0,0],"Dec":[0,0]}

        # set data by month
        for data in data_list:
            month_count[data[0]] = [100 - data[1], data[1]]

        # Prepare data for bar chart
        months = list(month_count.keys())
        real_percent = []
        fake_percent = []
        
        for item in month_count.values():
            real_percent.append(item[0])
            fake_percent.append(item[1])
        
        # Save bar data
        self.bar_data = [months, real_percent, fake_percent]

        # Plot Stacked bar chart on the canvas
        bar1 = self.bar_canvas.axes.bar(months, real_percent, color='#3480EB', label='Real')
        bar2 = self.bar_canvas.axes.bar(months, fake_percent, bottom=real_percent, color='red', label='Fake')
        
        self.bar_canvas.axes.set_xlabel('Month')
        self.bar_canvas.axes.set_ylabel('Percentage %')
        self.bar_canvas.axes.set_ylim(0, 100)  # Set y-axis range from 0 to 100
        self.bar_canvas.axes.set_title("Real vs Fake Over Months")
        # Rotate x-axis labels and adjust size
        self.bar_canvas.axes.set_xticklabels(months, rotation=45, ha='right', fontsize=8)
        # Place legend outside the plots
        legend_handles = [bar1, bar2]
        legend_labels = ['Real', 'Fake']
        self.bar_canvas.axes.legend(legend_handles, legend_labels, loc='center left', bbox_to_anchor=(1, 0.9))

        # Redraw the canvas
        self.bar_canvas.draw()
    
    # Plot pie chart    
    def create_piechart(self):
        # Clear plot element to refresh it
        self.pie_canvas.axes.clear()

        query = f"""SELECT source, count(source) as total from video v 
                    INNER JOIN detection d ON v.detection_id = d.detection_id 
                    WHERE d.user_id = '{self.logged_user.email}' AND result = 'Fake'
                    GROUP BY source
                    ORDER BY total DESC
                    LIMIT 5
                    """
        
        # Execute and retrieve data
        data_list = self.db_connection.execute_query(query)[1].fetchall()

        sources = []
        count = []

        # Extract source and count from data
        for item in data_list:
            sources.append(item[0])
            count.append(item[1])
        
        # When there is no data found
        if (not data_list):
            sources = ["None"]
            count = [1]
            
        # Save piechart data
        self.pie_data = [count, sources]

        # plot pie chart
        self.pie_canvas.axes.pie(count, labels=sources, autopct='%1.1f%%', startangle=140)
        self.pie_canvas.axes.set_title('Top 5 Deepfake Video Source')

        self.pie_canvas.draw()


    # Generate report
    def create_report(self):
        report = ReportUI(self.ui.from_date_edit.text() + " - " + self.ui.to_date_edit.text(),
                                   self.ui.source_combo.currentText(), 
                                   self.card_data, 
                                   self.ui.trend_year.currentText(),
                                   self.ui.trend_source.currentText(),
                                   self.bar_data,
                                   self.pie_data)
        report.save_to_pdf()

        MessageManager.show_message(QMessageBox.Information, "Report", "Your report has generated successfully")



class ReportUI(QMainWindow):
    def __init__(self, date_range, source, card_data, trend_year, trend_source, bar_data, pie_data):
        super().__init__()
        self.ui = Report_Screen.Ui_MainWindow()
        self.ui.setupUi(self)

        # Set UI elements
        self.ui.date_label.setText(date_range)
        self.ui.source_label.setText(source)
        self.ui.total_upload_label.setText(card_data[0])
        self.ui.total_deepfake_label.setText(card_data[1])
        self.ui.real_pcent_label.setText(card_data[2])
        self.ui.fake_pcent_label.setText(card_data[3])
        self.ui.year_label.setText(trend_year)
        self.ui.bar_source_label.setText(trend_source)

        # Create the matplotlib FigureCanvas object for bar chart and piechart
        self.bar_canvas = MplCanvas(self, width=10, height=5, dpi=100)
        self.pie_canvas = MplCanvas(self, width=10, height=5, dpi=100)

        # Add canvas to layout
        self.ui.bar_chart_layout.addWidget(self.bar_canvas)
        self.ui.pie_chart_layout.addWidget(self.pie_canvas)
        
        # Plot Stacked bar chart on the canvas
        months = bar_data[0]
        real_percent = bar_data[1]
        fake_percent = bar_data[2]
        bar1 = self.bar_canvas.axes.bar(months, real_percent, color='#3480EB', label='Real')
        bar2 = self.bar_canvas.axes.bar(months, fake_percent, bottom=real_percent, color='red', label='Fake')
        
        self.bar_canvas.axes.set_xlabel('Month')
        self.bar_canvas.axes.set_ylabel('Percentage %')
        self.bar_canvas.axes.set_ylim(0, 100)  # Set y-axis range from 0 to 100
        self.bar_canvas.axes.set_title("Real vs Fake Over Months")
        # Rotate x-axis labels and adjust size
        self.bar_canvas.axes.set_xticklabels(months, rotation=45, ha='right', fontsize=8)
        # Place legend outside the plots
        legend_handles = [bar1, bar2]
        legend_labels = ['Real', 'Fake']
        self.bar_canvas.axes.legend(legend_handles, legend_labels, loc='center left', bbox_to_anchor=(1, 0.9))


        # plot pie chart
        self.pie_canvas.axes.pie(pie_data[0], labels=pie_data[1], autopct='%1.1f%%', startangle=140)
        self.pie_canvas.axes.set_title('Top 5 Deepfake Video Source')

    # export ui to pdf
    def save_to_pdf(self):
        # Create file dialog to select file location
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(self, "Save PDF", "", "PDF Files (*.pdf);;All Files (*)", options=options)
        
        if not file_name:
            return

        # Create pdf writer
        pdf_writer = QPdfWriter(file_name)
        pdf_writer.setPageSize(QPdfWriter.A4)
        painter = QPainter(pdf_writer)
        
        # Get page resolution
        resolution = pdf_writer.resolution()
        page_rect = pdf_writer.pageLayout().fullRectPixels(resolution)
        
        # Scale painter to fit main window content into PDF page
        scale_x = page_rect.width() / 910
        scale_y = page_rect.height() / 1056
        scale = min(scale_x, scale_y)
        
        painter.scale(scale, scale)
        
        # Render main window content onto the painter
        self.ui.centralwidget.render(painter)
        
        painter.end()
        print("PDF exported successfully!")