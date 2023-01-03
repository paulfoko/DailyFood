var total = 0;
let cart_article = document.querySelector('#cart')

$(document).on('input','.qte', function(){
    var id_article = parseFloat(this.id.toString());
    panier[id_article]= Number(this.value)
    localStorage.setItem('panier', JSON.stringify(panier))
    total = 0;
    reloadCart(keys_article)
    document.getElementById('cart_length').innerHTML = keys_article.length
    if (keys_article.length == 0) {
        document.getElementById('total').innerHTML = keys_article.length
    }
})
$(document).on('click','.btn_delete', function(){
    var id_article = this.id.toString();
    panier[id_article] = undefined;
    localStorage.setItem('panier', JSON.stringify(panier))
    keys_article = keys_article.filter(item => item !== id_article)
    total = 0;
    reloadCart(keys_article)
    if (keys_article.length == 0) {
        document.getElementById('total').innerHTML = keys_article.length
    }
})
$(document).on('click','.add', function(){
    let name, article
    var item_id = this.id.toString();
    if(panier[item_id]!= undefined){
      panier[item_id] = panier[item_id] +1;
    }else{
      panier[item_id] = 1;
    }
    localStorage.setItem('panier', JSON.stringify(panier))
    fetch('http://127.0.0.1:8000/api/produits/?id='+item_id)
    .then(response => response.json())
    .then(res => { 
        keys_article.push(item_id)  
        name = String(res[0].name)
        article = [name]
        article.push(String(res[0].image))
        article.push(String(res[0].image_link))
        article.push(String(res[0].price))
        article.push(String(res[0].stock))
        localStorage.setItem(item_id,  JSON.stringify(article))
        console.log(localStorage)
        total = 0;
        reloadCart(keys_article)
        SetNbrArticles(keys_article)
    })
})
function SetNbrArticles(key) {
    var keys = Array.from(new Set(key));
    document.getElementById('cart_length').innerHTML = keys.length
}
function reloadCart(keys) {
    cart_article.innerHTML = '';
    var keys2 = Array.from(new Set(keys));
    for (var key of keys2) {
        article = JSON.parse(localStorage.getItem(key))
        nbr = panier[key]
        const name = article[0]
        const image = article[1]
        const image_link = article[2]
        const price = article[3]
        const stock = article[4]
        var x = Number(nbr) * Number(price)
        seTotal(x)
        displayArticle(name, image, image_link, price, stock, nbr, key)
    }
}
function displayArticle(name, image, image_link, price, stock, nbr, id) {
    const div = document.createElement('div');
    div.classList.add('Box_article')
    img = makeImage(image, image_link)
    content = makeContent(name, price, stock, nbr, id)
    del = makeDelete(id)
    div.appendChild(img)
    div.appendChild(content)
    div.appendChild(del)
    cart_article.appendChild(div)
}
function seTotal(value) {
    total += value
    document.getElementById('total').innerHTML = String(total)
}
function makeImage(image, image_link) {
    const img = document.createElement('img');
    if (image_link == '') {
        img.src = image
    }else{
        img.src = image_link
    }
    return img
}
function makeContent(name, price, stock, nbr, id) {
    const content = document.createElement('div')
    content.classList.add('content')
    const h3 = document.createElement('h3')
    h3.textContent = name
    const span1 = document.createElement('span')
    span1.classList.add('article_price')
    span1.textContent = price+" fcfa / Qte : "
    const span2 = document.createElement('span')
    span2.classList.add('article_quant')
    const input = document.createElement('input')
    input.min = 1
    input.max = Number(stock)
    input.classList.add('qte')
    input.id = String(id)+"qte"
    input.type = 'number'
    input.value = nbr
    span2.appendChild(input)
    content.appendChild(h3)
    content.appendChild(span1)
    content.appendChild(span2)
    return content
}
function makeDelete(id) {
    const span = document.createElement('span')
    const icon = document.createElement('ion-icon')
    icon.name = "trash-outline"
    span.classList.add('btn_delete')
    span.id = id
    span.appendChild(icon)
    return(span)
}