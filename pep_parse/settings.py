from pathlib import Path


BOT_NAME = 'pep_parse'

NEWSPIDER_MODULE = 'pep_parse.spiders'
SPIDER_MODULES = [f'{NEWSPIDER_MODULE}']

FEED_EXPORT_ENCODING = 'utf-8'

BASE_DIR = Path(__file__).parent.parent
RESULTS = 'results'
RESULTS_DIR = BASE_DIR / 'results'

FEEDS = {
    f'{RESULTS}/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
    }
}

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 100,
}
