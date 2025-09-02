import csv
import os
import json
from datetime import datetime
from uuid import uuid4
import pandas as pd


class Logger:
    def __init__(self, algorithm: str, run_id: str = None, params: dict = None, log_dir: str = "logs"):
        self.algorithm = algorithm
        self.run_id = run_id or str(uuid4())
        self.params = params or {}
        self.log_dir = log_dir
        self.gen_log = []

        os.makedirs(self.log_dir, exist_ok=True)

        self.log_file = os.path.join(self.log_dir, f"run_{self.run_id}.csv")
        self.settings_file = os.path.join(self.log_dir, "log_settings.csv")

        self.mandatory_keys = ["id", "algorithm", "generation", "best_fitness"]
        self.dynamic_keys = []

        self._create_run_csv()
        self._update_log_settings()


#verifica se o ficheiro de run nao existe e escreve o header
    def _create_run_csv(self):
        if not os.path.exists(self.log_file):
            with open(self.log_file, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(self.mandatory_keys + self.dynamic_keys)

#constroi o dicionario
#abre em modo append e escreve
    def _update_log_settings(self):
        row = {
            "id": self.run_id,
            "algorithm": self.algorithm,
            "logkeys": json.dumps(self.mandatory_keys + self.dynamic_keys),
            "params": json.dumps(self.params),
            "created_at": datetime.now().isoformat()
        }
        file_exists = os.path.exists(self.settings_file)
        with open(self.settings_file, "a", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=row.keys())
            if not file_exists:
                writer.writeheader()
            writer.writerow(row)

#recebe os parametros
    def log_generation(self, generation: int, best_fitness: float, **kwargs):
        for key in kwargs:
            if key not in self.dynamic_keys:
                self.dynamic_keys.append(key)

        row = {
            "id": self.run_id,
            "algorithm": self.algorithm,
            "generation": generation,
            "best_fitness": best_fitness
        }

        for key in self.dynamic_keys:
            row[key] = kwargs.get(key, "None")

        with open(self.log_file, "a", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=self.mandatory_keys + self.dynamic_keys)
            writer.writerow(row)

        self.gen_log.append(row)
        self._update_log_settings_dynamic_keys()



    def _update_log_settings_dynamic_keys(self):
        if not os.path.exists(self.settings_file):
            return

#procura id == self.run_id e carrega as logkeys
        settings_df = pd.read_csv(self.settings_file)
        updated = False
        for idx, row in settings_df.iterrows():
            if row["id"] == self.run_id:
                logkeys = json.loads(row["logkeys"])
                new_keys = self.mandatory_keys + self.dynamic_keys
                if set(logkeys) != set(new_keys):
                    settings_df.at[idx, "logkeys"] = json.dumps(new_keys)
                    updated = True

        if updated:
            settings_df.to_csv(self.settings_file, index=False)

    def get_log(self):
        return self.gen_log


#previne que run nova escreva em colunas diferentes
    def validate_metrics(self):
        if not os.path.exists(self.settings_file):
            return True

        with open(self.settings_file, "r", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row["algorithm"] != self.algorithm:
                    continue
                existing_keys = json.loads(row["logkeys"])
                current_keys = self.mandatory_keys + self.dynamic_keys
                if set(current_keys) != set(existing_keys):
                    raise ValueError(
                        f"Incompatible metrics with existing run of algorithm {self.algorithm}: {existing_keys}"
                    )
        return True

#load de run especifica
    def load_run(self, run_id: str):
        path = os.path.join(self.log_dir, f"run_{run_id}.csv")
        if not os.path.exists(path):
            raise FileNotFoundError(f"Run {run_id} not found.")
        return pd.read_csv(path)

#remove a run e reescreve o settings
    def delete_run(self, run_id: str):
        path = os.path.join(self.log_dir, f"run_{run_id}.csv")
        if os.path.exists(path):
            os.remove(path)
        if os.path.exists(self.settings_file):
            settings_df = pd.read_csv(self.settings_file)
            settings_df = settings_df[settings_df["id"] != run_id]
            settings_df.to_csv(self.settings_file, index=False)

'''

    def consolidate_runs(self):
        files = [f for f in os.listdir(self.log_dir) if f.startswith("run_") and f.endswith(".csv")]
        all_runs = []
        for f in files:
            df = pd.read_csv(os.path.join(self.log_dir, f))
            if not df.empty and df["algorithm"].iloc[0] == self.algorithm:
                all_runs.append(df)
        if all_runs:
            return pd.concat(all_runs, ignore_index=True)
        return pd.DataFrame()
'''