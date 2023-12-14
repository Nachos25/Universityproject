document.addEventListener('DOMContentLoaded', function() {
    let buttons = document.querySelectorAll('.buy-button');

    buttons.forEach(function(button) {
        button.addEventListener('click', function() {
            let info = this.getAttribute('data-info');
            addProductToCart(info);
        });
    });


    function updateCartItem(list){
        let cartItem = document.querySelector('.cart_text');
        let cart_length = list.length
        cartItem.innerHTML = '<span class="material-symbols-outlined cart-icon">shopping_cart</span>'+cart_length
    }

    function addProductToCart(info){
        let cart = localStorage.getItem('cart')

        if(cart === null){
            cart = []
        } else {
            cart = JSON.parse(cart);
        }
        cart.push(info);
        updateCartItem(cart);
        localStorage.setItem("cart", JSON.stringify(cart));
        localStorage.setItem('cart_length', cart.length);
    }


    document.addEventListener('click', function (event) {
        if (event.target.classList.contains('symbol')) {
            let info = event.target.getAttribute('data-info');
            deleteItemFromCart(info);
        }
    });

    function deleteItemFromCart(index){
        let cart = localStorage.getItem('cart');
        let json_data = JSON.parse(cart);
        console.log(index)
        json_data.splice(parseInt(index), 1);
        localStorage.setItem("cart", JSON.stringify(json_data));
        localStorage.setItem('cart_length', json_data.length);
        updateCartItem(json_data);
        updateGoodsList();
    }
});