import csv
from collections import defaultdict
from datetime import datetime as dt

from .settings import RESULTS_DIR

DATE_FORMAT = '%Y-%m-%d_%H-%M-%S'


class PepParsePipeline:
    def __init__(self):
        RESULTS_DIR.mkdir(exist_ok=True)

    def open_spider(self, spider):
        self.status_counter = defaultdict(int)

    def process_item(self, item, spider):
        self.status_counter[item['status']] += 1
        return item

    def close_spider(self, spider):
        filename = f'status_summary_{dt.now().strftime(DATE_FORMAT)}.csv'

        with open(
                RESULTS_DIR / filename, 'w', newline='', encoding='utf-8'
        ) as file:
            writer = csv.DictWriter(
                file,
                fieldnames=['Статус', 'Количество'],
                dialect=csv.unix_dialect,
            )
            writer.writeheader()
            writer.writerows([
                ['Статус', 'Количество'],
                *self.status_counter.items(),
                ['Итого', sum(self.status_counter.values())]
            ])
