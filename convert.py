def convert_ipynb():
    #to html
    tohtml = "jupyter nbconvert --to html linear_regression_project.ipynb"
    os.System(tohtml)

    #to python
    topython = "jupyter nbconvert --to python linear_regression_project.ipynb"
    os.System(topython)

convert_ipynb
