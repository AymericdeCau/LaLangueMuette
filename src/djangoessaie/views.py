from datetime import datetime
from django.shortcuts import render


def index(request):
    date = datetime.today()
    return render(request, "index.html",context={"questions": '1+1',
                                                 "date": date,
                                                 "rep1": "1",
                                                 "rep2": "2",
                                                 "rep3": "3",
                                                 "rep4": "4"})