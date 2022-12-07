from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect
from django.urls import reverse
from django.template import loader
from app.models import JobPost

job_title = [
    "First Job",
    "Second Job"
]

job_description = [
    "First job description",
    "Second job description"
]



# Create your views here.
class TempClass:
    x = 5


def hello(request):
    # 1- We can return a text which is impractical
    # return HttpResponse("Hello World")
    # 2- Or we can alternatively return HTML
    # return HttpResponse("<h3> Hello World! <h3>")
    # 3- Or we can return a link to another website
    # site = "https://google.com"
    # return HttpResponse(f"Visit <a href = {site}>Google Here </a>")
    # 4- render out HTML file inside templates foler in app
    # template = loader.get_template('app/hello.html')
    # This dictionery which maps keys to values and is passed to the template on run-time execution.
    # List and class and Context:
    # list = ["alpha", "beta"]
    # temp = TempClass()
    # context = {"name": "Django", "first_list":list, "temp_object": temp}
    # return HttpResponse(template.render(context, request))

    # 5- Using Render Function:
    list = ["alpha", "beta"]
    temp = TempClass()
    is_authenticated = False
    context = {"name": "Django", "first_list":list, "temp_object": temp, "is_authenticated": is_authenticated}
    return render(request, "app/hello.html", context)

def job_list(request):
    # 1- Make this function complicated by showing all jobs in it.
    # html_str = "<ul>"
    # for index,title in enumerate(job_title):
    #     detail_url = reverse('jobs_detail', args = (index,))
    #     html_str += f"<li> <a href = '{detail_url}'>{title}</li>"
    # html_str += "</ul>"
    # return HttpResponse(html_str)

    # 2- Migrating into the template folder
    # Each element of info would contain (job, url)
    # information = []
    # for i in range(len(job_title)):
    #     information.append((job_title[i], reverse('jobs_detail', args = (i,))))
    # context = {"information": information}
    # return render(request, "app/index.html", context)

    # 3- Now we connect the code to the database instead of defining the list in a hard-coded manner.
    jobs = JobPost.objects.all()
    context = {"jobs": jobs}
    return render(request, "app/index.html", context)


def job_detail(request, id):
    # id = int(id)
    # Simple example of re-directing:
    # Together with handling error:
    try:
        if id == 0:
            return redirect(reverse('jobs_home'))
        # Method 1 (directly return HTML)
        # return_html = f"<h1>{job_title[id]}</h1> <h3>{job_description[id]}</h3>"
        # Method 2 (Pass non-database-driven values to template)
        # context = {"title": job_title[id], "description":job_description[id]}
        # Method 3 (Load data from database and then pass them to the template)
        job = JobPost.objects.get(id=id)
        context = {"job": job}
        return render(request, "app/job_detail.html", context)
    except: 
        return HttpResponseNotFound("Not Found!")

