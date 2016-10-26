$(function () {
    var isMouseDown = false;
    $('.pack td')
      .mousedown(function () {
          isMouseDown = true;
          $(this).toggleClass('selected');
          return false;
      })
      .mouseover(function () {
          if (isMouseDown) {
              $(this).toggleClass('selected');
          }
      });

    $(document)
      .mouseup(function () {
          isMouseDown = false;
      });
});

function resetCheckBoxes() {
    $('td').removeClass('selected');
};

function saveTretment() {
    $()
}

