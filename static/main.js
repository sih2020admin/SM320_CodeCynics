
    var count=2;
    var data={
        'ACETIC ACID': 0.433402457992343,
 'HIGH SPEED DIESEL': 0.660305054354523,
 'SPLIT RBD PALM STEARIN FATTY ACID': -25812.5797077479,
 'CRUDE PALM OIL': 1.91722351090253,
 'RBD PALM STEARIN': 3.65580123221722,
 'CRUDE SUNFLOWER OIL': 0.790290749405205,
 'METHANOL': 0.889196780713228,
 'CRUDE SOYABEAN OIL': 2.25329745201629,
 'MOTOR SPIRIT': 1.35615408179278,
 'LINEAR ALKYL BENZENE': 0.937569218667097,
 'CRUDE PALM KERNEL OIL': 1.71762055214435,
 'HEAVY WHITE OIL': 0.387856321229309,
 'LPG BUTANE': 1.09831884921936,
 'LPG PROPANE': 1.15953900583481,
 'VINYL ACETATE MONOMER': 0.181204897591633,
 'DENATURED ETHYL ALCOHOL': 1.0675684374922,
 'DIETHYLENE GLYCOL': 0.650704840512238,
 'ALPHAPLUS C-20/24': 0.997082745359669,
 'CARBON BLACK FEED STOCK': 0.523665073840487,
 'METHYL TERTIARY BUTYL ETHER': 0.611954888318226,
 'ALPHAPLUS 1-TETRADECENE': 1.10696776116865,
 'SUPERIOR KEROSENE OIL': 1.12916612198562,
 'ACETIC ANHYDRIDE': -30.0301730187436,
 'OLEFINS(C13+ALL ISOMERS)ALPHAPLUS (R)C24-28': 0.937501902263917,
 'NAPHTHA': 1.35277531784082,
 'ALPHAPLUS(R) NAO 1 - DODECENE (C12H24)': 1.85626090831445,
 'BITUMEN': 1.12995336352639,
 'BENTONITE IN BULK': 0.785309439940771,
 'CONTAINER': 0.688731453337458,
 'BAUXITE IN BULK': 4.40318552625844,
 'MURITE OF POTASH': 2.58424611745609,
 'IRON ORE LUMPS': 4.0328349039842,
 'SILICA SAND': 1.68259860831273,
 'IRON ORE PELLETS': 2.64415609039828,
 'CRIMSON LENTILS': 0.359014444943003,
 'PET COKE': 0.742463079901291,
 'STONE / STONE CHIPS': 0.643916447561044,
 'BLACK MATPE': 0.895296640750421,
 'CAR': 0.359014444943003,
 'CRUDE PETROLEUM OIL': 0.507109293397066,
 'LIQUEFIED NATURAL GAS': 2.02988993796523,
 'STEAM COAL': 2.22694945288235,
 'COKING COAL': 2.22694945288235,
 'CRUDE GLYCERINE': 2.561726,
 'PALM KERNEL FATY ACID DISTILLATE': 3.41041,
 'F. O.': 1.779876,
 'RBD PALM OLEIN': 2.427081,
 'FATTY ACID C1618 UNDISTILLED': 2.450992,
 'GAS OIL (HSD)': 2.003393,
 'CRUDE PALM STEARIN': 2.937502,
 'SPLIT PALM FATTY ACID DISTILLATE': 2.142362,
 'RUBBER  PROCESS OIL (C-160 A)': 5.827102,
 'BASE OIL P 600': 5.827093,
 'ALPHA PLUS 1 HEXADECENE': 0.801587,
 'PETRELAB': 1.306943,
 'ALPHAPLUS (R) 1-DODECENE': 0.727081,
 'CAUSTIC SODA LIQUID': 1.029167,
 'N-PARAFFIN': 1.166666,
 'SHELL GTL WAXY RAFFINATE (EPIWAX 825)': 0.413889,
 'UREA': 3.7203,
 'PROJECT CARGO': 3.101443,
 'STEEL PIPES': 3.708401,
 'REPAIR/HANDLING MATERIAL': 3.0998555,
 'STEEL COINS': 2.618051,
 'STEEL PLATES': 3.237125,
 '(MPO)2-METHYL-1,3-PROPANEDIOL': 0.436113,
 'INDUSTRIAL SALT': 3.153765,
 'DAP': 4.16108,
 'GRANULATED BLAST FURNACE SLAG': 4.309533,
 'FLY ASH IN JUMBO BAGS': 3.259896,
 'BENTONITE IN JUMBO BAGS': 4.339585,
 'STEEL BENDS': 2.7786,
 'SODA ASH': 3.258798,
 'STEEL RAILS': 4.30347,
 'SUGAR IN BAGS': 10.399268,
 'WHITE CRYSTAL SUGAR': 10.399365,
 'SOYABEAN MEAL': 6.188547,
 'NITRO PHOSPHATE WITH POTASH': 3.500811,
 'LIME STONE': 4.627776,
 'YELLOW PEAS': 5.576991,
 'STEEL BARS': 7.146195,
 'POTESIUM MAGNASIUM SULPHATE': 3.75001,
 'IRON ORE FINE': 3.057222,
 'MET COKE': 1.899306,
 'CLINKER IN BULK': 1.579167,
 'WET ASH IN  BULK': 2.916666,
 'TOOR WHOLE': 0.745824,
 'THERMAL COAL': 2.735416,
 'PCI COAL (PULVERISED COAL)': 1.04375
    };
    var p=[];
    var w=[];
    var wp=[];
    var com=[];
    var t=0;
    var filling={};
    
    $( document ).ready(function() {
        $("#Weightl").hide()
        $("#weight1").hide()
        $("#conlist1").hide()
        $("#liqlist1").hide()
        $("#drylist1").hide()
        $("#commodity").hide()
        $('#timewindow').hide()
        $('#timel').hide()
        $('#add').hide()
        $('#revenue').hide()
        $("#rl").hide()
        $("#reset").click(function(){
            location.reload(true);
        });
});
   function set(){
       $('#add').show()
        if($("#cargo").val()=="Containers"){
            $("#Weightl").show()
        $("#weight1").show()
            $("#commodity").show()
            $("#conlist1").show()
            $("#liqlist1").hide()
            $("#drylist1").hide()

        }
        else if($("#cargo").val()=="Liquid"){
            $("#Weightl").show()
        $("#weight1").show()
            $("#commodity").show()
            $("#conlist1").hide()
            $("#liqlist1").show()
            $("#drylist1").hide()


        }
        else if($("#cargo").val()=="Dry"){
            $("#Weightl").show()
        $("#weight1").show()
            $("#commodity").show()
            $("#conlist1").hide()
            $("#liqlist1").hide()
            $("#drylist1").show()

        }
   }
