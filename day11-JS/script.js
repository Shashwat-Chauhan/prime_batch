// const parent = document.getElementById("parent")
// const ul = document.createElement('ul')


// const li1 = document.createElement("li")
// li1.innerText = "Item 1"

// const li2 = document.createElement("li")
// li2.innerText = "Item 2"

// const li3 = document.createElement("li")
// li3.innerText = "Item 3"

// ul.appendChild(li1)
// ul.appendChild(li2)
// ul.appendChild(li3)

// parent.appendChild(ul)


const domRoot = document.getElementById('parent')
const reactRoot = ReactDOM.createRoot(domRoot)

// const li = React.createElement("li", {
//     style:{
//         color: "red"
//     }
// } , "item 1") // --> type, options, children
// const l2 = React.createElement("li", {} , "item 2") // --> type, options, children
// const l3 = React.createElement("li", {} , "item 3") // --> type, options, children

// const ul = React.createElement("ul", {} , [li, l2, l3]) // --> type, options, children
// const title = React.createElement("h1", {}, "hello from React DOM")

// console.log("type of title", typeof title)
// console.log("title", title)

//creating my own react element
const title2 = <h1>Hello from JSX</h1>

reactRoot.render(title2)

const Title3 = () => {
    return <h1>Hello from Title3</h1>
}

reactRoot.render(<Title3/>)