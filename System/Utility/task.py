class Task:
    _instance = None
    _task_list = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Task, cls).__new__(cls)
            cls._task_list = []
        return cls._instance

    def clear_session(self):
        for i in range(len(self._task_list) - 1, -1, -1):
            self._task_list[i].stop()
            if i != 0:
                self._task_list.pop(i)

