
function current(id) {
    console.log(id);
    $.ajax({
        data: {
            status: 'Current',
            berth: $('#berth' + id).val(),
            id: id

        },
        type: "POST",
        url: '/current'
    })
        .done(function (data) {
            console.log(data);
            location.reload(true);
        })
}

function remove(id) {
    console.log(id);
    $.ajax({
        data: {
            id: id
        },
        type: "POST",
        url: '/remove'
    })
        .done(function (data) {
            console.log(data);
            location.reload(true);
        })

}

function finder(){
    $.ajax({
        data:{
            "name":$('#Vname').val()
        },
        type:"POST",
        url:'/info'
    })
    .done(function(data){
        console.log(data);
       $('#result').html(data.info)

    })
}