function addc(){
    if($("#cargo").val()=="Containers"){
           $('#addspace').append('<label id="commodity">Commodity</label><input list="con" id="conlist'+count+'"><br><label for="weight'+count+'">Weight</label><input type="number" name="weight'+count+'" id="weight'+count+'" step="0.0001"><br>')
           count++;
        }
        else if($("#cargo").val()=="Liquid"){
            $('#addspace').append('<label id="commodity">Commodity</label><input list="liq" id="liqlist'+count+'"><br><label for="weight'+count+'">Weight</label><input type="number" name="weight'+count+'" id="weight'+count+'" step="0.0001"><br>')
            count++;
        }
        else if($("#cargo").val()=="Dry"){
            $('#addspace').append('<label id="commodity">Commodity</label><input list="dry" id="drylist'+count+'"><br><label for="weight'+count+'">Weight</label><input type="number" name="weight'+count+'" id="weight'+count+'" step="0.0001"><br>')
            count++;
        }


}
function check(){
    $('#timewindow').show();
        $('#timel').show();
        $('#revenue').show()
        $("#rl").show()
       
    for(var i=1;i<count;i++){
        if($("#cargo").val()=="Containers"){
            com.push($('#conlist'+i).val());
          //  wp.push(data[$('#conlist'+i).val()]);
            w.push(parseFloat($('#weight'+i).val()));
        }
        else if($("#cargo").val()=="Liquid"){
            com.push($('#liqlist'+i).val());
            //wp.push(data[$('#liqlist'+i).val()]);
            w.push(parseFloat($('#weight'+i).val()));
        }
        else if($("#cargo").val()=="Dry"){
            com.push($('#drylist'+i).val());
           // wp.push(data[$('#drylist'+i).val()]);
            w.push(parseFloat($('#weight'+i).val()));
        }
        //p.push(w[i-1]/wp[i-1]);
       // t=t+(24/(count-1))*(w[i-1]/p[i-1]);

    

     }
    console.log(com);
    console.log(w);
    $.ajax({
        data:{
            count:count,
            w: JSON.stringify(w),
            com:JSON.stringify(com),
            type:$("#cargo").val(),
            eta:$('#ETA').val()

        },
        type:'POST',
        url:'/check'
    })
    .done(function(data){
        console.log(data);
        $('#timewindow').val(data['tat']);
        filling=data;
        $('#revenue').val('₹'+data['revenue']);
        $('#addspace').append('<p id="tat">Turn-Around Time:'+ data['time'] +' hours</p>');
        for(var i=0;i<data['prod'].length;i++){
            $('#addspace').append('<p id="sp'+i+'">Productivity for '+data['Commodities'][i] +' : '+data['prod'][i] +'</p>');
        }
           

        $('#checka').css("display","none");
     
        // console.log(JSON.parse(data['Commodities']))
    })
    event.preventDefault();
    com=[];
    w=[];


}

function onchangewindow(){
    $.ajax({
        data:{
           eta: $('#ETA').val(),
            end:$('#timewindow').val()
        },
        type:'POST',
        url:'/change'
    })
    .done(function(data){
        console.log(data);
        console.log((Date.parse(data['time'])-Date.parse(data['eta']))/3600000);
        var diff=(Date.parse(data['time'])-Date.parse(data['eta']))/3600000;
        var divi=filling['time']/diff;
        $('#tat').html('Turn-Around Time:'+ diff +' hours');
        filling['time']=diff;
        for(var i=0;i<filling['prod'].length;i++){
            filling['prod'][i]=divi*filling['prod'][i];
            $('#sp'+i).html('Productivity for '+filling['Commodities'][i] +' : '+filling['prod'][i] +'');

        }
    })
    
    



    console.log('Changed');

}
function saveinfo(){
    $.ajax({
        data:{
            name:$("#name").val(),
            details:JSON.stringify(filling)
        },
        type:"POST",
        url:'/save'
    })
    .done(function(data){
        console.log(data);
        window.location.href = '/';

    })
}
