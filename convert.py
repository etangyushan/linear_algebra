import os
def convert_ipynb():
    #to html
    tohtml = "jupyter nbconvert --to html linear_regression_project.ipynb"
    print tohtml
    os.system(tohtml)

    #to python
    topython = "jupyter nbconvert --to python linear_regression_project.ipynb"
    print topython
    os.system(topython)


convert_ipynb()
