import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.classes.CalculateMetaStatistics import generate_statistics_html


config = {
    'path': './data/message_*.json', # './data/message_*.json'
    'language': 'fr', # 'en' (default) or 'fr'
}

generate_statistics_html(config)
