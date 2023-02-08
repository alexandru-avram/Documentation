//Let's explore some events samples!

var headOne = document.querySelector('#one')
var headTwo = document.querySelector('#two')
var headThree = document.querySelector('#three')

// addEventListener(type, function(){})

// Mouse Events: click, dblclick, mousedown, mouseup, contextmenu, mouseout, mousewheel, mouseover
// Touch Events: touchstart, touchend, touchmove, touchcancel
// Keyboard Events: keydown, keyup, keypress
// Form Events: focus, blur, change, submit
// Window Events: resize, scroll, load, unload, hashchange

// MOUSE
// click: occurs when the user clicks on an element.
// dblclick: occurs when the user double-clicks on an element.
// mousedown & mouseup: a pointing device button is pressed/released on an element.
// mouseout: a pointing device is moved off the element that has the listener attached.


// Touch events are triggered on touch-enabled devices such as smartphones, tablets, and touch-screen laptops.

// KEYBOARD
// keydown: any key is pressed.
// keyup: any key is released.
// keypress: any key (except shift, Fn, or capslock) is in the pressed position(fired continuously).

// FORM
// focus: an element that has received focus.
// blur: an element that has lost focus.
// change: event that is fired for input, select, and textarea elements when an alteration to the element’s value is done by the user.
// submit: The submit button is pressed.

// WINDOWS
// resize: this event fires when the document view(window) has been resized.
// scroll: event fires when the document view or an element has been scrolled.
// load/unload: the load event is fired when the whole page has loaded, including all resources such as css and images. Unload is when the document or child resource is being unloaded.
// hashchange: this event is fired when the identifier of the URL has changed(the part of the URL that begins with a # symbol).

// OTHER
// error: a resource has failed to load.
// abort: the loading fo a resource was aborted.
// online: the browser has gained access to the network.
// animationstart: this event fires when a CSS animatino has started.


// Hover (mouseover and mouseout)

headOne.addEventListener('mouseover',function(){
  headOne.textContent = "Mouse currently Over";
  headOne.style.color = 'red';
})

headOne.addEventListener('mouseout',function(){
  headOne.textContent = "Mouse Not On me."
  headOne.style.color = 'blue';
})


// On Click
headTwo.addEventListener("click", function() {
  if (headTwo.textContent === "Clicked On") {
    headTwo.textContent = "Clicked Off";
    headTwo.style.color = "red";
  } else {
    headTwo.textContent = "Clicked On";
    headTwo.style.color = "blue";
  }
});


// Double Click
headThree.addEventListener("dblclick",function(){
  headThree.textContent = "Double Clicked!";
  headThree.style.color = 'red';
})


