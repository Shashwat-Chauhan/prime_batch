const getData = (text) => {
    const pr = fetch(`https://dummyjson.com/recipes/search?q=${text}`)
    pr.then((res) => {
        const pr2 = res.json()
        pr2.then((data) => {
            showCards(data.recipes)
        })
    })
}
const root = document.querySelector('#container_div')
const showCards = (dataArr) => {
    dataArr.forEach((elem) => {
        const newDiv = document.createElement('div')
        newDiv.className = 'card'
        newDiv.innerHTML = `
            <h4>${elem.name}</h4>
            <img src="${elem.image}" width="100px">
            <p>${elem.cuisine}</p>
        `
        root.appendChild(newDiv)
    })
}


let timeoutId = null;

const handleSearch = (e) => {
    clearTimeout(timeoutId); // Clear previous timeout before setting a new one
    timeoutId = setTimeout(() => {
        getData(e.target.value);
    }, 1000);
};
