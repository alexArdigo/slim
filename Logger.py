import csv
import os.path
import time


class Logger:
    log = {}
    gen_log = []

    def log_generation(self, *log_file):
        self.gen_log.append([*log_file])

    def log_total(self, log_path):

        if not os.path.isdir(os.path.dirname(log_path)):
            os.mkdir(os.path.dirname(log_path))

        with open(log_path, "a", newline="") as file:
            writer = csv.writer(file)

            for log in self.gen_log:
                writer.writerow(log)

        print("Test logger timing: ", self.time_log)