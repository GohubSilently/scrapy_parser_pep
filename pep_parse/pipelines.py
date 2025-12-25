import csv
from collections import defaultdict
from datetime import datetime

from itemadapter import ItemAdapter


class PepParsePipeline:
    def open_spider(self, spider):
        self.status_counter = defaultdict(int)
        self.total = 0

    def process_item(self, item, spider):
        status = item.get('status')
        if status:
            self.status_counter[status] += 1
            self.total += 1
        return item

    def close_spider(self, spider):
        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        filename = f'status_summary_{timestamp}.csv'

        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(
                f,
                fieldnames=['Статус', 'Количество']
            )
            writer.writeheader()

            for status, count in self.status_counter.items():
                writer.writerow({
                    'Статус': status,
                    'Количество': count
                })

            writer.writerow({
                'Статус': 'Total',
                'Количество': self.total
            })
