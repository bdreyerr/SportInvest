var inputBox = document.getElementById('id_num_shares');
// update Estimated cost based on number of inputted shares
inputBox.onkeyup = function(){
    var market_price = document.getElementById('market_price').innerHTML;
    var val = parseFloat(market_price.slice(1));
    
    document.getElementById('trade_calculation').innerHTML = "Estimated Cost: $" + (parseFloat(inputBox.value) * val).toFixed(2);
}