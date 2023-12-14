document.addEventListener('DOMContentLoaded', function () {
  let submitBtn = document.querySelector('.search-icon');
  let myForm = document.querySelector('.nav-search');
  submitBtn.addEventListener('click', function () {
    if(myForm.querySelector('.search-input').value !== ''){
      myForm.submit();
    }
  });
});