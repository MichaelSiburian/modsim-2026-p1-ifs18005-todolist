class InputUtil:
    @staticmethod
    def input(info: str) -> str:
        return input(f"{info} : ") or ""