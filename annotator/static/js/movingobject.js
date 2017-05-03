/**
 * LightSource
 */
 
 function MovingObject(vertices){
	this.polygon = new Polygon(vertices)
	//this.direction = new PointSphere(1, 0);
 }
 
 MovingObject.prototype.paint = function(kcanvas, inFocus){
	if(inFocus){
		this.polygon.lineWidth = 2;
		this.polygon.strokeStyle = "rgba(0,0,0,0.7)"
                // Make sure to remove fill
		//this.polygon.fillStyle = "rgba(255,255,0,0.3)";
                this.polygon.fillStyle = "rgba(0, 0, 200, 0)";
	}else{
		this.polygon.lineWidth = 2;
		this.polygon.strokeStyle = "rgba(0,0,0,0.35)"
                // Make sure to remove fill
                this.polygon.fillStyle = "rgba(0, 0, 200, 0)";
		//this.polygon.fillStyle = "rgba(255,255,0,0.15)";
	}
	//this.polygon.paint(kcanvas);
	
        log(this.polygon.vertices)
	if(this.movingobjectInputType == this.movingobjectInputEnum.human) {
                log('Drawing human')
                // draw points and skeleton
                var lineColor = "rgba(255, 0, 255, 0.75)";
                p = this.polygon.vertices
                for (var i=0; i < p.length; i++) {
                    kcanvas.drawCircle(p[i], 1, lineColor);
                }
                // knees, toes, head, elbows, hands
                // 0 connects to 1 (neck)
                kcanvas.drawLine(p[0], p[1], lineColor);
                // 1 connects to 2 (left shoulder)
                kcanvas.drawLine(p[1], p[2], lineColor);
                // 2 connects to 3 (left elbow)
                kcanvas.drawLine(p[2], p[3], lineColor);
                // 3 connects to 4 (left hand)
                kcanvas.drawLine(p[3], p[4], lineColor);
                // 1 connects to 5 (right shoulder)
                kcanvas.drawLine(p[1], p[5], lineColor);
                // 5 connects to 6 (right elbow)
                kcanvas.drawLine(p[5], p[6], lineColor);
                // 6 connects to 7 (right hand)
                kcanvas.drawLine(p[6], p[7], lineColor);
                // 1 connects to 8 (groin)
                kcanvas.drawLine(p[1], p[8], lineColor);
                // 8 connects to 9 (left hip)
                kcanvas.drawLine(p[8], p[9], lineColor);
                // 9 connects to 10 (left knee)
                kcanvas.drawLine(p[9], p[10], lineColor);
                // 10 connects to 11 (left foot)
                kcanvas.drawLine(p[10], p[11], lineColor);
                // 8 connects to 12 (right hip)
                kcanvas.drawLine(p[8], p[12], lineColor);
                // 12 connects to 13 (right knee)
                kcanvas.drawLine(p[12], p[13], lineColor);
                // 13 connects to 14 (right foot)
                kcanvas.drawLine(p[13], p[14], lineColor);
		/*var cartesian_direction = this.direction.cartesian();
		var centroid = this.polygon.findCentroid();
		var direction = cartesian_direction.project2D();
		var end = this.polygon.findCentroid().plus(direction);
        var normalizedDirY = (cartesian_direction.y+100)/200; //r = 100, see PointSphere.js
		kcanvas.drawLine(centroid, end, lineColor);
		
		var headlen = 10;
		var angle = Math.atan2(end.y-centroid.y, end.x-centroid.x);
		var arrowhead_right = new Point2D(end.x-headlen*Math.cos(angle-Math.PI/6), end.y-headlen*Math.sin(angle-Math.PI/6));
		var arrowhead_left = new Point2D(end.x-headlen*Math.cos(angle+Math.PI/6), end.y-headlen*Math.sin(angle+Math.PI/6));
		kcanvas.drawLine(end, arrowhead_right, "rgba(0,0,0,.5)");
		kcanvas.drawLine(end, arrowhead_left, lineColor);
		kcanvas.drawLine(end, arrowhead_right, lineColor);
		kcanvas.drawLine(end, arrowhead_left, lineColor);*/
	} else {
                // draw sphere
                if (this.polygon.vertices.length > 0) {
                    kcanvas.drawCircle(this.polygon.vertices[0], 1, "rgba(255, 0, 255, 0.75)");
                    kcanvas.drawCircle(this.polygon.vertices[0], this.sphereRadius, "rgba(255,255,0,0.3)");
                }
        }
 }
