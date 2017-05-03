/**
 * LightShaftHandler
 *
 */
 // Inherit from kCanvasHandler
MovingObjectHandler.prototype = new kCanvasHandler();
MovingObjectHandler.prototype.constructor = MovingObjectHandler;
function MovingObjectHandler(kcanvas){
	log("MovingObjectHandler construct");
	kCanvasHandler.call(this, kcanvas);
	this.movingobjects = new Array();
	this.focus = null;
	this.movingobjectInputEnum = {human : "human", sphere : "sphere"};
	//this.movingobjectInputType = this.movingobjectInputEnum.sphere;
	//this.shaftAngle3D = new Point2D(0.5, 0);
	//this.shaftSource2D = new Point2D(kcanvas.getWidth()/2, kcanvas.getHeight()/4);
        //this.spherePoint = new Point2D(0, 0.5);
        //this.sphereRadius = 10
        // human points
	this.moveVertexState = 0;
}

MovingObjectHandler.prototype.paint = function(kcanvas){
	if(kcanvas === undefined){
		kcanvas = this.kcanvas;
	}
	var self = this;
	//Draw human skeleton 
	$(this.movingobjects).each(function(key, value){
		value.paint(kcanvas, key === self.focus)//, value.movingobjectInputType == self.movingobjectInputEnum.human);
                log(value.movingobjectInputType)
	});
        // Draw sphere	
        /*
	if(this.movingobjectInputType == self.movingobjectInputEnum.sphere) {
                log("SPHERE")
                log(this.movingobjectInputType)
		if(this.moveVertexState == 0) {
			this.kcanvas.drawCircle(self.spherePoint, 7, "rgba(0,0,0,.5)");
			this.kcanvas.drawCircle(self.spherePoint, self.sphereRadius, "rgba(255,255,0,.5)");
		} else {		
			this.kcanvas.drawCircle(self.shaftSource2D, 7, "rgba(0,0,0,1)");
			this.kcanvas.drawCircle(self.shaftSource2D, 5, "rgba(255,255,0,1)");
		}
	} else if (this.movingobjectInputType == self.movingobjectInputEnum.sphere){
                log("HUMAN")
                log(this.movingobjectInputType)
        }*/
}

MovingObjectHandler.prototype.buildToolbar = function(){
	var self = this;
	
	var list = $(document.createElement('ul')).attr('class','toolbar-list');
	var list_elements = "";
	$(this.movingobjects).each(function(key, value){
		var element = $(document.createElement('li'));
		element.append(key + " ");
		var lat = $(document.createElement('span'));
		var lon = $(document.createElement('span'));
		element.append(lat);
		element.append(" ");
		element.append(lon);
		element.append($('<a class="add-vertex-link">[add]</a>').click(function(){ self.addVertexMode(key); }));
		element.append($('<a class="move-vertex-link">[move]</a>').click(function(){ self.moveVertexMode(key); }));
		element.append($('<a class="delete-link">[del]</a>').click(function(){ self.deleteMovingObject(key); }));
                element.append("&nbsp;&nbsp;&nbsp;&nbsp;Human:");
		if(value.movingobjectInputType == self.movingobjectInputEnum.human) {
			element.append($('<input type="checkbox" checked/>').click(function(){ self.toggleHuman(key); }));
		} else {
			element.append($('<input type="checkbox"/>').click(function(){ self.toggleHuman(key); }));
		}


		list.append(element);
	});
	$('#movingobject-list').html(list);
}

MovingObjectHandler.prototype.deleteMovingObject = function(key){
	log("[Moving Object] Deleting moving object" + key);
	
	this.movingobjects.splice(key,1);
	if(this.focus === key) this.focus = null;
	
	this.kcanvas.paintAll();
	this.buildToolbar();
}

MovingObjectHandler.prototype.addMovingObject = function(){
	log("[Moving Object] Adding moving object");

	var movingobject= new MovingObject([]);
        movingobject.movingobjectInputType = this.movingobjectInputEnum.sphere
        movingobject.sphereRadius = 10
	movingobject.movingobjectInputEnum = this.movingobjectInputEnum;
	this.movingobjects.push(movingobject);
    this.addVertexMode(this.movingobjects.length-1);
	//this.updateShaftAngle();
	this.buildToolbar();
}

MovingObjectHandler.prototype.addVertexMode = function(key){
	var self = this;
	this.focus = key;
	
	log("[MovingObject] Switching to add vertex mode for moving object "+key);
	
	$(this.kcanvas.canvas).unbind();
	$(this.kcanvas.canvas).mousedown(function(e){ self.addMovingObjectMouseDownHandler(e) })
    $(document).mousemove(function(e){ self.addMovingObjectMouseMoveHandler(e) });
	
	this.moveVertexState = 0;
	
	this.kcanvas.paintAll();
}

MovingObjectHandler.prototype.moveVertexMode = function(key){
	var self = this;
	this.focus = key;
	
	log("[MovingObject] Switching to move vertex mode for moving object "+key);
	
	$(this.kcanvas.canvas).unbind();
	$(this.kcanvas.canvas).mousedown(function(e){ self.moveMovingObjectMouseDownHandler(e) });
	$(document).mouseup(function(e){ self.moveMovingObjectMouseUpHandler(e) });
    $(document).mousemove(function(e){ self.moveMovingObjectMouseMoveHandler(e) });
	
	this.moveVertexState = 1;
	
	this.kcanvas.paintAll();
}


