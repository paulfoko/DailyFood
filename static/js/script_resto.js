$(document).on('click','.add', function(){
    let name, article
    var item_id = this.id.toString();
    if(panier[item_id]!= undefined){
      panier[item_id] = panier[item_id] +1;
    }else{
      panier[item_id] = 1;
    }
    localStorage.setItem('panier', JSON.stringify(panier))
    fetch('http://127.0.0.1:8000/api/produits/?id=&location1=1'+item_id)
    .then(response => response.json())
    .then(res => { 
    })
})