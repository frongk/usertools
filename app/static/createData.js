
function genDataSet(inData) {
    //Create Dataset
    var options = {}
    var data = new vis.DataSet(options);

    // add items
    var arrayLength = inData[0].length;
    for (var i = 0; i < arrayLength; i++) {
	data.add([
	          {x: inData[0][i], y: inData[1][i]}
	]);
    }
    
    //check to make sure it works
    var items = data.get({
 	fields: ['id','x','y']
    });
    console.log('formatted items', items);

    return data;
}
