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

  return song
}

// handle current song
function setProgress(opts){
  $('#play-progress').progress(opts);
}

function loadPlayer(){
  $.get( "/info", function( data ) {
    song = getSongData(data)

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
      $('#play-state').html('');
    }

    // Playing
    if(data.State == 'PLAY' || data.State == 'PAUSE'){
      var noPlay = {
        percent: (data.CurrentSec / data.TotalSec) * 100,
        text: {
          active: song.DisplayName
        }
      }
      setProgress(noPlay);
      $('#play-progress').addClass('teal');
      $('#play-state').html('Trạng thái: <a class="ui grey label tiny">' + data.State + '</a>');
    }
  });
}
loadPlayer();
setInterval(function(){
  loadPlayer();
}, 3000);


////////////////// END handle current song

// playlist
function loadPlaylist(){
  $.get( "/playlist", function(data) {
    try {

      var items = '';
      $.each(data.playlist, function(_, e){
        items += '<div class="ui segment">';
        if(song.File == e.path){
          items += '<p style="color: #009c95">'
          items += e.title
          items += '</p>'
        }else {
          items += e.title
        }
        items += '</div>';
      });
      $('.playlist').html(items);
    }
    catch(err) {
      $('.playlist').html('<div class="ui icon message"><i class="warning sign icon"></i><div class="content"><div class="header">Ồ, có lỗi</div><p>' + err + '.</p></div></div>');
    }
  })
}
loadPlaylist()
setInterval(function(){
  loadPlaylist();
}, 3000);
