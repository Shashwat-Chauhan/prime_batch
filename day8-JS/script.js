// // const call = () => {
// //     console.log("clicked")
// // }

// // document.querySelector("body").addEventListener("click", call)

// setTimeout(handleCall, 0)
// console.log("start")
// const handleInnerCall = () => {
//     console.log("step Y")
// }

// function handleCall(){
//     console.log("Step M")

//     handleInnerCall();

//     console.log("Step N")
// }

// // setTimeout(handleCall, 1000)
// // setTimeout(handleCall, 2000)
// // setTimeout(handleCall, 3000)
// // setTimeout(handleCall, 4000)

// console.log("end")





const res = fetch('https://dummyjson.com/products')
.then((res1) => {
    const res2 = res1.json()
    res2.then((data) => {
        console.log("Data", data.products[0].images[0])
    })


})