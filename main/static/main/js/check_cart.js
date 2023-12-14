let cart_length = localStorage.getItem("cart_length")
if(cart_length !== null){
    let cartItem = document.querySelector('.cart_text');
    cartItem.innerHTML = '<span class="material-symbols-outlined cart-icon">shopping_cart</span>'+cart_length
}