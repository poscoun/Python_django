from django.shortcuts import render, redirect
from django.http import HttpResponse
import pandas as pd

# calculate views.py

# Create your views here.
def calculate(request):
    file = request.FILES['fileInput']
    # print('file: ', file)
    df = pd.read_excel(file, sheet_name='Sheet1', header=0)
    # print(df.head(5))

    # grade별 value의 최소값, 최대값, 평균값
    # grade별 구분
    grade_dic = {}
    total_row_num = len(df.index)

    for i in range(total_row_num):
        data = df.loc(i)
        if not data['grade'] in grade_dic.key():
            grade_dic[data['grade']] = [data['value']]
        else:
            grade_dic[data['grade']].append(data['value'])

    # grade별 value의 최소값, 최대값, 평균값
    grade_calculate_dic = {}
    for key in grade_dic.keys():
        grade_calculate_dic[key] = {}
        grade_calculate_dic[key]['min'] = min(grade_dic[key])
        grade_calculate_dic[key]['max'] = max(grade_dic[key])
        grade_calculate_dic[key]['avg'] = float(sum(grade_dic[key])/len(grade_dic[key]))


    return HttpResponse('calculate views - calculate function()')