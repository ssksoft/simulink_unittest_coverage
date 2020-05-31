import pandas as pd
gain_url = 'file:///C:/Users/sasat/Desktop/simulink_unittest_coverage/model/test/slcov_output/CoverageDetails/docked__cov__report__gain__Normal.html'

switch_url = 'file:///C:/Users/sasat/Desktop/simulink_unittest_coverage/model/test/slcov_output/CoverageDetails/docked__cov__report__switch_func__Normal.html'

truthtable_url = 'file:///C:/Users/sasat/Desktop/simulink_unittest_coverage/model/test/slcov_output/CoverageDetails/docked__cov__report__truthtable_func__Normal.html'

urls = [gain_url, switch_url, truthtable_url]

model_names = ['1. gain', '1. switch_func', '1. truthtable_func']

coverage_overall_df = pd.read_csv('setting/coverage_overall_template.csv')

for current_model, model_name in zip(range(len(model_names)), model_names):
    fetched_dataframes = pd.io.html.read_html(
        urls[current_model], header=1, index_col=0)

    coverage_abstract = fetched_dataframes[4]
    print(coverage_abstract)

    print(model_name)
    print('のカバレッジを集計中')
    coverage_overall_df.loc[current_model, 'モデル名'] = model_name
    try:
        coverage_overall_df.loc[current_model,
                                '実行'] = coverage_abstract.loc[model_name, '実行']
    except:
        coverage_overall_df.loc[current_model, '実行'] = '-'
    try:
        coverage_overall_df.loc[current_model,
                                '判定'] = coverage_abstract.loc[model_name, '判定']
    except:
        coverage_overall_df.loc[current_model, '判定'] = '-'

    try:
        coverage_overall_df.loc[current_model,
                                '条件'] = coverage_abstract.loc[model_name, '条件']
    except:
        coverage_overall_df.loc[current_model, '条件'] = '-'

coverage_overall_df.to_csv('coverage_overall.csv',
                           encoding="utf-8_sig",   index=None)
