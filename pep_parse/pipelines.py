import csv
from collections import defaultdict
from datetime import datetime as dt

from pep_parse.settings import RESULTS_DIR

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
        filename = 'status_summary_{time}.csv'.format(
            time=dt.now().strftime(DATE_FORMAT)
        )
        status = [[key, value] for key, value in self.status_counter.items()]
        number_all_statuses = sum(self.status_counter.values())
        with open(
            RESULTS_DIR / filename, 'w', newline='', encoding='utf-8'
        ) as file:
            writer = csv.writer(
                file,
                dialect=csv.unix_dialect,
            )
            writer.writerows([
                ['Статус', 'Количество'],
                *status,
                ['Итого', number_all_statuses],
            ])
