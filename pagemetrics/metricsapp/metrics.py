import json
import subprocess

ACCESSIBILITY = 'Accessibility'
BEST_PRACTICES = 'Best Practices'
PERFORMANCE = 'Performance'
PWA = 'Progressive Web App'
SEO = 'SEO'


def lighthouse_scores(json_report):
    with open(json_report, "r") as read_file:
        data = json.load(read_file)
        report_categories = data['reportCategories']
        return {report_category['name']: report_category['score'] for report_category in report_categories}


def lighthouse_generate_report(url, output_path):
    lighthouse_cmd = "../lighthouse/node_modules/.bin/lighthouse --output html --output json --output-path " + output_path + ' ' + url
    cmd = ['bash', '-c', lighthouse_cmd]
    return subprocess.run(cmd)


"""
FOR THE TESTS TO PASS THE DJANGO SERVER MUST BE RUNNING
"""


def test_lighthouse_generate_report():
    output_path = './metricsapp/static/metricsapp/6.json'
    url = 'http://127.0.0.1:8000/metrics/test_site/6'
    result = lighthouse_generate_report(url, output_path)
    assert result.returncode == 0


def test_lighthouse_scores():
    json_report = './metricsapp/static/metricsapp/test.report.json'
    expected = {'Accessibility': 100,
                'Best Practices': 81.25,
                'Performance': 100,
                'Progressive Web App': 27.272727272727273,
                'SEO': 66.66666666666667}

    scores = lighthouse_scores(json_report)
    assert scores == expected
