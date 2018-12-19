$(document).ready(function () {
	
	$('#comment-form').on('submit', function(){
		event.preventDefault();
		writeComment();
	})

})

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