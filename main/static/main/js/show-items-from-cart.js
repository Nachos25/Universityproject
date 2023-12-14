function updateGoodsList() {
    let jsonInfo = JSON.parse(localStorage.getItem('cart'))
    if (localStorage.getItem('cart')) {
        if (jsonInfo.length === 0) {
            let cartSection = document.querySelector('.display');
            cartSection.innerHTML = "<span>Кошик порожній</span>"
        } else {
            let cartSection = document.querySelector('.items-display');
            cartSection.innerHTML = "<span>Кошик</span>"
            let price = 0
            for (let i = 0; i < jsonInfo.length; i++) {
                price += parseInt(JSON.parse(jsonInfo[i]).price.replace(' ', ''))
                cartSection.innerHTML += `
                    <div class='cart-item'>
                        <img class="image" src='${JSON.parse(jsonInfo[i]).image}'>
                        <div class="item-info">
                            <a href="${JSON.parse(jsonInfo[i]).link_to_product}" class="item-link">${JSON.parse(jsonInfo[i]).product_name}</a>
                            <div class="bottom-info">
                                <div class="pricing">
                                    <div class="price-box">
                                        <span class="price">${JSON.parse(jsonInfo[i]).price} ${JSON.parse(jsonInfo[i]).currency}</span>
                                    </div>
                                    <div class="old-price-box">
                                        <span class="price">${JSON.parse(jsonInfo[i]).old_price} ${JSON.parse(jsonInfo[i]).currency}</span>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="remove-button">
                            <span class="material-symbols-outlined symbol" data-info="${i}">delete</span>
                        </div>
                    </div>
                `
            }
            let price_info = document.querySelector('.price-info')
            price_info.innerHTML = price.toLocaleString() + " UAH"
        }
    } else {
        let cartSection = document.querySelector('.display');
        cartSection.innerHTML = "<span>Кошик порожній</span>"
    }
}
updateGoodsList()

document.addEventListener('DOMContentLoaded', function () {
  let buyButton = document.querySelector('.buy')
  buyButton.addEventListener('click', function () {
    window.location.href = "/order?text=default";
  });
});
document.addEventListener('DOMContentLoaded', function () {
  let buyCreditButton = document.querySelector('.credit-buy')
  buyCreditButton.addEventListener('click', function () {
    window.location.href = "/order?text=credit";
  });
});