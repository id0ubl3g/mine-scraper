from src.utils.system_utils import execute_before

from datetime import datetime
import pandas as pd
import os

class ExportData:
    def __init__(self):
        self.folder_path: str = 'src/temp'
        self.export_path: str = 'exports'
        self.data: list = []

    def read_files(self) -> None:
        for file in os.listdir(self.folder_path):
            file_path = os.path.join(self.folder_path, file)
            if os.path.isfile(file_path):
                with open(file_path, 'r', encoding='utf-8') as _file:
                    for line in _file:
                        self.data.append(line.strip())
        
        return

    @execute_before(read_files)
    def export_to_excel(self, filename: str, socialmedia_platform: str) -> None:
        now = datetime.now()
        current_date = now.strftime("%Y-%m-%d")
        current_time = now.strftime("%H:%M:%S")

        dataframe = pd.DataFrame({
            'emails': self.data,
            'found in': [socialmedia_platform] * len(self.data),
            'date': [current_date] * len(self.data),
            'time': [current_time] * len(self.data)
        })

        os.makedirs(self.export_path, exist_ok=True)
        output_export_path = os.path.join(self.export_path, f'{filename}.xlsx')
        dataframe.to_excel(output_export_path, index=False, engine='openpyxl')
        
        return