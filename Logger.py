import csv
import os.path
import time
from uuid import UUID


class Logger:
    log = {}
    gen_log = []

    def __init__(self):
        self.run_info = None

    def log_generation(self, run_info, *log_file):
        self.run_info = [str(info) for info in run_info]
        self.gen_log.append([*self.run_info, *log_file])

    def log_total(self, log_path):
        # call function to verify logging params in log_settings by log_path (ex. file1 + _settings + .csv)
        # if params match with log_file keys than append to gen_log
        # otherwise abort, throw error saying params don't match and that user should change log_path name


        if not os.path.isdir(os.path.dirname(log_path)):
            os.mkdir(os.path.dirname(log_path))

        with open(log_path, "a", newline="") as file:
            writer = csv.writer(file)

            for log in self.gen_log:
                writer.writerow(log)


    def log_settings(self, path: str, settings_dict: list, unique_run_id: UUID) -> None:
        """
        Log the settings to a CSV file.

        Parameters
        ----------
        path : str
            Path to the CSV file.
        settings_dict : list
            Dictionary of settings.
        unique_run_id : UUID
            Unique identifier for the run.

        Returns
        -------
        None
        """
        settings_dict = self.merge_settings(*settings_dict)
        del settings_dict["TERMINALS"]

        infos = [unique_run_id, settings_dict]

        with open(path, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(infos)


    def merge_settings(self, sd1: dict, sd2: dict, sd3: dict, sd4: dict) -> dict:
        """
        Merge multiple settings dictionaries into one.

        Parameters
        ----------
        sd1 : dict
            First settings dictionary.
        sd2 : dict
            Second settings dictionary.
        sd3 : dict
            Third settings dictionary.
        sd4 : dict
            Fourth settings dictionary.

        Returns
        -------
        dict
            Merged settings dictionary.
        """
        return {**sd1, **sd2, **sd3, **sd4}