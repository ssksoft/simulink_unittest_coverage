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

model_name = ['1. gain', '1. switch_func', '1. truthtable_func']

coverage_overall_df = pd.read_csv('setting/coverage_overall_template.csv')

fetched_dataframes = pd.io.html.read_html(urls[0], header=1, index_col=0)
i = 0
for fetched_dataframe in fetched_dataframes:
    print('table{}'.format(i))
    print(fetched_dataframe)
    print('##########################')
    i = i+1

coverage_abstract = fetched_dataframes[4]
# print(coverage_abstract)
print(coverage_abstract.loc[model_name[0], '実行'])

# coverage_abstract.to_csv('trial.csv', encoding="utf-8_sig")

# coverage_overall_df.loc[0, 'モデル名'] = 'gain'
# coverage_overall_df.loc[0, '実行'] \
#     = coverage_abstract.loc['実行', 'カバレッジ']
# try:
#     coverage_overall_df.loc[0, '判定'] \
#         = coverage_abstract.loc['判定', 'カバレッジ']
# except:
#     coverage_overall_df.loc[0, '判定'] \
#         = '-'

# try:
#     coverage_overall_df.loc[0, '条件'] \
#         = coverage_abstract.loc['条件', 'カバレッジ']
# except:
#     coverage_overall_df.loc[0, '条件'] \
#         = '-'

# coverage_overall_df.to_csv('coverage_overall.csv',
#                            encoding="utf-8_sig", index=None)

# # print(coverage_overall_df)
