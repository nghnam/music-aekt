var song = {}

// init checkbox
$('.ui.checkbox')
.checkbox()
;

// handle form
$('.ui.form')
.form({
  fields: {
    music_link: {
      identifier: 'music_link',
      rules: [
        {
          type   : 'empty',
          prompt : 'Link chưa đúng'
        }
      ]
    },
    terms: {
      identifier: 'terms',
      rules: [
        {
          type   : 'checked',
          prompt : 'Chưa hứa !!!!'
        }
      ]
    }
  },
  onSuccess: function(event, fields){
    console.log(this);
    event.preventDefault();

    $.post( "/", $( this ).serialize(), function( data ) {
      alert('OK, Chờ tý đang down về list nhạc');
    });
  }
})
;
////////////////// END handle form

function getSongData(data){
  song = {
    Title: data.SongTitle,
    Artist: data.Artist,
    State: data.State,
    File: data.File
  }

  // set song name
  if(data.SongTitle == ''){
    song.Title = data.File
  }

  song.DisplayName = song.Title

  if(song.Artist != '') {
    song.DisplayName = song.Title + ' - ' + song.Artist
  }

  song.DisplayName += "<br />" + song.State
  return song
}

function setControl(data) {
  if(data.State == 'PLAY') {
    $('.play-act').each(function(){
      $(this).removeClass('disabled');
    });
    $('#ctrl-play > i').removeClass('play').addClass('pause')
  }

  if(data.State == 'PAUSE') {
    $('.play-act').each(function(){
      $(this).removeClass('disabled');
    });
    $('#ctrl-play > i').removeClass('pause').addClass('play')
  }

  if(data.State == 'STOP') {
    $('.play-act').each(function(){
      $(this).addClass('disabled');
    });
    $('#ctrl-play > i').removeClass('pause').addClass('play')
  }

}

// handle current song

function setProgress(opts){
  $('#play-progress').progress(opts);
}

function loadPlayer(){
  $.get( "/info", function( data ) {
    // Stopping
    if(data.State == 'STOP'){
      var noPlay = {
        percent: 0,
        value: 0,
        text: {
          active: 'Đang không chơi bài nào'
        }
      }
      setProgress(noPlay);
      $('#play-progress').removeClass('teal');
    }

    // Playing
    if(data.State == 'PLAY' || data.State == 'PAUSE'){
      song = getSongData(data)
      var noPlay = {
        percent: (data.CurrentSec / data.TotalSec) * 100,
        text: {
          active: song.DisplayName
        }
      }
      setProgress(noPlay);
      $('#play-progress').addClass('teal');
    }

    setControl(data);
  });
}
loadPlayer();
setInterval(function(){
  loadPlayer();
}, 3000);


////////////////// END handle current song

/// control
function doAction(act, payload={}){
  $.get( "/" + act, payload, function( data ) {
    loadPlayer();
  })
}

$('#ctrl-play').click(function(event){
  if($(this).children('i').hasClass('play')){
    // click to play
    doAction('play')

  }else if ($(this).children('i').hasClass('pause')) {
    // click to pause
    doAction('pause')
  }
});

$('#ctrl-prev').click(function() {
  doAction('prev')
})
$('#ctrl-next').click(function() {
  doAction('next')
})
$(document).on('click', '.playit', function(){

    var file = $(this).attr('play')
    doAction('playit', {file: file})
    loadPlayer();
});
////////////////////// END control


// playlist
function loadPlaylist(){
  $.get( "/playlist", function(data) {
    try {

      var items = '';
      $.each(data.playlist, function(_, e){
        // items += '<div class="item"><div class="right floated content"><div class="ui button mini playit" play=' + e.path + '><i class="play icon"></i></div></div><div class="content">' + e.title + '</div></div>';
        items += '<div class="item"><div class="right floated content"></div><div class="content">';
        if(song.File == e.path){
          items += '<i class="ui icon angle double right teal"></i> '
          items += e.title
          items += '<i class="ui icon angle double left teal"></i>'
        }else {
          items += e.title
        }
        items += '</div></div>';
      });
      $('.playlist').html(items);
    }
    catch(err) {
      $('.playlist').html('<div class="ui icon message"><i class="warning sign icon"></i><div class="content"><div class="header">Ồ, có lỗi</div><p>' + err + '.</p></div></div>');
    }
    // $('.list').html('<div class="ui icon message"><i class="announcement icon"></i><div class="content"><div class="header">Ồ</div><p>Không có thông tin playlist.</p></div></div>');
    // loadPlayer();
  })
}
loadPlaylist()
setInterval(function(){
  loadPlaylist();
}, 3000);
