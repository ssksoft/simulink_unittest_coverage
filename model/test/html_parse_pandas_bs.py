import pandas
url = 'file:///C:/Users/sasat/Desktop/simulink_unittest_coverage/slcov_output/CoverageDetails/docked__cov__report__gain__Normal.html'
fetched_dataframes = pandas.io.html.read_html(url, header=0, index_col=0)
i = 0
for fetched_dataframe in fetched_dataframes:
    print('table{}'.format(i))
    print(fetched_dataframe)
    print('##########################')
    i = i+1

print(fetched_dataframes[12].loc['実行', 'カバレッジ'])
