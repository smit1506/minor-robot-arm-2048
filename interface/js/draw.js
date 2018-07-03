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

    canvas.onmousedown = function (e) {
        if (mouseDown == false && drawRectangle){
            if (element !== null) {
                remove(element);
            }
            mouseDown = true;
            mouse.startX = mouse.x;
            mouse.startY = mouse.y;
            element = document.createElement('div');
            document.getElementById('canvas-container').appendChild(element);
            element.className = 'rectangle';
            element.id = 'fieldTemplate';
            element.style.left = mouse.x + 'px';
            element.style.top = mouse.y + 'px';
            console.log("Click down");
        }
        else if (drawRectangle) {
            element.dataset.rct = [
              ((mouse.x - mouse.startX < 0) ? mouse.x : mouse.startX),
              ((mouse.y - mouse.startY < 0) ? mouse.y : mouse.startY),
              Math.abs(mouse.x - mouse.startX),
              Math.abs(mouse.y - mouse.startY)
            ];
            console.log("Click up");
            mouseDown = false;
        }
        else {
            mouseDown = false;
        }
    }

    canvas.onmouseup = function (e) {
        if (drawRectangle) {
            element.dataset.rct = [
              ((mouse.x - mouse.startX < 0) ? mouse.x - canvas.offsetLeft : mouse.startX - canvas.offsetLeft),
              ((mouse.y - mouse.startY < 0) ? mouse.y - canvas.offsetTop : mouse.startY - canvas.offsetTop),
              Math.abs(mouse.x - mouse.startX),
              Math.abs(mouse.y - mouse.startY)
            ];
            console.log("Click up");
            mouseDown = false;
        }
    }
}
