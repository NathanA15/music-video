$(document).ready(function () {

	var tag = document.createElement('script');

	tag.src = "https://www.youtube.com/iframe_api";
	var firstScriptTag = document.getElementsByTagName('script')[0];
	firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

	
	$('#comment-form').on('submit', function(){
		event.preventDefault();
		writeComment();
	});
	initializePlayer();
});

$('#likeVideo').on('click', function() {
		likeVideo();
});

var makeCount = true;

// 2. This code loads the IFrame Player API code asynchronously.
var tag = document.createElement('script');

tag.src = "https://www.youtube.com/iframe_api";
var firstScriptTag = document.getElementsByTagName('script')[0];
firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

// 3. This function creates an <iframe> (and YouTube player)
//    after the API code downloads.
var player;
function onYouTubeIframeAPIReady() {
	player = new YT.Player('player', {

	videoId: $('#player').data('video-id'),
	events: {
		'onReady': onPlayerReady,
		'onStateChange': onPlayerStateChange
		}
	});
}

// 4. The API will call this function when the video player is ready.
function onPlayerReady(event) {
	console.log('player ready');
	event.target.playVideo();
}

// 5. The API calls this function when the player's state changes.
//    The function indicates that when playing a video (state=1),
//    the player should play for six seconds and then stop.
var done = false;
function onPlayerStateChange(event) {
	console.log('onplayrrstate');
	if (event.data == YT.PlayerState.PLAYING && !done) {
		// setTimeout(stopVideo, 6000);
		done = true;
		console.log('123445678');
		$.ajax({
			url:  '/video_app/add_view_count/',
			type: 'POST',
			data: {
				video_id: $('#player').data('video-id'),
			},
			success: function(json) {
				$('#view-count').html(json.count);
				console.log(json.count);
			},
			error: function(xhr, errmsg, err) {
				console.log(errmsg, err);
				console.log('video already seen');
			},
		});		
	}
};


function stopVideo() {
	console.log('stop')
	player.stopVideo();
}


function likeVideo(){
	var video_id = $('#player').data('video-id');
	$.ajax({
			url: '/video_app/like_video/',
			type: 'POST',
			data: {
				video_id : video_id
			}
	})

	.done(function(data){
		if(data.code == 200){
			var nb_likes = data.nb_likes;
			var has_liked = data.has_liked;
			$('#nb_likes').text(nb_likes);
			if (has_liked) {
				$('#heart_pic').attr("src","/static/images/like_button.png");
			} else {
				$('#heart_pic').attr("src","/static/images/not_like_button.png");
			}
		}
	});
}


function writeComment() {
	$.ajax({
		url: '/comment_app/write_comment/' + $('#video-id').attr('video-id') ,
		type: 'POST',
		data: {
			text: $("#id_text").val(),
		},
		success: function(json) {
			$("#id_text").val('');
			addComment(json);
		},
		error: function(xhr, errmsg, err) {
			alert('Something went wrong!');
			console.log(errmsg, err);
		},
	})
}


function addComment(comment) {
	var commentHTML = ` 
		<hr>
		<p>` +comment.text+ `</p>`;

	$('#comments').prepend(commentHTML);

}

$('#btnSearch').on('click', function() {
		searchVideo();
		$('#txtVideoSearch').focus();
	});


$('#txtVideoSearch').on('keypress', function(event) {
	if(event.which == 13) {
		event.preventDefault();
		searchVideo();
		$('#txtVideoSearch').focus();
	}
});





function searchVideo(){
	var search = $('#txtVideoSearch').val();
	if(search.trim() == "") {
			alert("You must enter text");
			return;
	}
	window.location.replace("/video_app/search_video/" + search +"/");
}





$(document).ready(function () {
	$(function() {
		function getCookie(name) {
			var cookieValue = null;
			if (document.cookie && document.cookie != '') {
				var cookies = document.cookie.split(';');
				for (var i = 0; i < cookies.length; i++) {
					var cookie = jQuery.trim(cookies[i]);
					if (cookie.substring(0, name.length + 1) == (name + '=')) {
						cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
						break;
					}
				}
			}
			return cookieValue;
		}
		var csrftoken = getCookie('csrftoken');

		function csrfSafeMethod(method) {
			return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
		}

		function sameOrigin(url) {
			var host = document.location.host;
			var protocol = document.location.protocol;
			var sr_origin = '//' + host;
			var origin = protocol + sr_origin;
			return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
				(url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
				!(/^(\/\/|http:|https:).*/.test(url));
		}

		$.ajaxSetup({
			beforeSend: function(xhr, settings) {
				if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
					xhr.setRequestHeader("X-CSRFToken", csrftoken);
				}
			}
		});
	});
});
