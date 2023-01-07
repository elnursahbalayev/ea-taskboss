import sys
from PyQt5.QtCore import QTimer, QTime
from PyQt5.QtWidgets import QApplication, QWidget, QProgressBar, QLabel

class TimerWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Set the timer interval (in milliseconds)
        self.timer_interval = 1000

        # Create a timer object and set its timeout signal to the update_time slot
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)

        # Set the timer interval
        self.timer.setInterval(self.timer_interval)

        # Create a QTime object to keep track of the elapsed time
        self.elapsed_time = QTime(0, 0)

        # Create a progress bar and set its range
        self.progress_bar = QProgressBar(self)
        self.progress_bar.setRange(0, self.timer_interval * 60)

        # Create a label to display the elapsed time
        self.time_label = QLabel(self)
        self.time_label.setText(self.elapsed_time.toString())

        # Start the timer
        self.timer.start()

    def update_time(self):
        # Increment the elapsed time
        self.elapsed_time = self.elapsed_time.addMSecs(self.timer_interval)

        # Update the progress bar value
        self.progress_bar.setValue(self.elapsed_time.msecsSinceStartOfDay())

        # Update the time label
        self.time_label.setText(self.elapsed_time.toString())

app = QApplication(sys.argv)
timer_widget = TimerWidget()
timer_widget.show()
sys.exit(app.exec_())