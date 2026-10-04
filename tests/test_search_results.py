import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import app as app_module


def test_search_page_has_search_form_and_navigation():
    client = app_module.app.test_client()
    response = client.get('/shelter_search')
    assert response.status_code == 200
    html = response.get_data(as_text=True)
    assert '避難所検索' in html
    assert '条件を変えて再検索' not in html


def test_search_results_page_displays_result_table_and_navigation():
    client = app_module.app.test_client()
    response = client.get('/search_results?district=青森市')
    assert response.status_code == 200
    html = response.get_data(as_text=True)
    assert '避難所名' in html
    assert '住所' in html
    assert '空き状況' in html
    assert '検索画面に戻る' in html
    assert 'トップページへ戻る' in html
