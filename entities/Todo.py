class Todo:
    _counter = 0  # static variable (mirip companion object)

    def __init__(self, title="", is_finished=False):
        self.id = self._generate_id()
        self.title = title
        self.is_finished = is_finished

    @classmethod
    def _generate_id(cls):
        cls._counter += 1
        return cls._counter

    @classmethod
    def get_total_created(cls):
        return cls._counter

    def __str__(self):
        status = "Selesai" if self.is_finished else "Belum Selesai"
        return f"{self.id} | {self.title} | {status}"
