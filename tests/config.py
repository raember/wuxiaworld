"""Used for storing tests related data like paths for reuse"""
from os.path import dirname, abspath, join
from typing import Tuple

from spoofbot import Browser, Firefox
from spoofbot.adapter import HarAdapter, load_har

ROOT = dirname(dirname(abspath(__file__)))


def resolve_path(path) -> str:
    if isinstance(path, str):
        return join(ROOT, path.replace('../', ''))
    elif isinstance(path, Tuple):
        return join(ROOT, *[frag for frag in path if frag != '..'])


data_folder = ('test_data',)
cache_folder = ('tests', '.cache')


class Har:
    WW_HJC_COVER_C1_2 = (*data_folder, 'WW_HJC_Cover_C1-2.har')
    WW_WMW_COVER_C1 = (*data_folder, 'WW_WMW_Cover_C1.har')
    WW_SFF_Cover_C1_78F = (*data_folder, 'WW_SFF_Cover_C1-78F.har')
    WW_AST_Cover_C1_102 = (*data_folder, 'WW_AST_Cover_C1-102.har')
    WW_SEARCH = (*data_folder, 'WW_Search.har')
    WW_SEARCH_DEFAULT = (*data_folder, 'WW_Search_default.har')
    WW_SEARCH_MODERN = (*data_folder, 'WW_Search_modern.har')
    WM_SEARCH_RI_C1_5 = (*data_folder, 'webnovel_Search_RI_C1-5.har')
    WM_POTT_C92_95 = (*data_folder, 'webnovel_POTT_C92-95.har')
    QU_POT_C94_108 = (*data_folder, 'qidianunderground_POT_C94-108.har')


def prepare_browser(har_path: Tuple) -> Browser:
    browser = Firefox()
    har_adapter = HarAdapter(load_har(resolve_path(har_path)))
    har_adapter.strict_matching = False
    har_adapter.delete_after_match = False
    browser.session.mount('https://', har_adapter)
    browser.session.mount('http://', har_adapter)
    return browser
