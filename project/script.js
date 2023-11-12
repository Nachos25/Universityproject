fetch("shared/header.html")
    .then((response) => response.text())
    .then((data) => {
        document.getElementById("headerContainer").innerHTML = data;
    })
    .catch((error) => console.error("Error fetching header:", error));

fetch("shared/footer.html")
    .then((response) => response.text())
    .then((data) => {
        document.getElementById("footerContainer").innerHTML = data;
    })
    .catch((error) => console.error("Error fetching footer:", error));

fetch("shared/filter.html")
    .then((response) => response.text())
    .then((data) => {
        document.getElementById("filterContainer").innerHTML = data;
    })
    .catch((error) => console.error("Error fetching filter  :", error));
    
fetch("shared/items.html")
.then((response) => response.text())
.then((data) => {
    document.getElementById("itemsContainer").innerHTML = data;
})
.catch((error) => console.error("Error fetching filter  :", error));
