init -510 python:
    def delayed_call(target, delay):
        import time
        import threading

        def wrapper():
            time.sleep(delay)
            target()

        threading.Thread(target=wrapper).start()