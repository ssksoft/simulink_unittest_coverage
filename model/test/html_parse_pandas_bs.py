import pandas
gain_url = 'file:///C:/Users/sasat/Desktop/simulink_unittest_coverage/model/test/slcov_output/CoverageDetails/docked__cov__report__gain__Normal.html'

switch_url = 'file:///C:/Users/sasat/Desktop/simulink_unittest_coverage/model/test/slcov_output/CoverageDetails/docked__cov__report__switch_func__Normal.html'

truthtable_url = 'file:///C:/Users/sasat/Desktop/simulink_unittest_coverage/model/test/slcov_output/CoverageDetails/docked__cov__report__truthtable_func__Normal.html'

urls = [gain_url, switch_url, truthtable_url]

fetched_dataframes = pandas.io.html.read_html(urls[0], header=0, index_col=0)
i = 0
for fetched_dataframe in fetched_dataframes:
    print('table{}'.format(i))
    print(fetched_dataframe)
    print('##########################')
    i = i+1

print(fetched_dataframes[11].loc['実行', 'カバレッジ'])
