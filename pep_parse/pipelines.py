import csv
from collections import defaultdict
from datetime import datetime
from pathlib import Path


BASE_DIR = Path(__file__).parent.parent
RESULTS_DIR = BASE_DIR / 'results'
DATE_FORMAT = '%Y-%m-%d_%H-%M-%S'


class PepParsePipeline:
    def __init__(self):
        self.results_dir = RESULTS_DIR
        self.results_dir.mkdir(exist_ok=True)

    def open_spider(self, spider):
        self.status_counter = defaultdict(int)
        self.total = 0

    def process_item(self, item, spider):
        self.status_counter[item['status']] += 1
        self.total += 1
        return item

    def close_spider(self, spider):
        timestamp = datetime.now().strftime(DATE_FORMAT)
        filename = f'status_summary_{timestamp}.csv'

        with open(
                RESULTS_DIR / filename, 'w', newline='', encoding='utf-8'
        ) as file:
            writer = csv.DictWriter(
                file,
                fieldnames=['Статус', 'Количество']
            )
            writer.writeheader()

            for status, count in self.status_counter.items():
                writer.writerow({
                    'Статус': status,
                    'Количество': count
                })

            writer.writerow({
                'Статус': 'Всего',
                'Количество': self.total
            })
