function kCanvasHandler(kcanvas){
	log("-- kCanvasHandler construct");
	this.kcanvas = kcanvas;
	var self = this;
	
	log("-- Attaching this handler as painter to kcanvas.");
	
	if(this.kcanvas !== undefined){
		// Push this as painter
		this.kcanvas.painters.push(this);
	}else{
		log("---- kcanvas undefined");
	}
}

kCanvasHandler.prototype.paint = function(){
	alert("Paint not implemented");
}

kCanvasHandler.prototype.attachToCanvas = function(){
	var self = this;
	
	log("-- Attaching this handler as painter to kcanvas.");
	
	if(this.kcanvas !== undefined){
		// Push this as painter
		this.kcanvas.painters.push(this);
	}else{
		log("---- kcanvas undefined");
	}
}

