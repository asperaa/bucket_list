function CreateThumb(id,title,desc,filepath){
	
	var mainDiv=$('<div>').attr('class','col-lg-12 col-md-12');

	var thumbNail=$('<div>').attr('class','thumbnail');

	var img=$('<img>').attr({
		'src':filepath,
		'data-holder-rendered':true,
		'style':'height:auto;width:auto;display:block'
	});

	var caption=$('<div>').attr('class','caption');
	var title=$('<h3>').text(title);
	var desc=$('<p>').text(desc);

	var p=$('<p>');

	var btn=$('<button>').attr({
		'id':'btn_'+id;
		'type':'button',
		'class':'btn btn-danger btn-sm'
	});


	var span=$('<span>').attr({

		'class':'glyphicon glyphicon-thumbs-up',
		'aria-hidden':'true'
	});




	btn.append(span);
	p.append(btn);
	

	caption.append(title);
	caption.append(desc);
	caption.append(p);

	thumbNail.append(img);
	thumbNail.append(caption);

	mainDiv.append(thumbNail);


}