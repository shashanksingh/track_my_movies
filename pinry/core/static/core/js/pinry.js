/**
 * Based on Wookmark's endless scroll.
 */
$(window).ready(function () {
    var apiURL = '/api/pins/recent/'
    var page = 1;
    var handler = null;
    var isLoading = false;
    
    /**
     * When scrolled all the way to the bottom, add more tiles.
     */
    function onScroll(event) {
      if(!isLoading) {
          var closeToBottom = ($(window).scrollTop() + $(window).height() > $(document).height() - 100);
          if(closeToBottom) loadData();
      }
    };
    
    function applyLayout() {
      $('#pins').imagesLoaded(function() {
          // Clear our previous layout handler.
          if(handler) handler.wookmarkClear();
          
          // Create a new layout handler.
          handler = $('#pins .pin');
          handler.wookmark({
              autoResize: true,
              offset: 3,
              itemWidth: 242
          });
      });
    };
    
    /**
     * Loads data from the API.
     */
    function loadData() {
        isLoading = true;
        $('#loader').show();
        
        $.ajax({
            url: apiURL+page,
            success: onLoadData
        });
    };
    
    /**
     * Receives data from the API, creates HTML for images and updates the layout
     */
    function onLoadData(data) {
        isLoading = false;
        $('#loader').hide();
        
        page++;
        
        var html = '';
        var i=0, length=data.length, image;
        for(; i<length; i++) {
          image = data[i];
          html += '<div class="pin">';
              /*html += '<div class="pin-menu" onmouseover="this.style=\"display:inline\"></div>';*/
              html += '<a class="fancybox" rel="pins" href="'+image.original+'">';
                  html += '<img src="'+image.thumbnail+'" width="200" height="'+Math.round(image.height/image.width*200)+'">';
              html += '</a>';
              html += '<p>'+image.description+'</p><br/>';
        /*      if (image.blog_url != "" || image.blog_url != null ) html += '<a class="btn" href="'+image.blog_url+'">Read</a> &nbsp;'
              if (image.buy_url != "" || image.buy_url != null ) html += '<a class="btn" href="'+image.buy_url+'">Buy</a> &nbsp;'
              if (image.similar_items == true ) html += '<a class="btn" href="/ecommerce/similar-items/?pin_id='+image.id+'">Similar</a>'
              if (image.user_name != "" ) html += '<p align="right" class="info">'+image.user_name+'</p>'*/
          html += '</div>';
        }
        
        $('#pins').append(html);
        
        applyLayout();
    };
  
    $(document).ready(new function() {
        $(document).bind('scroll', onScroll);
        loadData();
    });

    /**
     * On clicking an image show fancybox original.
     */
    $('.fancybox').fancybox({
        openEffect: 'none',
        closeEffect: 'none'
    });
});
