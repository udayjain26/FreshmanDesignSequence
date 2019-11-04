
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Events, Comments
from .forms import NewEventsForm, CommentsForm
from django.shortcuts import redirect

@login_required(login_url="/users/login/")
def events(request):
	eventList = Events.objects.order_by('-timestamp')[0:10]
	context = {"events": eventList}
	return render(request,"events.html",context)

@login_required(login_url="/users/login/")
def event_page(request):
	if request.method == "GET":
		id_ = request.GET.get("id")
		id_ = id_.replace("'", "").replace('"', '')
		event = Events.objects.get(pk=id_)
		form = CommentsForm()

		comments = Comments.objects.filter(forEvent=event).order_by('-timestamp')

		return render(request, "event.html", {"event": event, "form": form, "comments": comments, "id_": id_})
	elif request.method == "POST" and "comment" in request.POST:
		id_ = request.POST["id"]
		id_ = id_.replace("'", "").replace('"', '')
		event = Events.objects.get(pk=id_)
		form = CommentsForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.byUser = request.user
			post.forEvent = event
			post.save()
		return redirect('events')

	else:
		return redirect("events")

@login_required(login_url="/users/login/")
def newEvents(request):
	if request.method == "POST":
		form = NewEventsForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.byUser = request.user
			post.upvotes = 0
			post.save()
		return redirect('events')
	else:
		form = NewEventsForm()
		return render(request, "newEvents.html", {'form':form})

# Create your views here.
