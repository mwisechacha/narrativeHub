function likeStory(storyId){
  $.ajax({
    type: 'POST',
    url: '/like/',
    data: {
      'story_id': storyId,
      'csrfmiddlewaretoken': '{{ csrf_token }}'
    },
    success: function(response) {
      // Update button and likes count
      var likesCount = response.likes_count;
      $('#likes-count-' + storyId).text(likesCount);
      $('.like-button').text('Unlike');
      $('.like-button').addClass('liked');
  },
  error: function(xhr, status, error) {
    console.log('An error occurred while liking the story.');
}
  });
}

