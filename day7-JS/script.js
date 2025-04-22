const root = document.getElementById("root");
const select = document.getElementById("select");

let data = JSON.parse(localStorage.getItem("cards")) || [
    { id: "rd1", name: "Rakesh", city: "Delhi" },
    { id: "sm2", name: "Sonia", city: "Mumbai" },
    { id: "ab3", name: "Amit", city: "Bangalore" },
    { id: "sc4", name: "Sakshi", city: "Chennai" },
];

const saveToLocalStorage = () => {
    localStorage.setItem("cards", JSON.stringify(data));
};


const showCards = (newData) => {
    root.innerHTML = "";
    newData.forEach((el) => {
        const card = document.createElement("div");
        card.innerHTML = `
            <div>${el.name}</div>
            <p>${el.city}</p>
            <button onClick="deleteCard('${el.id}')">Delete</button>
        `;
        card.classList.add("card");
        root.appendChild(card);
    });
};

const deleteCard = (elemId) => {
    data = data.filter(el => el.id !== elemId);
    saveToLocalStorage();
    showCards(data);
    updateDropDown();
};

const handleSelect = (e) => {
    const selectedCity = e.target.value;
    const newData = data.filter(curr => curr.city == selectedCity);
    showCards(newData);
};

const formSubmit = (e) => {
    e.preventDefault();
    const name = e.target.name.value;
    const city = e.target.city.value;
    const newCardData = {
        id: `id-${Date.now()}`, // Unique ID
        name,
        city
    };
    data.push(newCardData);
    saveToLocalStorage();
    showCards(data);
    updateDropDown();
};

const updateDropDown = () => {
    const options = [...new Set(data.map(el => el.city))];
    select.innerHTML = options.map(city => `<option value="${city}">${city}</option>`).join(" ");
};

showCards(data);
updateDropDown();
