import json
import subprocess

'''
*.json
{
  "reportCategories": [
    {
      "name": "Performance",
      "score": 83,
'''


def lighthouse_scores(json_report):
    with open(json_report, "r") as read_file:
        data = json.load(read_file)
        report_categories = data['reportCategories']
        return {report_category['name']: report_category['score'] for report_category in report_categories}


def lighthouse_generate_json_report(url, output_path):
    cmd = ['../lighthouse/node_modules/.bin/lighthouse', '--output json', '--output-path']
    cmd += [output_path, url]

    cmd = ['bash', '-c', "../lighthouse/node_modules/.bin/lighthouse --output html --output json --output-path ./metricsapp/static/metricsapp/5.json http://127.0.0.1:8000/metrics/test_site/5"]
    return subprocess.run(cmd)


def lighthouse_generate_html_report(url, output_path):
    cmd = ['../lighthouse/node_modules/.bin/lighthouse', '--output html', '--output-path']
    cmd += [output_path, url]
    print(cmd)
    return subprocess.run(cmd)


def test_lighthouse_generate_json_report():
    output_path = './metricsapp/static/metricsapp/4.json'
    url = 'http://127.0.0.1:8000/metrics/test_site/4'
    result = lighthouse_generate_json_report(url, output_path)
    assert result.returncode == 0

def test_lighthouse_generate_html_report():
    output_path = './metricsapp/static/metricsapp/4.html'
    url = 'http://127.0.0.1:8000/metrics/test_site/4'
    result = lighthouse_generate_html_report(url, output_path)
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
