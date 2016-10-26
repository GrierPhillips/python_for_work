$(function () {
    var isMouseDown = false;
    $('.plate td')
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

