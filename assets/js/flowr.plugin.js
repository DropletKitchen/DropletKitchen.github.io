(function(g){g.fn.flowr=function(p){$this=this;var q=["complete","data","responsive"],h={data:[],padding:5,height:240,render:null,append:!1,widthAttr:"width",heightAttr:"height",maxScale:1.5,maxWidth:this.width()-1,itemWidth:null,itemHeight:null,complete:null,rowClassName:"flowr-row",rows:-1,responsive:!0},a=g.extend(h,p);if(a.append&&$this.data("lastSettings")){lastSettings=$this.data("lastSettings");for(attr in h)0>q.indexOf(attr)&&a[attr]==h[attr]&&(a[attr]=lastSettings[attr]);lastRow=$this.data("lastRow");
0<lastRow.data.length&&25<a.maxWidth-lastRow.width&&(lastRowData=lastSettings.data.slice(lastSettings.data.length-lastRow.data.length-1),a.data=lastRowData.concat(a.data),g("."+a.rowClassName+":last",$this).detach())}!a.responsive&&!a.append&&$this.width($this.width());if(a.data instanceof Array){"number"!=typeof a.padding&&(a.padding=parseInt(a.padding));"function"!=typeof a.itemWidth&&(a.itemWidth=function(k){return k[a.widthAttr]});"function"!=typeof a.itemHeight&&(a.itemHeight=function(k){return k[a.heightAttr]});
var n={getNextRow:function(a,b){var e=0,g=a.length,f=[],c=0;for(requiredPadding=function(){return(f.length-1+(1==arguments.length?arguments[0]:0))*b.padding};c+requiredPadding()<b.maxWidth&&e<g;){var l=a[e],d=b.itemWidth.call($this,l),h=b.itemHeight.call($this,l),m=b.height,d=Math.floor(d*b.height/h);d>b.maxWidth&&(d=b.maxWidth-1-requiredPadding(1),m=b.height*m/d);if(c+d<b.maxWidth)f.push({height:m,width:d,itemData:l}),c+=d,e++;else break}testWidth=0;if(c<b.maxWidth){e=(b.maxWidth-requiredPadding()-
10)/c;e>b.maxScale&&(e=1);g=Math.round(b.height*e);for(i=0;i<f.length;i++)c=f[i],c.width=Math.floor(c.width*e),c.height=g,testWidth+=c.width}return{data:f,width:testWidth+requiredPadding()}},reorderContent:function(){var a=$this.data("width"),b=$this.width();a!=b&&($this.html(""),a=$this.data("lastSettings"),a.data=$this.data("data"),a.maxWidth=$this.width()-1,$this.flowr(a))}};a.responsive&&!$this.data("__responsive")&&(g(window).resize(function(){initialWidth=$this.data("width");newWidth=$this.width();
if(initialWidth!=newWidth){var a=$this.data("task_id");a&&clearTimeout(a);a=setTimeout(n.reorderContent,80);$this.data("task_id",a)}}),$this.data("__responsive",!0));return this.each(function(){var k=a.data.slice(0),b=null,e=0,h=0,f=[];for(i=0;i<k.length;i++)f.push(k[i]);for($this.data("data",f);null!=(b=n.getNextRow(k,a))&&0<b.data.length&&!(0<a.rows&&e>=a.rows);){k.splice(0,b.data.length);var f=g("<div>").addClass(a.rowClassName),c=$this[0].clientWidth-b.width-2*a.padding;for(i=0;i<b.data.length;i++){var l=
b.data[i],d=a.render.call($this,l),d=g(d);extraw=Math.floor(c/b.data.length);0==i&&(extraw+=c%b.data.length);d.css("width",l.width+extraw).css("height",l.height).css("margin-bottom",a.padding+"px").css("margin-left",0==i?"0":a.padding+"px");f.append(d);h++}$this.append(f);e++;$this.data("lastRow",b)}$this.data("lastSettings",a);"function"==typeof a.complete&&a.complete.call($this,{renderedRows:e,renderedItems:h})})}}})(jQuery);
