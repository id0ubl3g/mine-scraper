from config.path_config import add_project_root_to_path
add_project_root_to_path()

from src.modules.mine_scraper import MineScraper
from src.utils.system_utils import parse_arguments

args = parse_arguments()

if __name__ == '__main__':
    MineScraper(args).execute()