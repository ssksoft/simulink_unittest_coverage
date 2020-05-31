import pandas as pd
gain_url = 'file:///C:/Users/sasat/Desktop/simulink_unittest_coverage/model/test/slcov_output/CoverageDetails/docked__cov__report__gain__Normal.html'

switch_url = 'file:///C:/Users/sasat/Desktop/simulink_unittest_coverage/model/test/slcov_output/CoverageDetails/docked__cov__report__switch_func__Normal.html'

truthtable_url = 'file:///C:/Users/sasat/Desktop/simulink_unittest_coverage/model/test/slcov_output/CoverageDetails/docked__cov__report__truthtable_func__Normal.html'

urls = [gain_url, switch_url, truthtable_url]

# coverage_overall_df = pd.DataFrame({'モデル名': 'init',
#                                     '実行カバレッジ': '0',
#                                     '判定カバレッジ': '0',
#                                     '条件カバレッジ': '0'
#                                     })


coverage_overall_df = pd.read_csv('setting/coverage_overall_template.csv')
print(coverage_overall_df)


print(coverage_overall_df)

fetched_dataframes = pd.io.html.read_html(urls[0], header=0, index_col=0)
i = 0
# for fetched_dataframe in fetched_dataframes:
#     print('table{}'.format(i))
#     print(fetched_dataframe)
#     print('##########################')
#     i = i+1

# print(fetched_dataframes[11].loc['実行', 'カバレッジ'])
coverage_overall_df.loc[0, 'モデル名'] = 'gain'
coverage_overall_df.loc[0, '実行'] \
    = fetched_dataframes[11].loc['実行', 'カバレッジ']
try:
    coverage_overall_df.loc[0, '判定'] \
        = fetched_dataframes[11].loc['判定', 'カバレッジ']
except:
    coverage_overall_df.loc[0, '判定'] \
        = '-'

try:
    coverage_overall_df.loc[0, '条件'] \
        = fetched_dataframes[11].loc['条件', 'カバレッジ']
except:
    coverage_overall_df.loc[0, '条件'] \
        = '-'

coverage_overall_df.to_csv('coverage_overall.csv',
                           encoding="utf-8_sig", index=None)

# print(coverage_overall_df)
