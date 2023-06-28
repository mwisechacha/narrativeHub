from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from .models import Story
from .forms import StoryForm

# Create your views here.


def create_story(request):
    if request.method == 'GET':
        context = {'form': StoryForm()}
        return render(request, 'stories/story_form.html', context)
    elif request.method == 'POST':
        form = StoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'The story has been created successfully')
            return redirect('/')
        else:
            messages.error(request, 'Please correct the following error:')
            return render(request, 'stories/story_form.html', {'form': form})


def edit_story(request, id):
    story = get_object_or_404(Story, id=id)

    if request.method == 'GET':
        context = {'form': StoryForm(instance=story), 'id': id}
        return render(request, 'stories/story_form.html', context)

    elif request.method == 'POST':
        form = StoryForm(request.POST, instance=story)
        if form.is_valid():
            form.save()
            messages.success(request, 'Story has been updated successfully.')
            return redirect("/")
        else:
            messages.error(request, 'Please correct the following errors')
            return render(request, 'stories/story_form.html', {'form': form})


def delete_story(request, id):
    story = get_object_or_404(Story, id=id)
    context = {'story': story}

    if request.method == 'GET':
        return render(request, 'stories/story_confirm_delete.html', context)
    elif request.method == 'POST':
        story.delete()
        messages.success(request, 'The story has been deleted successfully')
        return redirect('storyposts')


def home(request):
    stories = Story.objects.all()
    context = {'stories': stories}
    return render(request, 'stories/home.html', context)


def about(request):
    return render(request, 'stories/about.html')


def contact(request):
    return render(request, "stories/contact.html")