MovingObjectHandler.prototype.toggleHuman = function(key){
        // See if this works
        var t = this.movingobjects[key].movingobjectInputType;
        log(t)
        if (t == this.movingobjectInputEnum.sphere) {
            this.movingobjects[key].movingobjectInputType = this.movingobjectInputEnum.human
            this.movingobjects[key].polygon.vertices = []
            log('Changing to human')
        } else {
            this.movingobjects[key].movingobjectInputType = this.movingobjectInputEnum.sphere
            this.movingobjects[key].polygon.vertices = []
            log('Changing to sphere')
        }
}



/**
 * HTML GUI buttons
 */
MovingObjectHandler.prototype.setShaftInput2D = function(){
	document.getElementById('shaft3d-phi-link').disabled = 1;
	document.getElementById('shaft3d-theta-link').disabled = 1;
	this.shaftInputType = this.shaftInputEnum.twoD;
	this.kcanvas.paintAll();
}

MovingObjectHandler.prototype.setShaftInput3D = function(){
	document.getElementById('shaft3d-phi-link').disabled = 0;
	document.getElementById('shaft3d-theta-link').disabled = 0;
	this.shaftInputType = this.shaftInputEnum.threeD;
	this.kcanvas.paintAll();
}

LightShaftHandler.prototype.updateShaftAngle = function(){
	//Update GUI
	var phi = parseFloat(document.getElementById('shaft3d-phi-link').value);
	var theta = parseFloat(document.getElementById('shaft3d-theta-link').value);
	phi = Math.floor(phi*1e2)/100; // Truncate to two decimal places
	theta = Math.floor(theta*1e2)/100;
	document.getElementById('shaft3d-phi-label-link').innerHTML = phi + " pi";
	document.getElementById('shaft3d-theta-label-link').innerHTML = theta + " pi";
	//Update shaft directions
	this.shaftAngle3D = new Point2D(phi, theta);
	$(this.lightshafts).each(function(key, value){
		value.direction.lat = 0.5+phi;
		value.direction.lon = theta;
	});
	this.kcanvas.paintAll();
}




/**
 * Mouse move handler for adding moving object 
 */
MovingObjectHandler.prototype.addMovingObjectMouseMoveHandler = function(e){
	e.preventDefault();
	var offset = $(this.kcanvas.canvas).offset();
	var x = e.pageX - offset.left;
	var y = e.pageY - offset.top;
}

/**
 * Mouse down handler for adding moving object
 */
var DRAG_RADIUS = 7;
MovingObjectHandler.prototype.addMovingObjectMouseDownHandler = function(e){
	e.preventDefault();

	var offset = $(this.kcanvas.canvas).offset();
	var x = e.pageX - offset.left;
	var y = e.pageY - offset.top;
	
	log("[MovingObject] Adding vertex ("+x+","+y+") to moving object" + this.focus + "."); 
        if ((this.movingobjects[this.focus].movingobjectInputType == this.movingobjectInputEnum.human) || (this.movingobjects[this.focus].polygon.vertices.length == 0)){
	    this.movingobjects[this.focus].polygon.vertices.push(new Point2D(x,y));
        }
	this.kcanvas.paintAll();
}




/**
 * Modify mouse move handler
 */
MovingObjectHandler.prototype.moveMovingObjectMouseMoveHandler = function(e){
	e.preventDefault();
	var offset = $(this.kcanvas.canvas).offset();
	var x = e.pageX - offset.left;
	var y = e.pageY - offset.top;

	// Move vertex if we're currently dragging it
	if(this.isMouseDown && this.dragVertex){
        this.dragVertex.translate(x, y);
		this.kcanvas.paintAll();
	}
        if (this.isMouseDown && this.dragSphere) {
            circleCenter = this.dragSphere.polygon.vertices[0]
            dist = Math.pow(Math.pow(circleCenter.x - x, 2) + Math.pow(circleCenter.y - y, 2), 0.5);
            this.dragSphere.sphereRadius = dist
            this.kcanvas.paintAll();
        }
}

/**
 * Modify mouse down handler
 */
var DRAG_RADIUS = 7;
MovingObjectHandler.prototype.moveMovingObjectMouseDownHandler = function(e){
	e.preventDefault();

	var offset = $(this.kcanvas.canvas).offset();
	var x = e.pageX - offset.left;
	var y = e.pageY - offset.top;;

	this.dragX = x;
	this.dragY = y;
	this.isMouseDown = true;
	self = this;
	
	// See if click was anywhere near a vertex
	$(this.movingobjects[this.focus].polygon.vertices).each(function(key, value){
		dist = Math.pow((value.x - x), 2) + Math.pow((value.y - y), 2);
		// If it was, move it
		if(dist < Math.pow(DRAG_RADIUS, 2)){
			self.dragVertex = value;
		}
	});
        // See if click was anywhere near a circle boundary
        if (this.movingobjects[this.focus].movingobjectInputType == this.movingobjectInputEnum.sphere) {
            console.log('True, obj is sphere')
            circleCenter = this.movingobjects[this.focus].polygon.vertices[0]
            sphereRadius = this.movingobjects[this.focus].sphereRadius
            dist = Math.pow((circleCenter.x - x), 2) + Math.pow((circleCenter.y - y), 2);
            if ((dist > Math.pow(DRAG_RADIUS, 2)) && (dist <= Math.pow(sphereRadius + DRAG_RADIUS, 2))) {
                self.dragSphere = this.movingobjects[this.focus];
            }
        }
}

/**
 * Modify mouse up function
 */
MovingObjectHandler.prototype.moveMovingObjectMouseUpHandler = function(e){
	this.isMouseDown = false;
	delete this.dragVertex;
        delete this.dragSphere;
}
