from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Story, Comment
from .forms import StoryForm, CommentForm

# Create your views here.


# story details
@login_required
def create_story(request):
    if request.method == 'GET':
        context = {'form': StoryForm()}
        return render(request, 'stories/story_form.html', context)
    elif request.method == 'POST':
        form = StoryForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.author = request.user
            user.save()
            messages.success(
                request, 'The story has been created successfully')
            return redirect('/')
        else:
            messages.error(request, 'Please correct the following error:')
            return render(request, 'stories/story_form.html', {'form': form})


@login_required
def edit_story(request, id):
    queryset = Story.objects.filter(author=request.user)
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


@login_required
def delete_story(request, id):
    queryset = Story.objects.filter(author=request.user)
    story = get_object_or_404(Story, pk=id)
    context = {'story': story}

    if request.method == 'GET':
        return render(request, 'stories/story_confirm_delete.html', context)
    elif request.method == 'POST':
        story.delete()
        messages.success(request, 'The story has been deleted successfully')
        return redirect('storyposts')

# comment section
def create_comment(request, id):
    story = Story.objects.get(id=id)

    if request.method == 'GET':
        context = {'form': CommentForm()}
        return render(request, 'stories/comment_form.html', context)
    
    elif request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.story = story
            print(comment.save())
            # messages.success(request, 'comment has been posted successfully')
            return redirect('storyposts')
        else:
            messages.error(request, 'Please correct the following errors')
            return render(request, 'stories/comment_form.html', {'form': form, 'story': story})

@login_required
def delete_comment(request, id):
    comment = get_object_or_404(Comment, id=id, author=request.user)
    comment.delete()
    return redirect('storyposts')

# like stories
def like_story(request, id):
    story = get_object_or_404(Story, id=id)
    if request.user.is_authenticated:
        if request.user in story.likes.all():
            story.likes.remove(request.user)
            liked = False
        else:
            story.likes(request.user)
            liked = True
        likes_count = story.likes.count()
        response_data = {'liked': liked, 'likes_count': likes_count}
        return JsonResponse(response_data)
    else:
        return JsonResponse({'error': 'Authentication required'}, status=401)
        return redirect('storyposts')

def unlike_story(request, id):
    story = get_object_or_404(Story, id=id)
    story.unlike(request.user)
    return redirect('storyposts')

def full_story(request, slug):
    story = get_object_or_404(Story, slug=slug)
    context = {'story': story}
    return render(request, 'stories/full_story.html', context)

def home(request):
    stories = Story.objects.all()

    for story in stories:
        # shorten tne content for preview
        story.preview_content = story.content[:200] + '...' if len(story.content) > 200 else story.content
    context = {'stories': stories}
    return render(request, 'stories/home.html', context)


def about(request):
    return render(request, 'stories/about.html')


def contact(request):
    return render(request, "stories/contact.html")

def on_sale(request):
    return render(request, 'stories/on_sale.html')
