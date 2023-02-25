def calc(project_grade, term_paper, midterm):
    # grade = project_grade * 15 + term_paper * .20 + midterm * .25 + final * .40
    # grade must be at least 90
    # 90 <= project_grade * 15 + term_paper * .20 + midterm * .25 + final * .40
    # 90 - (project_grade * 15 + term_paper * .20 + midterm * .25) <= final * .40
    # (90 - (project_grade * 15 + term_paper * .20 + midterm * .25))/40 <= final

    final_we_need = (90 - (project_grade * .15 + term_paper * .20 + midterm * .25)) //   .40
    if final_we_need > 100:
        print('impossible')
    else:
        print(final_we_need)


calc(85, 88, 92)