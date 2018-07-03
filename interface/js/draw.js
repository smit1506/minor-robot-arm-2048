initDraw(document.getElementById('canvas'));

function initDraw(canvas) {

    const mouse = {
        x: 0,
        y: 0,
        startX: 0,
        startY: 0
    }
    let element = null;
    let mouseDown = false;

    function setMousePosition(e) {
        mouse.x = e.pageX + window.pageXOffset;
        mouse.y = e.pageY + window.pageYOffset;
    };
    canvas.onmousemove = function (e) {
        setMousePosition(e);
        if (mouseDown && element !== null) {
            element.style.width = Math.abs(mouse.x - mouse.startX) + 'px';
            element.style.height = Math.abs(mouse.y - mouse.startY) + 'px';
            element.style.left = (mouse.x - mouse.startX < 0) ? mouse.x + 'px' : mouse.startX + 'px';
            element.style.top = (mouse.y - mouse.startY < 0) ? mouse.y + 'px' : mouse.startY + 'px';
        }
    }

    canvas.onclick = function (e) {
        if (mouseDown == false && drawRectangle){
            if (element !== null) {
                remove(element);
            }
            mouseDown = true;
            mouse.startX = mouse.x;
            mouse.startY = mouse.y;
            element = document.createElement('div');
            document.getElementById('canvas-container').appendChild(element)
            element.className = 'rectangle'
            element.style.left = mouse.x + 'px';
            element.style.top = mouse.y + 'px';
        }
        else {
            mouseDown = false
        }
    }
}
