// Tabs Part
const tabsContainer = document.querySelector(".product-tabs");
const filler = document.querySelector(".filler");
var finalOffset = null;

window.addEventListener("scroll", () => {
    if (finalOffset == null) finalOffset = tabsContainer.offsetTop;
    if (window.scrollY > finalOffset) {
        filler.style.height = `${tabsContainer.offsetHeight}px`;
        tabsContainer.classList.add("sticky");
    } else {
        filler.style.height = 0;
        tabsContainer.classList.remove("sticky");
    }
});

const tabs = document.querySelectorAll(".tab");
let scrollTarget = null;
let scrolling = false;

function deactivateTabs() {
    tabs.forEach((tab) => {
        tab.classList.remove("active");
    });
}

tabs.forEach((tab) => {
    tab.addEventListener("click", () => {
        deactivateTabs();
        tab.classList.add("active");
        switch (tab.classList[1]) {
            case "product":
                scrollTarget = document.querySelector(".about");
                break;
            case "desc":
                scrollTarget = document.querySelector(".description");
                break;
            case "chars":
                scrollTarget = document.querySelector(".attributes");
                break;
            default:
                scrollTarget = null;
                break;
        }
        if (scrollTarget != null) {
            if (scrollTarget != document.querySelector(".about")) scrollTarget.style.scrollMarginTop = `${tabsContainer.offsetHeight + 32}px`;
            scrollTarget.scrollIntoView({});
            scrolling = true;
            setTimeout(() => {
                scrolling = false;
            }, 500);
        }
    });
});

const aboutTab = document.querySelector(".tab.product");
const descrTab = document.querySelector(".tab.desc");
const charsTab = document.querySelector(".tab.chars");

var selectedTab = aboutTab;

function isViewed(el) {
    const rect = el.getBoundingClientRect();
    return (
        (rect.top >= 0 && rect.bottom <= (window.innerHeight || document.documentElement.clientHeight)) ||
        (rect.top <= 0 && rect.bottom >= (window.innerHeight || document.documentElement.clientHeight))
    );
}

function handleScroll() {
    if (scrolling) return;
    const aboutSection = document.querySelector(".about");
    const descrSection = document.querySelector(".description");
    const charsSection = document.querySelector(".attributes");

    if (isViewed(aboutSection)) {
        deactivateTabs();
        aboutTab.classList.add("active");
    } else if (isViewed(descrSection)) {
        deactivateTabs();
        descrTab.classList.add("active");
    } else if (isViewed(charsSection)) {
        deactivateTabs();
        charsTab.classList.add("active");
    }
}

window.addEventListener("scroll", handleScroll);

handleScroll();

// Images Part
const sideImages = document.querySelectorAll(".side-image");
const sideSlider = document.querySelector(".side-slider");
const mainSlider = document.querySelector(".main-slider");
var activeSideImage = null;

var screenWidth = window.innerWidth || document.documentElement.clientWidth || document.body.clientWidth;

window.addEventListener('resize', function () {
    screenWidth = window.innerWidth || document.documentElement.clientWidth || document.body.clientWidth;
    scrollSideSlider();
});

var imgIterator = 0;

sideImages.forEach((image) => {
    image.classList.add(imgIterator);
    if (imgIterator == 0) {
        image.classList.add("active");
        activeSideImage = image;
    }
    ++imgIterator;
    image.addEventListener("click", () => {
        sideImages.forEach((image) => {
            image.classList.remove("active");
        });
        image.classList.add("active");
        activeSideImage = image;
        mainSlider.style.transform = `translateX(${-100 * image.classList[1]}%)`;

        scrollSideSlider();
    });
});

function scrollSideSlider() {
    var scrollTreshold = (screenWidth > 926) ? 5 : 4;
    if (sideImages.length > scrollTreshold) {
        var axis = (screenWidth > 1024) ? 'Y' : 'X';
        var index = activeSideImage.classList[1];
        var shift = scrollTreshold == 4 ? 1 : 0;
        if (index == 1) {
            sideSlider.style.transform = `translate${axis}(${-80 * (index - 1)}px)`;
        } else if (index > 1 && index < sideImages.length - 2) {
            sideSlider.style.transform = `translate${axis}(${-80 * (index - 2)}px)`;
        } else if (index == sideImages.length - 2) {
            sideSlider.style.transform = `translate${axis}(${-80 * (index - 3 + shift)}px)`;
        } else if (index == sideImages.length - 1) {
            sideSlider.style.transform = `translate${axis}(${-80 * (index - 4 + shift)}px)`;
        }
    }
}

const descriptionTextElement = document.querySelector(".description-card");
const tripleSplit = descriptionTextElement.innerHTML.trim().split("   ");
var finalDescription = [];
descriptionTextElement.innerHTML.trim().split("  ").forEach((text) => {
    finalDescription.push(`<p class="description-text">${text}</p>`)
})
descriptionTextElement.innerHTML = finalDescription.join("");

const attributesTextList = document.querySelectorAll(".attribute-text");
attributesTextList.forEach((textElement) => {
    const textSplit = textElement.innerHTML.split('•');
    if (textSplit.length == 1) {
        textElement.innerHTML = `• ${textSplit[0]}`;
    } else {
        textElement.innerHTML = textSplit.slice(1).map((text) => '•' + text).join("<br>");
    }
})