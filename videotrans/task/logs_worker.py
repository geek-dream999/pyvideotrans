# 从日志队列获取日志
import json

from PySide6.QtCore import QThread, Signal as pyqtSignal

from videotrans.configure.config import queue_logs


class LogsWorker(QThread):
    post_logs = pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent=parent)

    def run(self):
        # queue_logs.put({"type":"open_toolbox"})
        while True:
            try:
                obj = queue_logs.get(True, 1)
                if "type" not in obj:
                    obj['type'] = 'logs'
                self.post_logs.emit(json.dumps(obj))
            except Exception as e:
                pass
