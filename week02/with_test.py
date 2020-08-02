class open:
    def __enter__(self):
        print("open")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit")

    def __call__(self, *args, **kwargs):
        print(args)

with open() as f:
    open().__call__("ceshi")
    pass