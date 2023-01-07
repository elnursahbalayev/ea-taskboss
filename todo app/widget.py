from PySide6.QtCore import QTime, QTimer
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox, QDialog, QLabel, QPushButton, QVBoxLayout
import time, sqlite3
from widget_ui import Ui_Widget
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtCore import QUrl


class Widget(QWidget, Ui_Widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowTitle('EA Timer')

        self.add_button.clicked.connect(self.add_task)
        self.remove_button.clicked.connect(self.remove_task)

        self.play_button.clicked.connect(self.play)
        self.pause_button.clicked.connect(self.pause)
        self.stop_button.clicked.connect(self.stop)

        self.progressBar.setValue(0)

        self.task_list_widget.itemClicked.connect(self.set_current_label)

        self.current_task_label.setStyleSheet("QLabel { background-color : white; }")

        self.timer_interval = 1000
        self.timer = QTimer(self)
        self.timer.setInterval(self.timer_interval)

        self.timer.timeout.connect(self.update_time)
        self.elapsed_time = QTime(0, 0)

        self.conn = sqlite3.connect('todos.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS todos (task text)''')

        self.cursor.execute('''SELECT task FROM todos''')
        todos = self.cursor.fetchall()
        for todo in todos:
            self.task_list_widget.addItem(todo[0])

        self.notification_filename = 'notification.wav'
        self.player = QMediaPlayer()
        self.player.setMedia(QMediaContent(QUrl.fromLocalFile(self.notification_filename)))

    def add_task(self):
        task = self.task_line_edit.text()
        task = task.strip()
        if task != '':
            self.task_list_widget.addItem(task)
            self.task_line_edit.clear()

            self.cursor.execute('''INSERT INTO todos (task) VALUES (?)''', (task,))
            self.conn.commit()

    def remove_task(self):
        task = self.task_list_widget.currentRow()
        task_text = self.task_list_widget.item(task).text()
        self.task_list_widget.takeItem(task)
        self.current_task_label.clear()

        self.cursor.execute('''DELETE FROM todos WHERE task=?''', (task_text,))
        self.conn.commit()

    def play(self):
        self.time_to_run = self.minute_spinbox.value()

        if self.time_to_run != 0:
            self.play_button.setEnabled(False)
            self.progressBar.setRange(0, self.time_to_run * 60 * 1000)

            beginning_time_hr = self.time_to_run // 60
            beginning_time_min = self.time_to_run % 60

            if beginning_time_hr < 10:
                beginning_time_hr = '0' + str(beginning_time_hr)
            if beginning_time_min < 10:
                beginning_time_min = '0' + str(beginning_time_min)

            self.elapsed_time_label.setText(f'{beginning_time_hr}:{beginning_time_min}:00')

            self.timer.start()

    def set_current_label(self):
        task = self.task_list_widget.currentItem().text()
        self.current_task_label.setText(f'Current task: {task}')

    def update_time(self):

        self.elapsed_time = self.elapsed_time.addMSecs(self.timer_interval)

        self.progressBar.setValue(self.elapsed_time.msecsSinceStartOfDay())

        remaining_time = self.time_to_run*60 - (self.elapsed_time.hour()*3600 + self.elapsed_time.minute()*60 +
                                                self.elapsed_time.second())

        remaining_time_hr = remaining_time//3600
        remaining_time = remaining_time - remaining_time_hr * 3600
        remaining_time_min = remaining_time//60
        remaining_time_sec = remaining_time - remaining_time_min * 60

        if remaining_time_hr < 10:
            remaining_time_hr = '0' + str(remaining_time_hr)
        if remaining_time_min < 10:
            remaining_time_min = '0' + str(remaining_time_min)
        if remaining_time_sec < 10:
            remaining_time_sec = '0' + str(remaining_time_sec)

        self.elapsed_time_label.setText(f'{remaining_time_hr}:{remaining_time_min}:{remaining_time_sec}')

        if self.elapsed_time.minute() == self.time_to_run:

            self.dialog_box = QDialog()
            self.dialog_box.setWindowTitle('Warning')
            self.dialog_box.info_label = QLabel('Time is up!')
            self.dialog_box.ok_button = QPushButton("OK")

            # Create a vertical layout and add the label and button
            self.layout = QVBoxLayout()
            self.layout.addWidget(self.dialog_box.info_label)
            self.layout.addWidget(self.dialog_box.ok_button)

            self.dialog_box.setLayout(self.layout)
            self.dialog_box.show()
            self.timer.stop()
            self.player.play()

    def pause(self):
        self.timer.stop()
        self.play_button.setEnabled(True)

    def stop(self):
        self.progressBar.setValue(0)
        self.timer.stop()
        self.elapsed_time = QTime(0,0)
        self.elapsed_time_label.setText('00:00:00')
        self.play_button.setEnabled(True)

